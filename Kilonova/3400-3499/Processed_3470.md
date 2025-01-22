Recently, Bob joined the Romanian Navy and has been entrusted with the task of piloting a helicopter. On his first mission, he will fly over an area currently in conflict. The topographic map of this area is given as an $N$ x $M$ matrix, where the position $(i, j)$ represents the height at that point.

The helicopter can move north, south, east, west, up, or down by one unit, with each movement taking one second. However, it is not allowed to leave this area, as it is extremely dangerous.

As we all know, Bob is a very cautious person. He wants to determine the minimum time it will take him to land in any scenario, in case of an emergency (we know that Bob has landed if his current altitude matches the altitude of the position he is on).

## Task

For any position $(i, j)$ where $1 \leq i \leq N $ and $1 \leq j \leq M $, determine the minimum time to land, knowing that Bob is at altitude $H$, **above all altitudes in the matrix**.$^†$

## Input data

The first line contains a single integer $T$ - the number of test cases. The description of a test case is as follows:
- The first line contains three integers, $N$, $M$, and $H$.
- The next $N$ lines each contain $M$ values, each representing the height at that point.

## Output data

For each test case, print the desired output in the following format:
- $N$ lines, each containing $M$ values, where each value represents the minimum time to land from that point.

## Constraints and clarifications

$\textcolor{red}{Attention!}$ Due to the large amount of input and output data, we recommend adding the following lines of code at the beginning of the `main` function:
```cpp
ios_base::sync_with_stdio(false);
cin.tie(0);
```

- $1 \leq T \leq 10^6$
- $1 \leq N \leq 10^6$, $1 \leq M \leq 10^6$
- Let $S$ be the sum of all $N×M$ values across all test cases:
  - $1 \leq S \leq 10^6$
- $1 \leq H \leq 10^7$
- $0 \leq$ values in the matrix $< H$
- ***$H$ > the maximum value in the matrix***$^†$

### Scoring

| Subtask | Points | Constraints                   |
|---------|--------|-------------------------------|
| 1       | 14     | $S \leq 10^3$                |
| 2       | 18     | $H \leq 10$                  |
| 3       | 20     | $N = 1$                      |
| 4       | 48     | No additional constraints    |

## Example

**Input**
```plaintext
2
2 2 5
0 1
2 3
5 5 6
2 0 1 2 0 
5 5 1 3 2 
1 0 3 0 0 
4 4 3 5 0 
4 0 3 0 4 
```

**Output**
```plaintext
4 3 
3 2 
2 2 3 4 5 
1 1 2 3 4 
2 2 3 2 3 
2 2 2 1 2 
2 3 3 2 2  
```

## Explanation

In the first test, an example strategy could be as follows:
- Take off from (1, 1), land at (2, 1)
- Take off from (1, 2), land at (2, 2)
- Take off from (2, 1), land at (2, 1)
- Take off from (2, 2), land at (2, 2)