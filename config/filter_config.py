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
config = {
    'producer_config':{
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
    },
    
    'country_config':{
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
    },

    'active_ingred_config':{
        "input_col": "hoatchat",
        "output_col": "active_ingredient",
        "filter": [
            {
                "output_value": "Acarbose",
                "include_keyword": [r"acarbose\b"],
                "exclude_keyword": [],
                'is_regex': True
            },
            {
                "output_value": "Aceclofenac",
                "include_keyword": [r"aceclofenac\b"],
                "exclude_keyword": [],
                'is_regex': True
            },
            {
                "output_value": "Acenocoumarol",
                "include_keyword": [r"acenocoumarol\b"],
                "exclude_keyword": [],
                'is_regex': True
            },
            {
                "output_value": "Paracetamol (acetaminophen)",
                "include_keyword": [
                    # Matches single ingredient Paracetamol/Acetaminophen and stops before '+'
                    r"^(paracetamol|acetaminophen)[^+]*$"
                    r'^paracetamol$',
                    r'^acetaminophen$',
                    'paracetamol',
                    'Paracetamol (acetaminophen)',
                ],
                "exclude_keyword": [
                    'micronized'
                ],
                "is_regex": True,
            },
            {
                "output_value": "Acetazolamid",
                "include_keyword": [r"acetazolamid$"],
                "exclude_keyword": [],
                'is_regex': True
            },
            {
                "output_value": "Acetyl leucin",
                "include_keyword": [
                    r"acetyl leucin$",
                    r'acetyl leucine$'
                ],
                "exclude_keyword": [],
                'is_regex': True
            },
            {
                "output_value": "Acetylcystein",
                "include_keyword": [
                    r"^acetylcystein$",
                    r"^acetylcysteine$",
                ],
                "exclude_keyword": [],
                'is_regex': True
            },
            {
                "output_value": "N-acetylcystein",
                "include_keyword": [
                    'N - Acetylcystein',
                    'N-Acetylcystein',
                    'N-acetylcystein',
                ],
                "exclude_keyword": []
            },
            {
                "output_value": "Acetylsalicylic acid (DL-lysin-acetylsalicylat)",
                "include_keyword": [
                    r"^acetylsalicylic acid[^+]*$"
                    r"^acid acetylsalicylic",
                    'acetylsalicylic acid',
                    'acid acetylsalicylic',
                    'aspirin',
                    'aspirin (Acetylsalicylic acid)',
                ],
                "exclude_keyword": [],
                'is_regex': True
            },
            {
                "output_value": "Acetylsalicylic acid + clopidogrel",
                "include_keyword": [
                    r"acetylsalicylic\s*acid\s*\+\s*clopidogrel\b",
                ],
                "exclude_keyword": [],
                'is_regex': True
            },
            {
                "output_value": "Acid amin + glucose + điện giải",
                "include_keyword": [
                    r"acid amin\s*\+\s*glucose\s*\+\s*điện giải"
                ],
                "exclude_keyword": [r"lipid"],
                "is_regex": True
            },
            {
                "output_value": "Acid amin + điện giải",
                "include_keyword": [
                    r"acid amin\s*\+\s*dien giai",
                    'acid amin + chat dien giai',
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Acid amin + glucose + lipid",
                "include_keyword": [
                    r"acid amin\s*\+\s*glucose\s*\+\s*lipid"
                ],
                "exclude_keyword": [r"dien giai"],
                "is_regex": True
            },
            {
                "output_value": "Acid amin*",
                "include_keyword": [
                    r"^acid amin\*?$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Aciclovir",
                "include_keyword": [
                    r"^ac(i|y)clovir\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vitamin C",
                "include_keyword": [
                    r"^vitamin c$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fusidic Acid",
                "include_keyword": [
                    r"^(acid fusidic|fusidic acid)$"
                ],
                "exclude_keyword": [r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Fusidic Acid + Betamethason",
                "include_keyword": [
                    r"fusidic acid.*betamethaso"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fusidic Acid + Hydrocortison",
                "include_keyword": [
                    r"fusidic acid.*hydrocortison"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Acid folic (vitamin B9)",
                "include_keyword": [
                    r"^(acid folic|folic acid)"
                ],
                "exclude_keyword": [r"\+", r"ferrous", r"sắt"],
                "is_regex": True
            },
            {
                "output_value": "Calci folinat (folinic acid, leucovorin)",
                "include_keyword": [
                    r"acid folinic",
                    r"calci folinat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Gadoteric acid",
                "include_keyword": [
                    r"acid gadoteric",
                    r"gadoteric acid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Salicylic acid + betamethason dipropionat",
                "include_keyword": [
                    r"(acid salicylic|salicylic acid)\s*\+\s*betamethason"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Acid thioctic (Meglumin thioctat)",
                "include_keyword": [
                    r"acid thioctic",
                    r"meglumin thioctat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tranexamic acid",
                "include_keyword": [
                    r"(acid tranexamic|tranexamic acid)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Acitretin",
                "include_keyword": [
                    r"^acitretin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Adalimumab",
                "include_keyword": [
                    r"^adalimumab\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Adenosin triphosphat",
                "include_keyword": [
                    r"adenosin triphosphat",
                    r"^adenosine\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Adrenalin",
                "include_keyword": [
                    r"^(adrenalin|epinephrin(\s*\(adrenalin\))?)$"
                ],
                "exclude_keyword": [r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Aescin",
                "include_keyword": [
                    r"^(aescin|aescinat natri)\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Albendazol",
                "include_keyword": [
                    r"^albendazol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Albumin",
                "include_keyword": [
                    r"^(albumin|albumin người|human albumin)\b",
                    r"protein huyết tương trong đó albumin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Acid alendronic",
                "include_keyword": [
                    r"alendronic acid",
                    r"natri alendronat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Alfuzosin",
                "include_keyword": [
                    r"^alfuzosin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Alimemazin",
                "include_keyword": [
                    r"^alimemazin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Allopurinol",
                "include_keyword": [
                    r"^allopurinol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Alphachymotrypsin",
                "include_keyword": [
                    r"alpha\s*chymotrypsin",
                    r"^chymotrypsin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Alteplase",
                "include_keyword": [
                    r"^alteplase\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Nhôm phosphat",
                "include_keyword": [
                    r"aluminum phosphat",
                    r"nhôm phosphat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Alverin + Simethicon",
                "include_keyword": [
                    r"alverin.*simethico",
                    r"simethicone\s*\+\s*alverine"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Alverin",
                "include_keyword": [
                    r"^alverin"
                ],
                "exclude_keyword": [r"simethico"],
                "is_regex": True
            },
            {
                "output_value": "Ambroxol",
                "include_keyword": [
                    r"^ambroxol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Amikacin",
                "include_keyword": [
                    r"^amikacin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Aminophylin",
                "include_keyword": [
                    r"aminophylin",
                    r"theophylin-ethylendiamin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Amiodaron",
                "include_keyword": [
                    r"^amiodaron"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Amisulprid",
                "include_keyword": [
                    r"^amisulprid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Amitriptylin",
                "include_keyword": [
                    r"^amitriptylin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Amlodipin + Atorvastatin",
                "include_keyword": [
                    r"amlodipin.*atorvastatin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Amlodipin + Indapamid + Perindopril",
                "include_keyword": [
                    r"amlodipin.*indapamid.*perindopril",
                    r"perindopril.*indapamide.*amlodipine"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Amlodipin + Indapamid",
                "include_keyword": [
                    r"amlodipin.*indapamid"
                ],
                "exclude_keyword": [r"perindopril"],
                "is_regex": True
            },
            {
                "output_value": "Amlodipin + Lisinopril",
                "include_keyword": [
                    r"amlodipin.*lisinopril"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Amlodipin + Losartan",
                "include_keyword": [
                    r"amlodipin.*losartan",
                    r"losartan.*amlodipine"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Amlodipin + Telmisartan",
                "include_keyword": [
                    r"amlodipin.*telmisartan",
                    r"telmisartan.*amlodipine"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Amlodipin + Valsartan + Hydrochlorothiazid",
                "include_keyword": [
                    r"amlodipin.*valsartan.*hydrochlorothiazid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Amlodipin + Valsartan",
                "include_keyword": [
                    r"amlodipin.*valsartan"
                ],
                "exclude_keyword": [r"hydrochlorothiazid"],
                "is_regex": True
            },
            {
                "output_value": "Amlodipin",
                "include_keyword": [
                    r"^amlodipin"
                ],
                "exclude_keyword": [r"\+", r";"],
                "is_regex": True
            },
            {
                "output_value": "Amoxicilin + Acid clavulanic",
                "include_keyword": [
                    r"amoxicil(l)?in.*(acid\s*)?clavulan"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Amoxicilin + Sulbactam",
                "include_keyword": [
                    r"amoxicilin.*sulbactam"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Amoxicilin",
                "include_keyword": [
                    r"^amoxicil(l)?in\b"
                ],
                "exclude_keyword": [r"clavulan", r"sulbactam", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Ampicilin + Sulbactam",
                "include_keyword": [
                    r"ampicil(l)?in.*sulbactam",
                    r"^sultamicillin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ampicilin (muối natri)",
                "include_keyword": [
                    r"^ampicilin\b"
                ],
                "exclude_keyword": [r"sulbactam", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Enzym tiêu hóa (Amylase + Lipase + Protease)",
                "include_keyword": [
                    r"amylase.*lipase.*protease",
                    r"pancreatin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Anastrozol",
                "include_keyword": [
                    r"^anastrozol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Apixaban",
                "include_keyword": [
                    r"^apixaban\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Atenolol",
                "include_keyword": [
                    r"^atenolol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Atorvastatin + Ezetimibe",
                "include_keyword": [
                    r"atorvastatin.*ezetimibe"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Atorvastatin",
                "include_keyword": [
                    r"^atorvastatin\b"
                ],
                "exclude_keyword": [r"amlodipin", r"ezetimibe", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Atosiban",
                "include_keyword": [
                    r"^atosiban\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Atracurium",
                "include_keyword": [
                    r"^atracurium\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Atropin sulfat",
                "include_keyword": [
                    r"^atropin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Attapulgit + Magnesi carbonat + Nhôm hydroxyd",
                "include_keyword": [
                    r"attapulgit.*(magnesi|nhôm)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Attapulgit",
                "include_keyword": [
                    r"^attapulgit\b"
                ],
                "exclude_keyword": [r"magnesi", r"nhôm", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Azithromycin",
                "include_keyword": [
                    r"^azithromycin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Bacillus clausii",
                "include_keyword": [
                    r"bacillus claus(s)?ii"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Bacillus subtilis",
                "include_keyword": [
                    r"bacillus subtilis"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Baclofen",
                "include_keyword": [
                    r"^baclofen\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Bambuterol",
                "include_keyword": [
                    r"^bambuterol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Beclometason (dipropionat)",
                "include_keyword": [
                    r"^beclometason\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Benazepril hydroclorid",
                "include_keyword": [
                    r"^benazepril\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Benzylpenicilin",
                "include_keyword": [
                    r"^benzylpenicilin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Berberin (hydroclorid)",
                "include_keyword": [
                    r"^berberin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Betahistin",
                "include_keyword": [
                    r"^betahistine?"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Betamethason + Clotrimazol + Gentamicin",
                "include_keyword": [
                    r"betamethason.*clotrimazol.*gentamicin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Betamethason + Dexchlorpheniramin",
                "include_keyword": [
                    r"betamethason.*dexchlorpheniramin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Betamethason",
                "include_keyword": [
                    r"^betamethason"
                ],
                "exclude_keyword": [r"clotrimazol", r"dexchlorpheniramin", r"salicylic", r"fusidic", r"calcipotriol"],
                "is_regex": True
            },
            {
                "output_value": "Bevacizumab",
                "include_keyword": [
                    r"^bevacizumab\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Bezafibrat",
                "include_keyword": [
                    r"^bezafibrat\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Bicalutamid",
                "include_keyword": [
                    r"^bicalutamid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Bilastine",
                "include_keyword": [
                    r"^bilastine\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Bimatoprost",
                "include_keyword": [
                    r"^bimatoprost\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Bisacodyl",
                "include_keyword": [
                    r"^bisacodyl\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Bismuth",
                "include_keyword": [
                    r"^bismuth\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Bisoprolol + Hydroclorothiazid",
                "include_keyword": [
                    r"bisoprolol.*hydroc(h)?lorothiazid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Bisoprolol",
                "include_keyword": [
                    r"^bisoprolol\b"
                ],
                "exclude_keyword": [r"hydroc(h)?lorothiazid", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Bleomycin",
                "include_keyword": [
                    r"^bleomycin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Botulinum toxin",
                "include_keyword": [
                    r"^botulinum toxin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Brimonidin + Timolol",
                "include_keyword": [
                    r"brimonidin.*timolol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Brimonidin",
                "include_keyword": [
                    r"^brimonidin"
                ],
                "exclude_keyword": [r"timolol"],
                "is_regex": True
            },
            {
                "output_value": "Brinzolamid + Timolol",
                "include_keyword": [
                    r"brinzolamid.*timolol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Brinzolamid",
                "include_keyword": [
                    r"^brinzolamid"
                ],
                "exclude_keyword": [r"timolol"],
                "is_regex": True
            },
            {
                "output_value": "Bromfenac",
                "include_keyword": [
                    r"^bromfenac\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Bromhexin",
                "include_keyword": [
                    r"^bromhexin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Budesonid + Formoterol",
                "include_keyword": [
                    r"budesonid.*formoterol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Budesonid",
                "include_keyword": [
                    r"budesonid"
                ],
                "exclude_keyword": [r"formoterol"],
                "is_regex": True
            },
            {
                "output_value": "Bupivacain",
                "include_keyword": [
                    r"^bupivacain"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Magnesi hydroxyd + nhôm hydroxyd + simethicon",
                "include_keyword": [
                    r"codried.*simethicon",
                    r"(nhôm|magnesi).*hydroxyd.*simethicon",
                    r"mỗi 10 ml hỗn dịch chứa.*nhôm hydroxyd.*magnesi hydroxyd.*simethicon"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Magnesi hydroxyd + nhôm hydroxyd",
                "include_keyword": [
                    r"magnesi hydroxyd\s*\+\s*nhôm hydroxyd",
                    r"mỗi 10ml chứa:\s*nhôm hydroxyd.*magnesi hydroxyd"
                ],
                "exclude_keyword": [r"simethicon"],
                "is_regex": True
            },
            {
                "output_value": "Magnesi trisilicat + nhôm hydroxyd",
                "include_keyword": [
                    'Magnesi hydroxyd (dưới dạng Magnesi hydroxyd 30% past) + nhôm oxyd (dưới dạng Nhôm Hydroxyd gel)',
                ],
                "exclude_keyword": [],
            },
            {
                "output_value": "Cafein citrat",
                "include_keyword": [
                    r"cafein\s*(\(citrat\)|citrat)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Calci carbonat + Vitamin D3",
                "include_keyword": [
                    r"calci carbonat.*vitamin d3"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Calci lactat + Calci carbonat",
                "include_keyword": [
                    r"calci carbonat\s*\+\s*calci (lactat gluconat|gluconolactat)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Calci carbonat",
                "include_keyword": [
                    r"^calci carbonat$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ringer lactat",
                "include_keyword": [
                    r"calci clorid.*kali clorid.*natri clorid.*natri lactat",
                    r"^ringer lactat$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Calci clorid",
                "include_keyword": [
                    r"^(calci|calcium) chlor?ide?( dihydrate| dihydrat)?",
                    'calci clorid'
                ],
                "exclude_keyword": [r"kali", r"natri"],
                "is_regex": True
            },
            {
                "output_value": "Calci gluconat",
                "include_keyword": [
                    r"^calci gluconat\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Calci glycerophosphat + Magnesi gluconat",
                "include_keyword": [
                    r"calci glycerophosphat.*magnesi gluconat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Calci lactat",
                "include_keyword": [
                    r"^(calci|calcium) lactat(e)?\b"
                ],
                "exclude_keyword": [r"carbonat"],
                "is_regex": True
            },
            {
                "output_value": "Calcipotriol + Betamethason",
                "include_keyword": [
                    r"calcipotriol\s*\+\s*betamethason"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Calcipotriol",
                "include_keyword": [
                    r"^calcipotriol$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Calcitonin",
                "include_keyword": [
                    r"^calcitonin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Calcitriol",
                "include_keyword": [
                    r"^calcitriol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Candesartan + hydrochlorothiazid",
                "include_keyword": [
                    r"candesartan.*hydroc(h)?lorothiazid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Candesartan",
                "include_keyword": [
                    r"^candesartan\b"
                ],
                "exclude_keyword": [r"hydroc(h)?lorothiazid", r"\+", r";"],
                "is_regex": True
            },
            {
                "output_value": "Cao ginkgo biloba + heptaminol clohydrat + troxerutin",
                "include_keyword": [
                    r"cao ginkgo biloba.*heptaminol.*troxerutin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ginkgo biloba",
                "include_keyword": [
                    r"ginkgo(nis)?\s*(biloba|extractum)",
                    r"lá bạch quả"
                ],
                "exclude_keyword": [r"heptaminol"],
                "is_regex": True
            },
            {
                "output_value": "Capsaicin",
                "include_keyword": [
                    r"^capsaicin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Captopril + Hydroclorothiazid",
                "include_keyword": [
                    r"captopril.*hydroclorothiazid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Captopril",
                "include_keyword": [
                    r"^captopril\b"
                ],
                "exclude_keyword": [r"hydroclorothiazid", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Carbamazepin",
                "include_keyword": [
                    r"^carbamazepin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Carbazochrom",
                "include_keyword": [
                    r"^carbazochrom\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Carbetocin",
                "include_keyword": [
                    r"^carbetocin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Carbimazol",
                "include_keyword": [
                    r"^carbimazol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Carbocistein + Promethazin",
                "include_keyword": [
                    r"carbocistein\s*\+\s*promethazin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Carbocistein",
                "include_keyword": [
                    r"^carbocistein\b"
                ],
                "exclude_keyword": [r"promethazin", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Carbomer",
                "include_keyword": [
                    r"^carbomer\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Carboplatin",
                "include_keyword": [
                    r"^carboplatin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Carboprost",
                "include_keyword": [
                    r"^carboprost\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Carvedilol",
                "include_keyword": [
                    r"^carvedilol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Caspofungin*",
                "include_keyword": [
                    r"^caspofungin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefaclor",
                "include_keyword": [
                    r"^cefaclor\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefadroxil",
                "include_keyword": [
                    r"^cefadroxil\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefalexin",
                "include_keyword": [
                    r"^cefa?lexin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefalothin",
                "include_keyword": [
                    r"^cefalothin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefamandol",
                "include_keyword": [
                    r"^cefamandol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefazolin",
                "include_keyword": [
                    r"^cefazolin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefdinir",
                "include_keyword": [
                    r"^cefdinir\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefepim",
                "include_keyword": [
                    r"^cefepim\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefixim",
                "include_keyword": [
                    r"^cefixim"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefmetazol",
                "include_keyword": [
                    r"^cefmetazol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefoperazon + Sulbactam",
                "include_keyword": [
                    r"cefoperazon(e)?.*sulbactam"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefoperazon",
                "include_keyword": [
                    r"^cefoperazon"
                ],
                "exclude_keyword": [r"sulbactam", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Cefotaxim",
                "include_keyword": [
                    r"^cefotaxim"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefotiam",
                "include_keyword": [
                    r"^cefotiam"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefoxitin",
                "include_keyword": [
                    r"^cefoxitin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefpirom",
                "include_keyword": [
                    r"^cefpirom\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefpodoxim",
                "include_keyword": [
                    r"^cefpodoxim\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefradin",
                "include_keyword": [
                    r"^cefradin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ceftazidim",
                "include_keyword": [
                    r"^ceftazidim\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ceftizoxim",
                "include_keyword": [
                    r"^ceftizoxim\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ceftriaxon",
                "include_keyword": [
                    r"^ceftriaxon"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cefuroxim",
                "include_keyword": [
                    r"^cefuroxim"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Celecoxib",
                "include_keyword": [
                    r"^celecoxib\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cetirizin",
                "include_keyword": [
                    r"^cetirizin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Chlorpheniramin + Dextromethorphan",
                "include_keyword": [
                    r"chlorpheniramin\s*\+\s*dextromethorphan"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Chlorpheniramin (hydrogen maleat)",
                "include_keyword": [
                    r"^(chlor|clor)pheniramin"
                ],
                "exclude_keyword": [r"dextromethorphan", r"paracetamol", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Chlorpromazin",
                "include_keyword": [
                    r"^(chlor|clor)promazin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Choline alfoscerat",
                "include_keyword": [
                    r"choline alfoscerat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ciclopirox",
                "include_keyword": [
                    r"^ciclopirox"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ciclosporin",
                "include_keyword": [
                    r"^c(i|y)closporin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cilnidipin",
                "include_keyword": [
                    r"^cilnidipin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cilostazol",
                "include_keyword": [
                    r"^cilostazol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cimetidin",
                "include_keyword": [
                    r"^cimetidin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cinnarizin",
                "include_keyword": [
                    r"^cinnarizin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ciprofibrat",
                "include_keyword": [
                    r"^ciprofibrat\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ciprofloxacin",
                "include_keyword": [
                    r"^ciprofloxacin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cisplatin",
                "include_keyword": [
                    r"^cisplatin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Citalopram",
                "include_keyword": [
                    r"^citalopram\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Citicolin",
                "include_keyword": [
                    r"^citicolin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Clarithromycin",
                "include_keyword": [
                    r"^clarithromycin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Clindamycin",
                "include_keyword": [
                    r"^clindamycin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Clobetasol",
                "include_keyword": [
                    r"^clobetasol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Clopidogrel",
                "include_keyword": [
                    r"^clopidogrel\b"
                ],
                "exclude_keyword": [r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Clotrimazol + Betamethason",
                "include_keyword": [
                    r"clotrimazol.*betamethason"
                ],
                "exclude_keyword": [r"gentamicin"],
                "is_regex": True
            },
            {
                "output_value": "Clotrimazol",
                "include_keyword": [
                    r"^clotrimazol"
                ],
                "exclude_keyword": [r"betamethason", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Cloxacilin",
                "include_keyword": [
                    r"^cloxacilin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Clozapin",
                "include_keyword": [
                    r"^clozapin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Codein + Sulfogaiacol + Grindelia",
                "include_keyword": [
                    r"codein.*sulfo(g)?uaiacol.*grindelia"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Codein + Terpin hydrat",
                "include_keyword": [
                    r"(codein.*terpin|terpin.*codein)"
                ],
                "exclude_keyword": [r"paracetamol"],
                "is_regex": True
            },
            {
                "output_value": "Colchicin",
                "include_keyword": [
                    r"^colchicin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Colistin*",
                "include_keyword": [
                    r"colist(in|imethat)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Crotamiton",
                "include_keyword": [
                    r"^crotamiton\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vitamin B12 (cyanocobalamin, hydroxocobalamin)",
                "include_keyword": [
                    'vitamin b12',
                    'vitamin b12 (cyanocobalamin, hydroxocobalamin)',
                    'cyanocobalamin',
                    'hydroxocobalamin'
                ],
                "exclude_keyword": []
            },
            {
                "output_value": "Cyclophosphamid",
                "include_keyword": [
                    r"^cyclophosphamid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cytidin + Uridin",
                "include_keyword": [
                    r"cytidin.*uridin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cồn boric",
                "include_keyword": [
                    r"^cồn (boric)$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cồn A.S.A",
                "include_keyword": [
                    r"^cồn (a\.s\.a)$"
                    # r"^cồn (70°|a\.s\.a|bsi|boric)$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cồn BSI",
                "include_keyword": [
                    r"^cồn (bsi)$"
                    # r"^cồn (70°|a\.s\.a|bsi|boric)$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cồn 70°",
                "include_keyword": [
                    r"^cồn (70°)$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cồn iod",
                "include_keyword": [
                    r"^cồn (iod)$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Mannitol",
                "include_keyword": [
                    r"^(d-)?mannitol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dabigatran",
                "include_keyword": [
                    r"^dabigatran\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dapagliflozin",
                "include_keyword": [
                    r"^dapagliflozin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Daptomycin",
                "include_keyword": [
                    r"^daptomycin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Deferasirox",
                "include_keyword": [
                    r"^deferasirox\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Deferipron",
                "include_keyword": [
                    r"^deferipron\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Deferoxamin",
                "include_keyword": [
                    r"^deferoxamin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dequalinium",
                "include_keyword": [
                    r"^dequalinium\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Desfluran",
                "include_keyword": [
                    r"^desflurane?\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Desloratadin",
                "include_keyword": [
                    r"^desloratadin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Desmopressin",
                "include_keyword": [
                    r"^desmopressin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dexamethason + Moxifloxacin",
                "include_keyword": [
                    r"moxifloxacin.*dexamethason",
                    r"dexamethason.*moxifloxacin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dexamethason + Neomycin + Polymyxin B",
                "include_keyword": [
                    r"dexamethason.*neomycin.*polymyxin",
                    r"neomycin.*polymy(c|x)in.*dexamethason"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tobramycin + dexamethason",
                "include_keyword": [
                    r"tobramycin.*dexamethaso"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dexamethason",
                "include_keyword": [
                    r"^dexamethason"
                ],
                "exclude_keyword": [r"neomycin", r"moxifloxacin", r"tobramycin", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Dexchlorpheniramin",
                "include_keyword": [
                    r"^dexc(h)?lorpheniramin"
                ],
                "exclude_keyword": [r"betamethason"],
                "is_regex": True
            },
            {
                "output_value": "Dexibuprofen",
                "include_keyword": [
                    r"^dexibuprofen\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dexpanthenol",
                "include_keyword": [
                    r"^dexpanthenol\b",
                    r"^vitamin b5$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sắt sucrose (hay dextran)",
                "include_keyword": [
                    r"^dextran$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dextran 40",
                "include_keyword": [
                    r"^dextran 40\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dextran 60",
                "include_keyword": [
                    r"^dextran 60\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dextran 70",
                "include_keyword": [
                    r"^dextran 70\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dextromethorphan",
                "include_keyword": [
                    r"^dextromethorphan\b"
                ],
                "exclude_keyword": [r"paracetamol", r"chlorpheniramin", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Diacerein",
                "include_keyword": [
                    r"^diacerein\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Diazepam",
                "include_keyword": [
                    r"^diazepam\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dibencozid",
                "include_keyword": [
                    r"^dibencozid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Diclofenac",
                "include_keyword": [
                    r"^diclofenac\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Diethylphtalat",
                "include_keyword": [
                    r"^diethylphtalat\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Digoxin",
                "include_keyword": [
                    r"^digoxin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dihydroergotamin",
                "include_keyword": [
                    r"^dihydro\s*ergotamin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Diltiazem",
                "include_keyword": [
                    r"^diltiazem\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dimenhydrinat",
                "include_keyword": [
                    r"^dimenhydrinat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dinoproston",
                "include_keyword": [
                    r"^dinoproston\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Diosmectit",
                "include_keyword": [
                    r"(dioctahedral\s*smectit|diosmectit)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Diosmin + Hesperidin",
                "include_keyword": [
                    r"diosmin.*hesperidin",
                    r"phân đoạn flavonoid vi hạt tinh chế.*diosmin.*hesperidin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Diosmin",
                "include_keyword": [
                    r"^diosmin$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Diphenhydramin",
                "include_keyword": [
                    r"^diphenhydramin\b"
                ],
                "exclude_keyword": [r"paracetamol", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Dobutamin",
                "include_keyword": [
                    r"^dobutamin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Docetaxel",
                "include_keyword": [
                    r"^docetaxel\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Docusat natri",
                "include_keyword": [
                    r"docusate\s*(natri|sodium)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dolutegravir + Lamivudin + Tenofovir",
                "include_keyword": [
                    r"dolutegravir.*lamivudine.*tenofovir"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Domperidon",
                "include_keyword": [
                    r"^domperidon"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Donepezil",
                "include_keyword": [
                    r"^donepezil\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dopamin",
                "include_keyword": [
                    r"^dopamin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Doripenem",
                "include_keyword": [
                    r"^doripenem"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Doxazosin",
                "include_keyword": [
                    r"^doxazosin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Doxorubicin",
                "include_keyword": [
                    r"^doxorubicin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Doxycyclin",
                "include_keyword": [
                    r"^doxycyclin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Drotaverin",
                "include_keyword": [
                    r"^drotaverin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dung dịch lọc ngoài thận",
                "include_keyword": [
                    r"dung dịch lọc (màng bụng|máu|thận)",
                    r"khoang a:.*khoang b:.*calcium clorid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dutasterid",
                "include_keyword": [
                    r"^dutasterid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dydrogesteron",
                "include_keyword": [
                    r"^dydrogesteron"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ebastin",
                "include_keyword": [
                    r"^ebastin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Econazol",
                "include_keyword": [
                    r"^econazol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Empagliflozin",
                "include_keyword": [
                    r"^empagliflozin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Enalapril + hydrochlorothiazid",
                "include_keyword": [
                    r"enalapril.*hydroc(h)?lorothiazid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Enalapril",
                "include_keyword": [
                    r"^enalapril"
                ],
                "exclude_keyword": [r"hydroc(h)?lorothiazid", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Enoxaparin (natri)",
                "include_keyword": [
                    r"^enoxaparin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Entecavir",
                "include_keyword": [
                    r"^entecavir\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Eperison",
                "include_keyword": [
                    r"^eperison\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ephedrin",
                "include_keyword": [
                    r"^ephedrin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Eprazinon",
                "include_keyword": [
                    r"^eprazinon\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Erlotinib",
                "include_keyword": [
                    r"^erlotinib\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ertapenem*",
                "include_keyword": [
                    r"^ertapenem"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Erythromycin",
                "include_keyword": [
                    r"^erythromycin\b"
                ],
                "exclude_keyword": [r"tretinoin"],
                "is_regex": True
            },
            {
                "output_value": "Erythropoietin",
                "include_keyword": [
                    r"erythropoietin\b"
                ],
                "exclude_keyword": [r"methoxy polyethylene glycol"],
                "is_regex": True
            },
            {
                "output_value": "Esomeprazol",
                "include_keyword": [
                    r"^esomeprazol"
                ],
                "exclude_keyword": [r"naproxen"],
                "is_regex": True
            },
            {
                "output_value": "Estradiol valerate",
                "include_keyword": [
                    r"^estradiol valerate"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Etamsylat",
                "include_keyword": [
                    r"^etamsylat\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dầu hạt thuốc phiện iod hóa",
                "include_keyword": [
                    r"ethyl ester của acid béo iod hóa trong dầu hạt thuốc phiện"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Etifoxin",
                "include_keyword": [
                    r"^etifoxin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Etodolac",
                "include_keyword": [
                    r"^etodolac\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Etomidat",
                "include_keyword": [
                    r"^etomidat\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Etoposid",
                "include_keyword": [
                    r"^etoposid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Etoricoxib",
                "include_keyword": [
                    r"^etoricoxib\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ezetimibe + Simvastatin",
                "include_keyword": [
                    r"ezetimibe.*simvastatin",
                    r"simvastatin.*ezetimibe"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ezetimibe",
                "include_keyword": [
                    r"^ezetimibe$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Famotidin",
                "include_keyword": [
                    r"^famotidin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Felodipin",
                "include_keyword": [
                    r"^felodipin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fenofibrat",
                "include_keyword": [
                    r"^fenofibrat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fenoterol + ipratropium",
                "include_keyword": [
                    r"fenoterol\s*\+\s*ipratropium",
                    r"ipratropium.*fenoterol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fenspirid",
                "include_keyword": [
                    r"^fenspirid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fentanyl",
                "include_keyword": [
                    r"^fentanyl\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fenticonazol",
                "include_keyword": [
                    r"^fenticonazol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sắt sulfat + acid folic",
                "include_keyword": [
                    r"(ferrous sulfate|sat.*sulfat|sat fumarat|sat.*(iii)?\s*hydroxyd.*polymaltose).*acid folic",
                    r"s[ắa]t\s*sulfat\s*\+\s*folic\s*acid",
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fexofenadin",
                "include_keyword": [
                    r"^fexofenadin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Filgrastim",
                "include_keyword": [
                    r"^filgrastim\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Flavoxat",
                "include_keyword": [
                    r"^flavoxat\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fluconazol",
                "include_keyword": [
                    r"^fluconazol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Flunarizin",
                "include_keyword": [
                    r"^flunarizin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fluocinolon acetonid",
                "include_keyword": [
                    r"^fluocinolon acetonid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fluorometholon",
                "include_keyword": [
                    r"^fluorometholon\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fluorouracil (5-FU)",
                "include_keyword": [
                    r"fluorouracil\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fluoxetin",
                "include_keyword": [
                    r"^fluoxetin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Flurbiprofen",
                "include_keyword": [
                    r"^flurbiprofen\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fluticason + Salmeterol",
                "include_keyword": [
                    r"fluticasone.*salmeterol",
                    r"salmeterol.*fluticason"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fluticason",
                "include_keyword": [
                    r"^fluticasone?\b"
                ],
                "exclude_keyword": [r"salmeterol", r";", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Fluvastatin",
                "include_keyword": [
                    r"^fluvastatin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fluvoxamin",
                "include_keyword": [
                    r"^fluvoxamin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fosfomycin*",
                "include_keyword": [
                    r"^fosfomycin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Fructose 1,6 diphosphat",
                "include_keyword": [
                    r"fructose 1,6 diphosphat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Furosemid + Spironolacton",
                "include_keyword": [
                    r"furosemid.*spironolacton"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Furosemid",
                "include_keyword": [
                    r"^furosemide?\b"
                ],
                "exclude_keyword": [r"spironolacton", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Gabapentin",
                "include_keyword": [
                    r"^gabapentin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Gadobenic acid (dimeglumin)",
                "include_keyword": [
                    r"gadobenic acid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Gadobutrol",
                "include_keyword": [
                    r"gadobutrol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Galantamin",
                "include_keyword": [
                    r"^galantamin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Gefitinib",
                "include_keyword": [
                    r"^gefitinib\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Gelatin succinyl",
                "include_keyword": [
                    r"gelatin succinyl"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Gemcitabin",
                "include_keyword": [
                    r"^gemcitabin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Gemfibrozil",
                "include_keyword": [
                    r"^gemfibrozil\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Gentamicin",
                "include_keyword": [
                    r"^gentamicin"
                ],
                "exclude_keyword": [r"betamethason"],
                "is_regex": True
            },
            {
                "output_value": "Glibenclamid + Metformin",
                "include_keyword": [
                    r"glibenclamid.*metformin",
                    r"metformin.*glibenclamid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Gliclazid + Metformin",
                "include_keyword": [
                    r"gliclazid(e)?.*metformin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Gliclazid",
                "include_keyword": [
                    r"^gliclazid"
                ],
                "exclude_keyword": [r"metformin", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Glimepirid + Metformin",
                "include_keyword": [
                    r"glimepirid.*metformin",
                    r"metformin.*glimepirid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Glimepirid",
                "include_keyword": [
                    r"^glimepirid"
                ],
                "exclude_keyword": [r"metformin", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Glipizid",
                "include_keyword": [
                    r"^glipizid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Glucosamin",
                "include_keyword": [
                    r"^glucosamin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Natri clorid + natri lactat + kali clorid + calcium clorid + glucose (Ringer lactat + glucose)",
                "include_keyword": [
                    r"glucose.*natri clorid.*(tri\s*)?natri\s*citrat.*kali clorid",
                    r"natri clorid.*kali clorid.*(natri citrat|tri natricitrat).*glucose",
                    r"natri clorid.*kali clorid.*monobasic kali phosphat.*dextrose",
                    r"natri clorid.*natri bicarbonat.*kali clorid.*dextrose",
                    r"natri lactat.*natri clorid.*kali clorid.*calcium clorid.*glucose",
                    'natri clorid, kali clorid, natri lactat, calci clorid.2h2o',
                    'natri clorid ;  natri lactat; kali clorid ; calci clorid dihydrat',
                    'natri clorid + kali clorid + natri lactat + calci clorid.2h2o',
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Glucose",
                "include_keyword": [
                    r"^glucose\b",
                    r"^mỗi 100ml chứa:?\s*glucose\b"
                ],
                "exclude_keyword": [r"natri clorid", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Glutathion",
                "include_keyword": [
                    r"^glutathion\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Glycerol",
                "include_keyword": [
                    r"^glycerol$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Glyceryl trinitrat (Nitroglycerin)",
                "include_keyword": [
                    r"glyceryl trinitrat",
                    r"nitroglycerin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Golimumab",
                "include_keyword": [
                    r"^golimumab\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Goserelin",
                "include_keyword": [
                    r"^goserelin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Granisetron",
                "include_keyword": [
                    r"^granisetron\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Griseofulvin",
                "include_keyword": [
                    r"^griseofulvin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Guaiazulen + Dimethicon",
                "include_keyword": [
                    r"guaiazulen\s*\+\s*dimethicon"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Haloperidol",
                "include_keyword": [
                    r"^haloperidol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Heparin (natri)",
                "include_keyword": [
                    r"^heparin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Heptaminol",
                "include_keyword": [
                    r"^heptaminol\b"
                ],
                "exclude_keyword": [r"ginkgo"],
                "is_regex": True
            },
            {
                "output_value": "Huyết thanh kháng dại",
                "include_keyword": [
                    r"huyết thanh kháng dại"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Huyết thanh kháng nọc rắn",
                "include_keyword": [
                    r"huyết thanh kháng nọc rắn"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Huyết thanh kháng uốn ván",
                "include_keyword": [
                    r"huyết thanh kháng uốn ván"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Hydroclorothiazid",
                "include_keyword": [
                    r"^hydroclorothiazid$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Hydrocortison",
                "include_keyword": [
                    r"^hydrocortison\b"
                ],
                "exclude_keyword": [r"fusidic"],
                "is_regex": True
            },
            {
                "output_value": "Hydroxocobalamin",
                "include_keyword": [
                    r"^hydroxocobalamin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Hydroxychloroquin",
                "include_keyword": [
                    r"hydroxy\s*cloroquin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Hydroxypropylmethylcellulose",
                "include_keyword": [
                    r"hydroxypropyl\s*methylcellulose"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Hydroxyurea (Hydroxycarbamid)",
                "include_keyword": [
                    r"hydroxyurea"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Hyoscin butylbromid",
                "include_keyword": [
                    r"hyoscin\s*(-n-)?\s*butylbromid",
                    r"scopolamin-n-butylbromid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ibuprofen + Codein",
                "include_keyword": [
                    r"ibuprofen\s*\+\s*codein"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ibuprofen",
                "include_keyword": [
                    r"^ibuprofen\b"
                ],
                "exclude_keyword": [r"codein", r"paracetamol", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Imatinib",
                "include_keyword": [
                    r"^imatinib\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Imidapril",
                "include_keyword": [
                    r"^imidapril\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Imipenem + cilastatin*",
                "include_keyword": [
                    r"imipenem.*cilastatin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Immunoglobulin người",
                "include_keyword": [
                    r"^(immune globulin|immunoglobulin người)\b",
                    r"immunoglobulin thông thường từ huyết tương người"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Indacaterol + Glycopyrronium",
                "include_keyword": [
                    r"indacaterol\s*\+\s*glycopyrronium"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Perindopril + indapamid",
                "include_keyword": [
                    r"indapamid\s*\+\s*perindopril",
                    r"perindopril.*indapamid"
                ],
                "exclude_keyword": [r"amlodipin"],
                "is_regex": True
            },
            {
                "output_value": "Indapamid",
                "include_keyword": [
                    r"^indapamide?\b"
                ],
                "exclude_keyword": [r"perindopril", r"amlodipin", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Indomethacin",
                "include_keyword": [
                    r"^indomethacin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Insulin Degludec + Insulin Aspart",
                "include_keyword": [
                    r"insulin degludec\s*\+\s*insulin aspart",
                    r"dạng trộn, hỗn hợp giữa insulin degludec và insulin aspart"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Insulin Degludec",
                "include_keyword": [
                    r"^insulin degludec$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Insulin Glargine",
                "include_keyword": [
                    r"^insulin glargine?"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Insulin Glulisine",
                "include_keyword": [
                    r"^insulin glulisine\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Insulin Lispro",
                "include_keyword": [
                    r"^insulin lispro\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Insulin analog",
                "include_keyword": [
                    r"^insulin analog\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Insulin người",
                "include_keyword": [
                    r"insulin (human|người|trộn|tác dụng)"
                ],
                "exclude_keyword": [r"analog", r"degludec", r"glargine", r"glulisine", r"lispro"],
                "is_regex": True
            },
            {
                "output_value": "Iobitridol",
                "include_keyword": [
                    r"iobitridol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Iohexol",
                "include_keyword": [
                    r"^iohexol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Iopamidol",
                "include_keyword": [
                    r"^iopamidol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Iopromid",
                "include_keyword": [
                    r"^iopromid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ipratropium bromid + Salbutamol",
                "include_keyword": [
                    r"ipratropium.*salbutamol",
                    r"salbutamol.*ipratropium"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Irbesartan + Hydroclorothiazid",
                "include_keyword": [
                    r"irbe(r)?sartan.*hydroc(h)?lorothiazid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Irbesartan",
                "include_keyword": [
                    r"^irbesartan\b"
                ],
                "exclude_keyword": [r"hydroc(h)?lorothiazid", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Irinotecan",
                "include_keyword": [
                    r"^irinotecan\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Isosorbid (dinitrat hoặc mononitrat)",
                "include_keyword": [
                    r"isosorbid(-5)?\s*mononitrat",
                    r"^isosorbid\s*\(dinitrat hoặc",
                    r"isosorbid dinitrat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Isotretinoin",
                "include_keyword": [
                    r"^isotretinoin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Itoprid",
                "include_keyword": [
                    r"^itoprid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Itraconazol",
                "include_keyword": [
                    r"^itraconazol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ivabradin",
                "include_keyword": [
                    r"^ivabradin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ivermectin",
                "include_keyword": [
                    r"^ivermectin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Kali clorid",
                "include_keyword": [
                    r"^(kali clorid|potassium chloride)$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Kali iodid + Natri iodid",
                "include_keyword": [
                    r"kali iodid\s*\+\s*natri iodid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ketamin",
                "include_keyword": [
                    r"^ketamin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ketoconazol",
                "include_keyword": [
                    r"^ketoconazol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ketoprofen",
                "include_keyword": [
                    r"^ketoprofen\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ketorolac",
                "include_keyword": [
                    r"^ketorolac\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ketotifen",
                "include_keyword": [
                    r"^ketotifen\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Polystyren sulfonat",
                "include_keyword": [
                    r"calcium polystyrene sufonate",
                    r"^polystyren$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Kẽm oxid",
                "include_keyword": [
                    r"kẽm oxid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Kẽm",
                "include_keyword": [
                    r"^kẽm\b"
                ],
                "exclude_keyword": [r"oxid"],
                "is_regex": True
            },
            {
                "output_value": "L-Ornithin L-Aspartat",
                "include_keyword": [
                    r"l-ornithin\s*-\s*l-\s*aspartat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lacidipin",
                "include_keyword": [
                    r"^lacidipin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lactobacillus acidophilus",
                "include_keyword": [
                    r"lactobacillus acidophilus"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lactulose",
                "include_keyword": [
                    r"^lactulose\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lamivudin + Tenofovir",
                "include_keyword": [
                    r"lamivudin\s*\+\s*tenofovir"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lamivudin",
                "include_keyword": [
                    r"^lamivudin$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lansoprazol",
                "include_keyword": [
                    r"^lan(s|z)oprazol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lercanidipin",
                "include_keyword": [
                    r"^lercanidipin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Letrozol",
                "include_keyword": [
                    r"^letrozol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Levetiracetam",
                "include_keyword": [
                    r"^levetiracetam\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Levobupivacain",
                "include_keyword": [
                    r"^levobupivacain\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Levocetirizin",
                "include_keyword": [
                    r"^levocetirizin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Levodopa + Carbidopa",
                "include_keyword": [
                    r"levodopa\s*\+\s*carbidopa"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Levofloxacin",
                "include_keyword": [
                    r"^levofloxacin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Levomepromazin",
                "include_keyword": [
                    r"^levomepromazin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Levosulpirid",
                "include_keyword": [
                    r"^levosulpirid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Levothyroxin (muối natri)",
                "include_keyword": [
                    r"^levothyroxin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lidocain + Adrenalin",
                "include_keyword": [
                    r"lidocain(e)?.*(adrenalin|epinephrin)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lidocain + Prilocain",
                "include_keyword": [
                    r"lidocain\s*\+\s*prilocain"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lidocain",
                "include_keyword": [
                    r"^lidocaine?"
                ],
                "exclude_keyword": [r"adrenalin", r"epinephrin", r"prilocain", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Linagliptin",
                "include_keyword": [
                    r"^linagliptin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Linezolid*",
                "include_keyword": [
                    r"^linezolid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lipidosterol",
                "include_keyword": [
                    r"serenoa\s*repens"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lisinopril + Hydroclorothiazid",
                "include_keyword": [
                    r"lisinopril.*hydroc(h)?lorothiazid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lisinopril",
                "include_keyword": [
                    r"^lisinopril\b"
                ],
                "exclude_keyword": [r"amlodipine", r"hydroc(h)?lorothiazid", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Loperamid",
                "include_keyword": [
                    r"^loperamid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Loratadin",
                "include_keyword": [
                    r"^loratadin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Losartan + Hydroclorothiazid",
                "include_keyword": [
                    r"losartan.*hydroc(h)?lorothiazid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Losartan",
                "include_keyword": [
                    r"^losartan\b"
                ],
                "exclude_keyword": [r"amlodipine", r"hydroc(h)?lorothiazid", r"\+", r";"],
                "is_regex": True
            },
            {
                "output_value": "Loteprednol",
                "include_keyword": [
                    r"^loteprednol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lovastatin",
                "include_keyword": [
                    r"^lovastatin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Loxoprofen",
                "include_keyword": [
                    r"^loxoprofen\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lynestrenol",
                "include_keyword": [
                    r"^lynestrenol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Lysin + Vitamin + Khoáng chất",
                "include_keyword": [
                    r"^lysin\s*\+\s*vitamin\s*\+\s*khoáng chất"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Macrogol + Điện giải",
                "include_keyword": [
                    r"macrogol.*natri sulfat.*natri bicarbonat.*natri clorid.*kali clorid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Macrogol",
                "include_keyword": [
                    r"^macrogol\b",
                    r"mỗi gói 10g chứa:\s*macrogol"
                ],
                "exclude_keyword": [r"natri sulfat", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Magnesi aspartat + Kali aspartat",
                "include_keyword": [
                    r"magnesi aspartat.*kali aspartat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vitamin B6 + magnesi lactat",
                "include_keyword": [
                    r"(magnesi(um)?\s*lactat(e)?.*(pyridoxin|vitamin b6)|(pyridoxin|vitamin b6).*magnesi(um)?\s*lactat(e)?)",
                    r"vitamin\s*b6\s*\+\s*magnesi",
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Magnesi sulfat",
                "include_keyword": [
                    r"magnesi su(l)?fat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Magnesi trisilicat + Nhôm hydroxyd",
                "include_keyword": [
                    r"magnesi trisilicat\s*\+\s*nhôm hydroxyd"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Mebendazol",
                "include_keyword": [
                    r"^mebendazol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Mebeverin",
                "include_keyword": [
                    r"^mebeverin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Meclofenoxat",
                "include_keyword": [
                    r"^meclop?henoxat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Mecobalamin",
                "include_keyword": [
                    r"^mecobalamin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Meglumin natri succinat",
                "include_keyword": [
                    r"^meglumin natri succinat\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Meloxicam",
                "include_keyword": [
                    r"^meloxicam\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Mequitazin",
                "include_keyword": [
                    r"^mequitazin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Meropenem*",
                "include_keyword": [
                    r"^meropenem"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Mesalazin (mesalamin)",
                "include_keyword": [
                    r"^(mesalamin|mesalazin)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Mesna",
                "include_keyword": [
                    r"^mesna\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Metformin",
                "include_keyword": [
                    r"^metformin\b"
                ],
                "exclude_keyword": [r"glibenclamid", r"glimepirid", r"gliclazid", r"sitagliptin", r"vildagliptin", r"saxagliptin", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Methimazol",
                "include_keyword": [
                    r"^(methimazol|thiamazol)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Methocarbamol",
                "include_keyword": [
                    r"^methocarbamol\b"
                ],
                "exclude_keyword": [r"paracetamol"],
                "is_regex": True
            },
            {
                "output_value": "Methotrexat",
                "include_keyword": [
                    r"^methotrexat\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Methoxy polyethylene glycol epoetin beta",
                "include_keyword": [
                    r"methoxy polyethylene glycol epoetin beta"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Methylergometrin",
                "include_keyword": [
                    r"^methyl(\s*)ergometrin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Methyldopa",
                "include_keyword": [
                    r"^methyldopa\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Methylphenidat",
                "include_keyword": [
                    r"^methylphenidate\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Methylprednisolon",
                "include_keyword": [
                    r"methyl\s*prednisolon"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Metoclopramid",
                "include_keyword": [
                    r"^metoclopramid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Metoprolol",
                "include_keyword": [
                    r"^metoprolol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Metronidazol + Neomycin + Nystatin",
                "include_keyword": [
                    r"(metronidazol.*neomycin.*nystatin|nystatin.*metronidazol.*neomycin)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Metronidazol",
                "include_keyword": [
                    r"^metronidazol"
                ],
                "exclude_keyword": [r"neomycin", r"nystatin", r"spiramycin", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Miconazol",
                "include_keyword": [
                    r"^miconazol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Midazolam",
                "include_keyword": [
                    r"^midazolam\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Milrinon",
                "include_keyword": [
                    r"^milrinon\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Mirtazapin",
                "include_keyword": [
                    r"^mirtazapin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Misoprostol",
                "include_keyword": [
                    r"^misoprostol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Molnupiravir",
                "include_keyword": [
                    r"^molnupiravir\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Mometason + Acid salicylic",
                "include_keyword": [
                    r"mometason.*salicylic acid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Mometason",
                "include_keyword": [
                    r"^mometason"
                ],
                "exclude_keyword": [r"salicylic"],
                "is_regex": True
            },
            {
                "output_value": "Prednisolon acetat (natri phosphate)",
                "include_keyword": [
                    r"monobasic natri phosphat.*dibasic natri phosphat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Montelukast",
                "include_keyword": [
                    r"montelukast\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Morphin",
                "include_keyword": [
                    r"^morphin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Moxifloxacin",
                "include_keyword": [
                    r"^moxifloxacin\b"
                ],
                "exclude_keyword": [r"dexamethason", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Mupirocin",
                "include_keyword": [
                    r"^mupirocin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Mycophenolat mofetil",
                "include_keyword": [
                    r"^mycophenolat\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Nabumeton",
                "include_keyword": [
                    r"^nabumeton\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Naloxon",
                "include_keyword": [
                    r"^naloxon\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Naphazolin",
                "include_keyword": [
                    r"^naphazolin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Naproxen + Esomeprazol",
                "include_keyword": [
                    r"naproxen\s*\+\s*esomeprazol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Naproxen",
                "include_keyword": [
                    r"^naproxen\b"
                ],
                "exclude_keyword": [r"esomeprazol", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Natamycin",
                "include_keyword": [
                    r"^natamycin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Natri hydrocarbonat (natri bicarbonat)",
                "include_keyword": [
                    r"natri (bicarbonat(e)?|hydrocarbonat)"
                ],
                "exclude_keyword": [r"kali", r"dextrose", r"glucose"],
                "is_regex": True
            },
            {
                "output_value": "Natri carboxymethylcellulose (natri CMC)",
                "include_keyword": [
                    r"natri carbox(y\s*)?methylcellulose"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Natri clorid",
                "include_keyword": [
                    r"^natri ch?lorid$",
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Dung dịch đa điện giải",
                "include_keyword": [
                    r"natri clorid.*natri acetat.*calci clorid.*magnesi clorid.*kali clorid",
                    r"sodiumchloride.*sodiumlactate.*potassium chloride.*calciumchloridedihydrate"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Natri diquafosol",
                "include_keyword": [
                    r"natri diquafosol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Natri hyaluronat",
                "include_keyword": [
                    r"natri hyaluronat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Phenobarbital",
                "include_keyword": [
                    r"phenobarbital\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Valproic acid",
                "include_keyword": [
                    r"valproat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Nebivolol",
                "include_keyword": [
                    r"^nebivolol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Nefopam",
                "include_keyword": [
                    r"^nefopam\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Nystatin + neomycin + polymyxin B",
                "include_keyword": [
                    r"(neomycin.*nystatin.*polymyxin|nystatin.*neomycin.*polymyxin)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Neostigmin",
                "include_keyword": [
                    r"^neostigmin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Nepafenac",
                "include_keyword": [
                    r"^nepafenac\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Netilmicin",
                "include_keyword": [
                    r"^netilmicin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Nicardipin",
                "include_keyword": [
                    r"^nicardipin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Nicorandil",
                "include_keyword": [
                    r"^nicorandil\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vitamin PP",
                "include_keyword": [
                    r"^nicotinamid\b",
                    r"^vitamin pp$"
                ],
                "exclude_keyword": [r"succinic"],
                "is_regex": True
            },
            {
                "output_value": "Nifedipin",
                "include_keyword": [
                    r"^nifedipine?\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Nimodipin",
                "include_keyword": [
                    r"^nimodipin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Nizatidin",
                "include_keyword": [
                    r"^nizatidin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Nor-epinephrin (Nor- adrenalin)",
                "include_keyword": [
                    r"nor(-|\s*)adrenalin",
                    r"nor(-|\s*)epinephrin",
                    'Nor- adrenalin'
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Norethisteron",
                "include_keyword": [
                    r"^norethisteron\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Nystatin",
                "include_keyword": [
                    r"^nystatin$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Nước cất pha tiêm",
                "include_keyword": [
                    r"nước (cất pha tiêm|để pha thuốc tiêm)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Hydro peroxyd",
                "include_keyword": [
                    r"nước oxy già"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Octreotid",
                "include_keyword": [
                    r"^octreotide?\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ofloxacin",
                "include_keyword": [
                    r"^ofloxacin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Olanzapin",
                "include_keyword": [
                    r"^olanzapin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Olopatadin",
                "include_keyword": [
                    r"^olopatadin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Omeprazol",
                "include_keyword": [
                    r"^omeprazol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ondansetron",
                "include_keyword": [
                    r"^ondansetron\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Oseltamivir",
                "include_keyword": [
                    r"^oseltamivir"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Otilonium bromide",
                "include_keyword": [
                    r"^otilonium\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Oxacilin",
                "include_keyword": [
                    r"^oxacil(l)?in\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Oxaliplatin",
                "include_keyword": [
                    r"^oxaliplatin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Oxcarbazepin",
                "include_keyword": [
                    r"^oxcarbazepine?\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Oxy dược dụng",
                "include_keyword": [
                    r"^oxy dược dụng$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Oxytocin",
                "include_keyword": [
                    r"^oxytocin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Paclitaxel",
                "include_keyword": [
                    r"^paclitaxel\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Palonosetron",
                "include_keyword": [
                    r"^palonosetron\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Acid pamidronic",
                "include_keyword": [
                    r"pamidronat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Panax notoginseng saponins",
                "include_keyword": [
                    r"panax notoginseng"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Pantoprazol",
                "include_keyword": [
                    r"^pantoprazol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Papaverin",
                "include_keyword": [
                    r"^papaverin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Paracetamol + chlorpheniramin + phenylephrine + dextromethorphan",
                "include_keyword": [
                    r"paracetamol.*chlorpheniramin.*phenylephrin.*dextromethorphan"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Paracetamol + Chlorpheniramin + Phenylephrin",
                "include_keyword": [
                    r"paracetamol.*(c(h)?lorpheniramin.*phenylephrin|phenylephrin.*c(h)?lorpheniramin)"
                ],
                "exclude_keyword": [r"dextromethorphan"],
                "is_regex": True
            },
            {
                "output_value": "Paracetamol + Chlorpheniramin",
                "include_keyword": [
                    r"paracetamol.*c(h)?lorpheniramin"
                ],
                "exclude_keyword": [r"phenylephrin", r"dextromethorphan"],
                "is_regex": True
            },
            {
                "output_value": "Paracetamol + Codein",
                "include_keyword": [
                    r"paracetamol.*codein"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Paracetamol + Diphenhydramin + Phenylephrin",
                "include_keyword": [
                    r"paracetamol.*diphenhydramin.*phenylephrin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Paracetamol + Diphenhydramin",
                "include_keyword": [
                    r"paracetamol.*diphenhydramin"
                ],
                "exclude_keyword": [r"phenylephrin"],
                "is_regex": True
            },
            {
                "output_value": "Paracetamol + Ibuprofen",
                "include_keyword": [
                    r"paracetamol.*ibuprofen"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Paracetamol + Methocarbamol",
                "include_keyword": [
                    r"paracetamol.*methocarbamol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Paracetamol + phenylephrin + dextromethorphan",
                "include_keyword": [
                    r"paracetamol.*phenylephrin.*dextromethorphan"
                ],
                "exclude_keyword": [r"chlorpheniramin"],
                "is_regex": True
            },
            {
                "output_value": "Paracetamol + Tramadol",
                "include_keyword": [
                    r"paracetamol.*tramadol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Paroxetin",
                "include_keyword": [
                    r"^paroxetin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Pegfilgrastim",
                "include_keyword": [
                    r"^pegfilgrastim\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Pemirolast",
                "include_keyword": [
                    r"^pemirolast\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Pentoxifyllin",
                "include_keyword": [
                    r"^pentoxifyllin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Cerebrolysin",
                "include_keyword": [
                    r"cerebrolysin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Perindopril + Amlodipin",
                "include_keyword": [
                    r"perindopril.*amlodip(in|ine)"
                ],
                "exclude_keyword": [r"indapamid"],
                "is_regex": True
            },
            {
                "output_value": "Perindopril",
                "include_keyword": [
                    r"^perindopril\b"
                ],
                "exclude_keyword": [r"amlodip", r"indapamid", r"\+", r";"],
                "is_regex": True
            },
            {
                "output_value": "Pethidin",
                "include_keyword": [
                    r"^pethidin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Phenylephrin",
                "include_keyword": [
                    r"^phenylephrin\b"
                ],
                "exclude_keyword": [r"paracetamol", r"tropicamid"],
                "is_regex": True
            },
            {
                "output_value": "Phenytoin",
                "include_keyword": [
                    r"^phenytoin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Phloroglucinol hydrat + trimethyl phloroglucinol",
                "include_keyword": [
                    r"phloroglucinol.*trimethylphloroglucinol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Phytomenadion (vitamin K1)",
                "include_keyword": [
                    r"phytomenadion",
                    r"^vitamin k1$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Hỗn hợp Terpen (Pinene + Camphene + Cineol...)",
                "include_keyword": [
                    r"pinene\s*\+\s*camphene"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Pipecuronium",
                "include_keyword": [
                    r"^pipecuronium\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Piperacilin + Tazobactam",
                "include_keyword": [
                    r"piperacil(l)?in.*tazobactam"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Piperacilin",
                "include_keyword": [
                    r"^piperacil(l)?in\b"
                ],
                "exclude_keyword": [r"tazobactam", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Piracetam",
                "include_keyword": [
                    r"^piracetam\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Pirenoxin",
                "include_keyword": [
                    r"^pirenoxin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Piroxicam",
                "include_keyword": [
                    r"^piroxicam\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tinh bột este hóa (hydroxyethyl starch)",
                "include_keyword": [
                    r"poly-\(o-2-hydroxyethyl\)\s*starch",
                    r"tinh bột este hóa"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Polyethylen glycol + Propylen glycol",
                "include_keyword": [
                    r"polyethylen(e)?\s*glycol.*propylen\s*glycol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Povidon iodin",
                "include_keyword": [
                    r"povidon(e)?\s*iod"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Pralidoxim",
                "include_keyword": [
                    r"^pralidoxim"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Pramipexol",
                "include_keyword": [
                    r"^pramipexol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Pravastatin",
                "include_keyword": [
                    r"^pravastatin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Praziquantel",
                "include_keyword": [
                    r"^praziquantel\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Prednisolon",
                "include_keyword": [
                    r"^prednisolon"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Prednison",
                "include_keyword": [
                    r"^prednison\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Pregabalin",
                "include_keyword": [
                    r"^pregabalin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Probenecid",
                "include_keyword": [
                    r"^probenecid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Procain",
                "include_keyword": [
                    r"^procain\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Progesteron",
                "include_keyword": [
                    r"^progesteron"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Promethazin",
                "include_keyword": [
                    r"^promethazin"
                ],
                "exclude_keyword": [r"carbocistein"],
                "is_regex": True
            },
            {
                "output_value": "Proparacain",
                "include_keyword": [
                    r"^proparacain\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Propofol",
                "include_keyword": [
                    r"^propofol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Propranolol",
                "include_keyword": [
                    r"^propranolol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Propylthiouracil (PTU)",
                "include_keyword": [
                    r"^propylthiouracil\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Pyrazinamid",
                "include_keyword": [
                    r"^pyrazinamide?\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vitamin B6",
                "include_keyword": [
                    r"^pyridoxin\b",
                    r"^vitamin b6$"
                ],
                "exclude_keyword": [r"thiamin", r"magnesi", r"vitamin b1", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Quetiapin",
                "include_keyword": [
                    r"^quetiapin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Quinapril",
                "include_keyword": [
                    r"^quinapril\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Rabeprazol",
                "include_keyword": [
                    r"^rabeprazol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Racecadotril",
                "include_keyword": [
                    r"^racecadotril\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ramipril",
                "include_keyword": [
                    r"^ramipril\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ranibizumab",
                "include_keyword": [
                    r"^ranibizumab\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Rebamipid",
                "include_keyword": [
                    r"^rebamipid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Repaglinid",
                "include_keyword": [
                    r"^repaglinid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ribavirin",
                "include_keyword": [
                    r"^ribavirin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Rifamycin",
                "include_keyword": [
                    r"^rifamycin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Acid risedronic",
                "include_keyword": [
                    r"^risedronat\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Risperidon",
                "include_keyword": [
                    r"^risperidon"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Rituximab",
                "include_keyword": [
                    r"^rituximab\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Rivaroxaban",
                "include_keyword": [
                    r"^rivaroxaban\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Rocuronium",
                "include_keyword": [
                    r"^rocuronium\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ropivacain",
                "include_keyword": [
                    r"^ropivacain\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Rosuvastatin",
                "include_keyword": [
                    r"^rosuvastatin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Rotundin",
                "include_keyword": [
                    r"^rotundin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Roxithromycin",
                "include_keyword": [
                    r"^roxithromycin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Rupatadine",
                "include_keyword": [
                    r"^rupatadine?\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Saccharomyces boulardii",
                "include_keyword": [
                    r"saccharomyces boulardii"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Salbutamol",
                "include_keyword": [
                    r"^salbutamol\b"
                ],
                "exclude_keyword": [r"ipratropium", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Saxagliptin + Metformin",
                "include_keyword": [
                    r"saxagliptin\s*\+\s*metformin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Saxagliptin",
                "include_keyword": [
                    r"^saxagliptin\b"
                ],
                "exclude_keyword": [r"metformin"],
                "is_regex": True
            },
            {
                "output_value": "Sertralin",
                "include_keyword": [
                    r"^sertralin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sevofluran",
                "include_keyword": [
                    r"^sevofluran"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Silymarin",
                "include_keyword": [
                    r"^silymarin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Simethicon",
                "include_keyword": [
                    r"^simethicon$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Simvastatin",
                "include_keyword": [
                    r"^simvastatin\b"
                ],
                "exclude_keyword": [r"ezetimibe", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Sitagliptin + Metformin",
                "include_keyword": [
                    r"sitagliptin\s*\+\s*metformin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sitagliptin",
                "include_keyword": [
                    r"^sitagliptin\b"
                ],
                "exclude_keyword": [r"metformin", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Sofosbuvir + Velpatasvir",
                "include_keyword": [
                    r"sofosbuvir\s*\+\s*velpatasvir"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sofosbuvir + Ledipasvir",
                "include_keyword": [
                    r"sofosbuvir\s*\+\s*ledipasvir"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sorafenib",
                "include_keyword": [
                    r"^sorafenib\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sorbitol",
                "include_keyword": [
                    r"sorbitol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sotalol",
                "include_keyword": [
                    r"^sotalol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Spiramycin + Metronidazol",
                "include_keyword": [
                    r"spiramycin\s*\+\s*metronidazol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Spiramycin",
                "include_keyword": [
                    r"^spiramycin\b"
                ],
                "exclude_keyword": [r"metronidazol"],
                "is_regex": True
            },
            {
                "output_value": "Spironolacton",
                "include_keyword": [
                    r"^spironolacton"
                ],
                "exclude_keyword": [r"furosemid"],
                "is_regex": True
            },
            {
                "output_value": "Succinic acid + Hỗn hợp vitamin/nucleotid",
                "include_keyword": [
                    r"succinic acid.*nicotinamid.*inosine"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sucralfat",
                "include_keyword": [
                    r"^sucralfat\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sugammadex",
                "include_keyword": [
                    r"^sugammadex\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sulfadiazin bạc",
                "include_keyword": [
                    r"sulfadiazin bạc"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sulfamethoxazol + Trimethoprim",
                "include_keyword": [
                    r"sulfamethoxazol\s*\+\s*trimethoprim"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sulfasalazin",
                "include_keyword": [
                    r"^sulfasalazin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sulpirid",
                "include_keyword": [
                    r"^sulpirid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sumatriptan",
                "include_keyword": [
                    r"^sumatriptan\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Surfactant (Phospholipid chiết xuất từ phổi lợn hoặc phổi bò; hoặc chất diện hoạt chiết xuất từ phổi bò (Bovine lung surfactant))",
                "include_keyword": [
                    r"surfactant",
                    r"phospholipid chiết (xuất )?từ phổi"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Suxamethonium",
                "include_keyword": [
                    r"^suxamethonium\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Khoáng chất đa lượng và vi lượng",
                "include_keyword": [
                    r"sắt clorid.*kẽm clorid.*mangan.*đồng.*crôm",
                    r"sắt gluconat.*mangan gluconat.*đồng gluconat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sắt protein succinylat",
                "include_keyword": [
                    r"sắt protein succinylat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Sắt (nguyên chất / phức hợp đơn chất)",
                "include_keyword": [
                    r"^sắt (nguyên tố|sucrose|\(iii\)\s*hydroxyd polymaltose)"
                ],
                "exclude_keyword": [r"acid folic", r"mangan", r"clorid"],
                "is_regex": True
            },
            {
                "output_value": "Tacrolimus",
                "include_keyword": [
                    r"^tacrolimus\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tafluprost",
                "include_keyword": [
                    r"^tafluprost\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tamoxifen",
                "include_keyword": [
                    r"^tamoxifen\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tamsulosin",
                "include_keyword": [
                    r"^tamsulosin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Teicoplanin*",
                "include_keyword": [
                    r"^teicoplanin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Telmisartan + Hydroclorothiazid",
                "include_keyword": [
                    r"telmisartan.*hydroc(h)?lorothiazid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Telmisartan",
                "include_keyword": [
                    r"^telmisartan\b"
                ],
                "exclude_keyword": [r"amlodip", r"hydroc(h)?lorothiazid", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Tenofovir (TDF)",
                "include_keyword": [
                    r"^tenofovir\b"
                ],
                "exclude_keyword": [r"lamivudin"],
                "is_regex": True
            },
            {
                "output_value": "Tenoxicam",
                "include_keyword": [
                    r"^tenoxicam\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Terbinafin (hydroclorid)",
                "include_keyword": [
                    r"^terbinafin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Terbutalin",
                "include_keyword": [
                    r"^terbutalin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Terlipressin",
                "include_keyword": [
                    r"^terlipressin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tetracain",
                "include_keyword": [
                    r"^tetracain\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tetracyclin",
                "include_keyword": [
                    r"tetracyclin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vitamin B1 + B6 + B12",
                "include_keyword": [
                    r"(thiamin.*pyridox.*cyanocobalamin|vitamin b1.*b6.*b12|vitamin b1.*vitamin b6.*vitamin b12)",
                    'vitamin b1 (thiamin mononitrat) + vitamin b12 (cyanocobalamin) + vitamin B6 (pyridoxin hydroclorid)',
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Thiamin (Vitamin B1)",
                "include_keyword": [
                    r"^thiamin\b",
                    r"^vitamin b1\b"
                ],
                "exclude_keyword": [r"pyridox", r"cyanocobalamin", r"vitamin b6", r"b12", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Thiocolchicosid",
                "include_keyword": [
                    r"^thiocolchicosid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tianeptin",
                "include_keyword": [
                    r"^tianeptin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tiaprofenic acid",
                "include_keyword": [
                    r"tiaprofenic acid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ticagrelor",
                "include_keyword": [
                    r"^ticagrelor\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ticarcillin + acid clavulanic",
                "include_keyword": [
                    r"ticarci(l)?lin.*(acid\s*)?clavulanic"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tigecyclin*",
                "include_keyword": [
                    r"^tigecyclin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Timolol",
                "include_keyword": [
                    r"^timolol\b"
                ],
                "exclude_keyword": [r"brinzolamid", r"travoprost", r"brimonidin", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Tinidazol",
                "include_keyword": [
                    r"^tinidazol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tiotropium",
                "include_keyword": [
                    r"^tiotropium\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tiropramid",
                "include_keyword": [
                    r"^tiropramid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tizanidin",
                "include_keyword": [
                    r"^tizanidin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tobramycin",
                "include_keyword": [
                    r"^tobramycin\b"
                ],
                "exclude_keyword": [r"dexamethason", r"\+"],
                "is_regex": True
            },
            {
                "output_value": "Tofisopam",
                "include_keyword": [
                    r"^tofisopam\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tolperison",
                "include_keyword": [
                    r"^tolperison\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Topiramat",
                "include_keyword": [
                    r"^topiramat\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tramadol",
                "include_keyword": [
                    r"^tramadol\b"
                ],
                "exclude_keyword": [r"paracetamol"],
                "is_regex": True
            },
            {
                "output_value": "Travoprost + Timolol",
                "include_keyword": [
                    r"travoprost.*timolol"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Travoprost",
                "include_keyword": [
                    r"^travoprost\b"
                ],
                "exclude_keyword": [r"timolol"],
                "is_regex": True
            },
            {
                "output_value": "Tretinoin + Erythromycin",
                "include_keyword": [
                    r"tretinoin\s*\+\s*erythromycin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Triamcinolon acetonid",
                "include_keyword": [
                    r"^triamcinolon acetonid\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tricalci phosphat",
                "include_keyword": [
                    r"tricalcium phosphat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Triclabendazol",
                "include_keyword": [
                    r"^triclabendazol\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Trihexyphenidyl",
                "include_keyword": [
                    r"^trihexyphenidyl\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Trimebutin",
                "include_keyword": [
                    r"^trimebutin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Trimetazidin",
                "include_keyword": [
                    r"^trimetazidin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Triptorelin",
                "include_keyword": [
                    r"^triptorelin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tropicamid + Phenylephrin",
                "include_keyword": [
                    r"tropicamid(e)?\s*\+\s*phenyl(-)?ephrine"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tropicamid",
                "include_keyword": [
                    r"^tropicamid\b"
                ],
                "exclude_keyword": [r"phenyl"],
                "is_regex": True
            },
            {
                "output_value": "Tyrothricin + benzocain+ benzalkonium",
                "include_keyword": [
                    r"tyrothricin\s*\+\s*benzocaine\s*\+\s*benzalkonium"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Tyrothricin",
                "include_keyword": [
                    r"^tyrothricin$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Urea",
                "include_keyword": [
                    r"^urea\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Ursodeoxycholic acid",
                "include_keyword": [
                    r"ursodeoxycholic acid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Valsartan + Hydroclorothiazid",
                "include_keyword": [
                    r"valsartan.*hydroc(h)?lorothiazid"
                ],
                "exclude_keyword": [r"amlodipin"],
                "is_regex": True
            },
            {
                "output_value": "Valsartan",
                "include_keyword": [
                    r"^valsartan$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vancomycin",
                "include_keyword": [
                    r"^vancomycin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Verapamil",
                "include_keyword": [
                    r"^verapamil\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vildagliptin + Metformin",
                "include_keyword": [
                    r"vildagliptin\s*\+\s*metformin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vildagliptin",
                "include_keyword": [
                    r"^vildagliptin\b"
                ],
                "exclude_keyword": [r"metformin"],
                "is_regex": True
            },
            {
                "output_value": "Vincristin",
                "include_keyword": [
                    r"^vincristin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vinpocetin",
                "include_keyword": [
                    r"^vinpocetin\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vitamin A + D2 (Vitamin A + D3)",
                "include_keyword": [
                    r"vitamin a\s*\+\s*(vitamin\s*)?d",
                    r"vitamin\s*a\s*\(\s*retinol\s*palmitat\s*\)\s*\+\s*vitamin\s*d3\s*\(\s*cholecalciferol\s*\)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vitamin A",
                "include_keyword": [
                    r"^vitamin a$"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vitamin D3",
                "include_keyword": [
                    r"^vitamin d3\b",
                    'vitamin d3 (cholecalciferol)'
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vitamin E",
                "include_keyword": [
                    r"^vitamin e\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Vitamin H (B8)",
                "include_keyword": [
                    r"vitamin h \(b8\)"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Xylometazolin",
                "include_keyword": [
                    r"^xylometazolin"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Zoledronic acid",
                "include_keyword": [
                    r"zoledronic acid"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Zopiclon",
                "include_keyword": [
                    r"^zopiclon\b"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Đồng sulfat",
                "include_keyword": [
                    r"dong sulfat"
                ],
                "exclude_keyword": [],
                "is_regex": True
            },
            {
                "output_value": "Nhũ dịch lipid",
                "include_keyword": [
                    'nhu dich lipid',
                    'Nhu dich lipid (dau dau nanh; lecithin trung; glycerol)'
                ],
                "exclude_keyword": [],
            },
            {
                "output_value": "Manitol",
                "include_keyword": [
                    'manitol',
                ],
                "exclude_keyword": [],
            }
        ]
    }

}