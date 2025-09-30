from pymongo import MongoClient
import time
import serial

PortRF = serial.Serial('/dev/ttyAMA0',9600)

client = MongoClient('mongodb://etu-web2.ut-capitole.fr:27017/')

db = client.rasp04

collection_list = db.list_collections()

class MongoDBConnection():
    def __init__(self):
        self.client = MongoClient('mongodb://etu-web2.ut-capitole.fr:27017/')
        self.dbObj = client.rasp04
    
    def show_collections(self):
        collections_list = db.list_collection_names()
        return collections_list
    
    def get_all_collection_records(self, collection_name):
        collection = db[f'{collection_name}']
        cursor = collection.find({})
        record_list = []
        for document in cursor:
            record_list.append(document)
        return record_list
    
    def write_record_to_collection(self, collection_name, record):
        collection = db[f'{collection_name}']
        # Add to check if collection item does not exits 
        cursor = collection.insert_one(record)
    
    def get_book_by_rfid():
        pass

    def get_user_by_rfid():
        pass
    
def show_major_options():

    print("\t 1- Add a new book to the library (scan rfid) \n")
    
    print("\t 2- Add a new user to the library (scan rfid) \n")

    print("\t 3- Change user name \n")

    chosen_option = input("Enter the number of the operation that you would like to do \n >")

    return chosen_option

def read_rfid():
    ID = ""
    while True:
        
        read_byte = PortRF.read()

        if not read_byte:
            continue

        if read_byte ==b"\x02":
            for i in range (0,12):
                read_byte=PortRF.read()
                ID += read_byte.decode('utf-8')
        if read_byte == b"\x03":
            break
        

    return ID


def run_library_interface():

    while True:

        print(" Welcome to the library manager\n")

        selected_option = show_major_options()

        print(f"\n Chosen option {selected_option}")

        # if selected_option == 1:

        time.sleep(1)

        print("\033[H\033[J", end="")




        

if __name__ == '__main__':
    # new_db_connection = MongoDBConnection()

    # print(new_db_connection.show_collections())

    # print(new_db_connection.get_all_collection_records('users'))

    # test_record = {'name': 'test from py name', 'rfid': '00002', 'books': []}

    # new_db_connection.write_record_to_collection('users', test_record)

    # run_library_interface()

    # print(read_rfid())
    pass
