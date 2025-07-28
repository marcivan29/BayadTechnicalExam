import sqlite3
import Utils.SqlQuery as SqlQuery


def balance_inquiry(id):
    conn = sqlite3.connect('Databases.db')
    cursor = conn.cursor()
    cursor.execute(SqlQuery.balance_inquiry(), (id,))
    rows = cursor.fetchall()
    for row in rows:
        
        if row == '':
            return 0
        else: 
            return row
    conn.close()
    
def update_balance(user_id, new_balance):
    try:

        conn = sqlite3.connect('Databases.db')
        cursor = conn.cursor()
        update_query = SqlQuery.cashin_debit_query()
        cursor.execute(update_query, (new_balance, user_id))
        conn.commit()
        conn.close()
        
    except:
        return False
    
def create_user(name):
    try:
        conn = sqlite3.connect('Databases.db')
        cursor = conn.cursor()
        update_query = SqlQuery.add_user_query()
        cursor.execute(update_query, (name, 0))
        conn.commit()
        conn.close()
        
    except:
        return False

def check_existing_user(name):

    conn = sqlite3.connect('Databases.db')
    cursor = conn.cursor()
    cursor.execute(SqlQuery.check_existing_user(), (name,))
    rows = cursor.fetchall()
    for row in rows:
        
        if row == '':
            return False
        else: 
            return True
    conn.close()
    