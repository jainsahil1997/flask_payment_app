# flask_payment_app
flask_payment_app


# Introduction

Basic flask which processes payment based on amount and route to 3 different servers.

# Requirement

Python 3.6 +

#S teps

clone the repository

$ pip install requirement.txt
$ python app.py
$ python cheapgateway.py
$ python expensivegateway.py
$ python premiumgateway.py

Curl testing

$ curl --location --request POST 'http://127.0.0.1:5000/api/v1.0/transactions?ccnumber=123456781234&ccname=Sahil%20Jain&expiration=202102&amount=900.00&securitycode=212'

Power Shell testing

$ $response = Invoke-RestMethod 'http://127.0.0.1:5000/api/v1.0/transactions?ccnumber=123456781234&ccname=Sahil Jain&expiration=202102&amount=900.00&securitycode=212' -Method 'POST' -Headers $headers
$ $response | ConvertTo-Json

Pytest

 $ python -m pytest --cov=./
