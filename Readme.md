## Production Branch
This branch contains the code modified for a production environment ,the core applications/features are retained from the previous master(developement) branch.The directory structure and URL mappings have been modified slightly as both the flask applications are now configured to run on a single server using one wsgi in a threaded mode.The  plan is to use gunicorn as the WSGI while deploying to production servers.

## Instrcutions
The first 2 steps are same as in master branch.  
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

3. To start the flask-app on the web-server : <br>
   ** This is done considering you are working inside a virtualenv and have installed gunicorn.<br>
        ` $ /env/bin/gunicorn -b :5000 run_both:application --threads 5 `<br>
 
 **Note : It is required to multithread the gunicorn instance else post requests to the ml-api will be stalled and timeout without successful termination.

4. Open browser at url specified in the prompt. That is  `http://127.0.0.1:5000`<br> 

## URL Map
<br>

Production Server
```

domain:5000
│   
│
└───+   /       
|   +   /signup
|   +   /login
|   +   /home
| 
│   
│
└───+   ml/api/get_Attributes
    +   ml/api/get_Jobs
    +   ml/api/predict

  

```

