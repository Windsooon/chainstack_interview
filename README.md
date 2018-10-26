## Challenge

Any Platform-as-a-Service usually has the following basic features:

- Resource management
- Identity and access management
- Quota management

Your Task

- Develop an API server that does simple resource, access and quota management based on the User Stories below.
You are required to:
- Deploy an instance of the API server on the public cloud or provide a one-step command to run your API server locally (e.g. using a Makefile or Docker Compose) for us to test run the APIs.
- Write sufficient documentation for the APIs and explain your technical choices. User Stories

1. As a platform user, I need to authenticate with an email address and password.
2. As a platform user, I need be able to create, list and delete resources.
3. As a platform user, I should not be able to access resources owned by other users.
4. As a platform user, I should not be able to create a new resource if the quota is exceeded.
5. As a platform administrator, I should be able to create, list and delete users and their resources.
6. As a platform administrator, I should be able to set the quota for any user.


Notes

- A resource is represented by a string with a unique identifier.
- Platform administrator is a platform user as well.
- By default, the quota is not set, which means a user can create as many resources as he wants.
- You should provide responses for any errors that might occur. Constraints

## README

#### Requirements
    python >= python3.6

#### Install and Migrate

    git clone git@github.com:Windsooon/chainstack_interview.git
    pip install -r requirements.txt && cd Pass && python manage.py migrate

#### Setup

1. Create superuser

    python manage.py createsuperuser

2. Run server

    python manage.py runserver

#### How to test
Login with [Admin](http://127.0.0.1:8000/admin/) to test admin features.

![Admin](https://raw.githubusercontent.com/Windsooon/chainstack_interview/master/Admin.png)

After create a normal user, you can use [Test Url](http://127.0.0.1:8000/) to test, for instance:

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

and you can read the [API documents](http://127.0.0.1:8000/docs/) here

![Docs](https://raw.githubusercontent.com/Windsooon/chainstack_interview/master/Docs.png)

### Tech Details
#### Authentication
Usually, in Paas, we should use a Public/Private key to authentication, a server should generate two pairs of key:

![pub_key](https://raw.githubusercontent.com/Windsooon/chainstack_interview/master/pub_key.png)

Users can use PUB\_KEY, timestamp and parameters for authentication or they can use their PRI\_KEY to the signature.

#### Resource
I did not use UUID as the primary key for performance in a single relational database.

#### Testing
The test coverage is about 85%.

### Technical Choices
#### Languages/Web Framework
I used Python/Django for more than 3 years, so I choose python to in this project.

#### Database
I used SQLite instead of mysql for testing.
