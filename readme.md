# Casting Agency API

The Casting Agency Api is a simple api whitch allow authorize people to do ceartin operations(list movies and actors delete post etc).
 There are three different user roles each role has one or permissions which are:
- Casting Assitant: Can get movies and actors.
- Casting Director: Can get or delete or update actors,can get and update movies.
- Executive Producer: Can view, add, modify, or delete actors and movies. 

# Running the API 

API endpoints can be accessed via https://udacity-capstone-proj.herokuapp.com/login


# Running Locally 

* First install Dependancies 
```
pip install -r requirements.txt
```

* Populate The database using these commnds:

```
createdb castagency
```

```
psql castagency < castagency.sql

```

* Run The server:

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

```



# Running tests

To run the test file,run the following command:
```
python test.py
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