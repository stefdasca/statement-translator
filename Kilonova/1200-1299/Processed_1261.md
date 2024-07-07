
A software production company is organizing an interview to fill a programmer position, to which $N$ candidates have applied. These candidates are ordered based on the moment they submitted their CV and numbered consecutively from $1$ to $N$. Each candidate has previously undergone a psychological profiling to determine their level of agitation caused by the upcoming interview, as well as the direction (increasing or decreasing) of change of this level. Thus, at the announced start time of the interview (which we will consider as moment $0$), each candidate has an initial level of agitation.

For each unit of time after moment $0$ and until the moment the candidate is invited for the interview (until then they must wait), their level of agitation changes by $1$: for some candidates, the level increases by $1$ unit, while for others it decreases by $1$ unit. If a candidate's level of agitation reaches $0$, from that moment on, for each subsequent unit of time, the level of agitation will increase by $1$ (the direction of the change in the level of agitation changes).

The company will invite candidates for the interview in groups, in the order of numbering (all candidates with order numbers less than a candidate $K$ will be invited in a previous group or in the same group as candidate $K$).

Before inviting a group, the interview committee may decide to wait for an integer number of units of time (zero or more). For a group, the duration of the interview is considered negligible (each candidate only needs to answer a few multiple-choice questions). From the moment a candidate is invited to the interview, their level of agitation remains constant. Since the company wants all candidates to maintain a good opinion regardless of the interview outcome, the committee will form the groups and choose the waiting times such that the total sum of the candidates' levels of agitation at the end of the interview is minimized.

# Task

Write a program that determines the total minimum sum of the candidates' levels of agitation at the end of the interview.

# Input data

The input file `agitatie.in` contains on the first line the natural number $N$, representing the number of candidates. On the next $N$ lines, there are two integers $A$ and $B$, separated by a space. $A$ represents the initial level of agitation of the candidate, and $B$ represents the direction of change of the agitation for each unit of time they wait (if $B$ is $1$, the level of agitation increases, and if $B$ is $-1$, the level of agitation decreases). Line $k+1$ in the file will contain the values corresponding to candidate number $k$.

# Output data

The output file `agitatie.out` will contain on the first (and only) line the total minimum sum of the candidates' levels of agitation at the end of the interview.

# Constraints and clarifications

* $1 \leq N \leq 3\ 000$
* $1 \leq$ initial level of agitation of each candidate $\leq 3\ 000$

# Example

`agitatie.in`
```
6
10 1
3 -1
2 -1
1 -1
9 1
6 -1
```

`agitatie.out`
```
23
```

# Explanation

The total minimum sum is $23$. A possible solution is the following: Form $3$ groups.

The first group consists of candidate $1$ alone and waits $0$ units of time. Thus, the final level of agitation for candidate $1$ will be $10$.

The second group will wait $2$ units of time from the moment the first group finishes its interview (thus starting the interview at moment $2$), and will include candidates $2, 3, 4,$ and $5$. The final levels of agitation for these candidates will be: $1, 0, 1,$ and $11$.

Note that candidate $4$'s level of agitation first dropped to $0$ and then increased to $1$. The third group will wait $4$ more units of time (thus starting the interview at moment $6$), and will include candidate $6$ alone. The final level of agitation for this candidate will be $0$.
```
