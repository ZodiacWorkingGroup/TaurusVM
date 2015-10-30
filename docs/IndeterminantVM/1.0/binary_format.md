# Binary Format of IndeterminantVM 1.0

IndeterminantVM 1.0 uses a custom file format to encode its binary files. This format is a subset of the overarching
Taurus file format.

Every IndeterminantVM (or other TaurusVM) program starts with a null-terminated string. This string contains a series
of positional arguments, separated by semicolons informing Taurus what VM and what version to use. The arguments are:

* VM
* Version

The rest of the code is then passed to the corresponding interpreter, in this case IndeterminantVM 1.0.

IndeterminantVM's code is, for the moment, a flat binary file. That is to say that when the interpreter starts executing
IndeterminantVM's code, it starts on the first instruction and progresses from there.