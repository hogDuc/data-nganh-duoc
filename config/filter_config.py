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

country_config = {
    "input_col":'nuocsx',
    "output_col":"country",
    'filter':[
        {
            "output_value": "Việt Nam",
            "include_keyword": [
                r"^viet nam", 
                r'^vietnam',
                r'^viet\\s*nam',
                'viet nam'
            ],
            "exclude_keyword": [],
            "is_regex": True
        },
        {
            "output_value": "Hoa Kỳ",
            "include_keyword": [
                "usa", 
                r'^hoa ky', 
                r'^my',
                r"cssx\s*:\s*my\b",
                r"cssx\s*:\s*my\b",
                r"nuoc san xuat\s*:\s*my\b",
            ],
            "exclude_keyword": [],
            "is_regex":True
        },
        {
            "output_value": "Ai Cập",
            "include_keyword": ["ai cap"],
            "exclude_keyword": []
        },
        {
            "output_value": "Ireland",
            "include_keyword": [
                "ai len", 
                "ireland", 
                r"^ireland",
                "ailen"
            ],
            "exclude_keyword": [],
            'is_regex': True
        },
        {
            "output_value": "Đức",
            "include_keyword": [
                r"cssx\s*:\s*duc\b",
                r"cssx\s*:\s*germany\b",
                r"co so san xuat\s*:\s*duc\b",
                r"^duc",
                r"^germany",
                
            ],
            "exclude_keyword": [],
            'is_regex': True
        },
        {
            "output_value": "Anh",
            "include_keyword": [
                r"^anh",
                r"^united kingdom",
                
            ],
            "exclude_keyword": [],
            'is_regex': True
        },
        {
            "output_value": "Argentina",
            "include_keyword": [
                r"^argentina",
                
            ],
            "exclude_keyword": [],
            'is_regex': True
        },
        {
            "output_value": "Úc",
            "include_keyword": [
                r"^australia",
                r"^uc",
                
            ],
            "exclude_keyword": [],
            'is_regex': True
        },
        {
            "output_value": "Áo",
            "include_keyword": [
                r"^austria",
                r"^ao",
                r"cssx\s*:\s*ao\b",
                
            ],
            "exclude_keyword": [],
            'is_regex': True
        },
        {
            "output_value": "Ba Lan",
            "include_keyword": [
                r"^ba lan",
                r"cssx[^;]*:\s*-?\s*ba lan\b",
                r"^poland"
                
            ],
            "exclude_keyword": [],
            'is_regex': True
        },
        {
            "output_value": "Bangladesh",
            "include_keyword": [
                r"^bangladesh",
                
            ],
            "exclude_keyword": [],
            'is_regex': True
        },
        {
            "output_value": "Belarus",
            "include_keyword": [r"^belarus\b", r"\bbach nga\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Bỉ",
            "include_keyword": [
                r"^bi\b",
                r"^belgium\b",
                r"cssx[^;]*:\s*bi\b",
                r"cssx[^;]*:\s*belgium\b",
            ],
            "exclude_keyword": [r"ban thanh pham:\s*bi\b", r"csdg[^;]*:\s*bi\b"],
            "is_regex": True,
        },
        {
            "output_value": "Bulgaria",
            "include_keyword": [r"^bulgaria\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Bồ Đào Nha",
            "include_keyword": [
                r"^bo dao nha\b",
                r"^portugal\b",
                r"cssx[^;]*:\s*bo dao nha\b",
                r"cssx[^;]*:\s*portugal\b",
            ],
            "exclude_keyword": [r"csdg[^;]*:\s*bo dao nha\b"],
            "is_regex": True,
        },
        {
            "output_value": "Canada",
            "include_keyword": [r"^canada\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Chile",
            "include_keyword": [r"^chile\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Croatia",
            "include_keyword": [r"^croatia\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Síp",
            "include_keyword": [
                r"^sip\b",
                r"^cyprus\b",
                r"\bcong hoa sip\b",
            ],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Séc",
            "include_keyword": [
                r"^sec\b",
                r"^czech\b",
                r"\bczech republic\b",
                r"\bcong hoa sec\b",
            ],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Đan Mạch",
            "include_keyword": [r"^dan mach\b", r"^denmark\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Đài Loan",
            "include_keyword": [r"^dai loan\b", r"^taiwan\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Estonia",
            "include_keyword": [r"^estonia\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Hà Lan",
            "include_keyword": [
                r"^ha lan\b",
                r"^the netherlands\b",
                r"^netherlands\b",
                r"cssx[^;]*:\s*ha lan\b",
            ],
            "exclude_keyword": [r"csdg[^;]*:\s*ha lan\b", r"dong goi:\s*ha lan\b"],
            "is_regex": True,
        },
        {
            "output_value": "Hàn Quốc",
            "include_keyword": [
                r"^han quoc\b",
                r"^korea\b",
                r"^south korea\b",
                r"^republic of korea\b",
            ],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Hungary",
            "include_keyword": [
                r"^hungary\b",
                r"^hungari\b",
                r"^bungary\b",
                r"\begis-hungary\b",
            ],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Hy Lạp",
            "include_keyword": [r"^hy lap\b", r"^greece\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Indonesia",
            "include_keyword": [r"^indonesia\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Ấn Độ",
            "include_keyword": [r"^an do\b", r"^india\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Latvia",
            "include_keyword": [r"^latvia\b", r"cssx[^;]*:\s*latvia\b"],
            "exclude_keyword": [
                r"xx:\s*latvia\b",
                r"xuat xuong[^;]*:\s*latvia\b",
            ],
            "is_regex": True,
        },
        {
            "output_value": "Litva",
            "include_keyword": [r"^litva\b", r"^lithuania\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Bắc Macedonia",
            "include_keyword": [r"^macedonia\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Malaysia",
            "include_keyword": [r"^malaysia\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Malta",
            "include_keyword": [r"^malta\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Na Uy",
            "include_keyword": [r"^na uy\b", r"^norway\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Nga",
            "include_keyword": [r"^nga\b", r"^russia\b", r"^russian\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Nhật Bản",
            "include_keyword": [r"^nhat ban\b", r"^nhat\b", r"^japan\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Pakistan",
            "include_keyword": [r"^pakistan\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Pháp",
            "include_keyword": [
                r"^phap\b",
                r"^france\b",
                r"cssx[^;]*:\s*phap\b",
                r"co so san xuat[^;]*:\s*phap\b",
            ],
            "exclude_keyword": [
                r"kiem nghiem va xuat xuong:\s*phap\b",
                r"csxx[^;]*:\s*phap\b",
            ],
            "is_regex": True,
        },
        {
            "output_value": "Phần Lan",
            "include_keyword": [r"^phan lan\b", r"^finland\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Puerto Rico",
            "include_keyword": [
                r"^puerto rico\b",
                r"cssx[^;]*:\s*puerto rico\b",
            ],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Romania",
            "include_keyword": [r"^romania\b", r"^romani\b", r"^rumani\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Singapore",
            "include_keyword": [r"^singapore\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Slovakia",
            "include_keyword": [
                r"^slovakia\b",
                r"^slovaka\b",
                r"\bsx, dg, kn:\s*slovakia\b",
                r"\bsan xuat[^:]*:\s*slovakia\b",
            ],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Slovenia",
            "include_keyword": [
                r"^slovenia\b",
                r"nuoc san xuat[^;]*:\s*slovenia\b",
            ],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Tây Ban Nha",
            "include_keyword": [
                r"^tay ban nha\b",
                r"^tay ba nha\b",
                r"^spain\b",
                r"cssx[^;]*:\s*tay ban nha\b",
                r"cssx[^;]*:\s*tay ba nha\b",
            ],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Thái Lan",
            "include_keyword": [r"^thai lan\b", r"^thailand\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Thổ Nhĩ Kỳ",
            "include_keyword": [
                r"^tho nhi ky\b",
                r"^turkey\b",
                r"co so san xuat[^;]*:\s*tho nhi ky\b",
                r"nuoc san xuat[^;]*:\s*tho nhi ky\b",
            ],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Thụy Điển",
            "include_keyword": [r"^thuy dien\b", r"^sweden\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Thụy Sĩ",
            "include_keyword": [
                r"^thuy si\b",
                r"^thuy sy\b",
                r"^switzerland\b",
                r"cssx[^;]*:\s*thuy si\b",
                r"cssx[^;]*:\s*thuy sy\b",
            ],
            "exclude_keyword": [
                r"dong goi[^;]*:\s*thuy sy\b",
                r"dong goi[^;]*:\s*thuy si\b",
                r"csdg[^;]*:\s*thuy sy\b",
                r"csdg[^;]*:\s*thuy si\b",
            ],
            "is_regex": True,
        },
        {
            "output_value": "Trung Quốc",
            "include_keyword": [
                r"^trung quoc\b",
                r"^china\b",
                r"\bcong hoa nhan dan trung hoa\b",
            ],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Ukraine",
            "include_keyword": [r"^ukraine\b"],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Ý",
            "include_keyword": [
                r"^y\b",
                r"^italy\b",
                r"^italia\b",
                r"^ytaly\b",
                r"cssx[^;]*:\s*y\b",
                r"co so san xuat[^;]*:\s*y\b",
            ],
            "exclude_keyword": [],
            "is_regex": True,
        },
        {
            "output_value": "Việt Nam",
            "include_keyword": [
                r"^viet nam\b",
                r"^vietnam\b",
                r"\bduoc pham am vi\b",
            ],
            "exclude_keyword": [r"\(\s*viet nam[^)]*dong goi"],
            "is_regex": True,
        }
    ]
}