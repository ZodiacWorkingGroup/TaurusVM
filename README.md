# TaurusVM
## A Bunch of Semi-Esoteric VMs

Hello! Welcome to the world of the TaurusVM!

TaurusVM is a collection of virtual machines designed by hppavilion[1] of the Zodiac Working Group. More info can be found in the `docs/` folder and on the homepage (http://esolangs.org/wiki/TaurusVM). This document will serve as a brief overview.

## Overview
TaurusVM is, as has been mentioned, a collection of virtual machines that run a machine code-like bytecode, similar to the JVM. YOu do not write this bytecode directly, you instead write in an intermediate language which is assembled or compiled (there is neither yet a compiler or an assembler to the TVM, though).

All the virtual machines run under a single program and are encoded in the same-ish file format. The VMs are:

### Virtual Machines

* *IndeterminantVM*: A VM supporting variable-length arguments.
* *ThueVM*: A VM that is based largely around string manipulation instead of on numbers. Otherwise, it bears little resemblance to Thue.
* *GreekVM*: An experimental VM (not designed for actual usage) and thought experiment revolving around an "Ancient Greek Computer". Based on Geometry instead of traditional computer arithmetic.
* *ArbourVM*: A potentially useful VM (easier to think of organizationally) that has registries that lie on a (binary?) tree and are manipulated around a pointer. 

### Assemblers
TaurusVM includes an assembler for each of its VMs. They have the same names, with "VM" replaced with "ASM". They will not be documented here, but it can be assumed by the reader that they're basically a human-readable version of the VMs with some additional features for the programmer.

### Compiled Languages
Various languages compile/assemble to the TVM. This section lists them (though their compilers/assembler may not be included in this particular repo)

* *brainfuck*: A classic Esolang that is really only included because it seems the easiest to make a compiler for. 
  * *zodiacfuck*: A Brainfuck derivative designed to be easier to use than normal brainfuck. Included because it's a step up from the normal brainfuck and would be more of an accomplishment to implement a compiler for (though neither is really an accomplishment)
* *Virgo*: A language somewhere between the realms of programming and assembly languages. Stack-based.
* *Stare*: A collection of dialcts of languages based around Stack Rewriting. Only 1.x and 2.x derivatives will be implemented as a compiler (in the forseeable future. If the programmers are feeling godly, they may implement 3.x and maybe even 4.x, which include dynamic typing and OO)
