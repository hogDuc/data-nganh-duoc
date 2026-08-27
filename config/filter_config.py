"""
Configuration cho các bộ lọc.

Các mục bắt buộc:
input_col: Tên cột cần lọc của dữ liệu gốc, ví dụ 'nhasx'
output_col: Tên cột gán nhãn cho đầu ra, ví dụ 'ticker'
filter: Bộ lọc chính
    output_value: Giá trị đã chuẩn hóa cho output, ví dụ phân loại theo nhà sản xuất thì sẽ đưa vào tên nhà sản xuất
    include_keyword: Các từ khóa để lọc trong dữ liệu
    exclude_keyword: Các từ khóa để loại ra các trường hợp bị lẫn
    is_regex: True cho một số trường hợp đặc biệt. Ví dụ sản xuất trung gian
Lưu ý:
Các keyword viết dưới dạng không dấu, viết thường, không viết hoa.
Các keyword BẮT BUỘC phải để trong ngoặc '' hoặc "", và chuỗi các keyword phải được đặt trong ngoặc [].
Nếu không có exclude thì để giá trị [].
"""

producer_config = {
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
            "output_value": "Minh Dân",
            "include_keyword": ["minh dan"],
            "exclude_keyword": []
        },
        {
            "output_value": "Tenamyd",
            "include_keyword": ["tenamyd"],
            "exclude_keyword": []
        },
        {
            "output_value": "ACS Dobfar",
            "include_keyword": [
                r"cssx\s*:\s*acs dobfar",
                r"^acs dobfar"
            ],
            "exclude_keyword": [],
            'is_regex':True
        },
        {
            "output_value": "Pymepharco",
            "include_keyword": ["pymepharco"],
            "exclude_keyword": []
        },
        {
            "output_value": "VCP",
            "include_keyword": ["vcp"],
            "exclude_keyword": []
        },
        {
            "output_value": "Polfa Tarchomin",
            "include_keyword": ["tarchomin"],
            "exclude_keyword": []
        },
        {
            "output_value": "Tarchomin Pharmaceutical",
            "include_keyword": ["tarchomin"],
            "exclude_keyword": []
        },
        {
            "output_value": "S.C. Antibiotice",
            "include_keyword": ["antibiotice"],
            "exclude_keyword": []
        },
        {
            "output_value": "S.C. Antibiotice",
            "include_keyword": ["antibiotice"],
            "exclude_keyword": []
        },
        {
            "output_value": "Wyeth Lederle S.R.L",
            "include_keyword": ["wyeth lederle s.r.l"],
            "exclude_keyword": []
        },
        {
            "output_value": "Wyeth Lederle S.R.L",
            "include_keyword": ["wyeth lederle s.r.l"],
            "exclude_keyword": []
        },
        {
            "output_value": "Fareva Mirabel",
            "is_regex": True,
            "include_keyword": [
                r"cssx\s*:\s*fareva mirabel",
                r"^fareva mirabel"
            ],
            "exclude_keyword": []
        },
        {
            "output_value": "DHG",
            "include_keyword": ["dhg", 'duoc hau giang'],
            "exclude_keyword": ['tnhh mtv duoc pham dhg']
        },
        {
            "output_value": "DHT",
            "include_keyword": ["duoc pham ha tay"],
            "exclude_keyword": []
        },
        {
            "output_value": "DBD",
            "include_keyword": ["bidiphar"],
            "exclude_keyword": ['cong ty co phan ky thuat duoc binh dinh', 'fresenius kabi bidiphar']
        },
        {
            "output_value": "TRA",
            "include_keyword": ["cong ty co phan traphaco", 'traphaco'],
            "exclude_keyword": []
        },
        {
            "output_value": "TRA",
            "include_keyword": ["cong ty co phan traphaco", 'traphaco'],
            "exclude_keyword": []
        },
        {
            "output_value": "DCL",
            "include_keyword": ['cuu long'],
            "exclude_keyword": []
        },
        {
            "output_value": "DTP",
            "include_keyword": ['ha noi'],
            "exclude_keyword": []
        },
        {
            "output_value": "DMC",
            "include_keyword": ['domesco'],
            "exclude_keyword": []
        },
        {
            "output_value": "OPC",
            "include_keyword": ['opc'],
            "exclude_keyword": ['tnhh', 'thhh']
        },
    ]
}