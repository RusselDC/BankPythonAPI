from controller.BankController import BankController
from fastapi import FastAPI
from domain.register_details import RegisterDetails
from domain.Service_response import ServiceResponse
from domain.transaction_domain import TransactionDomain
api = FastAPI()
controller = BankController()

@api.post("/register")
def register_user(register_details: RegisterDetails) -> ServiceResponse:
    err_message = controller.validate_registration(register_details.name, register_details.pin_code,  register_details.card_number)

    if len(list(err_message)) != 0:
        return ServiceResponse(status="Fail", code=422, data=str(err_message), message="User input failure")

    if controller.find_card(register_details.card_number) != None:
        return ServiceResponse(status="Fail", code=403, data=f"Card number is already used", message="User input failure")
    
    return ServiceResponse(status="Success", code=200, data=str(controller.register_account(register_details.card_number, register_details.name, register_details.pin_code)), message="User created :*")
@api.post("/account/deactivate")
def deactivate_account(register_details:RegisterDetails) -> ServiceResponse:
    account = controller.find_card(register_details.card_number)

    if account == None:
        return ServiceResponse(status="Fail",code=403, data="Account not found", message="User not found haha")
    
    if controller.check_pin_code(account,register_details.pin_code) != True:
        return ServiceResponse(status="Fail", code=403, data="Pin code is not correct", message="Wrong user input haha")

    return ServiceResponse(status="Success", code=200, data=str(controller.deactivate_account(register_details.card_number)), message="Account has been deactivated")

@api.post("/account/activate")
def activate_account(register_details:RegisterDetails) -> ServiceResponse:
    account = controller.find_card(register_details.card_number)

    if account == None:
        return ServiceResponse(status="Fail",code=403, data="Account not found", message="User not found haha")
    
    if controller.check_pin_code(account,register_details.pin_code) != True:
        return ServiceResponse(status="Fail", code=403, data="Pin code is not correct", message="Wrong user input haha")

    return ServiceResponse(status="Success", code=200, data=str(controller.activate_account(register_details.card_number)), message="Account has been activated")

@api.post("/transaction/debit")
def debit_transaction(transaction_details:TransactionDomain) -> ServiceResponse:
    account = controller.find_card(transaction_details.account_number)

    if account == None:
        return ServiceResponse(status="Fail", code=403, data="Account not found", message="User not found :P")
    
    if account.get("status") != 1:
        return ServiceResponse(status="Fail", code=403, data="Account is disabled", message="Account disabled, cant proceed with transaction")
    
    transaction = controller.debit_transact(transaction_details.account_number, transaction_details.amount, transaction_details.receiver_or_sender, transaction_details.description)

    return ServiceResponse(data=str(transaction), message="Transaction Done")

@api.post("/transaction/credit")
def credit_transaction(transaction_details:TransactionDomain) -> ServiceResponse:
    account = controller.find_card(transaction_details.account_number)

    if account == None:
        return ServiceResponse(status="Fail", code=403, data="Account not found", message="User not found :P")
    
    if account.get("status") != 1:
        return ServiceResponse(status="Fail", code=403, data="Account is disabled", message="Account disabled, cant proceed with transaction")

    if float(transaction_details.amount) > account.get("balance"):
        return ServiceResponse(status="Fail", code=403, data="Insufficient Balance", message="Cant Procced with the transaction, not enough balance")
    
    transaction = controller.credit_transact(transaction_details.account_number, transaction_details.amount, transaction_details.receiver_or_sender, transaction_details.description)

    return ServiceResponse(data=str(transaction), message="Transaction Done")

