import unittest
from app import views
from run import app
import json

class Test_Viewing_Offers(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()

    def test_get_available_offers(self):
        response = self.app.post("/api/v1/rides/add_offer",
            content_type='application/json',
            data=json.dumps(dict(id="1",driver_name="kyra",location="kawempe",
                                car_type="Benz",plate_number="uab 123x",contact="1672525252",availability="10am - 10pm",cost_per_km="200"),)
            )  
            
        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/rides/all_offers",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(reply2["message"],"Successfully viewed offers")

   