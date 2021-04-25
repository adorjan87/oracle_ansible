from ansible.module_utils.basic import *
import cx_Oracle
import os


class Oracle():

    def __init__(self, module):

        self.oracle_home = module.params['oracle_home']
        self.oracle_base = module.params['oracle_base']
        self.oracle_sid = module.params['oracle_sid']
        self.oracle_sys_pwd = module.params['sys_password']
        self.oracle_host = module.params['oracle_host'] 


    def set_environment(self):

        os.environ['ORACLE_HOME'] = self.oracle_home
        os.environ['ORACLE_BASE'] = self.oracle_base
        os.environ['ORACLE_SID'] = self.oracle_sid
        

    def connect(self):
        connection = cx_Oracle.connect("sys", self.oracle_sys_pwd, self.oracle_host, mode=cx_Oracle.SYSDBA, encoding="UTF-8")
        connection.close()
        pass


    pass