import unittest
import os
import json
from flask import json
from app import app
from models.transactions import TransactionSchema
params = "{'ccnumber':'123456781234','ccname':'SahilJain','expiration':'202101','amount':'9','securitycode':'212'}"
#Test 400
def test_add():
    response = app.test_client().post(
        '/api/v1.0/transactions?ccname=SahilJain&expiration=202101&amount=9&securitycode=212')

    assert response.status_code == 400

    response = app.test_client().post(
        '/api/v1.0/transactions?expiration=202101&amount=9&securitycode=212')

    assert response.status_code == 400

    response = app.test_client().post(
        '/api/v1.0/transactions?ccname=SahilJain&expiration=202101&amount=9')

    assert response.status_code == 400

    response = app.test_client().post(
        '/api/v1.0/transactions?ccname=SahilJain&expiration=202101&amount=9&securitycode=212')

    assert response.status_code == 400


def test_proper():
    response = app.test_client().post(
        '/api/v1.0/transactions?ccnumber=123456781234&ccname=SahilJain&expiration=202101&amount=29&securitycode=212')

    assert response.status_code == 400

    response = app.test_client().post(
        '/api/v1.0/transactions?ccnumber=123456781234&ccname=SahilJain&expiration=202101&amount=1&securitycode=212')

    assert response.status_code == 400

    response = app.test_client().post(
        '/api/v1.0/transactions?ccnumber=123456781234&ccname=SahilJain&expiration=202101&amount=600&securitycode=212')

    assert response.status_code == 400
