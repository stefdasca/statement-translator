After finishing cleaning the house, Harry remembered that he hadn't sent a message to his friends, Henry and Hetty, for a long time. Since his laptop is being repaired, Harry decided to send them a SMS. The message that Harry wants to send is composed of $N$ characters, all being among the first $K$ lowercase letters of the English alphabet.

Harry's phone has a QWERTY keyboard, but the keys are very small, so Harry can never be sure that he will press the desired key. For each character $C$ that has the order number $i$ in the English alphabet $(1 \leq i \leq K)$, Harry has determined the following probabilities:

* $pCorect_i$ - the probability that Harry will press the character $C$;
* $pIncorect_i$ - the probability that Harry will press a character other than $C$;
* $pBackspace_i$ - the probability that Harry will press backspace and thus delete the last written character.

It is well known that Harry always notices when he presses a wrong character, which he deletes immediately by pressing the Backspace key (which he will always press correctly). If it happens that Harry presses Backspace when there is no character written in the message, nothing happens.

# Task

Knowing that each key press lasts exactly one unit of time, calculate the average time it will take for Harry to type the message. The average time to write the message is defined as the sum of $T \cdot P_T$, for $T$ from $0$ to infinity, where $P_T$ is the probability of writing the text in exactly $T$ key presses.

# Input data

The first line of the input file `sms.in` will contain two natural numbers $N$ and $K$, with the meaning from the statement. The next line will contain the message Harry wants to send: a sequence of $N$ characters, composed only of the first $K$ letters of the English alphabet. On the next $K$ lines, the probabilities determined by Harry will be found as follows: on line $2+i, \\ (1 \leq i \leq k)$ there will be $3$ real numbers, $pCorect_i, \\ pIncorect_i, \\ pBackspace_i$, with the meaning from the statement.

# Output data

The first line of the output file `sms.out` will print a real number - the average time it will take for Harry to write the message.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$
* $1 \leq K \leq 26$
* The answer will be verified with a relative precision of $0.0001$.
* For $40\%$ of the tests, $1 \leq N \leq 500$.
* For any $i, 1 \leq i \leq K$, we have the equality $pCorect_i + pIncorect_i + pBackspace_i = 1$.

# Example 1

`sms.in`
```
1 1
a
0.5 0.0 0.5
```

`sms.out`
```
2.0
```

## Explanation

Harry has a $\\frac{1}{2^k}$ probability of pressing the `a` key correctly after $k$ presses for the first time. The average time to type it is thus $1 \cdot \\frac{1}{2} + 2 \cdot \\frac{1}{4} + 3 \cdot \\frac{1}{8} + 4 \cdot \\frac{1}{16} + \\dots = 2$

# Example 2

`sms.in`
```
3 1
aaa
0.5 0.5 0.0
```

`sms.out`
```
9.0
```

# Example 3

`sms.in`
```
3 1
aaa
0.5 0.25 0.25
```

`sms.out`
```
10.625
```

