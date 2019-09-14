from app.UserManager.view import user_routes


def register_routes(app):
    app.register_blueprint(user_routes, url_prefix='/api/v1/users')