import sqlite3
import random
import string
from datetime import datetime

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def database_set_up():
    conn = sqlite3.connect('feedback.db', check_same_thread=False)
    c = conn.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS feedback ( 
            date TEXT,
            id INTEGER,
            modules TEXT,
            feedback TEXT,
            emotionOne TEXT,
            emotionTwo TEXT,
            reason TEXT  
                
        )""")
    
    conn.commit()
    conn.close()

def enter_data(feedback,module,emotion1, emotion2, reasons):
    conn = sqlite3.connect('feedback.db', check_same_thread=False)
    c = conn.cursor()
    now = datetime.now()
    date = now.strftime('%d/%m/%Y')
    id = id_generator()

    data = [date, id, module, feedback, emotion1, emotion2, reasons]
    c.execute("INSERT INTO feedback VALUES (?,?,?,?,?,?,?)", data)

    conn.commit()
    conn.close()

def get_reasons():
    finalResult = []
    conn = sqlite3.connect('feedback.db', check_same_thread=False)
    c = conn.cursor()

    c.execute("""SELECT CONCAT(reason," ",modules) FROM feedback ORDER BY modules ASC""")
    result = c.fetchall()
    conn.commit()
    conn.close()
    
    for i in range(0,len(result)):
        
        feedback = " ".join(result[i])
        newFeedback = feedback.split(":",1)[1]
        cleanText = newFeedback.replace("\n", "")
        cleanText2 = cleanText.replace("•", "")
        finalResult.append(cleanText2)
        
    return finalResult

def get_count():
    conn = sqlite3.connect('feedback.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("""SELECT * FROM feedback""")
    result = c.fetchall()
    conn.commit()
    conn.close()

    total = len(result)
    return total

def get_all():
    conn = sqlite3.connect('feedback.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("""SELECT * FROM feedback""")
    result = c.fetchall()
    conn.commit()
    conn.close()

    total = len(result)
    return total

def get_dates():
    conn = sqlite3.connect('feedback.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("""SELECT date FROM feedback""")
    result = c.fetchall()
    conn.commit()
    conn.close()
    
    return result

def get_modules():
    conn = sqlite3.connect('feedback.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("""SELECT modules FROM feedback ORDER BY modules ASC""")
    result = c.fetchall()
    conn.commit()
    conn.close()

    return result

def get_emotions():
    conn = sqlite3.connect('feedback.db', check_same_thread=False)
    c = conn.cursor()

    c.execute("""SELECT emotionOne, emotionTwo FROM feedback """)
    result = c.fetchall()
    conn.commit()
    conn.close()

    return result
