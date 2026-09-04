import json
import re
import unicodedata
import pandas as pd
from bs4 import BeautifulSoup
from lxml import etree
from src.schemas.medicine_schema import MedicineRecord
from typing import Union, Literal, Optional
from pydantic import TypeAdapter
from typing import Literal

'''
Đây là các function cần thiết cho việc xử lý dữ liệu
'''

def validate_medical_df(
    df: pd.DataFrame, return_as: str = "df"
) -> Union[pd.DataFrame, list[MedicineRecord]]:
    """Đảm bảo các cột của dữ liệu được đúng loại data.

    Args:
        df: Dữ liệu raw đọc từ file của APD
        return_as: 'df' to get typed DataFrame, or 'models' to get
            list[MedicineRecord]
    """
    adapter = TypeAdapter(list[MedicineRecord])

    # Convert DataFrame to records dict and validate in batch
    records = df.to_dict(orient="records")
    validated_records = adapter.validate_python(records)

    if return_as == "models":
        return validated_records

    # Reconstruct DataFrame with clean, typed columns
    validated_dicts = [
        rec.model_dump(exclude_unset=False) for rec in validated_records
    ]

    return pd.DataFrame(validated_dicts)

def remove_vietnamese_diacritics(text):
    """Loại bỏ dấu tiếng Việt và chuẩn hóa khoảng trắng/xuống dòng

    Args:
        text (str): câu input

    Returns:
        str: Output đã loại bỏ dấu tiếng việt, khoảng trắng chuẩn
    """
    if pd.isna(text) or text is None:
        return ""
    
    # 1. Chuyển đổi ký tự đặc biệt đ/Đ và non-breaking space
    text = str(text).replace('đ', 'd').replace('Đ', 'D').replace('\xa0', ' ')
    
    # 2. Xóa toàn bộ dấu tiếng Việt
    text = unicodedata.normalize('NFD', text)
    text = re.sub(r'[\u0300-\u036f]', '', text)
    text = unicodedata.normalize('NFC', text)
    
    # 3. Gộp các ký tự xuống dòng (\n, \r), tab, và nhiều dấu cách liền nhau thành 1 khoảng trắng duy nhất
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip().lower()

def build_regex_pattern(keywords, is_regex: bool = False):
    """Xây dựng chuỗi regex pattern từ danh sách từ khóa.

    Hàm chuẩn hóa các từ khóa bằng cách loại bỏ dấu tiếng Việt, lọc bỏ
    chuỗi rỗng, bọc từng từ khóa trong non-capturing group `(?:...)`, 
    và ghép lại bằng toán tử OR (`|`).

    Args:
        keywords (Union[str, Iterable[str], None]): Chuỗi đơn lẻ hoặc danh sách
            các từ khóa cần tạo mẫu regex.
        is_regex (bool, optional): Nếu True, coi từ khóa đã là cú pháp regex hợp lệ.
            Nếu False, áp dụng `re.escape()` để vô hiệu hóa ký tự đặc biệt. 
            Mặc định là False.

    Returns:
        Optional[str]: Chuỗi regex hoàn chỉnh dạng `(?:k1)|(?:k2)`, hoặc None 
            nếu danh sách đầu vào rỗng/không hợp lệ.
    """
    if not keywords:
        return None
    if isinstance(keywords, str):
        keywords = [keywords]

    processed = []
    for k in keywords:
        if not k or not str(k).strip():
            continue
        cleaned = remove_vietnamese_diacritics(k)

        if is_regex:
            processed.append(f"(?:{cleaned})")
        else:
            processed.append(f"(?:{re.escape(cleaned)})")

    return "|".join(processed) if processed else None


def read_xml(path: str) -> pd.DataFrame:
    parser = etree.XMLParser(recover=True, encoding="utf-8")

    with open(path, "rb") as f:
        tree = etree.parse(f, parser=parser)

    root = tree.getroot()

    rows = []
    for row in root.xpath('.//*[local-name()="Row"]'):
        cells = []
        for cell in row.xpath('./*[local-name()="Cell"]'):
        # Get text inside <Data> if present, otherwise directly inside <Cell>
            text = cell.xpath('string(.)').strip()
            cells.append(text)

        # Only include non-empty rows
        if any(cells):
            rows.append(cells)

    if not rows or len(rows) < 2:
        return pd.DataFrame()

    # Set header from row 0
    headers = [col.strip() for col in rows[0]]
    df = pd.DataFrame(rows[1:], columns=headers)

    # Drop columns where the header is completely empty ('' or whitespace)
    df = df.loc[:, [col != "" for col in df.columns]]

    # Drop any leftover completely empty/blank columns
    df = df.dropna(how="all", axis=1)

    return df


class ConfigValidationError(Exception):
    """Raised when a configuration dictionary is missing required keys."""
    pass

def filter_data(
    df: pd.DataFrame, 
    config:dict, 
    return_unmatched: bool = False, 
    verbose: bool = True
) -> pd.DataFrame:
    """Lọc dữ liệu theo config

    Args:
        df (pd.DataFrame): Dữ liệu đầu vào
        config (dict): Dictionary config. Yêu cầu theo format {
            'input_col': 'input_column_name', -> Tên cột để lọc
            'output_col': 'output_column_name', -> Tên cột output sau khi lọc. Ví dụ: ticker, ten_hoachat,...
            'filter': [ -> Rule filter chính
                {
                    'output_value': 'output_value', -> Gán giá trị output
                    'include_keyword': ['keyword1', 'keyword2'], -> Các từ khóa để tìm lọc trong dữ liệu
                    'exclude_keyword': ['keyword3', 'keyword4'] -> Các từ khóa để loại nếu bị lẫn
                }
            ]
        }
        return_unmatched (bool, optional): Trả thêm dữ liệu chưa lọc. Defaults to False.
        verbose (bool, optional): Print summary dữ liệu. Defaults to True.

    Returns:
        pd.DataFrame: Dữ liệu đã được lọc theo tùy chọn
    """
    if isinstance(config, str):
        config = json.loads(config)

    if not isinstance(config, dict):
        raise ConfigValidationError(f"Expected config to be a dict, got {type(config).__name__}")

    # 1. Validate top-level keys
    required_root_keys = {'input_col', 'output_col', 'filter'}
    missing_root = required_root_keys - config.keys()
    if missing_root:
        raise ConfigValidationError(f"Root config is missing required key(s): {sorted(list(missing_root))}")

    col = config['input_col']
    output_col = config['output_col']
    filter_rules = config['filter']

    if not isinstance(filter_rules, list):
        raise ConfigValidationError(f"'filter' key must contain a list of rule dictionaries, got {type(filter_rules).__name__}")

    if not filter_rules:
        raise ConfigValidationError("'filter' rule list cannot be empty.")

    # 2. Validate input column in DataFrame
    if col not in df.columns:
        raise KeyError(f"Input column '{col}' does not exist in DataFrame columns: {list(df.columns)}")

    # 3. Chuẩn hóa dữ liệu một lần duy nhất
    clean_series = df[col].apply(remove_vietnamese_diacritics)
    
    matched_dfs = []
    
    # 4. Validate and iterate through each filter rule
    for idx, rule in enumerate(filter_rules):
        if not isinstance(rule, dict):
            raise ConfigValidationError(f"Rule at index {idx} in 'filter' must be a dictionary.")

        # Accept 'output_value' or 'ticker' or 'label' as the target label
        label_val = rule.get('output_value', rule.get('ticker', rule.get('label')))
        if label_val is None:
            raise ConfigValidationError(f"Rule at index {idx} is missing a target label key ('output_value' or 'ticker').")

        # Validate keyword presence
        has_keywords = 'include_keyword' in rule or 'include_keywords' in rule
        if not has_keywords:
            raise ConfigValidationError(f"Rule at index {idx} is missing 'include_keyword'.")

        include_kws = rule.get('include_keyword', rule.get('include_keywords', []))
        exclude_kws = rule.get('exclude_keyword', rule.get('exclude_keywords', []))

        is_regex = rule.get('is_regex', False)
        include_pat = build_regex_pattern(include_kws, is_regex=is_regex)
        exclude_pat = build_regex_pattern(exclude_kws, is_regex=is_regex)
        
        if not include_pat:
            continue
            
        cond = clean_series.str.contains(include_pat, na=False)
        if exclude_pat:
            cond = cond & (~clean_series.str.contains(exclude_pat, na=False))
            
        res = df.loc[cond].copy()
        res[output_col] = label_val
        matched_dfs.append(res)
        
    result_df = pd.concat(matched_dfs, ignore_index=False) if matched_dfs else pd.DataFrame()
    
    matched_idx = result_df.index.unique() if not result_df.empty else pd.Index([])
    unmatched_df = df.loc[~df.index.isin(matched_idx)].copy()
    
    if verbose:
        total = len(df)
        n_matched = len(matched_idx)
        n_unmatched = len(unmatched_df)
        print("=== BÁO CÁO MATCH DỮ LIỆU ===")
        print(f"Cột gán nhãn:       '{output_col}'")
        print(f"Tổng số dòng:       {total:,}")
        print(f"Đã match (gán nhãn): {n_matched:,} ({n_matched/total*100:.2f}%)")
        print(f"Chưa match:         {n_unmatched:,} ({n_unmatched/total*100:.2f}%)")
        if not result_df.empty:
            print(f"\nChi tiết theo '{output_col}':")
            print(result_df[output_col].value_counts().to_string())
        print("=" * 30)

    if return_unmatched:
        return result_df, unmatched_df
    return result_df

def validate_medical_df(
    df: pd.DataFrame, return_as: str = "df"
    ) -> Union[pd.DataFrame, list[MedicineRecord]]:
    """Validates DataFrame rows against MedicineRecord schema.

    Args:
        df: Raw extracted DataFrame from read_xml()
        return_as: 'df' to get typed DataFrame, or 'models' to get
            list[MedicineRecord]
    """
    adapter = TypeAdapter(list[MedicineRecord])

    # Convert DataFrame to records dict and validate in batch
    records = df.to_dict(orient="records")
    validated_records = adapter.validate_python(records)

    if return_as == "models":
        return validated_records

    # Reconstruct DataFrame with clean, typed columns
    validated_dicts = [
        rec.model_dump(exclude_unset=False) for rec in validated_records
    ]
    return pd.DataFrame(validated_dicts)

class LoadMedicalData:
    """Class xử lý dữ liệu ngành Dược
    Args:
        datasource (str|pd.DataFrame): PATH đến file .xls raw của APD hoặc dataframe
        config (dict): Dictionary chứa filter cho dữ liệu
        drug_types_path (str): PATH đến file excel của bảng Danh mục hoạt chất theo loại thuốc
    """
    def __init__(
          self, 
          datasource:str|pd.DataFrame, 
          config:dict, 
          drug_types_path:str|pd.DataFrame,
          processed=False
        ):

        if isinstance(drug_types_path, str) and drug_types_path.endswith('xlsx'):
           self.drug_types = pd.read_excel(drug_types_path).dropna(how='all').reset_index(drop=True)[1:]
           self.drug_types.columns = self.drug_types.iloc[0].values
           self.drug_types = self.drug_types[1:].reset_index(drop=True).dropna(axis=1, how='all').drop(
              columns='STT'
           )
           self.drug_types['Loại thuốc 1'] = self.drug_types['Loại thuốc 1'].ffill()
           self.drug_types['Loại thuốc 2'] = self.drug_types['Loại thuốc 2'].ffill()
           
        elif isinstance(drug_types_path, pd.DataFrame):
           self.drug_types = drug_types_path.copy()
        else:
           raise TypeError('Invalid drug types file. Only accept .xlsx')

        if isinstance(datasource, str):
            self.filepath = datasource
            self.df = read_xml(self.filepath)
            self.df = self.df.replace("", None)
            self.df = self.df[~self.df[['ma', 'ten', 'hoatchat']].isna().any(axis=1)]
            self.df = validate_medical_df(self.df)

        elif isinstance(datasource, pd.DataFrame):
            self.df = datasource.copy()
            self.filepath = None
        else:
            raise TypeError("Invalid datasource type. Expected str or pd.DataFrame.")


        if isinstance(config, dict):
            self.config = config
            self.config_producer = config['producer_config']
            self.config_country = config['country_config']
            self.config_ingred = config['active_ingred_config']
        else:
            raise TypeError("Invalid config type. Must be dictionary")

        if not processed:
           self.standardize_data()

    def apply_labeling(self, df:pd.DataFrame, sub_config:dict) -> pd.DataFrame:
        if not sub_config:
            return df
        matched, unmatched = filter_data(
           df, sub_config, return_unmatched=True, verbose=False
        )
        out_col = sub_config['output_col']
        if not unmatched.empty and out_col not in unmatched.columns:
            unmatched[out_col] = None
        return (
           pd.concat([matched, unmatched], ignore_index=True)
           if not matched.empty
           else df
        )

    def standardize_data(self):
        self.df = self.apply_labeling(self.df, self.config_producer)
        self.df = self.apply_labeling(self.df, self.config_country)
        self.df = self.apply_labeling(self.df, self.config_ingred)

        ingred_col = (
           self.config_ingred.get('output_col', 'hoatchat') 
           if self.config_ingred 
           else 'hoatchat'
        )
        self.df = pd.merge(
           self.df,
           self.drug_types,
           how='left',
           left_on=ingred_col,
           right_on='Tên hoạt chất'
        )
    
    def show_data(self) -> pd.DataFrame:
        """Trả về toàn bộ dữ liệu đã load

        Returns:
            pd.DataFrame
        """
        return self.df.copy()

    def filter(
        self,
        column:str,
        value:str

    ):
        if column not in self.df.columns:
           raise ValueError(f'Column {column} not found in data!')

        if value is None:
           filtered_df = self.df.copy()
        elif isinstance(value, (list, tuple, set)):
           filtered_df = self.df.loc[self.df[column].isin(value)].copy()
        else:
           filtered_df = self.df.loc[self.df[column] == value].copy()

        return LoadMedicalData(
           filtered_df.reset_index(drop=True),
           self.config,
           self.drug_types,
           processed=True
        )

    def sum(
        self,
        value_col:Literal['thanhtien', 'soluong'],
        groupby=None
    ):
        if value_col not in self.df.columns:
            raise KeyError("Column not found in dataframe")
        if groupby:
            cols = [groupby] if isinstance(groupby, str) else groupby
            for col in cols:
                if col not in self.df.columns:             
                    raise KeyError("Column not found in dataframe")
            return self.df.groupby(groupby)[value_col].sum()

        return self.df[value_col].sum()

    def average(
        self,
        value_col:Literal['thanhtien', 'soluong', 'gia'],
        groupby=None
    ):
        
        if value_col not in self.df.columns:
            raise KeyError("Column not found in dataframe")
        if groupby:
            cols = [groupby] if isinstance(groupby, str) else groupby
            for col in cols:
                if col not in self.df.columns:             
                    raise KeyError("Column not found in dataframe")
            return self.df.groupby(groupby)[value_col].mean()

        return self.df[value_col].mean()

    def get_unmatched(
        self,
        config_type: Literal['producer', 'country', 'ingred'],
        unique: bool = True
    ) -> Union[list, pd.DataFrame]:
        """Xem các giá trị chưa match/chưa được gán nhãn theo từng loại config.

        Args:
            config_type (Literal['producer', 'country', 'ingred']): Loại config cần kiểm tra.
            unique (bool, optional): Nếu True, trả về list các giá trị gốc duy nhất chưa match.
                                     Nếu False, trả về DataFrame đầy đủ của các dòng chưa match. Defaults to True.

        Returns:
            Union[list, pd.DataFrame]: Danh sách giá trị hoặc DataFrame các dòng chưa match.
        """
        config_map = {
            'producer': self.config_producer,
            'country': self.config_country,
            'ingred': self.config_ingred
        }

        if config_type not in config_map:
            raise ValueError(f"Invalid config_type: '{config_type}'. Choose from: {list(config_map.keys())}")

        sub_cfg = config_map[config_type]
        if not sub_cfg:
            raise ValueError(f"Config for '{config_type}' is not configured.")

        input_col = sub_cfg['input_col']
        output_col = sub_cfg['output_col']

        # Dòng chưa match là dòng có output_col là NaN/None hoặc rỗng
        unmatched_mask = self.df[output_col].isna() | (self.df[output_col] == '')
        unmatched_df = self.df.loc[unmatched_mask]

        if unique:
            # Lấy các giá trị gốc ban đầu chưa được phân loại, loại bỏ null/trắng
            unmatched_values = unmatched_df[input_col].dropna().unique().tolist()
            return [val for val in unmatched_values if str(val).strip()]

        print(f"Total unmatched rows for '{config_type}': {len(unmatched_df)}")
        
        return unmatched_df.reset_index(drop=True)

    def get_matched(
        self,
        config_type: Literal['producer', 'country', 'ingred'],
        value: Optional[Union[str, list]] = None,
        unique: bool = False
    ) -> pd.DataFrame:
        """Xem các dòng dữ liệu hoặc các giá trị đã match/đã được gán nhãn theo từng loại config.

        Args:
            config_type (Literal['producer', 'country', 'ingred']): Loại config cần kiểm tra ('producer', 'country', 'ingred').
            value (Optional[Union[str, list]], optional): Lọc theo giá trị output cụ thể (ví dụ: 'IMP', 'Nhật Bản', 'Paracetamol'). Defaults to None.
            unique (bool, optional): Nếu True, trả về DataFrame các cặp giá trị duy nhất [input_col, output_col].
                                     Nếu False, trả về toàn bộ DataFrame các dòng đã match. Defaults to False.

        Returns:
            pd.DataFrame: DataFrame gồm các dòng hoặc giá trị đã được lọc/gán nhãn.
        """
        config_map = {
            'producer': self.config_producer,
            'country': self.config_country,
            'ingred': self.config_ingred,
            'active_ingred': self.config_ingred,
            'ingredient': self.config_ingred
        }

        if config_type not in config_map:
            raise ValueError(f"Invalid config_type: '{config_type}'. Choose from: ['producer', 'country', 'ingred']")

        sub_cfg = config_map[config_type]
        if not sub_cfg:
            raise ValueError(f"Config for '{config_type}' is not configured.")

        input_col = sub_cfg['input_col']
        output_col = sub_cfg['output_col']

        if output_col not in self.df.columns:
            raise KeyError(f"Output column '{output_col}' not found in DataFrame.")

        # Dòng đã match là dòng có output_col không rỗng và không NaN
        matched_mask = self.df[output_col].notna() & (self.df[output_col] != '')
        matched_df = self.df.loc[matched_mask]

        if value is not None:
            if isinstance(value, (list, tuple, set)):
                matched_df = matched_df.loc[matched_df[output_col].isin(value)]
            else:
                matched_df = matched_df.loc[matched_df[output_col] == value]

        if unique:
            cols_to_show = [input_col, output_col] if input_col in matched_df.columns else [output_col]
            return matched_df[cols_to_show].drop_duplicates().reset_index(drop=True)

        return matched_df.reset_index(drop=True)

