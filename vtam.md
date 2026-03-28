## VTAM configuration

- Edit SYS1.VTAMLST(EXLOCAL).  You have to edit this because NET does not have USER.VTAMLST configured.
- Create EXLOCALO from it (for backup)
- change DLOGMOD to have value D4B32XX3,
- create an entry for CUADDR=061,   

Clean up

- Edit SYS1.VTAMLST(ATCCON00).  Remove IVPLCLI,IVPLCLT because the devices they reference do not exist. 