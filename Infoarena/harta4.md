## Task

Over time, Section One has collected numerous satellite photos, which are maps of different locations where various terrorist organizations operate. Birkhoff noticed that all these maps take up a lot of space on the Section servers, so he decided to compress them. To ensure that the maps cannot be decompressed by anyone outside the Section, Birkhoff invented his own decompression system. A decompressed map is stored as two natural numbers $N$ and $M$, representing the size of the map (number of rows and number of columns) and a matrix of natural numbers with $N$ rows and $M$ columns. A compressed map is stored as two natural numbers $N$ and $M$, representing the size of the map (number of rows and number of columns) and a string of natural numbers and letters. The content of the map is fully encoded by the string of natural numbers and letters as follows: if the encoding starts with a natural number $K$, then the map matrix has the number $K$ in all its cells; if the encoding starts with the letter "O", followed by a natural number (hereinafter referred to as $L$) and then descriptions of two other maps, the map matrix is divided into an upper sub-matrix (with $L$ rows and $M$ columns) and a lower sub-matrix (with $N - L$ rows and $M$ columns), and the two descriptions in the encoding correspond to the two sub-matrices respectively; if the encoding starts with the letter "V", followed by a natural number (hereinafter referred to as $C$) and then descriptions of two other maps, the map matrix is divided into a left sub-matrix (with $N$ rows and $C$ columns) and a right sub-matrix (with $N$ rows and $M - C$ columns), and the two descriptions in the encoding correspond to the two sub-matrices respectively. We can succinctly write the above as follows: Cod mat($N$, $M$) -> $K$ Cod mat($N$, $M$) -> "O", $L$, Cod sup($L$, $M$), Cod inf($N - L$, $M$) Cod mat($N$, $M$) -> "V", $C$, Cod st($N$, $C$), Cod dr($N$, $M - C$)

## Constraints

$1 \leq L \leq N$  
$1 \leq C \leq M$  

You have volunteered to help Birkhoff, so for a map he has provided, you need to tell him the minimum length of a string that compresses the map without loss of quality. 

## Input data

The input file `harta4.in` contains the first line with two natural numbers $N$ and $M$. Each of the following $N$ lines contain $M$ natural numbers, representing the map that Birkhoff has provided. 

## Output data

The output file `harta4.out` will contain a single natural number, representing the minimum length of a string that compresses the given map without loss of quality. 

## Constraints and clarifications

$1 \leq N, M \leq 30$  

The elements of the matrix will be natural numbers, ranging between $1$ and $100$. 

## Example

`harta4.in`  
3 3  
10 10 20  
10 10 20  
20 20 20  

`harta4.out`  
7  

## Explanation

The given matrix can be optimally encoded with the string: $O$, $2$, $V$, $2$, $10$, $20$, $20$, of length $7$. For clarification, we can parenthesize the string: $(O, 2, (V, 2, (10), (20)), (20))$.