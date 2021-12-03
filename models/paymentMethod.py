from mongoengine import Document, StringField, IntField


# Credit card number
# Expiration date
# Security code
# billing address


class PaymentMethod(Document):
    credit_card = StringField(required=True)
    expiration_date = StringField(required=True)
    security_code = StringField(max_length=3, required=True)
    billing_address = StringField(required=True)