import Utils.DbConnection as DbConnection
import Utils.TokenAuth as TokenAuth
from urllib.parse import urlparse
from urllib.parse import parse_qs

from flask import Flask, jsonify


def balance_inquiry(user_id, token_value):
    
    validated_token_response = TokenAuth.validate_token(token_value)
    if TokenAuth.validate_token(token_value) == "Valid":
      return_value = f"{DbConnection.balance_inquiry(user_id)}".strip('(,)')
      if return_value != "None": 
            return jsonify({"message": return_value})
      else: 
           return jsonify({"message: ": "User not found."})
    else:
        return jsonify({"message: ": validated_token_response})

      
def cashin(token_value, user_id, cashin_amount):

    validated_token_response = TokenAuth.validate_token(token_value)

    if TokenAuth.validate_token(token_value) == "Valid":

        if f"{DbConnection.balance_inquiry(user_id)}".strip('(,)') != "None":
            DbConnection.update_balance(user_id, (cashin_amount + float(f"{DbConnection.balance_inquiry(user_id)}".strip('(,)'))))
            message = "Successfully Cash-In. Your balance is: " + f"{DbConnection.balance_inquiry(user_id)}".strip('(,)')
            status_code = 200
        else:
            message = "User not found."
            status_code = 400
        return jsonify({"message": message}), status_code
    else:
        return jsonify({"message: ": validated_token_response})


def debit(token_value, user_id, debit_amount):

    validated_token_response = TokenAuth.validate_token(token_value)
    if TokenAuth.validate_token(token_value) == "Valid":

        if f"{DbConnection.balance_inquiry(user_id)}".strip('(,)') != "None":

            if debit_amount <= float(f"{DbConnection.balance_inquiry(user_id)}".strip('(,)')):
                DbConnection.update_balance(user_id, (float(f"{DbConnection.balance_inquiry(user_id)}".strip('(,)')) - float(debit_amount)))
                message = "Successfully debited. Your balance is: " + f"{DbConnection.balance_inquiry(user_id)}".strip('(,)')
                status_code = 200
                return jsonify({"message": message}), status_code
            else:
                message = "insufficient, your balance is: " + f"{DbConnection.balance_inquiry(user_id)}".strip('(,)')
                status_code = 400
                return jsonify({"message": message}), status_code
        else:
            message = "User not found."
            status_code = 400
            return jsonify({"message": message}), status_code
    else:
        return jsonify({"message: ": validated_token_response})
    
def generate_token(username, password, secret_key):
    return jsonify({"token": TokenAuth.generate_token(username, password, secret_key)})

def add_user(token_value, name):

    validated_token_response = TokenAuth.validate_token(token_value)
    if TokenAuth.validate_token(token_value) == "Valid":

        if DbConnection.check_existing_user(name) == True:
            return jsonify({"message": "Existing User."})
        else:
            DbConnection.create_user(name)
            return jsonify({"message": "Successfully Added"})
    
    else:
        return jsonify({"message: ": validated_token_response})

    