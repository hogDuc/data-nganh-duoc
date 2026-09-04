from datetime import datetime
from typing import Any, Optional, Union
import pandas as pd
from pydantic import BaseModel, ConfigDict, TypeAdapter, field_validator

'''
Schema hỗ trợ chuẩn hóa dữ liệu raw từ APD
Class MedicineRecord sẽ đảm bảo các cột có được đúng loại datatype và các cột dạng Mandatory như 'loai_thau', 'ma', 'ten' và 'hoatchat' không được trống
'''


class MedicineRecord(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True, str_strip_whitespace=True, extra="ignore"
    )

    # Mandatory
    loai_thau: str
    ma: str
    ten: str
    hoatchat: str

    # Optional Location & Facility info
    ma_tinh: Optional[str] = None
    ten_tinh: Optional[str] = None
    ten_don_vi: Optional[str] = None
    ma_cskcb: Optional[str] = None
    ten_cskcb: Optional[str] = None

    # Drug / Product Specifications
    ma_gy: Optional[str] = None
    duongdung: Optional[str] = None
    maduongdung: Optional[str] = None
    madd_gy: Optional[str] = None
    dangbaoche: Optional[str] = None
    hamluong: Optional[str] = None
    donggoi: Optional[str] = None
    sodk: Optional[str] = None
    nhasx: Optional[str] = None
    nuocsx: Optional[str] = None
    donvitinh: Optional[str] = None

    # Numerical Metrics
    soluong: Optional[float] = 0.0
    gia: Optional[float] = 0.0
    thanhtien: Optional[float] = 0.0

    # Contractor & Decision Details
    tennhathau: Optional[str] = None
    quyetdinh: Optional[str] = None
    goithau: Optional[str] = None
    tieuchuan: Optional[str] = None
    nhomthau: Optional[str] = None
    loai: Optional[str] = None
    sttpheduyet: Optional[str] = None
    hieuluc: Optional[str] = None
    ht_thau: Optional[str] = None

    # Date / Timestamp Fields
    created_date: Optional[datetime] = None
    tungay: Optional[datetime] = None
    denngay: Optional[datetime] = None
    congbo: Optional[datetime] = None
    tungay_hd: Optional[datetime] = None
    denngay_hd: Optional[datetime] = None

    # 1. Global validator for NaN and empty values
    @field_validator("*", mode="before")
    @classmethod
    def handle_missing_and_empty(cls, v: Any) -> Any:
        if pd.isna(v) or v == "" or str(v).strip().lower() in ("nan", "nat", "none"):
            return None
        return v

    # 2. Number validator
    @field_validator("soluong", "gia", "thanhtien", mode="before")
    @classmethod
    def parse_numbers(cls, v: Any) -> Optional[float]:
        if v is None or pd.isna(v) or v == "":
            return 0.0
        if isinstance(v, (int, float)):
            return float(v)
        clean_str = str(v).replace(",", "").strip()
        try:
            return float(clean_str)
        except ValueError:
            return 0.0

    # 3. Dedicated Date & Timestamp validator
    @field_validator(
        "created_date",
        "tungay",
        "denngay",
        "congbo",
        "tungay_hd",
        "denngay_hd",
        mode="before",
    )
    @classmethod
    def parse_dates(cls, v: Any) -> Optional[datetime]:
        if v is None or pd.isna(v) or v == "":
            return None

        if isinstance(v, pd.Timestamp):
            return v.to_pydatetime()
        if isinstance(v, datetime):
            return v

        v_str = str(v).strip()

        # Formats matching your exact APD export structure
        formats = (
            "%Y-%m-%d %H:%M:%S",  # e.g., '2025-04-11 00:00:00', '2025-10-25 22:21:51'
            "%Y-%m-%d",  # e.g., '2025-04-11'
            "%d/%m/%Y %H:%M:%S",  # e.g., '11/04/2025 00:00:00'
            "%d/%m/%Y",  # e.g., '11/04/2025'
        )

        for fmt in formats:
            try:
                return datetime.strptime(v_str, fmt)
            except ValueError:
                continue

        # Fallback to pandas robust parser
        try:
            parsed = pd.to_datetime(v_str)
            if pd.notna(parsed):
                return parsed.to_pydatetime()
        except Exception:
            pass

        return None