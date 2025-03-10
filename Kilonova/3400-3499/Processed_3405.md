
# Task

Lana is playing Dress to Impress with her friends and wants to quickly obtain the rank of Runway Queen. An outfit is composed of $k$ garments, each assigned a number $S$ of stars. The total score of an outfit is the sum of all $S$ values associated with the $k$ pieces of clothing.

Additionally, each round presents a theme identified by a natural number $t$. A player respects the theme if their outfit's total score is less than or equal to $t$. Thus, if the player respects the theme, they receive a bonus of $b$ points, and this also applies to Lana. The player with the highest final score is the winner.

Find out if Lana has won the round and is one step closer to becoming the Runway Queen.

# Input Data

The input file `dti.in` contains, on separate lines, the following natural values:
- $nr$, the number of garments in Lana's outfit
- $nr$ values representing the stars received for each piece in Lana's outfit
- $t$, the theme value that must be respected
- $b$, the bonus value
- $n$, representing the number of players competing with Lana
- the following $2 \cdot n$ lines contain, on separate lines, information about Lana's $n$ competitors:
  * the natural number $k$, the number of garments
  * $k$ natural values, representing the stars for each piece of clothing

# Output Data

The output file `dti.out` will contain the text "Da" and Lana's score separated by a space if she has won; otherwise, it will display "Nu" and the winning score. If Lana ties with another player for the highest score, Lana is considered the winner.

# Constraints and Clarifications

* $1 \le L \le 5 \ 000$;
* $1 \le k \le 5 \ 000$;
* $1 \le n \le 5 \ 000$;
* $1 \le t \le 5 \cdot 10^8$;
* $1 \le s \le 10^5$;
* $1 \le b \le 10^6$.

| # | Score | Constraints |
|:-:|:--------:|:----------:|
| 1 |   20   |   $n = 1$   |
| 2 |   30   |   $n = 3$   |
| 3 | 40     | $1 \le n \le 5 \ 000$ |

# Example

`dti.in`
```
5 
13 7 10 4 5 
30 11 
3 
4 
8 17 5 3 
6  
2 11 4 5 3 1 
3 
10 14 4 
```

`dti.out`
```
Da 39
```

## Explanation

Lana's score is $39=13+7+10+4+5$.  

The score of the first player is $33=8+17+5+3$. 

The score of the second player is $26=2+11+4+5+3+1$. This player respects the theme because $26 \le 30$, so they receive a bonus of $11$ points, making their final score $37=26+11$. 

The score of the third player is $28=10+14+4$. This player respects the theme and will receive the bonus, so their final score is $39=28+11$. 

Lana and the third player both have the highest score, but Lana is considered the winner.
```
