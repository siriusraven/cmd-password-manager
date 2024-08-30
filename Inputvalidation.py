import re
import sqlite3

def master_key_validation(master_key: str) -> None:
    if len(master_key) == 0 or master_key is None or " ":
        raise Exception("Provided master key is not valid")

def master_key_strenght_validation(master_key: str) -> None:
    regex_special = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    regex_num = re.compile('[0-9]+')

    print('Password requirements: lenght 8 - 31\n',
            'Must contain at least 1 uppercase letter, 1 lowercase letter, 1 number and 1 special character\n',
            f'Valid special characters: {regex_special.pattern}')
    
    if len(master_key) < 8:
        raise Exception("Provided master key is too short")
    if len(master_key) > 31:
        raise Exception("Provided master key is too long")
    
    if regex_special.search(master_key) == None:
        raise Exception("Provided master contains no special characters")
    if regex_num.search(master_key) == None:
        raise Exception("Provided master contains no special characters")
    
    if master_key.isupper():
        raise Exception("Provided master contains no uppercase letters")
    if master_key.islower():
        raise Exception("Provided master contains no lowercase letters")
    
    if master_key.islower():
        raise Exception("Provided master contains no lowercase letters")

def id_validation(id) -> None:
    if type(id) != int:
        raise Exception("Provided id is not valid")
    if id is None:
        raise Exception("Provided id is not valid")
    
    if id < 0:
        raise Exception("Provided id is not valid")
    if id > 2147483647:
        raise Exception("Provided id is not valid")
    if id == 0:
        raise Exception("Provided id is not valid")
    if id % 1 != 0:
        raise Exception("Provided id is not valid")
    
    if does_id_exists(id) == False:
        raise Exception("Provided id does not exists")
    
def does_id_exists(id: int) -> bool:
    connect = sqlite3.connect('pswd.db')

    cursor = connect.cursor()
    cursor.execute('SELECT id FROM passwords')
    all_ids = cursor.fetchall()

    connect.commit
    connect.close

    for x in all_ids:
        if id == x[0]:
            return True
    return False
