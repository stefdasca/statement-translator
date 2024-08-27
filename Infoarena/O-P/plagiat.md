Plagiarism

Giani, a high-ranking official of the city, is accused of plagiarism in his thesis titled "On the chromatics of traffic signs." A committee was naturally formed to decide on the veracity of this accusation. This committee is composed of a traffic sign, a citizen who deals with scrap metal trafficking, a dolphin, and a citizen who reads the stars. In this problem, we will focus on the method by which the star reader will make his decision. He will look at the sky map, consisting of $N$ point-like stars. Then he will consider all triangles that can be formed with vertices at the stars and if he finds two triangles such that the first can be obtained from the second only by a translation, he considers this a sign, and Giani is guilty. Given $T$ sky maps, decide for each whether Giani is guilty of plagiarism or not. 

## Input data

The input file `plagiat.in` contains on its first line $T$, the number of maps that need to be analyzed. Each map will be described by a number $N$, the number of stars, and $N$ pairs of natural numbers that describe the coordinates of the stars. 

## Output data

The output file `plagiat.out` will contain $T$ lines. The line numbered $i$ will contain the word "DA" if Giani is guilty according to the $i$-th map from the input. Otherwise it will contain the word "NU". 

## Constraints and clarifications

$1 \leq T \leq 5$  
$1 \leq N \leq 400$  
The coordinates of the stars are in the interval $[0, 10^9]$  
There will be no two stars with the same coordinates. 

## Example

`plagiat.in`

```
2
5
1 1
2 2
1 2
0 0
100 105
5
1 1
2 2
1 2
0 0
0 1
```

`plagiat.out`

```
NU
DA
```

## Explanation

In the first case, Giani is exonerated from any guilt, with all possible triangles being distinct relative to translations. In the second case, the triangles $(1, 2, 3)$ and $(1, 4, 5)$ can be obtained from each other through translations. In this case, Giani places his hopes in the dolphin's vote.