""" Object Classes modelling the system actors"""
class User:
    def __init__(self, id, firstname,secondname,username,contact, user_category, password):
        self.id = id
        self.firstname = firstname
        self.secondname = secondname
        self.username = username
        self.contact = contact
        self.user_category = user_category
        self.password = password
        

class Driver(User):
    def __init__(self, id, firstname,secondname, username, contact, user_category, car_type, reg_num, lic_num, password):
        User.__init__(self, id, firstname, secondname, username, contact, user_category, password)
        self.car_type = car_type
        self.reg_num = reg_num
        self.lic_num = lic_num


class RideOffer:
    def __init__(self, id, drive_name, location, car_type, plate_number, contact, availability, cost_per_km):
        """Constructor to the RideOffer Class"""
        self.id = id
        self.driver_name = drive_name
        self.location = location
        self.car_type = car_type
        self.plate_number = plate_number
        self.contact = contact
        self.availability = availability
        self.cost_per_km = cost_per_km


    def offer_to_Json(self):
        """Function to give the RideOffer model ability to be jsonified """
        offer = dict(
            id = self.id,
            offerer_name = self.driver_name,
            offerer_contact = self.contact,
            car_type = self.car_type,
            offerer_location = self.location,
            plate_number = self.plate_number,
            availability = self.availability,
            cost_per_km = self.cost_per_km
            )
        return offer 


class RideRequest:
    def __init__(self, id, passenger_name, contact, location):
        """ Constructor to the RideRequest Class """
        self.id = id
        self.passenger_name = passenger_name
        self.contact = contact
        self.location = location
       
    
    def RequestoJson(self):
        """Function to give the RideRequest model ability to be jsonified """
        request = dict(
            id = self.id,
            requester_name=self.passenger_name,
            requester_contact = self.contact,
            requester_location = self.location,
            
            )
        return request




        
