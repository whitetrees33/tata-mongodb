"""
Modify MongoDB data with PyMongo.
"""
import pprint

__all__ = ['ModifyDatabase']

class ModifyDatabase:

    def __init__(self, client, authdb_name):
        self.client = client
        self.authdb_name = authdb_name
        op_sub1 = ['check database info',
                   'insert data',
                   'delete data',
                   'update data']
        nop_sub1 = len(op_sub1)
        print('Action type?')
        for i in range(nop_sub1):
            print('{0}) {1} '.format(i+1, op_sub1[i]))
        while True:
            try:
                self.op_sub1_id = int(input())
                if (self.op_sub1_id > nop_sub1 or self.op_sub1_id < 1):
                    print('Invalid number.')
                    continue
                else:
                    break
            except ValueError:
                print('Invalid number.')      

##----------------------------------------------------------------------
    def check_database_info(self):

        print('\n'+'Check database information.')
        opdb_name = self.authdb_name
        opdb = self.client[opdb_name]
        old_coll_name_list = opdb.collection_names()
        print('database = ', opdb_name)
        print('available collections:')
        print(old_coll_name_list)
        print('number of documents in each collections:')
        for cid in range(len(old_coll_name_list)):
            print('{0}   {1}'.format(old_coll_name_list[cid], opdb[old_coll_name_list[cid]].count()))        
        
##----------------------------------------------------------------------
    def insert_data(self):

        print('\n'+'Insert data.')
        op_sub2 = ['create database',
                   'insert collection',
                   'insert document']
        print('\n'+'action type?')
        nop_sub2 = len(op_sub2)
        for i in range(nop_sub2):
            print('{0}) {1} '.format(i+1, op_sub2[i]))
        while True:
            try:
                op_sub2_id = int(input())
                if (op_sub2_id > nop_sub2 or op_sub2_id < 1):
                    print('Invalid number.')
                    continue
                else:
                    break
            except ValueError:
                print('Invalid number.')

        if (op_sub2_id == 1 and self.authdb_name == 'admin'):
            print('\n'+'Create database')
            print('old database list:')
            old_db_name_list = self.client.database_names() 
            print(old_db_name_list)
            print('\n'+'add database name?')
            while True:
                try:
                    opdb_name = input()
                    if (len(opdb_name) == 0):
                        print('Invalid input.')
                        continue
                    else:
                        break
                except ValueError:
                    print('Invalid input.')
            if (old_db_name_list.count(opdb_name) == 1):
                print('error: database already exist.')
            else:
                print('create database (y/n)?')
                while True:
                    try:
                        answer = input()
                        if (answer == 'y' or answer == 'Y'):
                            qopt = True
                            break
                        elif (answer == 'n' or answer == 'N'):
                            qopt = False
                            break
                        else:
                            print('Invalid input.')
                            continue
                    except ValueError:
                        print('Invalid input.')
                if (qopt):
                    opdb = self.client[opdb_name]
                    opcoll_name = 'emptcoll'
                    opcoll = opdb[opcoll_name]
                    emptdocu = {"xxx": "yyy"}
                    opcoll.insert_one(emptdocu)
                    new_db_name_list = self.client.database_names()
                    print('new database list:')
                    print(new_db_name_list)

        elif (op_sub2_id == 2):
            print('\n'+'Insert collection.')
            if (self.authdb_name == 'admin'):
                print('with administrator account')
                print('available database:')
                old_db_name_list = self.client.database_names()
                print(old_db_name_list)
                print('\n'+'operate database name?')
                while True:
                    try:
                        opdb_name = input()
                        if (old_db_name_list.count(opdb_name) == 0):
                            print('Invalid input.')
                            continue
                        else:
                            break
                    except ValueError:
                        print('Invalid input.')                
            else:
                opdb_name = self.authdb_name
            opdb = self.client[opdb_name]
            old_coll_name_list = opdb.collection_names()
            print('database = ', opdb_name)
            print('old collection list:')
            print(old_coll_name_list)
            add_coll_name_list = []
            add_coll_id = 0
            print('Input collection list (type 0 for termination)')
            while True:
                print('add coll ' + str(add_coll_id+1))
                add_name = input('collection name: ')
                if (add_name == '0'):
                    break
                elif (old_coll_name_list.count(add_name) > 0 or add_coll_name_list.count(add_name) > 0):
                    print('error: collection already exist.')
                    continue
                else:
                    add_coll_id = add_coll_id+1
                    add_coll_name_list.append(add_name)
            print('add coll name list=')
            print(add_coll_name_list)
            nadd_coll = len(add_coll_name_list)
            for aid in range(nadd_coll):
                opcoll = opdb[add_coll_name_list[aid]]
                emptdocu = {"xxx": "yyy"}
                opcoll.insert_one(emptdocu)
            new_coll_name_list = opdb.collection_names()
            print('database = ', opdb_name)
            print('new collection list:')
            print(new_coll_name_list)               
            




##----------------------------------------------------------------------
    def delete_data(self):
        
        print('\n'+'Delete data.')
        op_sub2 = ['remove database',
                   'delete collection',
                   'delete document']
        print('\n'+'action type?')
        nop_sub2 = len(op_sub2)
        for i in range(nop_sub2):
            print('{0}) {1} '.format(i+1, op_sub2[i]))
        while True:
            try:
                op_sub2_id = int(input())
                if (op_sub2_id > nop_sub2 or op_sub2_id < 1):
                    print('Invalid number.')
                    continue
                else:
                    break
            except ValueError:
                print('Invalid number.')

        if (op_sub2_id == 1 and self.authdb_name == 'admin'):
            print('\n'+'Delete database')
            print('old database list:')
            old_db_name_list = self.client.database_names() 
            print(old_db_name_list)
            print('\n'+'remove database name?')
            while True:
                try:
                    opdb_name = input()
                    if (old_db_name_list.count(opdb_name) == 0):
                        print('Invalid input.')
                        continue
                    else:
                        break
                except ValueError:
                    print('Invalid input.')
            print('remove database (y/n)?')
            while True:
                try:
                    answer = input()
                    if (answer == 'y' or answer == 'Y'):
                        qopt = True
                        break
                    elif (answer == 'n' or answer == 'N'):
                        qopt = False
                        break
                    else:
                        print('Invalid input.')
                        continue
                except ValueError:
                    print('Invalid input.')
            if (qopt):
                self.client.drop_database(opdb_name)
                new_db_name_list = self.client.database_names()
                print('new database list:')
                print(new_db_name_list)

        elif (op_sub2_id == 2):
            print('\n'+'Delete collection.')
            if (self.authdb_name == 'admin'):
                print('with administrator account')
                print('available database:')
                old_db_name_list = self.client.database_names()
                print(old_db_name_list)
                print('\n'+'operate database name?')
                while True:
                    try:
                        opdb_name = input()
                        if (old_db_name_list.count(opdb_name) == 0):
                            print('Invalid input.')
                            continue
                        else:
                            break
                    except ValueError:
                        print('Invalid input.')                
            else:
                opdb_name = self.authdb_name
            opdb = self.client[opdb_name]
            old_coll_name_list = opdb.collection_names()
            print('database = ', opdb_name)
            print('old collection list:')
            print(old_coll_name_list)
            del_coll_name_list = []
            del_coll_id = 0
            print('Input collection list (type 0 for termination)')
            while True:
                print('delete coll ' + str(del_coll_id+1))
                del_name = input('collection name: ')
                if (del_name == '0'):
                    break
                elif (old_coll_name_list.count(del_name) == 0):
                    print('error: collection does not exist')
                elif (del_coll_name_list.count(del_name) > 0):
                    print('error: collection already in deletion list.')
                    continue
                else:
                    del_coll_id = del_coll_id+1
                    del_coll_name_list.append(del_name)
            print('del coll name list=')
            print(del_coll_name_list)
            ndel_coll = len(del_coll_name_list)
            print('delete collections (y/n)?')
            while True:
                try:
                    answer = input()
                    if (answer == 'y' or answer == 'Y'):
                        qopt = True
                        break
                    elif (answer == 'n' or answer == 'N'):
                        qopt = False
                        break
                    else:
                        print('Invalid input.')
                        continue
                except ValueError:
                    print('Invalid input.')
            if (qopt):
                for aid in range(ndel_coll):
                    opdb.drop_collection(del_coll_name_list[aid])
                new_coll_name_list = opdb.collection_names()
                print('database = ', opdb_name)
                print('new collection list:')
                print(new_coll_name_list) 


##----------------------------------------------------------------------
    def update_data(self):
        
        print('\n'+'Update data.')
                


        
        
