## This project just for test environment

### Requirements
    python >= python3.6

### Install
    
    pip install -r requirements.txt && python manage.py migrate

### Setup

1. Create superuser

    python manage.py createsuperuser

2. Run server

    python manage.py runserver

### How to test
Login with [Admin](http://127.0.0.1:8000/admin/) to test admin features, after create a normal user, you can use [Test Url](http://127.0.0.1:8000/) to test, for instance:

    import requests
    from requests.auth import HTTPBasicAuth
    url = 'http://127.0.0.1:8000/resource/'
    # Create new resources
    requests.post(url, auth=HTTPBasicAuth('user@user.com', 'useruser'))
    # Get resource list
    url = 'http://127.0.0.1:8000/resource/1/'
    requests.get(url, auth=HTTPBasicAuth('user@user.com', 'useruser'))
    # Delete resource
    url = 'http://127.0.0.1:8000/resource/1/'
    requests.delete(url, auth=HTTPBasicAuth('user@user.com', 'useruser'))

and you can read the [API documents here](http://127.0.0.1:8000/docs/)

### Tech Details

#### Authentication
Uaually in Paas, we shou use Public/Private key to authentication, server should generate two pair of key:

Users can use PUB_KEY, timestamp and parameters for authentication or they can use their PRI_KEY to signature

#### Resource
I did not use UUID as primary key for performance in a single relation database.

#### Testing
The test coverage is about 85%.

### Technical Choices
#### Languages/Web Framework
I used python/django for more than 3 years, so I choose python to in this project.

#### Database
I used sqlite instead of mysql for testing.
