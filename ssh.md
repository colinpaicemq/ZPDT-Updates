## ssh 

           PARM='PGM /usr/sbin/sshd -f /etc/ssh/sshd_config '                      
edit /etc/ssh/sshd_config to add 

    ALLOWGROUPSS  SYS1  IZUADMIN            

and connect the userid to the group   

