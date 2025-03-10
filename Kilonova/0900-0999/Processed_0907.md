In a school, there is an access system using cards, connected to a computer and a printer. Each student in the school has a card. On a given day, whenever a card is used, the system prints the following information on paper, on a single line, according to the following rules:

- The character `b` if the student is a boy or the character `f` if the student is a girl. This character is followed by a space;
- The character `i` if the student entered the school or the character `e` if the student exited the school. This character is also followed by a space;
- The moment the card was used, expressed in hours, minutes, and seconds. These are represented on the line, in this exact order, as three natural numbers, separated by spaces.

# Task

Knowing all the $N$ lines printed in a day, determine:

1. How many boys and how many girls are at school after the $N$ actions printed by the system.
2. The total number of seconds in which an equal, non-zero, number of girls and boys were at school until the moment of the last card use. If this situation does not exist, print $0$.
3. The maximum number of seconds in which an odd number of boys were uninterruptedly at school until the moment of the last card use. If this situation does not exist, print $0$.

# Input data

The input file `cartele.in` contains on the first line a natural number $C$ representing the task number which can have the values $1$, $2$, or $3$, on the second line the natural number $N$, and on the next $N$ lines the information printed by the system in the form described in the statement, in strictly increasing order of the moment of card use.

# Output data

If $C = 1$, then the output file `cartele.out` will contain, in this order, separated by a space, the number of boys and the number of girls determined according to task $1$.
If $C = 2$ or $C = 3$, then the output file `cartele.out` will contain on the first line a single natural number representing the result determined according to the task.

# Constraints and clarifications

* $1 \leq N \leq 10\ 000$;
* At the moment of using the first card, there is no student in the school;
* The access system does not allow simultaneous use of two cards;
* For any line printed by the system $0 \leq hour \leq 23$, $0 \leq minutes \leq 59$; and $0 \leq seconds \leq 59$;
* On each line of the input file, after the last number representing the seconds, there is no space.
* For correct resolution of the first task $20$ points are awarded, for correct resolution of the second task $30$ points are awarded, and for correct resolution of the third task $40$ points are awarded. $10$ points are from the start.

# Example 1

`cartele.in`
```
1
3
b i 0 0 24
f i 0 0 26
b e 0 0 29
```

`cartele.out`
```
0 1
```

## Explanation

A boy entered at the moment $0 \ 0 \ 24$ (i.e., hour $0$, minute $0$ and second $24$) and exited at the moment $0 \ 0 \ 29$. A girl entered at the moment $0 \ 0 \ 26$.
After the $3$ actions, a girl remained in the school.

# Example 2

`cartele.in`
```
2
3
b i 0 0 24
f i 0 0 26
b e 0 0 29
```

`cartele.out`
```
3
```

## Explanation

Between the moment $0 \ 0 \ 24$ and $0 \ 0 \ 26$ there is only a boy in the school. Between the moment $0 \ 0 \ 26$ and $0 \ 0 \ 29$ there is a boy and a girl in the school, meaning an equal non-zero number of boys and girls.
Thus, the determined number of seconds is $3$.

# Example 3

`cartele.in`
```
2
8
f i 8 19 10
b i 8 19 12
b e 8 19 15
b i 8 20 0
b e 8 20 4
b i 8 20 10
b i 8 20 50
b i 8 20 51
```

`cartele.out`
```
47
```

## Explanation

Between the moments $8 \ 19 \ 12$ and $8 \ 19 \ 15$ there is $1$ boy and $1$ girl in the school, so the duration is $3$ seconds.
Between the moments $8 \ 20 \ 0$ and $8 \ 20 \ 4$ there is $1$ boy and $1$ girl in the school, so the duration is $4$ seconds.
Between the moments $8 \ 20 \ 10$ and $8 \ 20 \ 50$ there is $1$ boy and $1$ girl in the school, so the duration is $40$ seconds.
The total duration is $3$ + $4$ + $40$ = $47$ seconds.

# Example 4

`cartele.in`
```
3
9
f i 8 19 10
b i 8 19 12
f e 8 19 13
b e 8 19 15
b i 8 20 0
b i 8 20 1
b i 8 20 10
b i 8 20 12
b i 8 20 13
```

`cartele.out`
```
3
```

## Explanation

Between the moments $8 \ 19 \ 12$ and $8 \ 19 \ 15$ there is $1$ boy in the school, so the duration is $3$ seconds.
Between the moments $8 \ 20 \ 0$ and $8 \ 20 \ 1$ there is $1$ boy in the school, so the duration is $1$ second.
Between the moments $8 \ 20 \ 10$ and $8 \ 20 \ 12$ there are $3$ boys in the school, so the duration is $2$ seconds.