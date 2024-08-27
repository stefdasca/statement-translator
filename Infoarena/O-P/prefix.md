## Task 

We consider a string consisting of the lowercase letters $'a', 'b', \dots,'z'$. Determine its longest periodic prefix. A string $X$ is periodic if it can be written as $P + P + \dots + P$, where $A + B$ denotes the concatenation of strings $A$ and $B$. The string $P$ is called the period of $X$ and must be strictly shorter than $X$. For example, the strings $"abcaabcaabcaabca"$, $"xyyxyy"$, and $"wwwww"$ are periodic, while the strings $"abcaabcaabcaz"$, $"xyxyxz"$, and $"wwwaawww"$ are not periodic.

## Input Data 

The first line of the input file `prefix.in` contains the integer $T$, the number of strings present in the file. Each of the following $T$ lines contains a string.

## Output Data 

The output file `prefix.out` will contain, for each of the $T$ strings from the input file, the length of the longest periodic prefix.

## Constraints and Clarifications

$1 \leq T \leq 10$ 

Each string will have at least one and at most $1\ 000\ 000$ characters

## Example

`prefix.in`
```
10
abcdefgh 
z 
xxxuxxxu 
abbcaabbcaabbcaabbcaxyzxyzxyzxyz 
hellohellohellohellauhellohello 
aaaaaaaaazaaaaaaaaazaaaaaaaaa 
uvwuvwuvwuvwu 
sirperiodicsirperiodicsirperiodicsir 
aababcabcdabcdeabcdefabcdefgaerror 
mamatatabunicubunicaunchiumatusa
```

`prefix.out`
```
0 
0 
8 
20 
15 
20 
12 
33 
2 
4 
```