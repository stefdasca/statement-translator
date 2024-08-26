# Superbec

Marcel has $N$ light bulbs, numbered from $1$ to $N$, which can light up brightly, light up dimly, or not light up at all. To change the states of the bulbs, he can press any of the following buttons as many times as he wants:

Button $A$, which modifies the state of all the bulbs. Button $B$, which modifies the state of the bulbs with an even index. Button $C$, which modifies the state of the bulbs with an odd index. Button $D$, which modifies the state of the bulbs with an index of the form $\dots$, natural number Button $E$, which modifies the state of the bulbs with an index of the form $\dots$, natural number Button $F$, which modifies the state of the bulbs with an index of the form $\dots$, natural number Button $G$, which modifies the state of the bulbs with an index of the form $\dots$, natural number Button $H$, which modifies the state of the bulbs with an index of the form $\dots$, natural number Button $I$, which modifies the state of the bulbs with an index of the form $\dots$, natural number 

The modification of a button state is done as follows:

if the bulb was off, it will light up dimly; if it was dim, it will light up brightly; if it was bright, it will no longer light up. Initially, all bulbs are off. Marcel presses random buttons $M$ times, and in the end, he notes the state of each bulb. He wonders what is the number of ways to obtain that state, all from $M$ moves, considering that the initial state is the same (all bulbs are off). The order of pressing the buttons does not matter ($ABA$ is considered the same sequence of moves as $AAB$).

## Input data

The input file `superbec.in` will contain on the first line the number $T$ of tests. The structure of each test is described below: The first line will contain the numbers $N$ and $M$, and on the next line, $N$ characters equal to either $0$ (bulb off), $1$ (bulb lighting dimly), $2$ (bulb lighting brightly), or the character $?$ (bulb whose state is unknown even to Marcel), or $a$ (from Marcel's memories - bulb whose state can be $0$ or $1$), or $b$ (bulb whose state can be $1$ or $2$), representing the final state of the bulbs.

## Output data

The output file `superbec.out` will contain $T$ lines, each giving the answer to a test, the answer being a single number, representing the remainder when dividing by $ \dots $ the number of ways to press the buttons $M$ times and obtain the sequence given in the input, for that test.

## Constraints and clarifications

A way to press the buttons $M$ times is considered to obtain the sequence given in the input if there is a way to associate each character $?$ in the input with one of the characters $0$, $1$, or $2$, each character $a$ with $0$ or $1$, and each character $b$ with $1$ or $2$ such that the encoded sequence of bulbs in the input is identical to the encoded sequence of bulbs as they appear after the $M$ button presses.

$1 \leq M \leq 1\ 000\ 000\ 000$

$1 \leq N \leq 100\ 000$

$1 \leq T \leq 100$

Subtask 1 (20 points):
$1 \leq T, N, M \leq 10$

Subtask 2 (30 points):
the sum of those $T$ numbers $N$ will not exceed $10\ 000$
$1 \leq M \leq 200\ 000$

Subtask 3 (20 points):
the sum of those $T$ numbers $N$ will not exceed $10\ 000$

Subtask 4 (30 points):
initial constraints

## Example

`superbec.in`
```
10
5 1
01010
6 3
0a1?0?
10 5
01?02b?10?
7 3
b?a??0?
15 20
?22??222?a?bb10
20 56
?a?02ab22?b2?a?1?a1?
27 21
0?20?02??2122a?21?0?a?a10??
27 16
0?1a?0a0?a1a1?a?12a?aa?a0?a
30 10
???????a???a?????b????1???b??1
40 100
2??2??1???1??1??0??2??b?b2?????1???2?0??
1 3
1
```

`superbec.out`
```
36
1287
0
0
0
1109
48903492
```

## Explanation

First test: the only valid way to press the button is: $B$

Second test: the 3 valid ways to press the buttons are: $BHI$, $GHI$, $HII$

Third test: the only valid way to press the buttons is: $BCCDI$

Other tests: Trust the committee!