import re
from datetime import datetime
import requests
from requests.exceptions import ConnectionError
import sys
import logging
logging.basicConfig(level = logging.DEBUG)
cheapgatewayapi='http://127.0.0.1:5002/api/v1.0'

expensiveatewayapi='http://127.0.0.1:5003/api/v1.0'

premuimgatewayapi='http://127.0.0.1:5003/api/v1.0'
def routetocheap(details):
    print("cheap")
    try :
        res = requests.post(cheapgatewayapi,details)
        logging.info("processed with cheap gateway")
        return res.status_code
    except requests.exceptions.HTTPError as errh:
        logging.error ("Http Error:",errh)
        return 500
    except requests.exceptions.ConnectionError as errc:
        logging.error ("Error Connecting:",errc)
        return 500
    except requests.exceptions.Timeout as errt:
        logging.error ("Timeout Error:",errt)
        return 500
    except requests.exceptions.RequestException as err:
        logging.error ("OOps: Something Else",err)
        return 500

def routetoexpensive(details):
    print("expensive")
    try :
        res = requests.post(cheapgatewayapi,details)
        logging.info("processed with expensive gateway")
        return res.status_code
    except requests.exceptions.HTTPError as errh:
        logging.info ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        logging.info ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        logging.info ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        logging.info ("OOps: Something Else",err)
    return routetocheap(details)

def routetopremium(details):
    t=0
    while ( t<3 ) :s
        try :
            res = requests.post(cheapgatewayapi,details)
            logging.info ("processed with premium gateway")
            return res.status_code
        except requests.exceptions.HTTPError as errh:
            logging.info ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            logging.info ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            logging.info ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            logging.info ("OOps: Something Else",err)
        t=t+1
    return routetocheap(details)


def route_payment(details):
    if float(details['amount']) < 20.00 :
        return routetocheap(details)
    if float(details['amount']) < 500.00 :
        return routetoexpensive(details)
    if float(details['amount']) > 500.00 :
        return routetopremium(details)
