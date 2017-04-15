"""
Control MongoDB user accounts with PyMongo.
"""
import pprint

__all__ = ['ControlAccount']

class ControlAccount:

    def __init__(self, client, authdb_name):

        self.client = client
        self.authdb_name = authdb_name
        op_sub1 = ['check user info',
                   'add new user',
                   'remove user',
                   'change user role']
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
    def check_user_info(self):

        print('\n'+'Check user information.')
        if (self.authdb_name == 'admin'):
            print('with administrator account')
            print('available database:')
            old_db_name_list = self.client.database_names()
            print(old_db_name_list)
            print('\n'+'database name?')
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
            opdb = self.client[opdb_name]
            old_user_info = opdb.command('usersInfo')
            old_user_name_list = [old_user_info['users'][uid]['user'] for uid in range(len(old_user_info['users']))]
            old_user_role_list = [old_user_info['users'][uid]['roles'][0]['role']
                                  for uid in range(len(old_user_info['users']))]
            old_nuser = len(old_user_name_list)
            print('total number of users = ',old_nuser)
            print('\n'+'Select information:')
            op_sub2 = ['full inform',
                       'username',
                       'username and role']
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
            if (op_sub2_id == 1):
                pprint.pprint(old_user_info)
            elif (op_sub2_id == 2):
                pprint.pprint(old_user_name_list)
            elif (op_sub2_id == 3):
                for uid in range(old_nuser):
                    print(old_user_name_list[uid], old_user_role_list[uid])

##----------------------------------------------------------------------
    def add_user(self):

        print('\n'+'Add new user.')
        if (self.authdb_name == 'admin'):
            print('with administrator account')
            print('available database:')
            old_db_name_list = self.client.database_names()
            print(old_db_name_list)
            print('\n'+'database name?')
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
            opdb = self.client[opdb_name]
            old_user_info = opdb.command('usersInfo')
            old_user_name_list = [old_user_info['users'][uid]['user'] for uid in range(len(old_user_info['users']))]
            print('old user list = ')
            print(old_user_name_list)
            print('\n'+'Input new user information from:')
            op_sub2 = ['screen',
                       'file']
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
            if (op_sub2_id == 1):
                print('\n'+'input user records (end with username 0):')
                add_user_record_list = []
                add_user_name_list = []
                add_user_id = 0
                while True:
                    print('add user ' + str(add_user_id+1))
                    add_name = input('username: ')
                    if (add_name == '0'):
                        break
                    elif (old_user_name_list.count(add_name) > 0 or add_user_name_list.count(add_name) > 0):
                        print('error: user already exist.')
                        continue
                    else:
                        add_user_id = add_user_id+1
                        add_pwd = input('password: ')
                        print('role (read, readWrite):')
                        while True:
                            add_role = input()
                            if (add_role != 'read' and add_role != 'readWrite'):
                                print('Invalid input.')
                                continue
                            else:
                                break
                        add_user_record_list.append([add_name, add_pwd, add_role, opdb_name])
                        add_user_name_list.append(add_name)
                print('add user record list=')
                print(add_user_record_list)
                nadd_user = len(add_user_record_list)
                for aid in range(nadd_user):
                    opdb.add_user(add_user_record_list[aid][0], add_user_record_list[aid][1],
                                  roles=[{'role': add_user_record_list[aid][2],'db': add_user_record_list[aid][3]}])
            new_user_info = opdb.command('usersInfo')
            new_user_name_list = [new_user_info['users'][uid]['user'] for uid in range(len(new_user_info['users']))]
            print('\n' + 'database name = ' + opdb_name)
            print('new user list = ')
            print(new_user_name_list)

##----------------------------------------------------------------------
    def remove_user(self):

        print('\n'+'Remove user.')
        if (self.authdb_name == 'admin'):
            print('with administrator account')
            print('available database:')
            old_db_name_list = self.client.database_names()
            print(old_db_name_list)
            print('\n'+'database name?')
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
            opdb = self.client[opdb_name]
            old_user_info = opdb.command('usersInfo')
            old_user_name_list = [old_user_info['users'][uid]['user'] for uid in range(len(old_user_info['users']))]
            print(old_user_name_list)
            print('\n'+'Select user (end with username 0):')
            sel_user_name_list = []
            sel_user_id = 0
            while True:
                print('select user ' + str(sel_user_id+1))
                sel_name = input('username: ')
                if (sel_name == '0'):
                    break
                elif (old_user_name_list.count(sel_name) == 0):
                    print('error: user does not exist.')
                    continue
                elif (sel_user_name_list.count(sel_name) > 0):
                    print('error: user already selected.')
                    continue
                else:
                    sel_user_id = sel_user_id+1
                    sel_user_name_list.append(sel_name)
            print('selected user list=')
            print(sel_user_name_list)
            print('remove user (y/n)?')
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
                for uid in range(len(sel_user_name_list)):
                    opdb.remove_user(sel_user_name_list[uid])
            new_user_info = opdb.command('usersInfo')
            new_user_name_list = [new_user_info['users'][uid]['user'] for uid in range(len(new_user_info['users']))]
            print('\n' + 'database name = ' + opdb_name)
            print('new user list = ')
            print(new_user_name_list)

##----------------------------------------------------------------------
    def change_user_role(self):

        print('\n'+'Change user role.')
        print('sorry, this function is not available yet.')




