Gigel is curious to find out in which area of the country most of his ancestors lived. He manages to gather information about the genetic structure of people from different parts of the country and hopes that, by comparing it with his own genetic structure, he can identify a square area where most of his ancestors lived.

The genetic structure of a person is represented as a sequence of at most $20$ characters (lowercase English letters). A person can be considered an ancestor of Gigel if the degree of similarity between the sequence corresponding to that person and that of Gigel is strictly greater than a known number $K$.

The degree of similarity between two sequences is defined as the number of common characters between the two sequences. For example, for the sequences `abcdabd` and `acbdaad` the degree of similarity is $6$ ($2$ characters `a`, $2$ characters `d`, $1$ character `b`, $1$ character `c`).

Gigel represents the map of the country as a two-dimensional array with $N$ rows and $M$ columns where each element represents the genetic structure of a person from that respective area.

# Task

Given $N$, $M$, $K$, the genetic structure of Gigel and the map representation he identified, determine:

1) The position on the map and the genetic structure of the person or persons for whom the degree of similarity with Gigel's genetic structure is maximized;
2) A maximal square area in which all persons could be considered ancestors of Gigel.

# Input data

The input file `gene.in` contains on the first line the natural number $C$, which can only have the values $1$ or $2$ and indicates the number of the requirement that will be solved. The second line contains the natural numbers $N$, $M$, and $K$, separated by a space, as described above. The third line contains the genetic structure of Gigel, and the next $N \times M$ lines contain a sequence of at most $20$ lowercase English letters, which represents the genetic structures of the persons from the country, in the order of traversing the map by rows.

# Output data

The output file `gene.out` will contain the response to the solved requirement.

If the first requirement is solved, the output file will contain, on separate lines, the identification details for the persons with the highest degree of similarity, as follows: two natural numbers each, separated by a space, representing the position on the map of a person followed by a space and the sequence indicating their genetic structure.

If the requirement $2$ is solved, on the first line of the output file will be written, separated by a space, three natural numbers $x y lgmax$ representing the position of the top-left corner, expressed in the order of the row index and the column index, respectively the maximum side length of the identified square on the map.

# Constraints and clarifications

* $0 \lt N, M \leq 500$
* $0 \lt K \leq 20$
* The top-left corner of the map has the position $(1, 1)$
* If for requirement $1$ there are multiple persons with the maximum similarity degree, they will be listed in lexicographical order of the position on the map (increasing order of the row index, and in case of equality for this, in increasing order of the column index);
* If for requirement $2$ there are multiple maximal areas, the one with the smallest row index will be displayed, and in case of equality also for this, the one with the smaller column index will be displayed;
* For correctly solving the first requirement, $30$ points are awarded, for correctly solving the second requirement, $70$ points are awarded.

# Example 1

`gene.in`
```
1
3 3 3
acgt
aaacctg
abrcg
saasdfs
ecctg
abnctt
agtatggt
aaa
ccgtabd
bbbb
```

`gene.out`
```
1 1 aaacctg
3 2 ccgtabd
```

## Explanation

The sequence corresponding to Gigel is: `acgt`

For the sequences on the map, the degrees of similarity are:

$aaacctg$ – degree $4$  
$abrcg$ – degree $3$  
$saasdfs$ – degree $1$  
$ecctg$ – degree $3$  
$abnctt$ – degree $3$  
$agtatggt$ – degree $3$  
$aaa$ – degree $1$  
$ccgtabd$ – degree $4$  
$bbbb$ – degree $0$

thus the maximum is $4$ and it appears for two sequences

# Example 2

`gene.in`
```
2
4 4 2
acgt
aec
ctg
abvf
acgtaaa
bbbbttg
saa
acgec
actgt
abvf
nctt
cagtatggt
acgtaaa
bbabttg
saatg
sdfs
fhgj
```

`gene.out`
```
2 3 2 
```

## Explanation

For the given map, the degrees of similarity with the sequence acgt are, in order: $2 3 1 4 2 1 3 4 1 2 4 4 3 3 0 1$. Thus, the representation of the map in matrix form is:

$$ \begin{pmatrix}
2 & 3 & 1 & 4 \\
2 & 1 & 3 & 4 \\
1 & 2 & 4 & 4 \\
3 & 3 & 0 & 1 
\end{pmatrix} $$

The largest square area, where all degrees are strictly greater than $2$, has a side length of $2$ and starts at row $2$, column $3$.