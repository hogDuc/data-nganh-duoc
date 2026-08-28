from datetime import datetime
from typing import Any, Optional, Union
import pandas as pd
from pydantic import BaseModel, ConfigDict, field_validator


class MedicineRecord(BaseModel):
    model_config = ConfigDict(populate_by_name=True, str_strip_whitespace=True)

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

    # Numerical Metrics (Quantities, Prices)
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

    # 1. Global validator for NaN and empty strings
    @field_validator("*", mode="before")
    @classmethod
    def handle_missing_and_empty(cls, v: Any) -> Any:
        if pd.isna(v) or v == "":
            return None
        return v

    # 2. Number validator (handles '1,000,000' commas)
    @field_validator("soluong", "gia", "thanhtien", mode="before")
    @classmethod
    def parse_numbers(cls, v: Any) -> Optional[float]:
        if v is None or pd.isna(v) or v == "":
            return 0.0
        if isinstance(v, (int, float)):
            return float(v)
        # Remove commas and whitespace
        clean_str = str(v).replace(",", "").strip()
        try:
            return float(clean_str)
        except ValueError:
            return 0.0

    # 3. Date validator (handles 'DD/MM/YYYY' and 'YYYY-MM-DD')
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
        if isinstance(v, (datetime, pd.Timestamp)):
            return v.to_pydatetime() if isinstance(v, pd.Timestamp) else v
        v_str = str(v).strip()
        for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y", "%Y/%m/%d"):
            try:
                return datetime.strptime(v_str, fmt)
            except ValueError:
                pass
        return None