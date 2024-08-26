# The Commission

With the arrival of spring comes the recruitment of commissions, and much like snowdrops, abuses sprout everywhere to herald this fact. Today, we want to recruit a commission from a sequence of $N$ people found randomly on the street while they were standing in a queue. Each of these $N$ people has a minimum number of people the commission must meet for that person to accept participation. Moreover, we have assigned each person, in a subjective and profoundly discriminatory manner, a risk grade. The higher the risk grade, the more harm that person can potentially cause to the commission, whether it involves breaching the confidentiality of subjects, stealing technical equipment, or verbally and/or physically assaulting other commission members. Since the people were found standing in a queue and we didn't want to bother ordering them in any way, it is necessary for the entire commission to form a continuous subarray of the queue. Knowing this, we want to find a valid commission with the minimum total risk.

## Input data

The input file `comisia.in` contains on the first line the number $N$ representing the number of people. The second line contains the array $A$, which represents the requirements of each person. More specifically, if the $a_i$-th value is equal to $x$, the person at position $i$ in the queue desires at least $x$ members in the commission. The third line contains the array $B$, which represents the risk factor of each person.

## Output data

The output file `comisia.out` will contain a single value, representing the minimum total risk of a commission that meets the requirements of the involved people.

## Constraints

$3 \leq N \leq 200\,000$

$1 \leq A_i \leq N$

$1 \leq B_i \leq 1\,000\,000\,000$

For tests worth 20 points

$N \leq 4\,000$

## Example

`comisia.in`
```
3
1 2 2
50 6 6
```

`comisia.out`
```
12
```

## Explanation

The first person is willing to be the sole member of the commission, but for no apparent reason, they held an axe in their hand during questioning, which is why they were assigned a risk grade of $50$. Thus, it is better to form the commission from the 2nd and 3rd persons.