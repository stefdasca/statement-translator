Chef John is tired of making vegetable soup and has moved on to cooking soups with numbers! To complete his creative process, he bought a machine, but unfortunately, it has an advanced locking mechanism. Thus, he asks for your help to unlock it.

# Task
There is a hidden number $X$ that belongs to the interval $[1, N]$. 
You are allowed to make the following type of $query$:

```
ask(Y)
```

If $Y > X$, the function will return $-1$. 
If $Y < X$, the function will return $+1$. Additionally, different from the previous case, the number X will obtain a new value within the same interval, i.e., $[1, N]$. **Each number in the interval has an equal probability of being chosen as the new value of $X$.** 
> Otherwise, if $Y = X$, the function will return 0, and you can stop interacting. 
**$Y$ must belong to the interval $[1, N]$. Otherwise, the interaction will end!**

# Interaction Protocol
The contestant must implement a function:
```cpp
void solve(int N)
```
The parameter N is the one mentioned above. **The contestant does not need to implement the main function.** 
The contestant can call the following function for a query:
```cpp
int ask(int Y)
```
The function will behave as described in the statement.

# Constraints and clarifications
* $1 \leq N \leq 10^6$;
* You must include `bucataria.h`;
* You can write your code in `bucataria.cpp`, filling in the $solve$ function directly.
* Within a test: Let $best$ be the number of queries considered optimal by the committee, and let $you$ be the number of queries made by the contestant.
* The scoring per test is done using the following formula: $score = \lceil {testPoints \cdot \min(\frac{best + error}{you}, 1)} \rceil$, where $testPoints$ represents the number of points corresponding to the respective test, and $1 \leq error \leq 20$ is a tolerance allowed in your program to provide a chance for maximum points.

# Example
```plaintext
N = 10, X = 5
```

```plaintext
contestant: ask(3); committee: +1,X=4
contestant: ask(5); committee: -1
contestant: ask(4); committee: 0

the interaction ended successfully after 3 queries.
