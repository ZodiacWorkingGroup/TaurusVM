# TaurusVM File Format
TaurusVM uses a fairly simple file format for its commands.

The binaries are nearly flat, composed of standard ASCII characters to denote commands. 

First, the launcher reads a null-terminated string from the file that has the ISA name and the version, separated by a semicolon. It then passes the rest of the file to the correct executer.
 
The executer starts at the beginning and reads the first two characters as an instruction. It saves this to memory. It then reads a single character and interprets its ASCII value as the argument width. This is stored as a value called , for example, n. It then reads n groups of 8 characters and interprets them as arguments. It then, simply, runs the instruction, the repeats the process at the next character.