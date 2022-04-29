from email import header
import os 
import unittest
from app import create_app
import json
from flask_sqlalchemy import SQLAlchemy

from models import setup_database





class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        self.app=create_app()
        self.executive_producer_token=os.environ['executive_producer_token']
        self.casting_director_token=os.environ['casting_director_token']
        self.casting_assistant_token=os.environ['casting_assistant_token']
        self.client=self.app.test_client
        self.database_path="postgresql://{}:{}@{}/{}".format('postgres','','localhost:5432','castageny')
        setup_database(self.app,self.database_path)



        with self.app.app_context():
            self.db=SQLAlchemy()
            self.db.init_app(self.app)

            self.db.create_all()



        self.new_movie={
            'title':'test',
            'release_date':'2022'
        }



    def tearDown(self):
        pass




    def test_api_without_token(self):
        res=self.client().get('/movies')
        data=json.loads(res.data)

        self.assertEqual(res.status_code,401)
        self.assertEqual(data['success'],False)


    

    def test_get_movies(self):
        res=self.client().get('/movies',headers={'Authorization': "Bearer {}".format(self.executive_producer_token)})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['movies'])




    def test_post_movies(self):
        res=self.client().post('/movies',headers={'Authorization': "Bearer {}".format(self.executive_producer_token)},json=self.new_movie)
        data=json.loads(res.data)

        self.assertEqual(res.status_code,201)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['movie'])




    def test_get_actors(self):
        res=self.client().get('/actors',headers={'Authorization': "Bearer {}".format(self.executive_producer_token)})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)



    def test_delete_actors(self):
       res=self.client().delete('/actors/3',headers={'Authorization': "Bearer {}".format(self.executive_producer_token)}) 
       data=json.loads(res.data)

       self.assertEqual(res.status_code,200)
       self.assertEqual(data['success'],True)
       self.assertTrue(data['id'])


    def test_403_delete_actor_with_unaut_user(self):
        res=self.client().delete('/actors/3',headers={'Authorization': "Bearer {}".format(self.casting_assistant_token)})
        data=json.loads(res.data)

        self.assertEqual(res.status_code,401) 
        self.assertTrue(data['message'])



    
    def test_401_get_actor_without_auth_header(self):
        res=self.client().get('/actors')
        data=json.loads(res.data)

        self.assertEqual(res.status_code,401)
        self.assertEqual(data['message'],'missing auth header')





        

    



if __name__=='__main__':
    unittest.main()