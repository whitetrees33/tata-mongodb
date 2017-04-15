"""
Backup and restore MongoDB with PyMongo.
"""
import pprint
import os
import shlex, subprocess

__all__ = ['BackupRestore']

class BackupRestore:

    def __init__(self, client, authdb_name, my_hostname, my_port_num, my_username, my_password):

        self.client = client
        self.authdb_name = authdb_name
        self.my_hostname = my_hostname
        self.my_port_num = my_port_num
        self.my_username = my_username
        self.my_password = my_password
        mypath = os.getcwd()
        tempstr = mypath.split('/')[-1]
        self.dbdir = tempstr.split('-man')[0]
        op_sub1 = ['backup database',
                   'restore database',
                   'export file',
                   'import file']
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
    def backup_database(self):

        print('\n'+'Backup database.')
        bproot = '../' + self.dbdir + '-backup/'
        print('backup root = ')
        for i in range(1000):
            olddir = bproot + self.dbdir + '-bp-' + str(i)
            if  (not os.path.isdir(olddir)):
               break
        print(bpdir)
##        command_line = 'mongodump --host ' + self.my_hostname + ' --port ' + str(self.my_port_num) \
##                       + ' --username ' + self.my_username + ' --password ' + self.my_password + ' --out ' + bpdir
##        args = shlex.split(command_line)
##        print('execute:')
##        print(command_line)
##        proc = subprocess.Popen(args, stdout=subprocess.PIPE)
##        try:
##            outs, errs = proc.communicate(timeout=60)
##        except TimeoutExpired:
##            proc.kill()
##            outs, errs = proc.communicate()
##        outs = bytes.decode(outs)
##        print('stdout:') 
##        print(outs)
##        print('stderr:')
##        print(errs)


##----------------------------------------------------------------------
    def restore_database(self):

        print('\n'+'Restore database.')

##----------------------------------------------------------------------
    def export_file(self):

        print('\n'+'Export file.')

##----------------------------------------------------------------------
    def import_file(self):

        print('\n'+'Import file.')
