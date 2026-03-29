## RACF

See [OW55086: RACFTGT JOB DOES NOT INCLUDE RDEFINES FOR THE STARTED CLASS PROFILES RELATED TO SYSTEM TASKS](https://www.ibm.com/support/pages/apar/OW55086)
[Presentation on Started tasks](https://www.rshconsulting.com/RSHpres/RSH_Consulting__RACF_and_Started_Tasks__November_2023.pdf)

## Define RACF operator command prefix

Example: If the entry in IEFSSNxx is:
SUBSYS SUBNAME(RACF) INITRTN(IRRSSI00) INITPARM('#RACF1')
or
RACF,IRRSSI00,'#RACF1'
RACF is the subsystem name and #RACF1 is the command prefix. Because no scope is specified, the
command prefix is not registered with CPF.
Example: If the entry in IEFSSNxx is:
SUBSYS SUBNAME(RACF) INITRTN(IRRSSI00) INITPARM('#,M')
or
RACF,IRRSSI00,'#,M'
RACF is the subsystem name and # is the command prefix. The prefix has system scope, so a command
with this prefix runs on the system on which it is entered (or to which it is routed by way of the MVS
ROUTE command). Because a scope is specified, the command prefix is registered with CPF.
Example: If the entry in IEFSSNxx is:
