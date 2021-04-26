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

    arguments = dict(
        cdb=dict(required=True, type='bool'),
        oracle_host=dict(required=False, type='str'),
        oracle_home=dict(required=True, type='str'),
        oracle_base=dict(required=True, type='str'),
        global_db_name=dict(required=True, type='str'),
        oracle_sid=dict(required=True, type='str'),
        datafile_destination=dict(required=True, type='str'),
        recovery_area_destination=dict(required=True, type='str'),
        storage_type=dict(type='str'),
        character_set=dict(required=True,type='str'),
        sys_password=dict(required=True, no_log=True),
        system_password=dict(required=True, no_log=True)
    )

    module = AnsibleModule(argument_spec=arguments)
    
    obj1 = Oracle(module)
    obj1.set_environment()



    ##response = {"hello": "world"}
    ##module.exit_json(changed=False, something_else="12345")
    module.exit_json(changed=False)

  

if __name__ == '__main__':
    main()
