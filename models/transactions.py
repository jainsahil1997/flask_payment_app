from marshmallow import Schema, fields, validates, ValidationError
from marshmallow.validate import Length, Range
from datetime import datetime
import decimal
class TransactionSchema(Schema):
    """ /api/note - POST

    Parameters:
     - title (str)
     - note (str)
     - user_id (int)
     - time_created (time)
    """
    # the 'required' argument ensures the field exists
    ccnumber = fields.Int(required=True,validate=Range(min=100000000000,max=9999999999999999))
    
    ccname = fields.Str(required=True)

    expiration = fields.Str(required=True)
    @validates('expiration')
    def is_not_expired(resp,value):
        print(value,resp)
        today = datetime.today().strftime("%Y%m")
        if int(value) < int(today) :
            raise ValidationError("Card Expired")
    amount = fields.Decimal(required=True)
    @validates('amount')
    def is_decimal(resp,value):
        d=decimal.Decimal(value)
        d= d.as_tuple().exponent
        if (d != -2 ):
            raise ValidationError("Format of amount should be in two decimal places")

    securitycode= fields.Int()


##Extra Validattions to be added
