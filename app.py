import flask
from flask import request, jsonify, make_response,abort
from payment_handler import route_payment
from models.transactions import TransactionSchema
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
@app.errorhandler(400)
def not_found(error):
    return error, 400

create_transaction_schema=TransactionSchema()
@app.route('/api/v1.0/transactions', methods=['POST'])
def processpayment():
    errors = create_transaction_schema.validate(request.args)
    if errors:
        return errors,400
    print (request.args.get('ccnumber') )
    payment_request = {
        'ccnumber':  request.args.get('ccnumber'),
        'ccname': request.args.get('ccname'),
        'expiration': request.args.get('expiration'),
        'amount': request.args.get('amount'),
        'securitycode': request.args.get('securitycode'),
    }
    res=route_payment(payment_request)
    #pp(payment_request)
    if (res==200):
        return 'OK',200
    else :
        return "Exception Occured",500

app.run(debug=True,host='127.0.0.1', port=5000)
