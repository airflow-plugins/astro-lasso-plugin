from airflow.utils.db import provide_session
from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from AstroLasso import utils as lasso


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

        rec = {
            'src_sys': self.src_sys,
            'src_tbl': self.src_tbl,
            'src_col': self.src_col,
            'dst_sys': self.dst_sys,
            'dst_tbl': self.dst_tbl,
            'dst_col': self.dst_col
        }

        lasso.add_schema(rec)


class AstroLassoPlugin(AirflowPlugin):
    name = "AstroLasso"
    hooks = []
    operators = [PutSchemaOperator]
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []