<h1 align="center">
	<!-- <img alt="Logo" src=".github/logo.png" width="200px" /> -->
  Application Logo
</h1>

<h3 align="center">
  Backend Assessment - T10
</h3>


<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/EliasGcf/readme-template">

  <a href="https://www.linkedin.com/in/eliasgcf/">
    <img alt="Made by" src="https://img.shields.io/badge/made%20by-Elias%20Gabriel-gree">
  </a>
  
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/EliasGcf/readme-template">
  
  <a href="https://github.com/EliasGcf/readme-template/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/EliasGcf/readme-template">
  </a>
  
  <a href="https://github.com/EliasGcf/readme-template/issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/EliasGcf/readme-template">
  </a>
  
  <img alt="GitHub" src="https://img.shields.io/github/license/EliasGcf/readme-template">
</p>

<p align="center">
  <a href="#-challenge">Challenge</a>&nbsp;&nbsp;&nbsp;|&nbsp;
  <a href="#-getting-started">Getting started</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-routes">Routes</a>&nbsp;&nbsp;&nbsp;
</p>

<p id="insomniaButton" align="center">
  <a href="" target="_blank"><img src="https://insomnia.rest/images/run.svg" alt="Run in Insomnia"></a>
</p>

## 👨🏻‍💻 Challenge

A financial institution hired the services of T10 seeking greater data agility through the metrification of processes that, until then, were not observed (correctly). One of the processes is to request the automatic debit product from partner companies. The operation is performed manually and will be automated by this service, which will allow other services to freely consume their operational events.


## 💻 Getting started

### Requirements

- [Python3](https://www.python.org/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/index.html)
- [Docker](https://docs.docker.com/engine/install/)



**Clone the project and access the folder**

```bash
$ git clone https://github.com/paulohenriquerosa/teste-t10.git && cd teste-t10
```

**Follow the steps below**

```bash
# Create a Virtual environment
$ virtualenv .venv

# Enable the virtual environment
$ source .venv/bin/activate

# Setup app folder to become a package and install all packages
$ pip install -e .

# Disable and enable the virtual environment for load the changes
$ deactivate && source .venv/bin/activate

# Create the instance of postgreSQL using docker
$ docker run --name t10_database \
             -e POSTGRES_PASSWORD=docker \
             -p 5432:5432 -d postgres


# Access the principal file
$ cd app/shared/infra/http

# To finish, run the api service
$ uvicorn main:app --reload

# Well done, project is started!
```

To run the tests run the following command:
```bash
$ pytest
```
## 📝  Routes 

To see the routes available in the api just type the following link in your browser.

```bash
$ http://localhost:8000/docs
```
In this link you will see the resources that you can access, as well as the parameters and responses for each route.

To request the available routes you can use the REST Client [Insominia](https://insomnia.rest/) and import the `Insomnia.json` file that is in the repository

---

