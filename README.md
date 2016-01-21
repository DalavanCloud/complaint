CCDB-content
============
CCDB-content is a standalone Django project that runs the complaint database app.

## Dependencies

- Unix-based OS (including Macs). Windows is not supported at this time.
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) and [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/#), Python modules that keep dependencies  project specific and in their own virtual environments.
- [Autoenv](https://github.com/kennethreitz/autoenv)
- [Node](http://nodejs.org/)
- [Gulp](http://gulpjs.com/)
- [Capital Framework](http://cfpb.github.io/capital-framework/)
- [LESS](http://lesscss.org/)

## Setup

1. copy settings_secret.py.template to settings_secret.py
1. set up virtual environment 

  ```
  mkvirtualenv ccdb
  workon ccdb
  ```
1. install Django 1.6 etc

  ```
  pip install -r requirements.txt
  ```
1. run server

  ``` 
  python manage.py runserver 
  ```
1. install Gulp

  ``` 
  npm install --global gulp
  ``` 
1. install [Autoenv](https://github.com/kennethreitz/autoenv) 

  ```
  $ pip install autoenv
  ```
1. copy `.env_SAMPLE` to `.env` and cd into root directory to execute `.env`.

1. run front end build

  ``` 
  sh ./setup.sh
  ``` 
1. go to landing pages: 
  - http://127.0.0.1:8000/complaintdatabase/
  - http://127.0.0.1:8000/complaintdatabase/data-use/
  - http://127.0.0.1:8000/complaint/process/
  - http://127.0.0.1:8000/complaint/


###Installing app to your project
The Complaint Database and Complaint apps can be installed into other Django projects by doing the following:

In your Django project `url.py`, you will need to include the following in your `urlpatterns` list for each app:
```python
url(r'^complaint/', include('complaint.urls')),
url(r'^complaintdatabase/', include('complaintdatabase.urls')),
```

In your Django project `settings.py`, you will need to include the following in your `INSTALLED_APPS` tuple:
```python
'complaint_common',
'complaint,
'complaintdatabase’,
```

Add this to your `requirements.txt` file:
```
-e git+https://fake.ghe.domain/CCDB4/CCDB-content.git#egg=complaintdatabase
```

Then run the `requirements.txt` file in your terminal your virtual environment:
```
pip install -r requirements.txt
```


## Testing
For Python/Django tests, in the base directory, run the following:

```shell
python manage.py test
```
