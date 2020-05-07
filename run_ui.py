from UI_server import create_app as app_frontend_create_app
frontend = app_frontend_create_app()

if __name__ == '__main__':
    frontend.run(host='localhost',port=8080,debug=True)