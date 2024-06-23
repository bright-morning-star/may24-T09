# AI300 May 2024 - Group T09
## Deploying Machine Learning Systems to the Cloud

### 1. Capstone Documentation
| Team Number | T09 |
| -------- | ------- |
| Team Member 1  | Siau Wei Hong |
| Team Member 2  | Ong Chai Heng |

| Deployed Flask Web Application on AWS | http://ec2-18-142-245-87.ap-southeast-1.compute.amazonaws.com/ |
| -------- | ------- |
| Docker Hub Image Repository  | https://hub.docker.com/repository/docker/polarisroute/ai300-capstone-app/general |

| API Endpoint | http://ec2-18-142-245-87.ap-southeast-1.compute.amazonaws.com/api/predict |
| -------- | ------- |
| JSON Input for POST Request  | ``` {"tenure_months": "12", "num_referrals": "1", "total_long_distance_fee": "0", "total_monthly_fee": "0", "total_charges_quarter": "0", "age": "0", "num_dependents": "1", "has_internet_service": "1", "has_unlimited_data": "1", "has_premium_tech_support": "1", "has_online_security": "1", "paperless_billing": "1", "senior_citizen": "1", "married": "1", "contract_type": "1","payment_method": "1"} ``` |

| Chosen Final Model | Catboost Classifier |
| -------- | ------- |
| Hyper Parameter Tuning  | GridSearchCV |
| Depth  | 4 |
| Iterations  | 100 |

| Calculated Metrics Score | Catboost Classifier |
| -------- | ------- |
| AUC  | 0.889 |
| Precision  | 0.753 |
| Recall  | 0.711 |
| F1  | 0.731 |

### 2. Repository Documentation
| Folder | Description |
| -------- | ------- |
| archive  | files not used and backup purpose only |
| model  | Storing the selected machine learning model exported from pynb |
| notebooks  | pynb notebook of the Data Exploration, Feature Engineering and calculating AUC of the different models  |
| src  | source code folder for app.py and index.html |
| requirements.txt  | installing the package required versions on venv (virtual environment) |
| Dockerfile  | config file for building the docker image (only for publishing the app to docker and deploying on public aws) |

### 3. Instruction guide to set up the repository on your local environment
3.1 Clone the repoistory into your local environment
```
git clone https://github.com/bright-morning-star/may24-T09.git
```

```
cd <repo-folder>
cd may24-T09
```

3.2 Setup new virtual environment
```
<PYTHON_ANACONDA_PATH> -m virtualenv venv
```

3.3 Activate virtual environment
```
source venv/Scripts/activate
```

3.4 Install requirements on virtual environment
```
pip install -r requirements.txt
```

3.5 Test running on flask local development server (ensure any running server is terminated beforehand)
```
<PYTHON_ANACONDA_PATH> src/app.py
```

Access the webpage on http://localhost:5000 and access the API on http://localhost:5000/api/predict (Refer to json input found in section 1)

3.7 Test running on Waitress WSGI Web Server Gateway Interface (Production Quality Server) (ensure any running server is terminated beforehand)

Windows Users
```
export PYTHONPATH=./src
waitress-serve --listen=0.0.0.0:80 src.app:app
```

Access the webpage on http://localhost:80 and access the API on http://localhost:80/api/predict (Refer to json input found in section 1)

Unix users (Mac / Linux OS)
```
export PYTHONPATH=./src
gunicorn --bind=0.0.0.0:80 src.app:app
```

### 4. Instruction guide to build docker image and push to docker hub
4.1 Build Image with selected tag number version
```
docker build -t <app-name>:1.0 .
```

4.2 Test the docker image locally for any errors
```
docker run -d -p=80:80 <app-name>:1.0
```

4.3 Access the webpage on http://localhost:80 and access the API on http://localhost:80/api/predict (Refer to json input found in section 1)

4.4 Create a new public repository on docker hub website first.

4.5 Tag the docker image to your new docker repository name
```
docker tag <app-name>:1.0 <docker-account-name>/<docker-repository-name>:1.0
```

4.6 Push the docker image to your new docker repository name
```
docker push <docker-account-name>/<docker-repository-name>:1.0
```

### 5. Instruction guide to setup AWS EC2 and Pull Docker Image
5.1 Setup a instance on AWS EC2 (free-tier) on Amazon Linux

5.2 Connect either on AWS console or SSH to the terminal

5.3 Install docker on the EC2 instance
```
# updates the yum respository and installs the latest docker package
sudo yum update -y
sudo yum install -y docker

# provides ec2-user with privileges to run docker without sudo
sudo usermod -a -G docker ec2-user
```

5.4 Start the docker service on the Linux machine.
```
sudo service docker start
```

5.5 Pull the public Docker image and start running its associated container
```
docker run -d -p=80:80 --name=<app-name> <docker-account-name>/<docker-repository-name>
```

5.6 Access the URL through the public IPv4 address of the EC2 container.
</br>

### 6. Afternote: Sprint Backlog (For Info Purpose)
6.1 Sprint #1 Product Backlog (1 Jun - 15 Jun) Lesson 4 & Lesson 5
</br># added first research model using Random Forest(0.89) and XGBoost (0.91)
</br># added second research model using catboost (0.88) and lightgbm (0.84)
</br># combine both notebooks (research model) together to complete the EDA and model evaluation for Data Exploration and Model Selection

6.2 Sprint #2 Product Backlog (15 Jun - 29 Jun) Lesson 6 & Lesson 7.
</br># added requirements.txt, model.py (some error) and app.py.
</br># added docker build file and pushed image to docker hub.
</br># added ec2 instance url and pull docker image from docker hub
</br># run image on ec2
