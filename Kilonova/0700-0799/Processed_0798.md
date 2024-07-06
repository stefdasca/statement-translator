Vasilică is training on a competitive programming site with online evaluation. When he submits a solution to a problem on the site, it is evaluated on a certain number of tests. The score obtained for that problem will be equal to the sum of the points obtained on each test. Points assigned to the tests can be different. Moreover, if the problem is completely solved (i.e., it obtains maximum points on all tests), Vasilică also receives a bonus.

Vasilică can submit the solution to a problem multiple times. When he submits the solution for the first time, the score is calculated as described above. When he submits the solution for the second time, Vasilică is penalized by two points (that is, two points are subtracted from the total score obtained for the problem). When he submits the solution for the third time, the penalty is 4 points, for the fourth time it is 6 points, and so on. Note that each new attempt incurs a penalty that increases by two points.

# Task

Given the results obtained by Vasilică on each test for every solution he submitted, determine the maximum score he could obtain for that problem.

# Input data

The input file `submit.in` contains:

- The first line contains the natural number $N$ representing the number of tests on which the solution is evaluated.
- The second line contains $N$ natural numbers separated by spaces $P_1, P_2, \dots, P_N$, representing in order the score awarded for each of the $N$ tests.
- The third line contains a natural number $B$ representing the bonus (number of points awarded if the solution obtains a score on all tests).
- The fourth line contains a natural number $M$ representing the number of solutions submitted by Vasilică for the problem.
- The next $M$ lines, each containing the results obtained on tests for the $M$ solutions sent by Vasilică, in the order of submission. On the $i$-th line among the $M$, there are written $N$ values from the set $\{0, 1\}$, separated by spaces; the $j$-th value is $0$ if test $j$ was not solved correctly, respectively $1$ if test $j$ was solved correctly (obtaining the maximum allocated points on the test).

# Output data

The output file `submit.out` will contain a single line that will print the maximum score obtained by Vasilică on that problem.

# Constraints and clarifications

* $1 \leq N, M \leq 100$;
* $0 \leq P_i, B \leq 100$;

# Example

`submit.in`
```
4
10 5 5 20
13
3
0 0 0 0
1 1 1 1
0 1 0 1
```

`submit.out`
```
51
```

## Explanation

The problem is evaluated on $4$ tests. The points awarded on the tests are $10, 5, 5,$ and $20$. If all tests are correctly solved, a bonus of $13$ points is awarded.

For this problem, Vasilică submits $3$ solutions:

- The first submitted solution does not solve any test correctly, hence it obtains $0$ points.
- The second submitted solution correctly solves all tests, receiving $10+5+5+20=40$ points on the tests, to which $13$ bonus points are added; but since it is the second solution submitted, a penalty of two points applies. In total $40+13-2=51$ points.
- The third submitted solution correctly solves only tests $2$ and $4$, thus obtaining $5+20=25$ points and a penalty of $4$ points is applied, so the total score is $21$.

Therefore, the maximum score obtained by Vasilică is $51$.