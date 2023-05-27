# from applications.view.admin import register_admin_views
# from applications.view.index import register_index_views
# from applications.view.passport import register_passport_views
# from applications.view.rights import register_rights_view
# from applications.view.department import register_dept_views
# from applications.view.test import register_test_views
from .auth import register_auth_views
from .admin import register_admin_views


def init_routers(app):
    # register_auth_views(app)
    register_admin_views(app)
#     register_index_views(app)
#     register_rights_view(app)
#     register_passport_views(app)
#     register_test_views(app)
#     register_dept_views(app)
