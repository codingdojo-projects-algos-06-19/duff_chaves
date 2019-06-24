from config import app
from server.controllers import users

app.add_url_rule('/user/register', view_func=users.register, endpoint='users:register')
app.add_url_rule('/user/create', view_func=users.create, methods=['POST'], endpoint='users:create')
app.add_url_rule('/user/thankyou', view_func=users.thankyou, endpoint='users:thankyou')
app.add_url_rule('/user/login', view_func=users.login, endpoint='users:login')
app.add_url_rule('/user/my_account', view_func=users.my_account, endpoint='users:my_account')
app.add_url_rule('/user/update/<id>', view_func=users.update, methods=['POST'], endpoint='users:update')
app.add_url_rule('/user/process_login', view_func=users.process_login, methods=['POST'], endpoint='users:process_login')
app.add_url_rule('/user/welcome', view_func=users.welcome, endpoint='users:welcome')
app.add_url_rule('/user/logout', view_func=users.logout, endpoint='users:logout')
app.add_url_rule('/admin/users', view_func=users.user_list, endpoint='users:user_list')
app.add_url_rule('/admin/user/update/<id>', view_func=users.admin_update, methods=['POST'], endpoint='users:admin_update')
app.add_url_rule('/admin/user/<id>/edit', view_func=users.admin_edit, endpoint='users:admin_edit')
