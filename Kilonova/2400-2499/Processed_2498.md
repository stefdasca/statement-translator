> Grandpa says this, brother... there is a saying: "The wolf may lose its fur, but it still eats sheep." - Grandpa, "The coolest hack"

# Task

Following a flood from the enemies, Grandpa lost his two wallets somewhere on the Ox axis. To find them, Grandpa will use his secret weapon: the coolest hack.

If Grandpa is at coordinate $x$ and the two wallets are at coordinates $a$ and $b$ ($-10^4 \le x,a,b \le 10^4$, $a<b$), then the coolest hack will calculate the sum of the distances from Grandpa to the two wallets (i.e., $|x-a|+|x-b|$).

Help Grandpa find his wallets, using the coolest hack as few times as possible.

# Interaction Protocol

The contestant will need to implement the following function:
```c++
std::pair<int,int> solve();
```
This function will return a pair of integers $(a,b)$ ($-10^4 \le a<b \le 10^4$), the coordinates of the lost wallets.

The contestant can call the following function to see the sum of the distances from Grandpa (who is at coordinate $x$) to the two wallets:
```c++
int cel_mai_tare_hack(int x);
```
For any call to this function, $x$ must satisfy $-10^4 \le x \le 10^4$. Otherwise, the submitted source will receive the verdict "Invalid query".

# Constraints and clarifications

* $-10^4 \le a < b \le 10^4$;
* The file `cel_mai_tare_hack.h` must be included in the submitted sources.
* In "Attachments" you can find the grader `lgrader.cpp`, the header `cel_mai_tare_hack.h`, and an example source (`cel_mai_tare_hack.cpp`).

# Scoring

We denote by:
- `optim`: the number of calls to the `cel_mai_tare_hack` function by the commission's source
- `Q`: the number of calls to the `cel_mai_tare_hack` function by the contestant's source

If the maximum score associated with a test is $s$, then a source that correctly identifies the coordinates of the wallets will receive on that test a score equal to $s \cdot p$, where:
* $p=0$, if $Q>2 \cdot 10^4+5$
* $p=0.1$, if $10^4 < Q \le 2 \cdot 10^4+5$
* $p=0.1 + 0.1 \cdot (4-\log_{10}(Q))$, if $100 < Q \le 10^4$
* $p=0.3 + 0.1 \cdot \frac{100-Q}{35}$, if $65 < Q \le 100$
* $p=0.4 + 0.2 \cdot \frac{65-Q}{30}$, if $35 < Q \le 65$
* $p=0.7 - 0.1 \cdot \frac{Q-optim}{35}$, if $optim+1 < Q \le 35$
* $p=0.9$, if $Q=optim+1$
* $p=1$, if $Q \le optim$

# Example interaction

* Commission: reads $a=-3$ and $b=-2$
* Commission: `solve()`
* Contestant: `cel_mai_tare_hack(-1)`
* Commission: `3`
* Contestant: `cel_mai_tare_hack(-3)`
* Commission: `1`
* Contestant: `return {-3,-2}`
* Commission: `OK 2 queries used