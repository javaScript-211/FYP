import sqlite3
import random
import string
from datetime import datetime
import pandas as pd

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def database_set_up():
    conn = sqlite3.connect('feedback2.db', check_same_thread=False)
    c = conn.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS feedback ( 
            date TEXT,
            id INTEGER,
            modules TEXT,
            feedback TEXT,
            emotionOne TEXT,
            emotionTwo TEXT,
            emotionthree TEXT,
            reason TEXT  
                
        )""")
    
    conn.commit()
    conn.close()

def prompt_db_set_up():
    conn = sqlite3.connect('feedback2.db', check_same_thread=False)
    c = conn.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS queries ( 
            id Text,
            prompt TEXT,
            response TEXT
                
        )""")
    conn.commit()
    conn.close()

def enter_data(feedback,module,emotion1, emotion2, emotion3, reasons):
    conn = sqlite3.connect('feedback2.db', check_same_thread=False)
    c = conn.cursor()
    now = datetime.now()
    date = now.strftime('%d/%m/%Y')
    id = id_generator()

    data = [date, id, module, feedback, emotion1, emotion2, emotion3, reasons]
    c.execute("INSERT INTO feedback VALUES (?,?,?,?,?,?,?,?)", data)

    conn.commit()
    conn.close()

def enter_query(prompt, response):
    conn = sqlite3.connect('feedback2.db', check_same_thread=False)
    c = conn.cursor()
    id = id_generator()

    data = [id, prompt, response]
    c.execute("INSERT INTO queries VALUES (?,?,?)", data)

    conn.commit()
    conn.close()

def get_reasons():
    conn = sqlite3.connect("feedback2.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT modules, reason FROM feedback ORDER BY modules") 
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return pd.DataFrame(result, columns=["Module", "Reason"])

def get_queries():
    conn = sqlite3.connect("feedback2.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT prompt, response FROM queries") 
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return pd.DataFrame(result, columns=["Prompt", "Response"])



def get_count():
    conn = sqlite3.connect('feedback2.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("""SELECT * FROM feedback""")
    result = c.fetchall()
    conn.commit()
    conn.close()

    total = len(result)
    return total

def get_all():
    conn = sqlite3.connect('feedback2.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("""SELECT * FROM feedback""")
    result = c.fetchall()
    conn.commit()
    conn.close()

    return result

def get_dates():
    conn = sqlite3.connect('feedback2.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("""SELECT date FROM feedback""")
    result = c.fetchall()
    conn.commit()
    conn.close()
    
    return result

def get_modules():
    conn = sqlite3.connect('feedback2.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("""SELECT modules FROM feedback ORDER BY modules ASC""")
    result = c.fetchall()
    conn.commit()
    conn.close()

    return result

def get_emotions():
    conn = sqlite3.connect('feedback2.db', check_same_thread=False)
    c = conn.cursor()

    c.execute("""SELECT emotionOne, emotionTwo, emotionThree FROM feedback """)
    result = c.fetchall()
    conn.commit()
    conn.close()

    return result

prompt_db_set_up()