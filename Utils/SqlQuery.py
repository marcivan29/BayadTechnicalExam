def balance_inquiry():
    return "SELECT Balance FROM DigitalWallet WHERE Id = ?"

def cashin_debit_query():
    return """UPDATE DigitalWallet SET Balance = ? WHERE Id = ?;"""
