# Introduction

This project is the last destination with udacity's Full-Stack Naondegree, what a beautiful journey! I developed this project to make use of the knowledge that I acquired along the journy.
I tried to make use of all what i learend from following PEP 8 standards,meet RESTApi architectural constraints and much more,also I aspire to conribute in open-source projects soon.
so I provide to you this simple API which can do CRUD operations whith authentication and authorization using third party service `Auth0`.


## Casting Agency API

The Casting Agency Api is a simple api whitch allow authorize people to do ceartin operations(list movies and actors delete post etc).
 There are three different user roles each role has one or permissions which are:
- Casting Assitant: Can get movies and actors.
- Casting Director: Can get or delete or update actors,can get and update movies.
- Executive Producer: Can view, add, modify, or delete actors and movies. 

## Running the API 

API endpoints can be accessed via https://udacity-capstone-proj.herokuapp.com/login


## Running Locally

### Installing Dependancies 

#### python 3.8

follow along with the instructions to install the latest version of python for your platform in the [python Docs] (https://www.python.org/downloads/)


#### PIP Dependancies

this command will install all the required packages to run the app

```
pip3 install -r requirements.txt
```

that command might not work for windows if it not try this:

```
pip install -r requirements.txt
```


### Database

This app uses `PostgreSQL` database,you should have postgres available in your local machine 

For Mac/Linux Install Postgres using Brew. Reference: https://wiki.postgresql.org/wiki/Homebrew 
```
brew install postgresql
```
Verify the installation
```
postgres --version
pg_ctl -D /usr/local/var/postgres start
pg_ctl -D /usr/local/var/postgres stop

```

#### Populate The database using these commnds:

```
createdb castagency
```

```
psql castagency < castagency.sql

```

### Run The server:

clone the project repo and `cd` to main directory 

* for Linux and Mac
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

```
* for Windows
```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```



### Running tests

To run the test file,run the following command:
```
python test.py
```
or 

```
python3 test.py
```


### Deploy to Heroku Platform

* initilize git repo

```
git init
```

for the first time commit you need to configure the git user name and email

```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

* create an app in heroku 

```
heroku create [my-app-name] --buildpack heroku/python

```
Note: your app name must be uniqe 


run this command to see remote repo:

```
git remote -v 
```

If you cannot see the Heroku "remote" repository URL in the output, you can use the command:

```
git remote add heroku [heroku_remote_git_url]

```

* Add PostgreSQL addon for our database
run this code in order to create your database and connect it to your application:

```
heroku addons:create heroku-postgresql:hobby-dev --app [my-app-name]

```

* set up enviroment variables in the Heroku Cloud

```
heroku config --app [my-app-name]
```

copy the DATABASE_URL generated from the step above, and update your local DATABASE_URL environment variable:

go to `setup.sh` file and paste your URL like this example:

```
export DATABASE_URL="postgres://xjlhouchsdbnuw:0e9a708916e496be7136d0eda4c546253f1f5425ec041fd6e3efda3a1f819ba2@ec2-35-175-68-90.compute-1.amazonaws.com:5432/d3mrjpmsi4vvn1"
```


* push the app

```
git add -A
git status 
git commit -m "Your comment"
```

```
git push heroku master
```
The above command may not work because the default git branch form master to main.

You can start new branch:

```
git checkout -b masterbranch
```

and push it:

```
git push heroku masterbranch:main
```



# API Documentation

Errors
`401`
`403`
`404`
`405`





401
- 401 occurs when there is no authorization header on the request or invalid token 
```
{
	"error": 401,
	"message": "Unauthorized",
	"success": false
}
```
403
- 403 not allowed to access
```
{
	"error": 403,
	"message": "Forbidden.",
	"success": false
}
```
404
- 404 this errors occurs when the resource can not ne found
```
{
	"error": 404,
	"message": "not found.",
	"success": false
}
```
405
- 405 when the method is not allowed to be performed on a specific resource 
```
{
	"error": 405,
	"message": "Method Not Alowed",
	"success": false
}
```

Endpoints
`GET '/login'`
`GET '/actors'`
`GET '/movies'`
`POST '/actors'`
`POST '/movies'`
`PATCH '/actors/<int:actor_id>'`
`PATCH '/movies/<int:movie_id>'`
`DELETE '/actors/<int:actor_id>'`
`DELETE '/movies/<int:movie_id>'`




GET '/login'
- Returns: html page with a login button will redirect you to auth0 login page.
- after login you going to have fresh token 




GET '/actors'
- Returns: A list of actors from the database along with success messgae equal to true
```
{
    "actors": [
        {
            "age": 45,
            "gender": "M",
            "id": 5,
            "name": "brad bet"
        },
        {
            "age": 78,
            "gender": "male",
            "id": 6,
            "name": "Robert De Niro"
        },
        {
            "age": 82,
            "gender": "male",
            "id": 7,
            "name": "Al Pacino"
        },
        {
            "age": 35,
            "gender": "female",
            "id": 8,
            "name": "Emilia Clarke"
        },
    ],
    "success": true
}

```



GET '/movies'
- Returns: A list of movies from the database along with success messgae equal to true
```
{
    "movies": [
        {
            "id": 8,
            "release_date": "1972",
            "title": "The God Father"
        },
        {
            "id": 9,
            "release_date": "September 19,1990",
            "title": "Goodfellas"
        },
        {
            "id": 10,
            "release_date": "April 1957",
            "title": "12 Angry men"
        }
    ],
    "success": true
}
```
POST '/actors'
- creats a new actor
- Returns: the new added actor with the success message.

```
{
    "actor": {
        "age": 82,
        "gender": "male",
        "id": 7,
        "name": "Al Pacino"
    },
    "success": true
}

```
POST '/movies'
- creates new movie
- Returns: the new added movie with the success message

```
{
    "movie": {
        "id": 10,
        "release_date": "April 1957",
        "title": "12 Angry men"
    },
    "succes": true
}
```



PATCH '/actors/<int:actor_id>'
- updates an existing actor in the database.
-  takes an argument which is the actor id,for instance `/actors/5`
- Returns : The updated actor along whith the success message 

```
{
    "success": true,
    "updated": {
        "age": 60,
        "gender": "male",
        "id": 10,
        "name": "brad Pitt"
    }
}
```





PATCH '/movies/<int:movie_id>'
- updates an existing movie in the database.
-  takes an argument which is the movie id,for instance `/movies/5`
- Returns : the updated movie and success message 
```
{
    "success": true,
    "updated": {
        "id": 12,
        "release_date": "test2",
        "title": "test2"
    }
}

```





DELETE '/actors/<int:actor_id>'
- Deletes the selected actor from the database permently
- it takes the id of the actor as an argument
- Returns: id for the deleted actor and success message
```
{
    "id": 9,
    "success": true
}

```
DELETE '/movies/<int:movie_id>'
- Deletes the selected movie from the database permently
- it takes the id of the movie as an argument
- Returns: id for the deleted movie and success message
```
{
    "id": 11,
    "success": true
}

```