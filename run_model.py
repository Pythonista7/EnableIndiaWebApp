from model_server import create_app as create_model_app
model_app = create_model_app()

if __name__ == '__main__':
    model_app.run(host='localhost',port=9090,debug=True)