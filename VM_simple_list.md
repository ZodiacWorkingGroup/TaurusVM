* **IndeterminantVM**: Variable-length Arguments. Instructions have an "argument length" byte clause, which tells it how many 64-bit instructions to read.
* **GreekVM**: Geometry(/basic algebra)-based. Every registry contains two 32-bit floating-point integers representing a line (or, if they are the same, a point). Operations revolve around doing things with groups of lines.
* **ArbourVM**: Tree-based. Registries lie on a tree, making it easier to understand in some cases.
* **ThueVM**: A string-rewriting/handling-based VM. Registries are strings instead of numbers.