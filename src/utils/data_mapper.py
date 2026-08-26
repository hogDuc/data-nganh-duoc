import json
import re
import unicodedata
import pandas as pd

def remove_vietnamese_diacritics(text):
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

def filter_by_ticker_config(
    df: pd.DataFrame, 
    config, 
    col, 
    output_col: str = 'ticker', 
    return_unmatched: bool = False, 
    verbose: bool = True
):
    """
    Lọc DataFrame theo cấu hình Ticker/Từ khóa và gán nhãn vào cột tùy chọn.
    
    Parameters:
    - df: DataFrame gốc
    - config: dict / JSON string (1 config) hoặc list các dict / JSON string (nhiều configs)
    - col: Tên cột hoặc chỉ số cột cần tìm kiếm (mặc định: 17)
    - output_col: Tên cột kết quả được tạo ra (mặc định: 'ticker')
    - return_unmatched: Trả về (df_matched, df_unmatched) nếu True
    - verbose: In báo cáo thống kê nếu True
    
    Returns:
    - pd.DataFrame (hoặc tuple (matched_df, unmatched_df))
    """
    if isinstance(config, str):
        config = json.loads(config)
    
    # 1. Chuẩn hóa cột dữ liệu 1 lần duy nhất để tối ưu hiệu năng
    clean_series = df[col].apply(remove_vietnamese_diacritics)
    
    configs_list = config if isinstance(config, list) else [config]
    matched_dfs = []
    
    for cfg in configs_list:
        # Lấy giá trị nhãn: ưu tiên lấy theo tên output_col, nếu không có thì lấy 'ticker' hoặc 'label'
        label_val = cfg.get(output_col, cfg.get('ticker', cfg.get('label', '')))
        
        include_kws = cfg.get('include_keyword', cfg.get('include_keywords', []))
        exclude_kws = cfg.get('exclude_keyword', cfg.get('exclude_keywords', []))
        
        include_pat = build_regex_pattern(include_kws)
        exclude_pat = build_regex_pattern(exclude_kws)
        
        if not include_pat:
            continue
            
        cond = clean_series.str.contains(include_pat, na=False)
        if exclude_pat:
            cond = cond & (~clean_series.str.contains(exclude_pat, na=False))
            
        res = df.loc[cond].copy()
        res[output_col] = label_val  # Gán giá trị vào cột output_col tùy chọn
        matched_dfs.append(res)
        
    result_df = pd.concat(matched_dfs, ignore_index=False) if matched_dfs else pd.DataFrame()
    
    # Tính toán các dòng chưa match
    matched_idx = result_df.index.unique() if not result_df.empty else pd.Index([])
    unmatched_df = df.loc[~df.index.isin(matched_idx)].copy()
    
    if verbose:
        total = len(df)
        n_matched = len(matched_idx)
        n_unmatched = len(unmatched_df)
        print(f"=== BÁO CÁO MATCH DỮ LIỆU ===")
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