import os
import pprint
from pymongo import MongoClient
from db_tata_man_py3 import backup_restore
from db_tata_man_py3 import control_account
from db_tata_man_py3 import modify_database

##----------------------------------------------------------------------------------
def connect_mongdb():
    global my_hostname
    global my_port_num
    global my_dbname
    global my_username
    global my_password

    print('Collect MongoDB information for connection.')
    qread = False
    filein1 = './info-files/db_login_record.dat'
    if  (os.path.isfile(filein1)):
        while True:
            try:
                answer = input('read record infomation from file (y/n)? \n')
                if (answer == 'y' or answer == 'Y'):
                    qread = True
                    break
                elif (answer == 'n' or answer == 'N'):
                    qread = False
                    break
                else:
                    print('Invalid input.')
                    continue
            except ValueError:
                print('Invalid input.')
    if (qread):
        print('read file: ', filein1)
        with open(filein1, 'r') as f2:
            f2.readline()
            my_hostname = f2.readline().rstrip('\n')
            f2.readline()
            my_port_num = int(f2.readline().rstrip('\n'))
            f2.readline()
            my_dbname = f2.readline().rstrip('\n')
            f2.readline()
            my_username = f2.readline().rstrip('\n')
            f2.readline()
            my_password = f2.readline().rstrip('\n')
            f2.readline()
            my_mechanism = f2.readline().rstrip('\n')

    qgenf = False
    if (not qread):
        my_hostname = input('host name: ')
        my_port_num = input('port number: ')
        my_dbname = input('database name: ')
        my_username = input('username: ')
        my_password = input('password: ')
        my_mechanism = input('mechanism: ')
        if (len(my_hostname) == 0):
            my_hostname = 'localhost'
        if (len(my_mechanism) == 0):
            my_mechanism = 'SCRAM-SHA-1'
        while True:
            try:
                answer = input('generate/replace record file (y/n)? \n')
                if (answer == 'y' or answer == 'Y'):
                    qgenf = True
                    break
                elif (answer == 'n' or answer == 'N'):
                    qgenf = False
                    break
                else:
                    print('Invalid input.')
                    continue
            except ValueError:
                print('Invalid input.')
        if (qgenf):
            fileout1 = filein1
            with open(fileout1, 'w') as f1:
                f1.write("host name \n")
                f1.write(my_hostname + "\n")
                f1.write("port number \n")
                f1.write(str(my_port_num) + "\n")
                f1.write("database name \n")
                f1.write(my_dbname + "\n")
                f1.write("username \n")
                f1.write(my_username + "\n")
                f1.write("password  \n")
                f1.write(my_password + "\n")
                f1.write("mechanism \n")
                f1.write(my_mechanism + "\n")

    print('host name = ', my_hostname)
    print('port number = ', my_port_num)
    print('database name = ', my_dbname)
    print('username = ', my_username)
    print('password = ', my_password)
    print('mechanism = ', my_mechanism)

    client = MongoClient(my_hostname, my_port_num)
    auth_status = client[my_dbname].authenticate(my_username, my_password, mechanism=my_mechanism)
    print('connect to client...')
    print('authentication status = {0} \n'.format(auth_status))

    return(client)

##----------------------------------------------------------------------------------
def mongdb_man():
    """
    Main script.
    """
    client = connect_mongdb()
    op_type = ['backup or restore database',
               'control account',
               'modify database',
               'query database',
               'generate input for ML']
    nop_type = len(op_type)
    print('Operation type?')
    for i in range(nop_type):
        print('{0}) {1} '.format(i+1, op_type[i]))
    while True:
        try:
            op_type_id = int(input())
            if (op_type_id > nop_type or op_type_id < 1):
                print('Invalid number.')
                continue
            else:
                break
        except ValueError:
            print('Invalid number.')
    print('\nSelected operation = ')
    print('{0}) {1} \n'.format(op_type_id, op_type[op_type_id-1]))

    if (op_type_id == 1):
        operator = backup_restore.BackupRestore(client, my_dbname, my_hostname, my_port_num, my_username, my_password)
        if (operator.op_sub1_id == 1):
            operator.backup_database()
        elif (operator.op_sub1_id == 2):
            operator.restore_database()
        elif (operator.op_sub1_id == 3):
            operator.export_file()
        elif (operator.op_sub1_id == 4):
            operator.import_file()
    elif (op_type_id == 2):
        if (my_dbname != 'admin'):
            print('error: operation only available to administrators.')
        else:
            operator = control_account.ControlAccount(client, my_dbname)
            if (operator.op_sub1_id == 1):
                operator.check_user_info()
            elif (operator.op_sub1_id == 2):
                operator.add_user()
            elif (operator.op_sub1_id == 3):
                operator.remove_user()
            elif (operator.op_sub1_id == 4):
                operator.change_user_role()
    elif (op_type_id == 3):
        operator = modify_database.ModifyDatabase(client, my_dbname)
        if (operator.op_sub1_id == 1):
            operator.check_database_info()
        elif (operator.op_sub1_id == 2):
            operator.insert_data()
        elif (operator.op_sub1_id == 3):
            operator.delete_data()
        elif (operator.op_sub1_id == 4):
            operator.update_data()




##----------------------------------------------------------------------------------
if __name__ == '__main__':
    mongdb_man()
