# TaurusVM Archive File Format
TaurusVM supports an archive file format containing various executable files and resource documents. This file describes what that format is.

## File Extension
Taurus Archive Files have the `.tau` file extension.

## File Enconding
`.tau` files are basically `.tar.gz`s with a different file extension. This was chosen because `.tar.gz` is an awesome file format.

## File Tree
When ungziped and untarred, a .tau file has the following file tree:
`
/
	meta.zfg: A file describing the archive executable's attributes.
	libs.zfg: A file listing the external (dynamically-linked) libraries that the executable uses
    *<name>.taurus: Various flat binaries.
	resources/
		*.*: Various resource files that the executable uses.
	src/ (optional)
		*.*: The source code of the application (need not be include, but can be)
`
### meta.zfg
Meta.zfg is a standard zfg file with the following tags:
`
name: The name of the program
order: List of the order in which to run files (any file excluded will only be executed if called from another file)
srcincluded: Boolean describing whether or not the program source is available
`