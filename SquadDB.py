import sqlite3 as sql

'''
REDO ALL THE FUCKING METHODS SO THAT THEY CORRECTLY USE THE NEW TABLES!!!!!!
There are now 3 table: Users, Inputs, & Responses. Get rid of User its trash

Users is all users who use a /think or /create from baybot
Inputs is from /think
Response is baybot's response to the Users /think

In the future there will be a pictureInput and pictureResponse, this will do
similar to Inputs and Reponses, but will capture the /create prompt and 
pictureResponse will store the picture.   
'''
class DatabaseHandler:
    def __init__(self, path):
        self.conn = sql.connect(path)
        self.cursor = self.conn.cursor()
        self.running = True

    def testing(self):
        i = 0
        while self.running:
            print("\n\n\n\nHI! Database testing\n"
                  "1.) Enter new database entry\n"
                  "2.) Update reponse\n"
                  "3.) update input\n"
                  "4.) print a certain Users database information\n"
                  "5.) print all database information\n"
                  "6.) Exit\n\n\n")

            hehe = int(input("Input: "))
            match hehe:
                case 1:
                    dbEntryName = input("Enter new entrys name in this order: {Name, input(optional), reponse(optional)")
                    self.insert_new_user(dbEntryName)
                case 2:
                    dbEntryName = input("Enter name to add response to: ")
                    dbEntryReponse = input("Enter response: ")
                    #db.insert_new_response(dbEntryName, dbEntryReponse)
                    case2run = True
                    while case2run:
                        if self.name_in_db(dbEntryName):
                            dbEntryName = input("Enter name to add response to: ")
                            case2run = False

                        else:
                            dbEntryName = input("Name not found, try again or type exit: ")
                            if dbEntryName == "exit" :
                                self.running = False

                    self.insert_new_response(dbEntryName, dbEntryReponse)


                case 3:
                    dbEntryName = input("Enter name to add response to: ")
                    dbEntryInput = input("Enter input: ")
                    # db.insert_new_response(dbEntryName, dbEntryInput)
                    while not self.insert_new_input(dbEntryName, dbEntryInput):
                        input("Name not in database, try again: ")
                        # db.insert_new_response(dbEntryName, dbEntryReponse)
                case 4:
                    dbEntryName = input("Enter name to print out: ")
                    while not self.fetch_user_info_by_name(dbEntryName):
                        input("Name not in database, try again: ")

                    print(self.fetch_user_info_by_name(dbEntryName)[1])


                case 5:
                    print(self.fetch_all_db_info())
                case 6:
                    self.running = False


    def create_tables(self):
        self.cursor.execute \
            ('''
        CREATE TABLE IF NOT EXISTS 
        User (id INTEGER PRIMARY KEY, Name TEXT, userInput TEXT, gptResponse TEXT)
        
        ''')

        self.cursor.execute \
            ('''
                        CREATE TABLE IF NOT EXISTS 
                        Inputs( input_id INTEGER PRIMARY KEY, user_id INTEGER, input_text TEXT, FOREIGN KEY(user_id) REFERENCES Users(user_id))
                        ''')

        self.cursor.execute \
            ('''
                CREATE TABLE IF NOT EXISTS Responses (
                response_id INTEGER PRIMARY KEY,
                input_id INTEGER,
                response_text TEXT,
                FOREIGN KEY(input_id) REFERENCES Inputs(input_id))
                ''')

        self.cursor.execute \
            ('''
        CREATE TABLE IF NOT EXISTS 
        Users (user_id INTEGER PRIMARY KEY, name TEXT)
        ''')
        self.conn.commit()

    # need to change to discord username
    def insert_new_user(self, name, userInput="DEFAULT", response="DEFAULT"):
        self.cursor.execute("INSERT INTO User (Name, userInput, gptResponse) VALUES (?, ?, ?)", (name, userInput, response))
        self.conn.commit()

    def insert_new_input(self, name, userInput):
        self.cursor.execute("SELECT * FROM User WHERE Name = ?", (name,))
        if self.cursor.fetchone():
            self.cursor.execute("UPDATE User SET userInput = ? WHERE Name = ?", (userInput, name))
            self.conn.commit()
            return True
        else:
            print("Name not in database, try again")
            self.insert_new_input(name,userInput )

    def insert_new_response(self, name, response):
        self.cursor.execute("SELECT * FROM User WHERE Name = ?", (name,))
        if self.cursor.fetchone():
            self.cursor.execute("UPDATE User SET gptResponse = ? WHERE Name = ?", (response, name))
            self.conn.commit()
            return True
        else:
            print("Name not in database, try again")
            self.insert_new_response(name, response)

    def name_in_db(self, name):
        self.cursor.execute("SELECT * FROM User WHERE Name = ?", (name,))
        if self.cursor.fetchone():
            return True
        else:
            return False

    def fetch_user_info_by_name(self, name):
        self.cursor.execute("SELECT * FROM User WHERE Name = ?", (name,))
        if self.cursor.fetchone():
            self.cursor.execute("SELECT * FROM User WHERE Name = ?", (name,))
            return True, self.cursor.fetchone()
        else:
            print("Name not in database, try again")
            self.fetch_user_info_by_name(name)

    def fetch_all_db_info(self):
        self.cursor.execute("SELECT * FROM User")
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}\n Name: {row[1]}\n User Input: {row[2]}\n GPT Response: {row[3]}")
        #return self.cursor.fetchall()

    def close(self):
        self.conn.close()





db = DatabaseHandler('squad.db')
db.create_tables()
'''
db.insert_new_user("ALEX")
db.insert_new_user("JESSE")
db.insert_new_user("SABRINA")
db.insert_new_response("SABRINA", "HELLO!")
print(db.fetch_user_info_by_name("SABRINA"))
print(db.fetch_all_db_info())
'''
print("start")
db.testing()
print("end")


db.close()