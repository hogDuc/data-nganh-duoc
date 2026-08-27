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

    # Global validator: converts pandas NaN / float('nan') / empty strings to None before validating
    @field_validator("*", mode="before")
    @classmethod
    def handle_missing_and_empty(cls, v: Any) -> Any:
        if pd.isna(v) or v == "":
            return None
        return v