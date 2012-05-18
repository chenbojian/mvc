import sqlite3

from config.db_config import DB_PATH

class Outlaw(object):

    def __init__(self, name='', surname='', reward=0.0, outlaw_id=None):
        self.outlaw_id = outlaw_id
        self.name = name
        self.surname = surname
        self.reward = reward

    def save(self):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
               
        cursor.execute('INSERT INTO outlaws(name,surname,reward) VALUES (?, ?, ?)', (self.name, self.surname, self.reward))        
        connection.commit()
        
        cursor.close()
        connection.close()
        
    def __str__(self):
        return ('Outlaw Id: ' + self.outlaw_id + 
                '\nOutlaw Name: ' + self.name + 
                '\nSurname: ' + self.surname + 
                '\nReward: ' + str(self.reward))
        
    @staticmethod
    def find_by_surname(surname):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM outlaws WHERE surname = ?', (surname,))
        result = cursor.fetchall()
        result = list(result[0])
        
        cursor.close()
        connection.close()
        
        return Outlaw(result[1], result[2], result[3], result[0])
    
    @staticmethod
    def get_all():
        _all = []
        
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM outlaws')
        result = cursor.fetchall()
        
        for i in result:
            row = list(i)
            _all.append(Outlaw(row[1], row[2], row[3], row[0]))
        
        cursor.close()
        connection.close()
        
        return _all        
    
    @staticmethod
    def delete_all():
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        
        cursor.execute('DELETE FROM outlaws')
        connection.commit()
        
        cursor.close()
        connection.close()