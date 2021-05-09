DOCUMENTATION = '''
---

module: create_db
short_description: Create database module
version_added: "1.0.0"

description: 
  - This module can create an oracle non CDB database or empty CDB database.
  - You can not create RAC databas this module 
  - It uses oracle dbca on silent mode.
  - cx_Oracle module have to install target computer.

options:
    create_container_db:
        description:
                - It decides to use non CDB or empty CDB database.
                - There are two options True or False.:
                    - False: Create non CDB
                    - True: Create empty CDB 
        required: False
        default: Faslse
        aliases: ['create_cdb']
        type: bool
    
    oracle_home:
        description: 
                - Where oracle have been installed.
        required: True
        type: str
    
    oracle_base: 
        description:
                - Oracle base location.
        required: True
        type: str
    
    template_name:
        description:
                - Oracle dbca basict template names
        required: True
        default: General_Purpose.dbc
        type: str
    
    global_db_name:
        description:
                - Database FQDN name.
        required: True
        type: str
    
    oracle_sid:
        description:
                - Database name.
        required: True
        type: str
    
    datafile_destination:
        description:
                - Location of database files.
        required: True
        type: str

    enable_archive_log:
        description:
                - Archivelog mode enable or not.
        required: False
        default: False
        Type: bool
    
    archive_log_mode:
        description:
                - Archivelog switch mode.
        required: False
        default: Auto
        Type: str
        choices: ["AUTO", "MANUAL"]
        default: AUTO  
  
    fra_destination:
        description:
                - FRA locaion in filesystem, or ASM
        required: False
        type: str

    storage_type:
        description:
                - What kind of storage want to use: Filesystem or ASM
        required: True
        type: str
        choices: ["FS", "ASM"]

    use_omf:
        description:
                - Oracle managed files uses
        required: False
        type: bool
        default: True

    character_set:
        description:
                - Caratcter type
        requiredd True
        type: str
        default: character_set
    
    sys_password:
        description:
                - Sys user password.
        required: True
        type: str

    system_password:
        description:
                - System user password
        required: True
        type: str
    
    redo_size:
        description:
                - Online redo log size in MB
        required: True
        type: int
        default: 50
    
    em_config:
        descriptionj: 
                - Enterprise manager agent configuration.
        required: False
        type: bool
        default: False




'''



from ansible.module_utils.basic import *
import cx_Oracle
import os
from ansible_collections.adorjan87.oracle.plugins.module_utils.oracle import Oracle


def main():
    
    default_values = {
        'storage_type':('ASM','FS')
    }

##('create_container_db', True, ['pdb_number', 'pdb_name']),
    required_if = [
        ('enable_archive_log', True, ['fra_destination', 'archive_log_mode'])
    
    ]

    arguments = dict(
        create_container_db=dict(required=False, type='bool', default=False, aliases=['create_cdb']),
        
        pdb_number=dict(required=False, type='int'),
        pdb_name=dict(required=False, type='list'),
        
        oracle_home=dict(required=True, type='str'),
        oracle_base=dict(required=True, type='str'),
        template_name=dict(required=False, type='str', default='General_Purpose.dbc'),
        global_db_name=dict(required=True, type='str'),
        oracle_sid=dict(required=True, type='str'),
        datafile_destination=dict(required=True, type='str'),
        
        enable_archive_log=dict(required=False, type='bool', default=False),
        archive_log_mode=dict(required=False, type='str', choices=["AUTO", "MANUAL"], default="AUTO"),
        fra_destination=dict(required=False, type='str'),
        
        storage_type=dict(required=True, type='str', choices=["FS", "ASM"]),
        use_omf=dict(required=False, type='bool',default=True),
        character_set=dict(required=False, type='str', default='AL32UTF8'),
        sys_password=dict(required=True, no_log=True),
        system_password=dict(required=True, no_log=True),
        redo_size=dict(required=False, type='int', default=50),
        em_config=dict(required=False, type='bool', default=False)
    )

    module = AnsibleModule(argument_spec=arguments, required_if=required_if)
    
    obj1 = Oracle(module)
    obj1.set_environment()
    obj1.create_database(module)
    



    ##response = {"hello": "world"}
    module.exit_json(changed=True)
    #, something_else=obj1.create_database(module))
    #something_else=obj1.create_database(module)
    ##module.exit_json(changed=False)

  

if __name__ == '__main__':
    main()
