## Task

On May 1st, the weather is scorching, so two charming individuals buy a bottle of still water each and drink them in the Unirii area. Unfortunately for them, the Romanian Police are doing their duty that day, ensuring no one over-hydrates during the celebration. The law enforcement officers catch the two drinkers and inform them that it's not polite to consume water in public spaces and that it would have been better to go to a terrace or at least a park. Justice does its duty and they need to legitimize the two charming individuals. Being smart guys, they think of lying to the law officers by giving a fake $CNP$. To make it plausible, the first individual thinks of a number $A$, and the second individual a number $B$. The number of digits in $A$ and $B$ is the same. Then they calculate the sum $A+B$ and apply a dubious hash function to this number which transforms the sum into $CNP$ (we won’t specify this function so no one is tempted to deceive the Romanian Police). Unfortunately, after drinking too much water, the two lads cannot calculate the sum $A+B$. Quickly write a program to get the two handsome guys out of trouble!

## Input data

The input file `staropramen.in` contains on the first line $T$, the number of tests. Each test will contain on the first line $N$, the number of digits of $A$ and $B$. On the next line are $2 \times N$ digits. Let $a_1, a_2, a_3, \dots, a_N$ be the digits of $A$ and $b_1, b_2, b_3, \dots, b_N$ be the digits of $B$. Due to the water, the brilliant individuals transmit the number in the form $a_1, b_1, a_2, b_2, \dots, a_N, b_N$. For clarifications, see the example!

## Output data

In the output file `staropramen.out` will be $T$ numbers. Each line will contain the sum $A+B$.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N \leq 500\ 000$

The numbers $A$ and $B$ will not contain "leading zeros".

Attention! Read the format in which the numbers $A$ and $B$ are provided.

Beware of the memory limit!

The two charming guys agree with Ombladon's 2014 hit 🙂.

## Example

`staropramen.in`

```
3
1
23
3
257135
1
57
5
788
12
```

`staropramen.out`

```
5
788
12
```

## Explanation

$2+3 = 5$

$273+515 = 788$

$5+7 = 12$