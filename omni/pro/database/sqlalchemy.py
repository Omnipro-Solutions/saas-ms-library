from typing import Optional

from sqlalchemy.orm import mapped_column as mapped_column_alchemy
from sqlalchemy.orm.properties import MappedColumn


class MappedColumnOmni(MappedColumn):
    def __init__(self, *args, is_filterable=True, is_exportable=True, is_importable=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.column.is_filterable = is_filterable
        self.column.is_exportable = is_exportable
        self.column.is_importable = is_importable


def mapped_column(
    *args,
    is_filterable: Optional[bool] = True,
    is_exportable: Optional[bool] = True,
    is_importable: Optional[bool] = True,
    **kwargs
):
    mc = mapped_column_alchemy(*args, **kwargs)
    mc.column.is_filterable = is_filterable
    mc.column.is_exportable = is_exportable
    mc.column.is_importable = is_importable
    return mc
