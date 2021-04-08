# Ansible Collection - adorjan87.oracle

Documentation for the collection.

Ansible version:ansible 2.10.6
This collection contains a roles: oracle19_install
This role can able to install oracle19c rdbms binaries.


Role variables
Role usages Oracle OFA folder structure
Available variables are listed below, along with default values (see roles/oracle19_install/defaults/main.yml):

oracle_version: 19c  
oracle_edition: EE
mount_point_name: /u01
oracle_home: /u01/app/oracle/product/19.3.0.0/dbhome_1
oracle_base: /u01/app/oracle
ora_inventory: /u01/app/oraInventory
oracle_owner: oracle
oracle_group: oinstall


<div id="foo" class="bar">
  sdsds
  sdsd
</div>


Usages

1. Have to copy oracle install file to oracle19_install/files/oracle19/Oracle19.3.0.zip
2. Run it from playbook.

**Example**

```ansible
---
- hosts: oracle-servers
  collections: adorjan87.oracle
  tasks:
    - import_role:
        name: oracle19_install

```
