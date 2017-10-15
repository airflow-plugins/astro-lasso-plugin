from airflow.plugins_manager import AirflowPlugin
from AstroLasso.models import SchemaManager
from flask import Blueprint
from flask_admin import BaseView, expose
from flask_admin.base import MenuLink

ml1 = MenuLink(
    # name='Astro Lasson (Schema Management)',
    name='Example Pipelines',
    category='Astro Tools',
    url='/astro-lasso')

ml2 = MenuLink(
    # name='Astro Lasson (Schema Management)',
    name='Support',
    category='Astro Tools',
    url='/astro-lasso')

ml3 = MenuLink(
    # name='Astro Lasson (Schema Management)',
    name='Billing',
    category='Astro Tools',
    url='/astro-lasso')

# # Creating a flask admin BaseView
# class TestView(BaseView):
#     @expose('/')
#     def test(self):
#         # in this example, put your test_plugin/test.html template at airflow/plugins/templates/test_plugin/test.html
#         return self.render("test_plugin/test.html", content="Hello galaxy!")

# v = TestView(category="Test Plugin", name="Test View")

# # Creating a flask blueprint to intergrate the templates and static folder
# bp = Blueprint(
#     "astro_lasso",
#     'astro_lasso_bp,
#     template_folder='templates', # registers airflow/plugins/templates as a Jinja template folder
#     static_folder='static',
#     static_url_path='/static/test_plugin')

bp1 = Blueprint(
    "astro_lasso_blueprint",
    __name__,
    template_folder="/AstroLasso/templates",
    static_folder="static",
    static_url_path="/static/dcmp"
)


class AstroLassoPlugin(AirflowPlugin):
    name = "AstroLasso"
    hooks = []
    operators = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = [ml1, ml2, ml3]
