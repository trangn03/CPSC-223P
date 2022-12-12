# Name: Trang Ngo
# Date: 11/30/2022
# File Purpose: Using sqlite3

import sqlite3
import os
 
class Contacts:
    def __init__(self):
        # store database file and intitialize to an empty string
        self.database_name = ''
   
    def set_database_name(self, database_name):
        self.database_name = database_name
 
        if os.path.exists(self.database_name):
            return
        else:
            connection = sqlite3.connect(self.database_name)
            cur = connection.cursor() # cursor
 
            cur.execute(''' CREATE TABLE IF NOT EXISTS contacts (
                contact_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL)''')
 
            cur.execute(''' CREATE TABLE IF NOT EXISTS phones (
                phone_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                contact_id INTEGER NOT NULL,
                phone_type TEXT NOT NULL,
                phone_number TEXT NOT NULL)''')
   
            connection.commit()
            connection.close()
   
    def get_database_name(self):
        return self.database_name
 
    def add_contact(self, first_name, last_name):
        connection = sqlite3.connect(self.database_name)
        cur = connection.cursor()

        cur.execute(''' INSERT INTO contacts (first_name, last_name) VALUES (?,?)''',
        (first_name, last_name))

        connection.commit()
        connection.close()
 
    def modify_contact(self, contact_id, first_name, last_name):
        connection = sqlite3.connect(self.database_name)
        cur = connection.cursor()
        
        cur.execute(''' UPDATE contacts SET first_name = ?, last_name = ? WHERE contact_id = ?''',
        (first_name, last_name, contact_id))

        connection.commit()
        connection.close()
 
    def add_phone(self, contact_id, phone_type, phone_number):
        connection = sqlite3.connect(self.database_name)
        cur = connection.cursor()

        cur.execute(''' INSERT INTO phones (contact_id, phone_type, phone_number) VALUES (?,?,?)''',
        (contact_id, phone_type, phone_number))

        connection.commit()
        connection.close()
 
    def modify_phone(self, phone_id, phone_type, phone_number):
        connection = sqlite3.connect(self.database_name)
        cur = connection.cursor()

        cur.execute(''' UPDATE phones SET phone_type = ?, phone_number = ? WHERE phone_id = ?''',
        (phone_type, phone_number, phone_id))

        connection.commit()
        connection.close()
 
    def get_contact_phone_list(self):
        connection = sqlite3.connect(self.database_name)
        cur = connection.cursor()

        cur.execute(''' SELECT contacts.*, phones.*
        FROM contacts LEFT JOIN phones ON contacts.contact_id = phones.contact_id''')

        temp = cur.fetchall()
        connection.commit()
        connection.close()
        return temp