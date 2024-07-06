```markdown
# Task
The local zoo has acquired a large open garden where animals can move freely as in their natural habitats and can entertain visitors with their usual antics.
The most appreciated animals are the monkeys. With their climbing, jumping, and other skills, they delight both old and young visitors alike.
\
One species of monkey specializes in climbing tall trees and gathering coconuts. Another species specializes in cracking them open.
There are $N$ monkeys of the first type (numbered from $1$ to $N$) and $M$ monkeys of the second type (numbered from $1$ to $M$).

Monkey $k$ of the first type needs $A_k$ seconds to find a good spot on the tree from which it gathers the first coconut. Thereafter, the monkey collects a new coconut every $B_k$ seconds.
Monkey $k$ of the second type needs $C_k$ seconds to find a good tool to open the coconuts, after which it opens the first coconut. Thereafter, the monkey opens a new coconut every $D_k$ seconds.
\
Unfortunately, the second type of monkey is extremely aggressive, so it is not possible for both types to be in the garden at the same time. Therefore, the zoo caretakers will drive away the first type of monkeys as soon as they have collected all the coconuts. Similarly, if the second type of monkeys stays too long after opening all the coconuts, there will be fights between the monkey mafia clans. For this reason, the zoo caretakers will remove them from the garden immediately after they have opened all the coconuts.
\
The zookeepers arrive first immediately after all the coconuts have been collected and again immediately after the monkeys open them all. The time it takes for the monkeys to enter or leave the garden is also negligibly small.
\
Little Tommy particularly likes the second type of monkey but can never guess when to arrive to see them. Help him calculate the hour at which the second type arrives if he knows the total time spent by the monkeys in the garden (the total time of both types), but does not know the number of coconuts in the garden.
\
**Note: The input data is read from the keyboard, and the output data is displayed in the console.**

# Input data
The first input line contains the natural number $T$, the total time spent by the monkeys in the garden.
The second input line contains the natural number $N$, the number of monkeys of the first type.
The next $N$ input lines contain pairs of natural numbers $A_k \\ B_k$, representing the speeds of the first type of monkeys.
The next input line contains the natural number $M$, the number of monkeys of the second type.
The next $M$ input lines contain pairs of natural numbers $C_k \\ D_k$, representing the speeds of the second type of monkeys.

# Output data
Print on the first line the number of seconds between the arrival of the first type of monkeys and the arrival of the second type of monkeys.

# Constraints and clarifications
- $ 1 \\le T \\le 10^9 $
- $ 1 \\le N, M \\le 100 $
- $ 1 \\le A_k, B_k, C_k, D_k \\le 10^9 $
- For 60 points, $T \\le 1000$.

# Example 1
  `stdin`
  ```
12
1
3 1
1
5 1
  ```

  `stdout`
  ```
5
  ```

# Example 2

`stdin`
  ```
20
2
3 2
1 3
3
3 1
4 1
5 1
  ```

  `stdout`
  ```
13
  ```
```
