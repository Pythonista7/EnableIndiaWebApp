## Instructions 
1. clone repository<br> 
2. On linux cd into the repository folder , run the following command<br> 
    Create Virtual environment with virtual env : 
    <br> 
    `$ virtualenv env`
    <br>
    If the above command prompt error "virtualenv command not found" run : `$ pip install virtualenv` and try again. <br>
    Once the virtual environment is created you will see a new folder called venv in pwd,now run <br> 
    ` $ source env/bin/activate `<br> 
    ` $ pip install -r requirements.txt`<br> 

3. To run the flask-app : <br>
    Start the web-application with:<br>
        ` $ python Flask/main.py `<br>
    Start the ML server with:<br>
        ` $ python model_server/main.py`<br> 

4. Once both the servers are up and running.Open browser at url specified in the prompt. That is  `http://127.0.0.1:8080`<br> 

## URL Map
<br>

Flask Server
```

localhost:8080
│   
│
└───+   /       
    +   /signup
    +   /login
    +   /home
  

```
<br><br>

Model Server
```

localhost:9090
│   
│
└───+   /api/get_Attributes
    +   /api/get_Jobs
    +   /api/predict

  

```
