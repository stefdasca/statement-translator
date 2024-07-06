Sure, here is the translated text while preserving the format and extensions:

---

The Sports Club SEPI also has a section for figure skating. The club's management has decided to participate in the pairs event at the next Olympics and needs to make some decisions regarding the teams they can register.

Each participating team at the Olympics must consist of a pair of skaters (a girl and a boy) and a coach. Additionally, the values of the team members must be as close as possible. The value of an athlete and respectively of a coach is calculated based on the results obtained in previous competitions. These are encoded as a single number with at most $9$ digits. Each digit of the number represents a previous result, and **the sum of the digits represents the value of the athlete or coach**. For example, the number $18305$ encodes the results $1, 8, 3, 0, 5$, obtained in the last $5$ competitions, which corresponds to the value $17(= 1 + 8 + 3 + 0 + 5)$.

At the Olympics, each athlete and each coach can be part of at most one registered team. Additionally, for each team, if we denote $V_M$ as the maximum among the values of the coach, the girl, and the boy, and $V_m$ as the minimum among the values of the coach, the girl, and the boy, registration in the competition is only allowed if $V_M - V_m \leq 1$.

# Task
Given the numbers that encode the results of the coaches, girls, and boys, write a program to determine:
1. The maximum number of teams, $N_P$, that SEPI Sports Club can register at the Olympics such that they meet the above rules.
2. The maximum value, $V$, of a club coach who can train a pair of skaters (girl, boy), who can be registered at the Olympics according to the above rules and the number of variants $N_V$ in which a team can be chosen that can be trained by a coach with value $V$.

# Input data
The text file `patinaj.in` contains:
* the first line contains the natural number $C$ which represents the task number and can have one of the values $1$ or $2$;
* the second line contains a natural number $N$, which represents both the number of hired coaches, as well as the number of girls and boys registered at the club;
* each of the following three lines contains $N$ values, separated by a space. The third line represents the encoding of the previous results of the $N$ coaches, the fourth line represents the encoding of the previous results of the $N$ girls, and the values on the fifth line represent the encoding of the previous results of the $N$ boys.

# Output data
In the text file `patinaj.out` you will print:
* for task $1$: the maximum number of teams $N_P$ that can be registered at the Olympics according to the above-mentioned rules;
* for task $2$: two natural numbers, $V$ and $N_V$, separated by a space, representing the maximum value of a club coach for which there is at least one pair he can train and respectively the number of variants in which the club can choose a team that can be trained by a coach with value $V$, if task $2$ is being solved. If the club cannot register any pair, print a single number: $−1$.

# Constraints and clarifications
* $1 \leq N \leq 100 \ 000$;
* each of the numbers read from the third, fourth, and fifth lines of the file is a natural number **with at most 9 digits**;
* For $51$ points, $C = 1$;
* For $49$ points, $C = 2$;

# Example 1

`patinaj.in`
```
1
4
8093 18305 20009 188
1803 3303331 909 91995
8017 20009 0 8017
```

`patinaj.out`
```
2
```

## Explanation

At most $2$ teams can be formed. The first could be formed from the girl with encoding $1803$ and the boy with encoding $20009$ and trained by the coach with encoding $20009$. The second could be formed from the girl $3303331$, the boy $8017$, and trained by the coach $18305$.

# Example 2

`patinaj.in`
```
2
4
8093 18305 20009 188
1803 3303331 909 91995
8017 20009 0 8017
```

`patinaj.out`
```
17 4
```

## Explanation

The club has 4 coaches with values 
$20 = 8 + 0 + 9 + 3$, $17 = 1 + 8 + 3 + 0 + 5$,
$11 = 2 + 0 + 0 + 0 + 9$ and $17 = 1 + 8 + 8$.
The maximum value is $20$, but there is no pair that can be trained by the coach with value $20$ according to the imposed rules. 
Instead, a coach with value $17$ can train a pair registered at the Olympics. There are $4$ options to choose a team trained by a coach with value $17$. These could include the girl $3303331$ and one of the two boys with previous results encoding $8017$. Such a pair could be trained by the coach $18305$ or $188$.

---