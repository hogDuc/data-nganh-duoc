# Set up
### Tải code từ github

__Bước 1:__ Tạo một folder mới để chưa code

__Bước 2:__ Mở folder trong VSCode và sử dụng Terminal trong VSCode, hoặc thao tác chuột phải -> open in Terminal

__Bước 3:__ Nhập câu lệnh `git clone https://github.com/hogDuc/data-nganh-duoc.git`

__Lưu ý:__ cần phải cài đặt git trước nếu chưa có trong máy. [Link](https://git-scm.com/install/windows)
### Cài đặt thư viện
Chạy code `pip install -r requirements.txt` trong terminal hoặc notebook (.ipynb) để cài các thư viện cần thiết
### Dữ liệu
Tải dữ liệu raw từ APD, đưa vào folder data/raw/
# Hướng dẫn sử dụng
### Cài đặt filter
__Thủ công__
Để điều chỉnh, thêm, bớt các filter cho dữ liệu, truy cập [file]('config/filter_config.py')

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
Ví dụ:
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

Lưu ý:
- Các keyword viết dưới dạng không dấu, viết thường, không viết hoa.
- Các keyword BẮT BUỘC phải để trong ngoặc '' hoặc "", và chuỗi các keyword phải được đặt trong ngoặc [].
- Các mục phải được ngăn cách bởi dấu ','
- Nếu không có exclude thì để giá trị []. 

__Sử dụng Antigravity extension để nhập giá trị filter mới__
Trong trường hợp còn sót các giá trị chưa được lọc, ví dụ đối với bộ lọc theo nhà sản xuất còn sót giá trị 'CSSX: Nhật Bản; CSĐG: Anh; CSkiểm tra chất lượng và XX lô: Thụy Điển':
- Bước 1: Vào chatbox Antigravity, nhập `/standardize_country` để sử dụng skill và đưa giá trị raw ở trên vào ô chat.
- Bước 2: Enter và chatbot sẽ trả về đoạn dictionary như sau
    ```{
        "output_value": "Nhật Bản",
        "include_keyword": [
            r"(?:cssx|co so (?:san xuat|sx)|nuoc (?:san xuat|sx)|s(?:an )?x(?:uat)?|nsx|dc cssx)[^;:\n]*[:\s]+(?:nhat(?: ban)?|japan)\b",
        ],
        "exclude_keyword": [],
        "is_regex": True,
    }```
- Bước 3: Copy paste phần 'include_keyword' vào file [config](config/filter_config.py)

### Demo
Truy cập hướng dẫn tại [đây]('tests/example.ipynb')