#-----------------------
# Imports
#-----------------------

from asyncio import ThreadedChildWatcher
from flask import Flask,request,abort,jsonify,redirect,url_for,render_template
from auth.auth import requires_auth,AuthError
from models import setup_database,Actors,Movies
import json



def create_app(test_config=None):
#--------------------------------
# Set Up The App
#--------------------------------
    app=Flask(__name__)

    setup_database(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,PATCH')
        return response



#---------------------------------
# Endpoints
#---------------------------------


# simple log in page with one button 
    @app.route('/login')
    def index():
        return render_template('index.html')


    @app.route('/movies')
    @requires_auth('get:movie')
    def get_movies(paylod):
        movies=Movies.query.all()

        formated=[movie.format() for movie in movies]
        return jsonify({
            'success':True,
            'movies':formated
        }),200



    @app.route('/actors')
    @requires_auth('get:actor')
    def get_actors(payload):
        actors=Actors.query.all()

        formatted=[actor.format() for actor in actors]

        return jsonify({
            'success':True,
            'actors':formatted
        }),200



    @app.route('/movies',methods=['POST'])
    @requires_auth('post:movie')
    def post_new_movie(paylod):
        body=request.get_json(force=True)

        title=body['title']
        release_date=body['release_date']
        if 'title' not in body:
            abort(404)

        try:
            new_movie=Movies(
                title=title,
                release_date=release_date
            )

            Movies.insert(new_movie)

            return jsonify({
                'success':True,
                'movie':Movies.format(new_movie)
            }),201

        except:
            abort(405)



    @app.route('/actors',methods=['POST'])
    @requires_auth('post:actor')
    def add_new_actor(paylod):
        body=request.get_json(force=True)

        name=body['name']
        age=body['age']
        gender=body['gender']
        if 'name' not in body:
            abort(404)

        try:
            new_actor=Actors(
                name=name,
                age=age,
                gender=gender
            )

            Actors.insert(new_actor)

            return jsonify({
                'success':True,
                'actor':Actors.format(new_actor)

            }),201


        except:
            abort(405)



    @app.route('/actors/<int:id>',methods=['PATCH'])
    @requires_auth('patch:actor')
    def update_an_actor(paylod,id):
        # check if there is an id 
        if not id:
            abort(404)

        selected_actor=Actors.query.get_or_404(id)

        body=request.get_json(force=True)

        if 'name' in body and body['name']:
          selected_actor.name = body['name']
        
        if 'age' in body and body['age']:
           selected_actor.age=body['age']

        if 'gender' in body and body['gender']:
           selected_actor.gender=body['gender']

        
        try:
            selected_actor.update()

            return jsonify({
                'success':True,
                'updated':Actors.format(selected_actor)
            }),200

        except:
            abort(405)



    @app.route('/movies/<int:movie_id>',methods=['PATCH'])
    @requires_auth('patch:movie')
    def update_movies(paylod,movie_id):
        # check if there is an id 

        if not movie_id:
            abort(404)

        selected_movie=Movies.query.get_or_404(movie_id)

        body=request.get_json(force=True)

        if 'title' in body and body['title']:
            selected_movie.title= body['title']
        
        if 'release_date' in body and body['release_date']:
             selected_movie.release_date=body['release_date']

        else:
            abort(404)


        
        try:
            selected_movie.update()

            return jsonify({
                'success':True,
                'updated':Movies.format(selected_movie)
            }),200

        except:
            abort(405)





    @app.route('/actors/<int:id>',methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actors(paylod,id):
        if not id:
            abort(404)

        deleted_actor=Actors.query.filter(Actors.id==id).one_or_none()

        if not deleted_actor:
            abort(404)

        

        try:
            Actors.delete(deleted_actor)

            return jsonify({
                'success':True,
                'id':id
            }),200

        except:
            abort(405)



    @app.route('/movies/<int:movie_id>',methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_movie(paylod,movie_id):
        deleted_movie=Movies.query.filter(Movies.id==movie_id).one_or_none()

        if not movie_id:
            abort(404)

        if not deleted_movie:
            abort(404)

        try:
            Movies.delete(deleted_movie)

            return jsonify({
                'success':True,
                'id':movie_id
            }),200

        except:
            abort(405)


    #-----------------------------------

    # Error Handelers 

    #-----------------------------------

    @app.errorhandler(401)
    def not_authorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Forbidden."
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "not found."
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Request could not be processed."
        }), 422

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error['description']
        }), error.status_code


    return app


# app=create_app()

