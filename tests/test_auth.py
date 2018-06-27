import unittest
from run import app
from flask import jsonify, json
from app.models import User, Driver

class Test_auth(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_registration(self):
        """ Test for successful user register """
        response = self.app.post("/api/v1/register",
            content_type='application/json',
            data=json.dumps(dict(firstname="shakira",secondname="kyra",username="kyooq",
                                contact="0888887676",user_category="driver",password="farooq",car_type="rover",reg_num="uab1234",lic_num="4567789999"),)
            )      
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "New Driver successfully registered")
        self.assertEquals(response.status_code, 201)

    
    def test_registration_with_empty_first_name(self):
        """ Test for empty contact validation """
        
        response = self.app.post(
                "/api/v1/register",
            content_type='application/json',
            data=json.dumps(dict(firstname="",secondname="kyra",username="araali",
                                contact="0384464662",user_category="driver",password="xxxx",car_type="benz",reg_num="uab1234",lic_num="4567789999"),)
            )              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "first name is missing")
        self.assertEquals(response.status_code, 400)  

    def test_registration_with_empty_password(self):
        """ Test for empty password validation """
        response = self.app.post("/api/v1/register",
            content_type='application/json',
            data=json.dumps(dict(firstname="shakira",secondname="kyra",username="kyooq",
                                contact="0888887676",user_category="driver",password="",car_type="rover",reg_num="uab1234",lic_num="4567789999"),)
            )              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "password is missing")
        self.assertEquals(response.status_code, 400)

    def test_registration_with_empty_username(self):
        """ Test for empty username validation """
       
        response = self.app.post(
                "/api/v1/register",
            content_type='application/json',
            data=json.dumps(dict(firstname="shakira",secondname="kyra",username="",
                                contact="0888887676",user_category="driver",password="xxxx",car_type="rover",reg_num="uab1234",lic_num="4567789999"),)
            )              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "username is missing")
        self.assertEquals(response.status_code, 400)

    def test_registration_with_empty_contact(self):
        """ Test for empty contact validation """
        
        response = self.app.post(
                "/api/v1/register",
            content_type='application/json',
            data=json.dumps(dict(firstname="shakira",secondname="kyra",username="araali",
                                contact="",user_category="driver",password="xxxx",car_type="rover",reg_num="uab1234",lic_num="4567789999"),)
            )              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "contact is missing")
        self.assertEquals(response.status_code, 400)


    def test_registration_with_empty_car_type(self):
        """ Test for empty car type validation """
        
        response = self.app.post(
                "/api/v1/register",
            content_type='application/json',
            data=json.dumps(dict(firstname="shakira",secondname="kyra",username="araali",
                                contact="0384464662",user_category="driver",password="xxxx",car_type="",reg_num="uab1234",lic_num="4567789999"),)
            )              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "car type is missing")
        self.assertEquals(response.status_code, 400)  


    def test_registration_with_empty_registration_number(self):
        """ Test for empty registration number validation """
        
        response = self.app.post(
                "/api/v1/register",
            content_type='application/json',
            data=json.dumps(dict(firstname="shakira",secondname="kyra",username="araali",
                                contact="0384464662",user_category="driver",password="xxxx",car_type="audi",reg_num="",lic_num="4567789999"),)
            )              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "registration number is missing")
        self.assertEquals(response.status_code, 400)  


    def test_registration_with_empty_licence_number(self):
        """ Test for empty licence number validation """
        
        response = self.app.post(
                "/api/v1/register",
            content_type='application/json',
            data=json.dumps(dict(firstname="shakira",secondname="kyra",username="araali",
                                contact="0384464662",user_category="driver",password="xxxx",car_type="vitz",reg_num="uab1234",lic_num=""),)
            )              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "licence number is missing")
        self.assertEquals(response.status_code, 400)  
    
  
    def test_user_login_successful(self):
        """ Test for successful login """
                   
        response = self.app.post(
                "/api/v1/login",
                content_type='application/json',
                data=json.dumps(dict(username="araali", password="xxxx"))
                )            
        reply = json.loads(response.data)

        self.assertEquals(reply["message"], "Successfully Logged in")
        self.assertEquals(response.status_code, 200)


    def test_user_login_with_wrong_or_no_password(self):
        """ Test for login with wrong or no password """
                      
        response = self.app.post(
                "/api/v1/login",
                content_type='application/json',
                data=json.dumps(dict(username="araali", password=""))
                )            
        reply = json.loads(response.data)

        self.assertEquals(reply["message"], "Missing or Wrong password")
        self.assertEquals(response.status_code, 400)


    def test_user_login_with_wrong_or_no_username(self):
        """ Test for login with wrong or no username """
                      
        response = self.app.post(
                "/api/v1/login",
                content_type='application/json',
                data=json.dumps(dict(username="", password="xxxx"))
                )            
        reply = json.loads(response.data)

        self.assertEquals(reply["message"], "Missing or Wrong username")
        self.assertEquals(response.status_code, 400)