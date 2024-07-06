# Problem Statement

$N$ soldiers stand in a line from left to right. Each soldier has a distinct number from $1$ to $N$ associated with them. Every morning, the sergeant in charge comes and calls the soldiers corresponding to the numbers $1 \ 2 \ \dots K$. If they are not exactly in the order $1 \ 2 \ \dots K$, all $N$ soldiers will face severe punishment.

The sergeant, noticing that the $K$ soldiers are not correctly arranged, will start ordering the soldiers. He will order the $K$ soldiers using swaps of adjacent soldiers. At each step, he will choose $2$ soldiers in consecutive order (from the $N$) and force them to swap positions.

The sergeant is very efficient and will order the soldiers with numbers $1 \ 2 \ \dots K$ using a minimum number of swaps, however, for each such swap, he will force all soldiers to do a push-up.

Today, the sergeant is too nervous and busy and asks you to tell him how many push-ups the $N$ soldiers must do.

# Implementation Details

You need to implement the following function:

```cpp
long long minimum_swaps(std::vector<int> S, int K);
```

The function `minimum_swaps` will be called exactly once for each test. $S$ will contain the order of the $N$ soldiers from left to right, and $K$ will represent the number of soldiers called to the front. **It is guaranteed that the array $S$ will contain exactly once each number from $1$ to $N$ and that $1 \leq K \leq N**.

The function should return a natural number, representing how many push-ups the $N$ soldiers will be forced to do because they were not correctly ordered.

# Scoring

|#|Points|Constraints|
|-|-|--------|
|1|21|$1 \leq N \leq 15$|
|2|6|$1 \leq N \leq 100$|
|3|5|$1 \leq N \leq 20\ 000 \\ K \leq 50$|
|4|6|$1 \leq N \leq 20\ 000 \\ K \leq 500$|
|5|37|$1 \leq N \leq 200\ 000 \\ K \leq 5\ 000$|
|6|5|$1 \leq N \leq 200\ 000 \\ K = N$|
|7|20|$1 \leq N \leq 200\ 000$|

# Grader Model

**Attention! This grader is not necessarily the one used for submission evaluations**.

You have access to a grader to compile and test your code locally. It will read input data from the console in the following format:
* line $1$: $N \ K$, representing the number of soldiers and the number of soldiers called to the front.
* line $2$: $S_0 \ S_1 \dots S_{N-1}$ (separated by a space)
The grader will display your answer on the console, on a single line, as an integer in base $10$.

# Example 1

`stdin`
```
6 3
6 1 5 2 4 3
```

`stdout`
```
0
```

## Explanation

In the first example, the sergeant calls those with numbers $1$, $2$, and $3$. Luckily, they are already in the correct order, so the soldiers are not forced to do push-ups.

# Example 2

`stdin`
```
6 5
6 1 5 2 4 3
```

`stdout`
```
4
```

## Explanation

In the second example, due to the soldiers with numbers $4$ and $5$, the order of the soldiers is no longer correct.
The sergeant can arrange them as follows using 4 swaps: 

$6 \ 1 \ (5 \ 2) \ 4 \ 3 \rightarrow 6 \ 1 \ 2 \ 5 \ (4 \ 3) \rightarrow 6 \ 1 \ 2 \ (5 \ 3) \ 4 \rightarrow 6 \ 1 \ 2 \ 3 \ (5 \ 4) \rightarrow 6 \ 1 \ 2 \ 3 \ 4 \ 5$.

There is no method to arrange the soldiers with numbers $1 \ 2 \ 3 \ 4$ and $5$ using less than 4 swaps.

# Example 3

`stdin`
```
7 4
4 5 1 7 2 6 3
```

`stdout`
```
6
```

## Explanation

In the third example, one of the methods to order the soldiers with numbers $1 \ 2 \ 3$ and $4$ using $6$ swaps is:

$(4 \ 5) 1 \ 7 \ 2 \ 6 \ 3 \rightarrow 5 \ 4 \ 1 \ 7 \ 2 \ (6 \ 3) \rightarrow 5 \ (4 \ 1) \ 7 \ 2 \ 3 \ 6 \rightarrow 5 \ 1 \ (4 \ 7) \ 2 \ 3 \ 6 \rightarrow 5 \ 1 \ 7 \ (4 \ 2) 3 \ 6 \rightarrow 5 \ 1 \ 7 \ 2 \ (4 \ 3) 6 \rightarrow 5 \ 1 \ 7 \ 2 \ 3 \ 4 \ 6$.