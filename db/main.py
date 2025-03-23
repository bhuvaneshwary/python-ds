import db 
import logging

def main():
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        database = db.DataBase()
        database.store()
        database.store_with_timeout()
        database.retrieve()
        database.database_load()
        database.count()
if __name__ == "__main__":
        main()