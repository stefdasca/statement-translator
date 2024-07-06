```markdown
# Task
**This problem is interactive!**
Gigel, along with his friends, arrives by bus at Euro. Once the organizers learned this, they started preparing to receive him. They own a parking lot where the spots are lined up. The parking lot has a length of $N$ and is represented by a binary string $p$ of length $N$, where $p_i$ is $0$ if the $i$-th spot is free and $1$ if it is occupied. This parking lot is made for cars, not for buses, but the organizers make a compromise for Gigel, allowing him to park his bus "in reverse" (see drawing) on free spots. However, they tell Gigel that he **CANNOT** park his bus of length $K$ on a **maximal sequence of free spots with a length greater than $4K$**.
Since the organizers do not know the length of Gigel's bus, they want to write a string of natural numbers less than or equal to $1000$ on a piece of paper.

A maximal sequence of free spots is a sequence of free spots that has occupied spots or the ends of the parking lot to its left and right.

~[desen_autocar.png|align=center|width=50%]

# Interaction Protocol
The contestant must implement the functions:
```c++
vector<int> init(int N, vector<bool> p);
pair<int,int> solve(int N, int K, vector<int> v);
```
The function `init` will receive $N$ and the string $p$, indexed from 0, representing the parking lot, and will return the string $v$, which the organizers will write on the paper. The function `init` will be called only once for each test.
The function `solve` will receive $N$, $K$, and the string $v$ written on the paper by the organizers and **will return the ends of the maximal free sequence where Gigel's bus will be parked** (**for example, if spots 3, 4, 5, 6, 7 are free and the bus has a length of 2, it will return {3,7}**). It is guaranteed that there is always a place where Gigel can park his bus. The function `solve` will be called multiple times for each test, but the parking lot configuration will remain the initial one.

**The contestant WILL NOT have the `main` function in their program!**
**The contestant WILL NOT have global variables in their program!**

# Constraints and clarifications

* $1 \leq K \leq N \leq 1\ 000$

# Scoring
* If for a test, in a call to the `solve` function, the returned answer is incorrect, the solution will receive 0 points for that test.
* Let $L$ be the length of the string written by the organizers on the paper. Let $R = min(1,20/L)$.
* The score obtained for a test of $T$ points will be $T \cdot R^2$.
```

After reviewing the translated text, the translation is correct, syntax is preserved, and there are no grammatical errors.