# ride_my_way_api

[![Build Status](https://travis-ci.org/araaliFarooq/ride_my_way_api.svg?branch=master)](https://travis-ci.org/araaliFarooq/ride_my_way_api)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a606be0961af4491be9614153d1fa01d)](https://www.codacy.com/app/araaliFarooq/ride_my_way_api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=araaliFarooq/ride_my_way_api&amp;utm_campaign=Badge_Grade) 
[![Coverage Status](https://coveralls.io/repos/github/araaliFarooq/ride_my_way_api/badge.svg?branch=master)](https://coveralls.io/github/araaliFarooq/ride_my_way_api?branch=master)



## About
This is an API for a transportation application that allows users (Drivers) to create and add ride offers to which other users (Passengers) make request to join.

## Features
- Get all the offers for logged in users
- Request to join a ride offer
- Create and add a ride offer.
- View a particular ride offer.

## Other features
- Register a user
- Login a user

## Tools Used
[Flask](http://flask.pocoo.org/) - web microframework for Python
## Requirements
Python 2.7.x - 3.x.x+
## Run (Use) on your local machine
First clone the repository
```sh
   $ git clone https://github.com/araaliFarooq/ride_my_way_api
   ```
   Head over to the cloned directory, create a virtual environment, use pip to install the requirements, then run the app
   ```sh
    $ cd ride_my_way_api
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python run.py
```
#### Endpoints to create a user account and login into the application
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/v1/register | True | Create an account
POST | /api/v1/login | True | Login a user

#### Endpoints to create, read user ride offers and requests
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/v1/rides/add_offer | True | Create an offer
GET | /api/v1/rides/all_offers | False | Fetch all offers for a logged in user
GET | /api/v1/rides/<ride_id> | False | Fetch a single offer for a logged in user
GET | /api/v1/<user_id>/<offer_id>/requests | False | Send a request to join a ride offer for a logged in user

## Authors
[Araali Sseruwu Farooq](https://github.com/araalifarooq)