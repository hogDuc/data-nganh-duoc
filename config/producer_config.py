"""
Configuration cho các bộ lọc.
input_col: Tên cột cần lọc của dữ liệu gốc, ví dụ 'nhasx'
output_col: Tên cột gán nhãn cho đầu ra, ví dụ 'ticker'
filter: Bộ lọc chính
    output_value: Giá trị đã chuẩn hóa cho output, ví dụ phân loại theo nhà sản xuất thì sẽ đưa vào tên nhà sản xuất
    include_keyword: Các từ khóa để lọc trong dữ liệu
    exclude_keyword: Các từ khóa để loại ra các trường hợp bị lẫn

Lưu ý:
Các keyword BẮT BUỘC phải để trong ngoặc '' hoặc "", và chuỗi các keyword phải được đặt trong ngoặc []
"""

configs = {
    "input_col":'nhasx',
    "output_col":"ticker",
    'filter':[
        {
            "output_value": "IMP",
            "include_keyword": ["imexpharm"],
            "exclude_keyword": ["agimexpharm"]
        },
        {
            "output_value": "Pharbaco",
            "include_keyword": ["pharbaco"],
            "exclude_keyword": []
        },
        {
            "output_value": "Pharbaco",
            "include_keyword": ["pharbaco"],
            "exclude_keyword": ["agimexpharm"]
        },
    ]
}