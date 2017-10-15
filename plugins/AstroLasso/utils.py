from AstroLasso.models import SchemaManager as SM
from airflow.utils.db import provide_session
from sqlalchemy.orm import exc

@provide_session
def add_schema(rec, session=None):
    
    new_sm = SM(**rec)
    
    # check if exists
    if not (session.query(SM).filter(
            SM.src_sys == new_sm.src_sys,
            SM.src_tbl == new_sm.src_tbl,
            SM.src_col == new_sm.src_col,
            SM.dst_sys == new_sm.dst_sys,
            SM.dst_tbl == new_sm.dst_tbl,
            SM.dst_col == new_sm.dst_col).first()):

        session.add(new_sm)
    else:
        print('SchemaManagement record already exsists!')
    
    session.commit()

@provide_session
def del_schema(src_sys, src_tbl, src_col,
               dst_sys, dst_tbl, dst_col, session=None):
    
    try:
        to_delete = (session.query(SM).filter(
            SM.src_sys == src_sys,
            SM.src_tbl == src_tbl,
            SM.src_col == src_col,
            SM.dst_sys == dst_sys,
            SM.dst_tbl == dst_tbl,
            SM.dst_col == dst_col).one()
        )

        session.delete(to_delete)
        session.commit()

    except exc.NoResultFound:
        print('Record does not exist - nothing to delete!')
    
    except exc.MultipleResultsFound:
        # TODO
        print('Multiple records found - darn?')

# def add_schemas(recs):
#     for rec in recs:
#         # TODO validate rec
#         add_schema(rec)
    
# def del_schemas(recs):
#     for rec in recs:
#         # TODO validate rec
#         del_schema(rec)