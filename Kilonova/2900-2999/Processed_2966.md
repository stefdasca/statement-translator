**This is an interactive problem!**

Radu the Dragon is preparing for the match against Belgium. He wants to find out the number $N$ on the jersey of his direct opponent, Lakaka. Coach Fisu' lu' Tasu', who knows the number of the feared Belgian striker, wants to give him a hand, the process consisting of several steps. At each step, Radu comes with a sheet on which he writes a maximum of 5 numbers, and Fisu' will tell him which of them are divisors of the sought number. Because time is limited, Radu wants to be prepared for the match in as few steps as possible. Meanwhile, the Belgian Football Federation has announced that all their players will have numbers on their jerseys with prime divisors from the set $2, 3, 5, 7, 11$ and between $1$ and $10^{18}$.

# Interaction Protocol

You will need to write a program (`dragon.cpp`) that implements the following function:
```c++
long long solve();
```
It will need to return the number sought by Radu.

You can use this function (which represents one of the steps). **Attention! The array a must have a maximum length of 5**
```c++
vector<bool> ask(vector<long long> a);
```

**You must include `"dragon.h"`**
**The contestant will NOT have the main function in the program!**

# Local Testing

To test your program more easily, you have the attachments `grader.cpp` and `dragon.h`. The reading is done from the file `dragon.in` (the number $N$) and is displayed in `dragon.out` (the answer given by your program and the number of calls to the ask function).

# Constraints and Clarifications

* $1 \leq N,$ the numbers written by Radu on the sheet $\leq 10^{18} $;

# Scoring

* `userQ` = the number of queries made by your program, `bestQ` = the number of queries made by the official source;
* If the function returns an incorrect number, $0$ points will be awarded;
* If the function returns the correct number, the score will be calculated using the formula $1 - (1 - (bestQ / userQ) ^ {0.65})$.