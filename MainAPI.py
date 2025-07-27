import Gateway
from flask import Flask, request

app = Flask(__name__)


# Use to Generate Token
@app.route('/GenerateToken', methods=['POST'])
def generate_token():
      
      return Gateway.generate_token(request.get_json()['username'], request.get_json()['password'], request.get_json()['secret_key'])
 
# Balance Inquiry
@app.route('/BalanceInquiry', methods=['POST'])
def balance_inquiry():
      return Gateway.balance_inquiry(request.get_json()['user_id'], request.get_json()['token_value'])   
      
# Cash In
@app.route('/CashIn', methods=['PUT'])
def cash_in():
      return Gateway.cashin(request.get_json()['token_value'], request.get_json()['user_id'], request.get_json()['cashin_amount'])

# Debit
@app.route('/Debit', methods=['PUT'])

def debit():
      return Gateway.debit(request.get_json()['token_value'], request.get_json()['user_id'], request.get_json()['debit_amount'])

# Add User
@app.route('/AddUser', methods=['POST'])
def add_user():
      return Gateway.add_user(request.get_json()['token_value'], request.get_json()['name'])

if __name__ == '__main__':
        app.run(debug=True)