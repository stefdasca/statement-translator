~[img1.jpg|align=right|width=auto]

Goku is put in a SHOCKING situation: He has been poisoned by Dr. Gero and needs to find an antidote that will save his life. To prepare the antidote, he first needs to find the poison. He has $N$ bottles at his disposal, of which exactly one is poisoned. To help him, Krillin has made himself useful and duplicated himself $M$ times, so now Goku can use the $M$ Krillins as guinea pigs. Goku organizes a number of rounds; in each round, each Krillin drinks from a subset of bottles. Each Krillin who drank from a subset that contains the poisoned bottle dies and can no longer be used by Goku in the following rounds. You need to help Goku organize the rounds, and because he does not know how many rounds he has left to live, your goal is to determine the bottle with the antidote in as few rounds as possible.

# Interaction

Your program will interact with the commission's program. You must include the commission's header `dbsuper.h` at the beginning of your source and implement the function
```cpp
void solve()
```
You can have auxiliary functions, but the commission's program will call the `solve` function to test your solution. To solve the problem, the commission provides you with the following:
```cpp
void getBottlesAndKrillins(int &nrBottles, int &nrKrillins)
```
- You receive through the parameters $nrBottles$ and $nrKrillins$ the number of bottles and Krillins that Goku has at his disposal. This function can be called as many times as needed.
```cpp
void giveBottleToKrillin(int indexBottle, int indexKrillin)
```
- You give the bottle with index $indexBottle$ to the Krillin with index $indexKrillin$. You can call this function at the beginning of a round as many times as needed with any combination of parameters that respect the conditions: $1 \leq indexBottle \leq N$ and $1 \leq indexKrillin \leq M$, and the Krillin with index $indexKrillin$ is still alive.
```cpp
void testKrillins()
```
- You notify the commission that you have finished determining who drinks from which bottles. This call is made once per round, after you have finished all `giveBottleToKrillin` calls.
```cpp
void getDeadKrillins(int &P, int index[])
```
- You receive through the parameters $P$ and $index$, the number of Krillins dead in this round and their indices starting from position $0$ in the array. This function is called once after `testKrillins`, signifying the end of a round.
```cpp
void revealBottle(int indexBottle)
```
- You send the bottle with index $indexBottle$ as being the one with the antidote. This call is made once at the end instead of starting a new round.

A successful interaction consists of: calling `getBottlesAndKrillins`, then for each round calling `giveBottleToKrillin` followed by a `testKrillins` call and a `getDeadKrillins` call. After $R$ rounds, a final `revealBottle` call is made.

# Scoring

To receive the maximum score on a test, the number of rounds in which you find the solution must be less than or equal to the number of rounds required in the worst-case scenario. If $rounds[i]$ is the number of rounds your program finds if the poisoned bottle has index $i$, then your strategy must minimize the value $max(round[i] \ | \ 1 \leq i \leq nrBottles)$.

# Constraints and clarifications

- $1 \leq \ nrBottles \ \leq 125 \ 000$;
- $1 \leq \ nrKrillins \ \leq 16$;
- **Attention!** Your source will not have a `main` function.
- **Attention!** Failure to comply with the interaction mode will result in a null score.
- **Attention!** For a test, the `solve` function will be called multiple times.
- **Attention!** The new season of Dragon Ball Super will start in July $2015$.

# Example

Grader : `solve()`

Contestant : `getBottlesAndKrillins(N, M)`

Grader : $N = 2, M = 1$

Contestant : `giveBottleToKrillin(1, 1)`

Contestant : `testKrillins()`

Contestant : `getDeadKrillins(P, index)`

Grader : $P = 0, index = []$

Contestant : `revealBottle(2)`

## Explanation

We determine $N$ and $M$ initially, then give the first bottle to the only Krillin. We then notify the commission that we have finished determining who drinks from which bottles and ask to see the dead Krillins. We see that the tested Krillin is not dead, so the second bottle is the poisoned one.