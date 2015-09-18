# TaurusVM File Extensions
TaurusVM uses a few file extensions to keep everything running properly. This document lists what those extensions are.
`
.taurus: Describes two types of file: Standalone executable and flat binaries. Standalone executables start with a null-terminated header describing their VM and VM version followed by a flat binary code, whereas flat binaries contain JUST the binary code.
.tau: Archive executable. Contains multiple .taurus binaries, files packed with them, and metadata describing what each file is. 
.zfg: A Zodiac Configuration File. Basically, an extension of CFGs. Found in .tau archives describing the files inside.
`