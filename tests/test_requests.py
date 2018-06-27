import unittest
from app import views
from run import app
import json

class Test_Requests(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()

    def test_request_to_join_offers(self):
        '''Test to request to join an offer'''
        response = self.app.post("/api/v1/rides/add_offer",
            content_type='application/json',
            data=json.dumps(dict(id="1",driver_name="kyra",location="kawempe",
                                car_type="Benz",plate_number="uab 123x",contact="1672525252",availability="10am - 10pm",cost_per_km="200"),)
            ) 
        response = self.app.post("/api/v1/register",
            content_type='application/json',
            data=json.dumps(dict(firstname="shakira",secondname="kyra",username="kyooq",
                                contact="0888887676",user_category="driver",password="farooq",car_type="rover",reg_num="uab1234",lic_num="4567789999"),)
            )      
            
        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/1/1/requests",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(reply2["message"],"Request sent successfully")
        self.assertEquals(response.status_code, 201)






        
            

   