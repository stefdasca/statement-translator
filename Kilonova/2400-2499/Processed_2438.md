# Task

Gigi's record label wants to earn the copyright royalties from several songs over the $3$ quarters of the year $2024$. Each quarter, his record label has a rating $X$. In order to gain the copyright royalties from a song, it must have a rating of exactly $X$. Gigi's record label has $N$ songs under consideration in each quarter with the ratings: $A_1, A_2, A_3, \dots, A_N$. The song ratings change every week as they enter or exit the trending charts. Gigi can influence the trending charts, and implicitly the ratings of the songs, as follows: he can increase or decrease the rating of any song, but the total sum of all changes must be equal to $0$. The new ratings can be any integer.

For example, if we have $2$ songs with ratings $5$ and $12$, he can change them at the end of the week to $7$ and $10$ ($+2\ –\ 2 = 0$), but he cannot change them to $3$ and $13$ ($-2\ +\ 1 = -1 \neq 0$).

Given the number of songs, the record label's rating, and the rating of those $N$ songs, you are required to find the minimum number of weeks Gigi needs to win the royalties from all the songs, for each quarter.

# Input data

The first line of the input file `casa-de-discuri.in` contains two integers, $N$ (the number of songs for the first quarter) and $X$ (the record label’s rating in the first quarter).

The next line contains $N$ numbers representing the ratings of the $N$ songs in the first quarter.
The third line contains two integers, $N$ (the number of songs for the second quarter) and $X$ (the record label’s rating in the second quarter).
The next line contains $N$ numbers representing the ratings of the $N$ songs in the second quarter.
The fifth line contains two integers, $N$ (the number of songs for the third quarter) and $X$ (the record label’s rating in the third quarter).
The next line contains $N$ numbers representing the ratings of the $N$ songs in the third quarter.

# Output data

On each of the first three lines of the output file `casa-de-discuri.out` there will be a number representing the minimum number of weeks Gigi needs to win the royalties from all songs in the first, second, and third quarter, respectively.

# Constraints and clarifications

* For $20\%$ of the tests $2 \leq N \leq 100$;
* For $100\%$ of the tests $2 \leq N \leq 1\ 000\ 000$;
* $A_i \leq 100\ 000$;
* $X \leq 100\ 000$;
* If Gigi wins the royalties for a song, he does not lose them if the song changes its rating to a number different from $X$ (in practice, the song only needs to have the rating $X$ once).

# Example 1

`casa-de-discuri.in`
```
6 4
4 4 4 4 4 4 
2 10
8 11
2 69
68 70
```

`casa-de-discuri.out`
```
0
2
1
```

## Explanation

For the first quarter, no changes are needed, so in $0$ weeks we can win all the royalties.

For the second quarter, we need $2$ weeks to win all the royalties. In the first week, we increase the rating of the first song by $2$ and are forced to decrease the second song by $2$. We will have songs with ratings $10$ and $9$. We have won the royalties for the first song. In the second week, we decrease the rating of the first song by $1$ and increase the rating of the second song by $1$. We will have $9$ and $10$. Now we have won the royalties for the second song as well.

For the third quarter, we need one week to win all royalties (in one week, we change the first song from $68$ to $69$ and the second from $70$ to $69$; the sum of the changes is $1 + (-1) = 0$).
