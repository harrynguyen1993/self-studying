class DatabaseA:
    def connect_db(self):
        print("conected")
    
    def disconect_db(self):
        print("disconected")

_database_a =  DatabaseA()

connect_db = _database_a.connect_db
disconect_db = _database_a.disconect_db()

# from database import database
'''A problem with the preceding class is that the database object is created
immediately when the module is first imported'''


''' We could delay creating the database until it is actually needed by calling
an initialize_database function to create the module-level variable:''' 
class DatabaseB:
    # the database implementation
    pass
databaseb = None

def initialize_database():
    global databaseb
    databaseb = DatabaseB()