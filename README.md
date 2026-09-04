# Set up
### Tải code từ github
- __Bước 1:__ Tạo một folder mới để chưa code
- __Bước 2:__ Mở folder trong VSCode và sử dụng Terminal trong VSCode, hoặc thao tác chuột phải -> open in Terminal
- __Bước 3:__ Nhập câu lệnh `git clone https://github.com/hogDuc/data-nganh-duoc.git`

__Lưu ý:__ cần phải cài đặt git trước nếu chưa có trong máy. [Link](https://git-scm.com/install/windows)
### Cài đặt thư viện
Chạy code `pip install -r requirements.txt` trong terminal hoặc notebook (.ipynb) để cài các thư viện cần thiết
### Chuẩn bị dữ liệu
Tải dữ liệu raw từ APD, đưa vào folder [data](data/raw/).
### File .env
Đây là file chứa đường dẫn quan trọng cho codebase. Để tạo file `.env`, copy paste file [.env.example](.env.example) vào folder hiện tại và đưa đường dẫn folder cần thiết vào.

_Ví dụ:_
```
DRUG_TYPES_TEMPLATE = "D:/Users/OneDrive - fpts.com.vn/work/Dược/data/template/drug_type.xlsx"
```
# Hướng dẫn sử dụng

## Tính năng

Hiện tại, Codebase cho phép người dùng thực hiện các tác vụ sau:
- **Xử lý và chuẩn hóa dữ liệu raw:** Chuẩn hóa tên quốc gia, nhà sản xuất, các hoạt chất dựa theo tùy chỉnh của người dùng tại file [config](config/filter_config.py). Gán Loại thuốc 1, 2 tương ứng cho các hoạt chất dựa theo [template](data/template/drug_type.xlsx).
- **Lọc dữ liệu** theo yêu cầu của người dùng (Filter theo loại thuốc, hoạt chất, nhóm thuốc, nhà sản xuất, nước sản xuất,...).
- **Tính tổng, trung bình** giá trị thành tiền, số lượng, giá tiền theo bộ lọc, hoặc theo nhóm (groupby).

__Truy cập file demo tại [đây]('tests/example.ipynb').__
## Cài đặt filter

Để thực hiện chuẩn hóa dữ liệu cho việc lọc (filter), người dùng cần nhập các "quy tắc" filter. Hiện tại đã có sẵn bộ quy tắc tại file [config](config/filter_config.py). Người dùng sẽ cần nhập thêm trong các trường hợp:
1. Có các value mới (ví dụ cần theo dõi thêm các doanh nghiệp mới, thêm loại hoạt chất mới vào danh sách theo dõi,...)
2. Trong quá trình sử dụng dữ liệu, vẫn còn sót các giá trị chưa được lọc. Phương pháp kiểm tra chất lượng lọc xem trong file [DEMO]('tests/example.ipynb').

### Cách 1: Sử dụng Antigravity extension để nhập giá trị filter mới

Trong trường hợp còn sót các giá trị chưa được lọc, hoặc thêm mới, ví dụ đối với bộ lọc theo quốc gia sản xuất có giá trị gốc là _'CSSX: Nhật Bản; CSĐG: Anh; CSkiểm tra chất lượng và XX lô: Thụy Điển'_:
- **Bước 1**: Vào chatbox Antigravity, nhập `/standardize_country` để sử dụng skill và đưa giá trị raw ở trên vào ô chat. 

    `/standardize-country 'CSSX: Nhật Bản; CSĐG: Anh; CSkiểm tra chất lượng và XX lô: Thụy Điển'`
- **Bước 2**: Enter và chatbot sẽ trả về đoạn dictionary như sau
    ```{
        "output_value": "Nhật Bản",
        "include_keyword": [
            r"(?:cssx|co so (?:san xuat|sx)|nuoc (?:san xuat|sx)|s(?:an )?x(?:uat)?|nsx|dc cssx)[^;:\n]*[:\s]+(?:nhat(?: ban)?|japan)\b",
        ],
        "exclude_keyword": [],
        "is_regex": True,
    }```
- **Bước 3**: Copy paste phần 'include_keyword' vào file [config](config/filter_config.py)

### Cách 2: Cài đặt thủ công

Để điều chỉnh, thêm, bớt các filter cho dữ liệu, truy cập [file]('config/filter_config.py').

Về cấu trúc của filter gồm các mục bắt buộc sau:
```
    input_col: Tên cột cần lọc của dữ liệu gốc, ví dụ 'nhasx'
    output_col: Tên cột gán nhãn cho đầu ra, ví dụ 'ticker'
    filter: Bộ lọc chính
        [
            output_value: Giá trị đã chuẩn hóa cho output, ví dụ phân loại theo nhà sản xuất thì sẽ đưa vào tên nhà sản xuất
            include_keyword: Các từ khóa để lọc trong dữ liệu
            exclude_keyword: Các từ khóa để loại ra các trường hợp bị lẫn
            is_regex: True cho một số trường hợp đặc biệt. Ví dụ 'sản xuất trung gian'
        ]
```
_Ví dụ:_
```
producer_config:{
    "input_col":'nhasx',
    "output_col":"ticker",
    'filter':[
        {
            "output_value": "IMP",
            "include_keyword": ["imexpharm"],
            "exclude_keyword": ["agimexpharm"]
        },
    ]
}
```

**Lưu ý:**
- Các phần config cần phải được đưa vào đúng loại config: 
    - Nhà sản xuất -> `producer_config`
    - Quốc gia sản xuất -> `country_config`
    - Hoạt chất -> `active_ingred_config`
- Các keyword viết dưới dạng __không dấu, viết thường__, không viết hoa.
- Các keyword BẮT BUỘC phải để trong ngoặc `''` hoặc `""`, và chuỗi các keyword phải được đặt trong ngoặc `[]`.
- Các mục phải được ngăn cách bởi dấu `,`.
- Nếu không có exclude thì để giá trị list trống `[]`.
