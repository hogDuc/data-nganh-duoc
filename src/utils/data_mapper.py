import json
import re
import unicodedata
import pandas as pd
from bs4 import BeautifulSoup

def remove_vietnamese_diacritics(text):
    """Loại bỏ dấu tiếng Việt

    Args:
        text (str): câu input

    Returns:
        str: Output đã loại bỏ dấu tiếng việt
    """
    if pd.isna(text) or text is None:
        return ""
    text = str(text).replace('đ', 'd').replace('Đ', 'D')
    text = unicodedata.normalize('NFD', text)
    text = re.sub(r'[\u0300-\u036f]', '', text)
    return unicodedata.normalize('NFC', text).strip().lower()

def build_regex_pattern(keywords):

    if not keywords:
        return None
    if isinstance(keywords, str):
        keywords = [keywords]
    escaped = [
        re.escape(remove_vietnamese_diacritics(k)) 
        for k in keywords 
        if k and str(k).strip()
    ]
    return '|'.join(escaped) if escaped else None


def read_xml(path) -> pd.DataFrame:
    """Đọc dữ liệu XML từ APD

    Args:
        path (str): PATH đến file dữ liệu gốc

    Returns:
        pd.DataFrame: Dữ liệu bảng
    """

    with open(path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'xml')

    rows = []
    for row in soup.find_all('Row'):
        rows.append([cell.get_text(strip=True) for cell in row.find_all('Cell')])

    df = pd.DataFrame(rows[1:], columns=rows[0])

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
        
        include_pat = build_regex_pattern(include_kws)
        exclude_pat = build_regex_pattern(exclude_kws)
        
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