# TaurusVM Standalone Executable File Format
TaurusVM uses a fairly simple file format for its standalone executables (files that directly contain everything that ISN'T non-executable resources).

The binaries are nearly flat, composed of standard ASCII characters to denote commands. 

First, the launcher reads a null-terminated string from the file that has the ISA name and the version, separated by a semicolon. It then passes the rest of the file to the correct executer.
 
The documentation for how each interpreter works can be found in its docs directory.