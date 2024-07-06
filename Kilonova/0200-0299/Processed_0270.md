```markdown
A group of `N` robots votes to accept a proposal. Each robot votes `YES` or `NO`. The robots want to decide if at least half of them have voted `YES`.

All robots stand in a line. The robots can be in different states. The states are elements of the set `{1, ..., 28, Y, N, Major, Minor}`. At each step, robot `i` is in a state $ \it S_i$ and must decide which state to transition to for the next step. This decision depends only on $ \it S_{i-1}$, $ \it S_i$ and $ \it S_{i+1}$ because robots can only see their neighbors. They have a **common** set of rules that they follow (at a step, all robots will change their state according to this set of rules **simultaneously**). The leftmost and rightmost robot see the state `X` to the left and right, respectively (this state represents a "cliff" robot). At step `0`, all robots are either in state `N` (`NO`) or state `Y` (`YES`). They follow the set of rules until a robot declares that the result is `Major` (at least half of the votes are `YES`) or `Minor` (less than half of the votes are `YES`). If multiple robots declare at the same time, the leftmost one has priority. Additionally, the robots have a limit on the number of iterations. They must make a decision within this limit.

You need to determine a set of rules for the robots to correctly decide whether to accept the proposal or not. The basic format for the rules is as follows, notice how in this statement, uppercase italic letters represent any state:
\
$ \displaystyle \\text{\\it L \\ M \\ R \\ \rightarrow \\ E} $
\
A robot in state $ \it M$ whose left neighbor is in state $ \it L$ and right neighbor is in state $ \it R$ transitions to state $ \it E$. You can use the character `?` as a wildcard. It can replace any state among $ \it L, M, R$. You can also use multiple states separated by `/`, without spaces (only for $ \it L, M, R$). For example:
\
$ \displaystyle \\text{
? \\ 2/Y/10 \\ X \\ \rightarrow \\ Major
}
$
\
Here, the rightmost robot (because its right neighbor is in state $ \it X$), when its state is one of `2, Y` or `10`, will declare majority. If there are multiple rules that match for a robot, then the first one has priority. For example:
\
$ \displaystyle 
\\text{
1 \\ ? \\ 3 \\ \rightarrow \\ Major }
\\\\
\\text{
? \\ 2 \\ 3/10 \\ \rightarrow \\ 4
}
$
\
If a robot is in state `2`, with neighbors in states `1` (left) and `3` (right), this robot will declare majority because the corresponding rule is the first one. **Attention!** If a robot has no applicable instruction at a given time, the solution is considered incorrect.

# Output data

You must print the set of rules, each rule on a separate line.

# Constraints and clarifications
* `1 \leq N \leq 1\ 500`
* The maximum number of iterations is `7\ 500`.
* Note: You can select "Output Only" as the language to submit only the set of rules or you can declare a string in C++ over multiple lines as:
```cpp
std::string longString = R""""( 
line1
line2
)"""";
```

# Scoring
The score on the test is multiplied by a coefficient S which is determined based on the number of iterations and a constant T specific to each test:

* If `NrIterations \leq T`, then `S = 1`;
* If `T < NrIterations \leq T + 7`, then `S = 0.85`;
* If `NrIterations > T + 7`, then $max \left(0.75 \cdot \left (\frac{T +8}{NrIterations} \right) ^ {0.85}, 0.2 \right)$.

## Subtask 1 (10 points)
* `N \leq 10`
* `T = N + 1`
## Subtask 2 (20 points)
* `N \leq 99`
* `N` is odd
* `T = N + 1`
## Subtask 3 (30 points)
* `N \leq 1\ 499`
* `N` is odd
* $T = \left\lceil\frac{N}{2}\right\rceil+3$

## Subtask 4 (20 points)
* `N \leq 1\ 500`
* `N` is even.
* $T = \left\lceil\frac{N}{2}\right\rceil+3$

## Subtask 5 (20 points)
* `N \leq 1\ 500`
* $T = \left\lceil\frac{N}{2}\right\rceil+3$


# Example

`stdin` 
```text
In this problem, nothing is read from input. Instead, we offer you here an opportunity to rediscover yourself.
On a hill foot,
On a mouth of heaven,
Here they come,
Descending to the valley,
...
```
`stdout`
```
Y Y ? -> Major
? Y Y -> Major
Y ? Y -> Major
Y/N Y/N Y/N -> Minor
? Y ? -> Y
? N ? -> N
```

Explanation
---

The given example is a sequence of instructions that successfully determines the result for `N = 3`.
We can observe that the first `4` rules can be used only by robot `2` (because robots `1` or `3` "see" an `X`), and that robot can decide the winner (because `N = 3`). We notice that the rules need to be applied in order, as specified in the statement. The other `2` rules are for robots `1` or `3`.

```

