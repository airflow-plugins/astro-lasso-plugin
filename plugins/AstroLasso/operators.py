from airflow.utils.db import provide_session
from airflow.models import BaseOperator
from AstroLasso.models import SchemaManager

class PutSchemaOperator(BaseOperator):
    def __init__(self,
                 src_sys=None, src_tbl=None, src_col=None,
                 dst_sys=None, dst_tbl=None, dst_col=None,
                 *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.src_sys = src_sys
        self.src_tbl = src_tbl
        self.src_col = src_col
        self.dst_sys = dst_sys
        self.dst_tbl = dst_tbl
        self.dst_col = dst_tbl

    @provide_session
    def execute(self, context, session=None):

        sm = SchemaManager(self.src_sys, self.src_tbl, self.src_col,
                        self.dst_sys, self.dst_tbl, self.dst_col)

        session.add(sm)
        session.commit()