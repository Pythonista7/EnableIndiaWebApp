from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from UI_server import create_app as app_frontend_create_app
frontend = app_frontend_create_app()

from model_server import create_app as create_model_app
model_app = create_model_app()

application = DispatcherMiddleware(
    frontend, {
    '/ml': model_app
})
if __name__ == '__main__':
    run_simple(
        hostname='localhost',
        port=5000,
        application=application,
        use_reloader=True,
        use_debugger=True,
        use_evalex=True)