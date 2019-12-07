How to use Docker & deploy it in Django from scratch
1. Install Docker to your machine. Click this link to Install Docker in your machine. 

Signup docker In order to install docker you will be asked to signup. Once you have signed up 

Check if you have installed docker Open your terminal and type docker - version. If you have received something like this then docker has been installed.

(django_docker) bash-3.2$ docker - version
Docker version 19.03.5, build 633a0ea

2. Create a django Project
 In the command prompt (terminal) create a django project folder
mkdir django_docker
Create a virtual environment using pipenv

Type the command below to install a virtual pip environment using python 3
pipenv install django==2.2.4 gunicorn - python 3.6
Open the pipenv shell using the below command

pipenv shell
Once you have provided the above, you will be allowed to execute the commands inside the shell. Now you will be creating a django project by typing the below commands as such:

(django_docker) bash-3.2$ django-admin startproject django_docker_tutorial
(django_docker) bash-3.2$ python manage.py migrate
(django_docker) bash-3.2$ python manage.py createsuperuser
Username (leave blank to use 'Vignesh'): vvignesh501
Email address: *********@email.com
Password:********
Password (again):*******
Superuser created successfully.

3. Open /your_project/setttings.py file
(django_docker) bash-3.2$cd django_docker/settings.py
In settings.py comment out the line DEBUG = TRUE and write the below code & save the file using Ctrl + S
#DEBUG = True
DEBUG = int(os.environ.get('DEBUG', default=1))

4. Deploy the docker web application server gunicorn is standalone WSGI(an interface between web server & the application that you have created) web application server. We use the below command to deploy the web application server for Django
gunicorn django_docker.wsgi:application - bind 0.0.0.0:8000
Tips: If you receive an error as below then there is an issue while you installed you pipenv or pipFile is unavailable in your directory.
[pipenv.exceptions.PipenvOptionsError]: File "/usr/local/lib/python3.6/site-packages/pipenv/core.py", line 282, in ensure_pipfile
[pipenv.exceptions.PipenvOptionsError]: " - system is intended to be used for pre-existing Pipfile
ERROR:: - system is intended to be used for pre-existing Pipfile installation, not installation of specific packages. Aborting.
Solution: This is because there is no PipFile & PipFile.lock in your project directory. Make sure the path you install pipenv previously is the same path as now. If not remove the Pipfile & PipFile.lock in the parent folder rm Pipfile & rm Pipfile.lock 
Make sure when you install the pipenv you are in the parent directory. Once you have confirmed that you have PipFile & PipFile.lock in your directory.
Strucute of a docker directory$ docker build -t docker-django-project -f Dockerfile .
Tips: If you received an error as below then your docker build has some issues while you run the above command prompt you will be receiving an error like this

[2019–12–06 01:02:59 -0800] [91542] [INFO] Starting gunicorn 20.0.4
[2019–12–06 01:02:59 -0800] [91542] [ERROR] Connection in use: ('0.0.0.0', 8000)
[2019–12–06 01:03:02 -0800] [91542] [ERROR] Retrying in 1 second.
[2019–12–06 01:03:03 -0800] [91542] [ERROR] Connection in use: ('0.0.0.0', 8000)
[2019–12–06 01:03:03 -0800] [91542] [ERROR] Retrying in 1 second.
[2019–12–06 01:03:04 -0800] [91542] [ERROR] Can't connect to ('0.0.0.0', 8000)

Solution: This means the port is already in use and that needs to be removed first. Kill all the process that uses 8000 and then try to build again.
(django_docker) bash-3.2$ sudo lsof -i -P -n | grep 8000
python3   89364 pranamyaakella    6u  IPv4 0x6bfb2374fb4ea34d      0t0  TCP *:8000 (LISTEN)
(django_docker) bash-3.2$ kill -9 89364

5. Confirm the docker has been deployed successfully
If you run the gunicorn bind command, you will be receiving the below response. You will be receiving a port to listen like http://0.0.0.0:8000
(django_docker) bash-3.2$ gunicorn django_docker.wsgi:application - bind 0.0.0.0:8000
[2019–12–06 01:09:44 -0800] [92404] [INFO] Starting gunicorn 20.0.4
[2019–12–06 01:09:44 -0800] [92404] [INFO] Listening at: http://0.0.0.0:8000 (92404)
[2019–12–06 01:09:44 -0800] [92404] [INFO] Using worker: sync
[2019–12–06 01:09:44 -0800] [92407] [INFO] Booting worker with pid: 92407
Copy http://0.0.0.0:8000 and type paste it in your browser & if you have received a response like below, then you docker has successfully deployed your application.If you get the below response then embrance yourself, you have done a great job in deploying the django application using Docker. :) 

6. Stop the docker
If you want to stop the docker, then type the below command and get the running unique container ID's of all the deployed dockers. You will be getting the information of all the container ID's that you have created. So be careful while deleting the specific.
(django_docker) bash-3.2$ docker ps
Once you have received the container ID, then give the below command
(django_docker) bash-3.2$ docker stop 11fe6da1d03c
# Django_tutorials
