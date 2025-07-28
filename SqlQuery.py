def balance_inquiry():
    return "SELECT Balance FROM DigitalWallet WHERE Id = ?"

def cashin_debit_query():
    return """UPDATE DigitalWallet SET Balance = ? WHERE Id = ?;"""

def add_user_query():
    return '''INSERT INTO DigitalWallet (Name, Balance) VALUES (?, ?)'''

def check_existing_user():
    return "SELECT Name FROM DigitalWallet WHERE Name = ?"