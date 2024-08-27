## Task

On the occasion of the centenary of the publication of the theory of general relativity, Gheorghe Fierar debunks, one by one, in an exclusive statement at Digi 23 Puncte, the theories of his brother Albert. Among the accusations made by his excellence is the plagiarism regarding the famous equation $E = mc^2$, which actually appears for the first time in the works of the poet as $E = albastra \cdot dulce \ floare$. Automatically, the calculations regarding the gravitational wave velocity are also wrong, being composed by "an alienated person". Fortunately, the geometry of versification in poetry allows us to deduce the equation $V=F \cdot G$, where $G$ is noted as the genius constant, and $F$ is the frequency of the ephemeral existence charm.

An avid viewer of the mentioned station, Calif Gutzanu understands the exceptional nature of Mr. Fierar's revelations and realizes that one day he will become famous and revolutionize modern physics if he manages to experimentally confirm the equation. To be able to obtain experimental data, however, Calif Gutzanu needs at least two black holes to accurately measure the space-time distortions. Said and done, Mr. Gutzanu "borrows" an interferometer from the university's laboratory and settles in Dristor because, he says, the most unstable substance in the Universe capable of spontaneously generating black holes is precisely the shawarma produced strictly by them. As the shawarma disintegrates, Gutzanu notes $N$ resulting values in the sequence $v_1, v_2, \dots, v_N$, the frequencies emitted by the shawarma. Knowing the constant $G$, he now wonders how many pairs $[st, dr]$ with $st \leq dr$ exist in the sequence such that the product of the subarray $v_{st} \cdot v_{st+1} \cdots v_{dr-1} \cdot v_{dr}$ can be written as $F \cdot G$, where $F$ is some variable. If this number is too small, the experiment will have to be repeated with more mayonnaise and spicy sauce.

## Input data

The input file's first line contains $T$, the number of tests. The first line of each test contains the numbers $N$ and $G$, followed by the next line that describes the sequence $v_1, v_2, \dots, v_N$.

## Output data

The output file will contain $T$ lines, each with an integer representing the required number of pairs.

## Constraints and clarifications

$1 \leq T \leq 5$

$1 \leq N \leq 10^5$

$1 \leq G \leq N$

$1 \leq v_i \leq 10^6$

## Example

shukarime.in

```
2 
6 2 
7 6 15 5 3 2 
6 2 
2 17 2 1 23 23 
```

shukarime.out

```
1
3
```

## Explanation

In the first example, the product of the subarray between positions $[3, 5]$ is $225$ and is the only one that can be written as $225 = 15 \cdot G = 15 \cdot 2$. In the second example, the sequences are $[4, 4]$, $[4, 6]$, $[5, 6]$.