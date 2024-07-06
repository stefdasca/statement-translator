```markdown
Costel owns an array $p$ of $n$ precious stones numbered from $1$ to $n$. Because Costel is a superstitious person, he collects stones of only certain types. The type of a stone is represented by a lowercase letter of the English alphabet, and each type has a specific value. <br/> <br/>

One day, Costel decided to distribute the array of $n$ stones on $k$ shelves so that each shelf contains a nonempty subarray of stones from the original array, and finally, each stone is on exactly one shelf. We define the value of a shelf as the sum of the values of the stones on that shelf.

# Task

Given the array of $n$ stones, distribute the stones from the array into $k$ disjoint subarrays so that:
* The largest value of a shelf is maximized.
* The smallest value of a shelf is maximized.

# Input data

The input file `pietricele.in` will contain on the first line the natural numbers $c$, $n$ and $k$ separated by a space, where $c$ represents the task to be solved, $n$ represents the number of stones in the array, and $k$ represents the number of shelves on which the stones will be distributed. The second line of the file will contain $n$ lowercase letters of the English alphabet, representing the types of the stones in Costel's array. The third line contains $26$ numbers separated by spaces, representing the value of each stone type from `a` to `z`.

# Output data

The output file `pietricele.out` contains the answer for the given task.

# Constraints and clarifications

* $c \in \{1, 2\}$
* $1$ ≤ $k$ ≤ $n$ ≤ $200\ 000$
* The values of the stone types are in the range \[$1$, $2 \cdot 10^9$\].
* A subarray of the array $p$ is a sequence of stones located at consecutive positions: $p_i, p_{i+1}, \ldots, p_j,\; 1 \leq i \leq j \leq n$.
* Two subarrays are disjoint if they have no stones in common.
* It is recommended to use the data type `long long`.

|# | Points | Constraints|
| - | - | ------------|
|1|10|$c = 1$, for each stone in the array $\\mathit{value}[p_i] \\le \\mathit{value}[p_{i + 1}]$|
|2|20|$c = 1$, without additional constraints|
|3|10|$c=2$, $n \le 5000$ and $k=3$|
|4|10|$c=2$, $1 \le k \le n \le 100$|
|5|10|$c=2$ and the values of all stone types are equal.|
|6|40|without additional constraints|

# Examples

`pietricele.in`
```
1 12 3
abbaacabcbaa
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
```

`pietricele.out`
```
18
```

`pietricele.in`
```
2 12 3
aabaacabcbaa
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
```

`pietricele.out`
```
6
```

# Explanations

The largest value a shelf can have is $18$ and is obtained by the following distribution on the shelves: `a`, `bbaacabcba`, `a`, each with values $1$, $18$, and $1$ respectively. <br/>
The array is distributed on $3$ shelves as follows: `aabaa`, `cab`, `cbaa`, each with values $6$, $6$ and $7$ respectively. Thus, $6$ is the smallest value of a shelf, which for this example is the maximum possible.
```