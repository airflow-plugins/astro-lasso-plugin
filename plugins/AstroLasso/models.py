from airflow.models import Base
from sqlalchemy.exc import InvalidRequestError
from airflow import logging
from sqlalchemy import (
    Column, Integer, String, DateTime, Text, Boolean, ForeignKey, PickleType,
    Index, Float)

try:
    class SchemaManager(Base):
        """
        Manage your schemas in airflow
        """
        __tablename__ = "astrolasso"

        id = Column(Integer(), primary_key=True)
        src_sys = Column(String(500))
        src_tbl = Column(String(500))
        src_col = Column(String(500))
        dst_sys = Column(String(500))
        dst_tbl = Column(String(500))
        dst_col = Column(String(500))

        def __init__(self,
                    src_sys=None, src_tbl=None, src_col=None,
                    dst_sys=None, dst_tbl=None, dst_col=None):

            self.src_sys = src_sys
            self.src_tbl = src_tbl
            self.src_col = src_col
            self.dst_sys = dst_sys
            self.dst_tbl = dst_tbl
            self.dst_col = dst_tbl

except InvalidRequestError:
    SchemaManager = Base.metadata.tables['astrolasso']