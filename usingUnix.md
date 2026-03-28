## Using z/OS Unix

# Set up OMVS 

The /usr file system is set up read only.  
I want to mount various files systems, so you need to define a directory.
You cannot use /u because of automount getting in the way.

    chmount -w /usr          
    mkdir /usr/zopen/        
    mkdir /usr/tmp/          
    chmount -r /usr   
