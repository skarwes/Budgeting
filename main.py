from Database.db import initialize_database
from Backend import transactions


def main():
    #Creates an database if it does not exist
    initialize_database()

    
if __name__ == "__main__":
    main()