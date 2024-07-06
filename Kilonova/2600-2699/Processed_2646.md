~[geologie.png|align=right]

George the Geologist recently discovered a very beautiful cave in the Iași area, ideal for studying stalactites. Inside the cave, there are $N$ stalactites, arranged in a straight line. After weeks of thorough work and analysis of the cave, George discovered that each stalactite consists of layers of deposits with various chemical compositions.

To save time, the geologist invented a system to note the structure of each stalactite. He associated each different type of layer with a prime number so that if two layers have the same chemical composition, they are associated with the same number, and he calculated the value of the stalactite as the product of the prime numbers of its layers.

Thus, if he has a stalactite with $4$ layers, associated with the prime numbers $2$, $11$, $2$, $3$, then that stalactite will have the value $132 = 2 \cdot 2 \cdot 3 \cdot 11$.

George has obtained the array $A$ of $N$ numbers, representing the sequence of stalactite values in the order they appear in the cave.

To further fund his research, George invited members of the scientific committee of the "Grigore Cobălcescu" Museum of Mineralogy and Petrography in Iași to visit the cave. To impress them, he plans to choose a subarray of stalactites, situated at consecutive positions in the cave, which he will clean by possibly removing some layers so that for each stalactite, exactly one layer remains (thus one prime number), and the obtained subarray should consist only of consecutive prime numbers, in strictly increasing order (George's mathematical tastes...). We say that two prime numbers $x$ and $y$ are consecutive if there is no other prime number $z$ with $x < z < y$.

# Task

Find the maximum number of stalactites that form a subarray obtained through cleaning, which satisfies George's taste.

# Input data

The first line of the file `geologie.in` contains the natural number $N$, with the significance mentioned in the statement, and the second line contains $N$ natural numbers, representing the elements of the array $A$, of stalactite values in the order in the cave.

# Output data

The file `geologie.out` must contain on the first line the maximum number demanded.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$
* $2 \leq A_i \leq 1 \ 000 \ 000$

|#|Points|Constraints|
|-|-|-----------|
|1|17|$A_i$ is prime|
|2|24|$N \leq 1 \ 000$|
|3|36|$A_i \leq 50 \ 000$|
|4|23|No additional constraints|

# Example

`geologie.in`
```
7
3 4 6 10 11 14 21
```

`geologie.out`
```
3
```

## Explanation

$A_1 = 3$ can be cleaned to remain $3$.  
$A_2 = 4$ can be cleaned to remain $2$.  
$A_3 = 6$ can be cleaned to remain $2$ or $3$.  
$A_4 = 10$ can be cleaned to remain $2$ or $5$.  
$A_5 = 11$ can be cleaned to remain $11$.  
$A_6 = 14$ can be cleaned to remain $2$ or $7$.  
$A_7 = 21$ can be cleaned to remain $3$ or $7$.  

For the optimal solution, $A$ can be modified as follows: $3 \ \textbf{2 3 5} \ 11 \ 7 \ 3$, thus obtaining a subarray of $3$ stalactites.

Note that the subarray $3 \ \textbf{2 3 5 11 7} \ 3$ also contains consecutive prime numbers, but they do not appear in strictly increasing order.