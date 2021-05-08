from ansible.module_utils.basic import *
import cx_Oracle
import os
from ansible_collections.adorjan87.oracle.plugins.module_utils.oracle import Oracle


def main():
    #module = AnsibleModule(argument_spec={})
    #response = {"hello": "world"}
    #module.exit_json(changed=False, meta=response)
    
    
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
    #module = AnsibleModule(argument_spec=arguments, required_if=required_if)
    
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
