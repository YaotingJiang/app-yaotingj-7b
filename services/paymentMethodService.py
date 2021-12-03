from models.paymentMethod import PaymentMethod


# Credit card number
# Expiration date
# Security code
# billing address

def init_payment_method():
    existing_payment_method = PaymentMethod.objects()
    if len(existing_payment_method) == 0:
        create_payment_method('2000 0000 0000 0000', '11/11/21', '000', '111 toyama dr, Sunnyvale, CA, 94089')


def get_payment_method(payment_method_id: str):
    if payment_method_id is None:
        payment_method_doc = PaymentMethod.objects()
    else:
        payment_method_doc = PaymentMethod.objects(id=payment_method_id)
    return payment_method_doc

def create_payment_method(credit_card: str, expiration_date: str, security_code: str, billing_address: str):
    payment_method_doc = PaymentMethod(credit_card=credit_card, expiration_date=expiration_date, security_code=security_code, billing_address=billing_address)
    payment_method_doc.save()
    return payment_method_doc

def update_payment_method(payment_method_id: str, credit_card: str, expiration_date: str, security_code: str, billing_address: str):
    payment_method_doc = PaymentMethod.objects(id=payment_method_id).first()  # extracting the first object from a list of one object
    payment_method_doc.update(credit_card=credit_card, expiration_date=expiration_date, security_code=security_code, billing_address=billing_address)
    payment_method_doc.reload()
    return payment_method_doc

def delete_payment_method(payment_method_id: str):
    payment_method_doc = PaymentMethod.objects(id=payment_method_id)
    payment_method_doc.delete()
    return payment_method_doc