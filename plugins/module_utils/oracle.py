from ansible.module_utils.basic import *
import cx_Oracle
import os


class Oracle():

    def __init__(self,module):

        self.oracle_home = module.params['oracle_home']
        self.oracle_base = module.params['oracle_base']
        self.oracle_sid = module.params['oracle_sid']
        #self.oracle_host = module.params['oracle_host'] 
        

    def set_environment(self):

        os.environ['ORACLE_HOME'] = self.oracle_home
        os.environ['ORACLE_BASE'] = self.oracle_base
        os.environ['ORACLE_SID'] = self.oracle_sid

    
    def create_database(self,module):

        template_name = module.params['template_name']
        global_db_name = module.params['global_db_name']     
        oracle_sys_pwd = module.params['sys_password']
        oracle_system_password = module.params['system_password']
        oracle_character_set = module.params['character_set']
        create_container_db = module.params['create_container_db']
        number_of_pdbs = module.params['pdb_number']
        pdb_name = module.params['pdb_name']
        storage_type = module.params['storage_type']
        use_omf = module.params['use_omf']
        datafile_destination = module.params['datafile_destination']
        redo_size = module.params['redo_size']
        em_config = module.params['em_config']

        command = "%s/bin/dbca -silent -createDatabase" % self.oracle_home
        command += " -templateName %s" % template_name
        command += " -createAsContainerDatabase %s" % create_container_db 
        command += " -gdbname %s" % global_db_name 
        command += " -sid %s" % self.oracle_sid
        command += " -storageType %s" % storage_type
        command += " -useOMF %s" %use_omf
        command += " -datafileDestination %s" % datafile_destination
        command += " -sysPassword %s" % oracle_sys_pwd
        command += " -systemPassword %s" % oracle_system_password
        command += " -characterSet %s" % oracle_character_set
        command += " -redoLogFileSize %s" % redo_size
        command += " -emConfiguration %s" % em_config
        command += " -ignorePreReqs"

        #if pdb_name != None and create_container_db is True:
        #    command += " -pdbName %s" % pdb_name
        
        #return command
        #-useOMF
        return os.system(command)


    def connect(self):
        connection = cx_Oracle.connect("sys", self.oracle_sys_pwd, self.oracle_host, mode=cx_Oracle.SYSDBA, encoding="UTF-8")
        connection.close()
        pass
