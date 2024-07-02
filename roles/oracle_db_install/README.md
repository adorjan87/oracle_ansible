# oracle_db_install

This role installs Oracle Database 19 or 23ai.
It doesn't contain or download any Oracle instaler. 
You have to download it befor you use this role.  

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

## Role Variables
--------------

* ***oracle_version*** <br>
You can addjust installed Orale version.  
Suppoerted version: 19c, 23ai  
Default:19c  

* ***oracle_edition*** <br>
It can be Enterprise (EE) or Standard (SE) based on Oracle unattanded file.  
Default: EE


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
