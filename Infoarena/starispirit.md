## Task

Gigel has a new hobby: he follows his friends' activities on the social network FaceBook each day. Thus, for any friend of his on the social network, Gigel knows the activity performed on a certain day. Moreover, Gigel started to keep various statistics about the moods that each friend goes through, as well as about the activities they perform. As a result, for each friend, Gigel knows both the $M$ activities performed by them, and the $K$ moods that the respective friend goes through. Furthermore, he has observed or calculated the following things about his friends:

1. The probability distribution of moods for each of his friends ($dist[1\ldots K]$). This is used by Gigel to estimate the mood only if there is no information about any previous day.

2. The mood of a day depends only on the mood of the previous day. In fact, the real model is more complicated, but Gigel thought to help you by using this assumption. The transition probability from a mood on the previous day to the mood on the current day is denoted by the matrix $A[1\ldots K][1\ldots K]$, called the transition matrix. These matrices are individual for each person.

3. The activity performed by each person on a day depends only on their mood on that day. Therefore, for each friend's mood, Gigel knows the probability distribution that his friend performs a certain activity on that day. This distribution is modeled by a matrix $B[1\ldots K][1\ldots M]$, where each row in this matrix specifies the distribution for mood $K$. So $B[i][j]$ represents the probability that the person performs activity $j$ if they are in mood $i$.

Gigel needs you to help him solve the following problem: determine the most probable sequence of $N$ moods that one of his friends goes through, starting from the list of activities performed by them for a consecutive sequence of $N$ days.

## Input data

The input data is read from the file `starispirit.in`.

The first line contains the number of tests, $T$.

After that, for each test, the following information is read.

The first line for each test contains 3 natural numbers: $N$ - the number of days in the analyzed sequence, $K$ - the number of moods, and $M$ - the number of activities performed by the current friend.

The second line contains $N$ natural numbers between $1\ldots M$ separated by spaces, representing the activities performed by Gigel's friend in the sequence of $N$ days.

The next line contains the $K$ real numbers modeling the distribution $dist[1\ldots K]$ separated by spaces.

The following $K$ lines contain $K$ real numbers modeling the distribution corresponding to $A[i], 1 \leq i \leq K$.

Finally, the last $K$ lines contain $M$ real numbers modeling the distribution corresponding to $B[j], 1 \leq j \leq K$.

## Output data

For each test, print a line in the file `starispirit.out`, which contains $N$ real numbers corresponding to the most probable sequence of moods that Gigel's friend went through.

## Constraints

$1 \leq T \leq 20$

$1 \leq N, M \leq 1000$

$1 \leq K \leq 30$

Activities are numbered from $1 \ldots M$

Moods are numbered from $1 \ldots K$

## Example

`starispirit.in`

```
4
1 2 2
1
0.75 0.25
0.5 0.5
0.3 0.7
0.5 0.5
0.5 0.5
1 2 2
1
0.75 0.25
0.5 0.5
0.3 0.7
0.1 0.9
0.5 0.5
4 2 3
1 2 2 2
0.75 0.25
0.75 0.25
0.25 0.75
0.50 0.25 0.25
0.1 0.9 0.1
3 2 3
1 2 3
0.6 0.4
0.7 0.3
0.4 0.6
0.5 0.4 0.1
0.1 0.3 0.6
```

`starispirit.out`

```
1
2
1 2 1 2
2 2 2
```

## Explanation

All probabilities that influence the mood of a day are independent of each other.

When there is no previous day, the most probable mood is determined only based on the activity performed on that day and the mood distribution $dist$.

Therefore, for the first two tests, only the activity observed on the single day of the respective test and the probability $dist$ to have a certain mood on the first day matter.

For the other two tests, for all days except the first day both the mood of the previous day and the activity performed on the current day matter.

## Clarifications

### Clarification for the first two tests:

First test: 
$0.75 \cdot 0.5$ (for the first mood) $\gt 0.25 \cdot 0.5$ (for the second mood) $\Rightarrow$ the first mood is more probable 

Second test: 
$0.75 \cdot 0.1$ (for the first mood) $\lt 0.25 \cdot 0.9$ (for the second mood) $\Rightarrow$ the second mood is more probable 

Final observation: probabilities are fractional numbers!