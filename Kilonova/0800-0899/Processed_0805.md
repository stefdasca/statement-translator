~[0.jpg|align=right|width=12em]

The specialists in chemistry have successfully created a wide range of immiscible liquid substances (which do not mix with each other), of the same density and different colors.

This result was used by specialists in physics to study the principle of communicating vessels. According to this principle â€œ*in a system of communicating vessels, the liquid level is the same regardless of the shape of the vessels*â€.

\
The physicists' experiments are conducted as follows:

In a system with **two** communicating vessels, graduated identically on each branch with $0$, $1$, $2$, $3$, $\\dots$, the physicists introduce a number of $n$ liquids, on the left branch or on the right branch. The volumes introduced from each liquid, denoted by $V_i$ ($1 \\leq i \\leq n$), are **positive even natural numbers** such that, at equilibrium, any liquid will settle between two graduations on the same side of a branch or on both branches of the communicating vessel system. The liquids are identified by their color, colors numbered $1$, $2$, $3$, $\\dots$, $n$. The introduction of the liquids in the system with two communicating vessels is done in increasing order of color numbers, starting with the liquid of color $1$.

~[1.png|align=right|width=15em]

\
The aim of the experiment is to determine the maximum graduation to which the liquids rise in the system with two communicating vessels, as well as to determine between which graduations a liquid of color $x$ is found, among those introduced.

For example, if the system with two communicating vessels contains $n=3$ liquids in order: $V_1=4$ liquid of color $1$ introduced through the right branch (operation coded `4 D`), $V_2=4$ liquid of color $2$ introduced through the left branch (operation coded `4 S`) and $V_3=2$ liquid of color $3$ introduced through the left branch (operation coded `2 S`) then the maximum graduation up to which the level of liquids rises in the system with two communicating vessels is $5$, and the liquid of color $x=2$ is found between graduations: $3$ on the left branch (`3 S`) and $1$ on the right branch (`1 D`), as shown in the attached figure.

# Task
Write a program that, given the number $n$ of liquids introduced in the system with two communicating vessels, the volume $V_i$ and the branch through which the liquid of color $i$ is introduced ($1 \\leq i \\leq n$), as well as the color $x$, calculates the maximum graduation to which the liquids rise in this system at equilibrium and determines between which graduations the liquid of color $x$ is found.

# Input data
The first line of the input file `vase.in` contains a single positive natural number $n$, with the above meaning. Each line, from the next $n$ lines, contains two values separated by a space: a positive even natural number and a capital letter, `S` or `D`, representing the volume introduced of the liquid of color $i$ and the branch (`S` for the left branch and `D` for the right branch) through which it is introduced. Line $n+2$ of the input file contains a single positive number $x$ representing the color of the desired liquid.

# Output data
The output file `vase.out` will contain on the first line a positive natural number representing the maximum graduation to which the liquids rise in the system of communicating vessels at equilibrium. The next two lines will each contain two values separated by a space: a natural number and a capital letter (`S` or `D`), representing the graduation and the branch where the desired liquid is placed.

# Constraints and clarifications
- $1 \\leq x \\leq n \\leq 100\\ 000$
- $2 \\leq V_i \\leq 100\\ 000$ for $1 \\leq i \\leq n$
- The system of vessels is graduated in the same units of measurement as the volumes of liquid.
- If the desired liquid, of color $x$, is placed on the same branch, the upper graduation will be displayed first and then the lower graduation.
- If the desired liquid, of color $x$, is placed on different branches, the graduation on the left branch will be displayed first and then the one on the right branch.
- If one of the graduations between which the desired liquid, of color $x$, is placed is $0$, then it is considered to be on the same branch as the other graduation.
- For solving the first requirement, $20\\%$ of the score is awarded, and for the second requirement, $80\\%$ of the score is awarded.

# Example
`vase.in`
```
3
4 D
4 S
2 S
2
```
`vase.out`
```
5
3 S
1 D
```

## Explanation
3 liquids are introduced into the system of two communicating vessels:
- the first with volume $4$, introduced on the right and has color $1$;
- the second with volume $4$, introduced on the left and has color $2$;
- the third with volume $2$, introduced on the left and has color $3$;

The graduations corresponding to the liquid of color $2$ are sought.
The maximum graduation that the liquid level reaches is $5$.
The liquid of color $2$ is placed between graduations $3$ on the left branch and $1$ on the right branch.