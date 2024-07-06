The Evil Ogre is holding the beautiful princess captive in an isolated castle, in a tall tower. RAU-Gigel hears this and rushes to save her. He has to cross a defense channel of length $K$, by placing $N$ stones of equal size units, in the form of steps with heights $h$, $h+1$, $h+2$, $h+3$, ..., $h+K-1$. The first step must have at least one stone, and if a single stone is left undistributed, the entire construction will collapse.

If the number $N$ of magical stones and the distance $K$ between RAU-Gigel's position and the princess's dungeon are known, can we determine if RAU-Gigel will successfully build the steps?

~[img1.jpg|align=center|width=26em]

RAU-Gigel attempts his chances. A failure will mean giving up on the princess. However, a success will lead to a surprise from the ogre: he will subject RAU-Gigel to a new challenge:

> RAU-Gigel, my boy,
> I will challenge you hard!
> If you win the test,
> You shall have the princess!

And he proposes the following test: "*we will alternately choose one of the steps you have constructed and knock down any number of stones from it, at least one, at most all. The too-beautiful princess will remain with the one of us who knocks down the last stone*." RAU-Gigel will start first, and both RAU-Gigel and the ogre will play responsibly, meaning they will always make the best choice in their own interest. Will RAU-Gigel manage to free the princess?

For example, if we have $N = 5$ and $K = 2$, RAU-Gigel constructs $2$ steps with heights $2$ and $3$, so no stones remain unused. Let's see now who will win the second challenge. RAU-Gigel will choose first. He can choose the first step and knock down all the stones on it, but this will be a wrong choice as the ogre will knock down all the stones from the second step, keeping the princess captive. Therefore, RAU-Gigel will not start by knocking down all the stones from a step.

Another option would be for RAU-Gigel to choose the first step and knock down a single stone. This would again be a wrong move, as the ogre would knock down two stones from the second step, and now, whatever choice RAU-Gigel makes, he would lose.

Surely, RAU-Gigel will choose the second step and knock down a single stone. The ogre will have no way out of this situation: if he knocks down both stones from any step, RAU-Gigel will knock down the other two stones and win; if the ogre knocks down only one stone from any step, RAU-Gigel will choose a stone from the other step, and then again, they will take turns knocking down one stone each, and the ogre will have nothing left to knock down, and RAU-Gigel will leave with the too-beautiful girl.

# Task

Multiple scenarios like the one above will be tested.

# Input Data

The input file `donjon.in` contains on the first line the number $Q$ representing the number of scenarios, then on the next $Q$ lines there will be two numbers $N$ and $K$ separated by a space, with the meaning from the statement.

# Output Data

The output file `donjon.out` will contain $Q$ lines with the answers to the $Q$ scenarios, as follows: if RAU-Gigel does not manage to build the steps, the answer will be the uppercase letter `C`. If he manages to build the steps, the answer will be $x \\ y$, separated by a space, where $x$ is the uppercase letter `C` if the ogre wins the second challenge, or the uppercase letter `G` if RAU-Gigel saves the princess, and $y$ is a non-zero natural number representing the number of stones used by RAU-Gigel for the first step.

# Constraints and Clarifications

* $1 \\leq Q \\leq 10$
* $2 \\leq N \\leq 10^{18}$
* $2 \\leq K \\leq 10^9$
* For tests worth 20 points: $Q \\leq 5$, $N \\leq 10$ for all scenarios.
* Tests worth 30 points are favorable to RAU-Gigel for all scenarios, meaning that if he passes the first challenge and manages to build the steps according to the task, it is guaranteed that he will also win the second challenge.

# Example

`donjon.in`
```
3
5 2
6 3
5 3
```

`donjon.out`
```
G 2
C 1
C
```

## Explanation

We have $3$ scenarios.

In the first scenario, there are $5$ stones, and the width of the channel is $2$. The answer for this scenario will be `G 2` because RAU-Gigel succeeds in both challenges, and the first step constructed has $2$ stones (see explanation above).

For the second scenario, we have $N = 6$ and $K = 3$. RAU-Gigel passes the first test and constructs the three steps: $1$, $2$, $3$. But, no matter how he tries to knock them down, the ogre will have the last move. The answer for this scenario will be `C 1` because, although RAU-Gigel passes the first challenge by placing one stone as the first step, he loses the final game.

For the last scenario, the answer is `C`, RAU-Gigel cannot build $3$ steps with $5$ stones, according to the task, which would ensure his passage to the princess's dungeon.