## Task

After so many years of eating seeds, Hamster Vlăduţ decided to switch to a healthier diet. He has a running track consisting of a rectangle formed by joining several cells end to end, with the start and finish being the two edges that border the track (left and right, respectively). He plans to run each day among the following days. Bobo the Mole, his old childhood enemy, discovers Vlăduţ's plan and decides to cause some trouble. He will choose a number of distinct cells of the track and dig a trench exactly after each chosen cell (if the cell is $i$, he will create a trench that separates cells $i$ and $i+1$). Seeing what Bobo has done, Vlăduţ decides that on each day $d$ he will run over the first $d$ holes (from left to right), where $d$ is the number of the current day, and $x$ is a non-zero natural number chosen by him. Furthermore, since he is just starting and is too lazy to jump over holes, he decides to borrow some planks from his neighbor, which will cover all the holes in his path. His neighbor can lend him an unlimited number of planks on day $d$, but under the condition of returning them by evening. Hamster Vlăduţ needs your help to achieve his plan and asks you to find out for each day $d$ among the $K$ of his diet, what the optimal (minimum) number of planks he needs to fully cover the holes he has to traverse (a plank is not allowed to cover a cell only partially, and a hole is considered covered if it is anywhere inside the plank, or at the edges, just like a closed interval).

## Input data

The input file hamster.in contains on the first line two non-zero natural numbers, separated by a space, which represent in order the numbers $N$ and $K$ from the statement. The next line contains $K$ non-zero natural numbers separated two by two adjacent by a space, representing the indices of the cells after which Bobo digs a trench, in ascending order. The file contains another $K$ lines, on line $i$ containing two non-zero natural numbers separated by a space, representing in order $d$ and $x$.

## Output data

The output file hamster.out must contain $K$ lines, each containing a natural number. The line $i$ will contain the minimum number of planks needed for day $d_i$ of the diet.

## Constraints

Subtask 1 (20 points): $1 \leq N \leq 2000$  
$0 \leq K \leq 10\ 9$  
(Feedback test 4)

Subtask 2 (30 points): $1 \leq N \leq 1000$  
$1 \leq K \leq 3 \cdot 10\ 5$  
$0 \leq d \leq 10\ 9$   
and $K = N$  
(Feedback tests 7 and 10)

Subtask 3 (30 points): $1 \leq N \leq 1000$  
$1 \leq K \leq 3 \cdot 10\ 5$  
and $0 \leq d \leq 10\ 9$  
(Feedback test 16)

Subtask 4 (20 points): $1 \leq N \leq 3000$  
$1 \leq K \leq 3 \cdot 10\ 5$  
and $0 \leq d \leq 10\ 15$  
(Feedback test 20)

In all subtasks $1 \leq i \leq N$ and $1 \leq x \leq N$.

$d_i$ has been noted as the coordinate of the $i$-th hole. It is guaranteed that the data in the input file is correct (the indices of the holes will not exceed the maximum length of the track, likewise $d_i$’s). It is guaranteed that any two different positions of holes have different coordinates.

The indices of holes are already sorted in ascending order.

ATTENTION! Parsing the input file hamster.in is recommended to obtain the maximum score. You can use the code from this site (both for users of C++ with similar syntax to fstream, as well as for lovers of pure C).

## Example

`hamster.in`:
```
5 6
2 4 5 7 9
3 2
3 1
3 5
5 5
1 5
2 4
3 2
2 1
4 3
2 2
32 28
3 6
9 11
14 17
20 22
25 28
30 32
34 37
40 43
45 48
50 52
54 57
60 62
64 66
69 71
74 76
79 82
27 11
24 8
29 14
26 8
31 11
25 9
25 10
29 14
29 14
26 10
22 15
30 10
29 14
25 8
21 8
29 12
25 10
21 13
30 10
21 9
24 14
27 8
29 13
30 11
25 14
26 13
26 14
25 10
6 7
5 7
6 6
6 5
5 6
4 7
5 7
6 6
6 6
4 7
5 7
6 6
4 7
5 4
7 4
5 7
6 5
6 6
4 7
5 4
7 5
6 6
4 5
5 4
6
```

`hamster.out`:
```
1
5
2
4
3
2
2
1
4
3
2
3
8
11
14
17
20
22
25
28
30
32
34
37
40
43
45
48
50
52
54
57
60
62
64
66
69
71
74
76
79
82
27
11
24
7
29
14
26
8
31
11
25
9
25
10
29
14
29
14
26
10
22
15
30
10
29
14
25
8
21
8
29
12
25
10
21
13
30
10
21
9
24
14
27
8
29
13
30
11
25
14
26
13
26
14
25
10
6
7
5
7
6
6
6
5
5
6
4
7
4
7
5
6
4
5
4
6
```

## Explanation

The first example is the one from the picture.