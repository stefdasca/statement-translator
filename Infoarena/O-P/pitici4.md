## Pitici4

Laura lives together with the $N$ dwarves. On one of the past days, the dwarves went for a walk through the forest surrounding their cottage. During the walk, the dwarves formed several groups, each dwarf forming a group with his closest friends. As the forest paths are quite narrow, two groups of dwarves could not walk in parallel. Unfortunately, in such situations when the dwarves start chatting, they tend to forget their good manners, and soon they became so noisy that they started disturbing the other creatures in the forest. Laura found out about this and decided to scold them, but first, she wanted to know how they were arranged in groups. The dwarves do not want to betray their close friends and, therefore, all they are willing to tell Laura are phrases of the following type: The total number of dwarves from other groups that were in front of me and behind me is $A_i$ and, respectively, $B_i$. Some of the smarter dwarves figured out that this information is sufficient for Laura to reconstruct their group arrangement and to confuse her, they lied. As things did not add up, Laura realized that some dwarves lied to her. Since she can no longer reconstruct their arrangement, she wants to know the maximum number of dwarves whose information does not contradict each other.

## Task

Knowing the information provided by the dwarves, determine the maximum number of dwarves whose information does not contradict each other.

## Input data

The input file `pitici4.in` will contain, on the first line, the integer $N$. The following $N$ lines contain two integers $A_i$ and $B_i$ corresponding to the statements made by the dwarves.

## Output data

The output file `pitici4.out` will contain a single integer representing the maximum number of dwarves whose information does not contradict each other.

## Constraints

$1 \leq N \leq 200\ 000$

$0 \leq A_i$

$0 \leq B_i \leq 10^6$

For $20\%$ of the tests, $N \leq 18$

For $50\%$ of the tests, $N \leq 5\ 000$

## Example

`pitici4.in`
```
9
6 4
0 4
4 4
6 0
5 3
0 4
0 4
6 0
7 0
```

`pitici4.out`
```
6
```

## Explanation

**Example 1**

: We can assume that there are 3 groups: the first of 5 dwarves, the second of 1 dwarf, and the last of 3 dwarves. For this group arrangement, the dwarves whose information does not contradict are $2$, $4$, $5$, $6$, $7$, and $8$. Dwarves $2$, $6$, and $7$ would belong to the first group, dwarf $5$ forms the second group, while dwarves $4$ and $8$ would belong to the third group. This group arrangement corresponds to the maximum number of dwarves whose information does not contradict. In this example, we also notice that the statement of the first dwarf will never be true (he claims that there are at least $6+1+4=11$ dwarves in total).

**Example 2**

: We can assume that there are two groups: one of 3 dwarves and one consisting of a single dwarf. We can consider that any 3 dwarves are telling the truth, but the fourth one must necessarily be lying (since he cannot be in the same group with the other $3$, who state that one dwarf is in another group behind them).