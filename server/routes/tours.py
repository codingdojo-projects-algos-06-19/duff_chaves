from config import app
from server.controllers import tours

app.add_url_rule('/tour', view_func=tours.tours, endpoint='tours:tours')
app.add_url_rule('/tour/view/<id>', view_func=tours.view, endpoint='tours:view')
app.add_url_rule('/admin/tours', view_func=tours.admin_tours_list, endpoint='tours:admin_tours_list')
app.add_url_rule('/admin/add/tours', view_func=tours.admin_add_tours, endpoint='tours:admin_add_tours')
app.add_url_rule('/admin/tour/create', view_func=tours.admin_tour_create, methods=['POST'], endpoint='tours:admin_tour_create')
app.add_url_rule('/admin/tour/<id>/edit', view_func=tours.admin_tour_edit, endpoint='tours:admin_tour_edit')
app.add_url_rule('/admin/tour/<id>/update', view_func=tours.admin_tour_update, methods=['POST'], endpoint='tours:admin_tour_update')
app.add_url_rule('/admin/tour/<id>/delete', view_func=tours.admin_tour_delete, methods=['POST'], endpoint='tours:admin_tour_delete')
