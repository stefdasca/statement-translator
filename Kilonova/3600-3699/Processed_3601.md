A common occurrence in any competition is having a number of sponsors. For example, JBOI 2022, the Junior Balkan Olympiad in Informatics, held in Romania, in Botoșani, benefited from the support of seven major sponsors. The list of these sponsors is published in any promotional material referring to the respective competition. Our competition, OMI 2025, also benefits from the support of $N$ sponsors. Going through the list of sponsors, we found that by selecting certain sponsors from the list and arranging them in a specific order, the first letters of the selected sponsors' names form the word `OLIMPIADADE`, and the last letters form the word `INFORMATICA`.

# Task

Write a program that determines the number of ways to select from the list of sponsors those that meet this property, as well as the lexicographically minimal solution.

# Input data

The input file `sponsor.in` contains on the first line two natural values $C$ and $N$ separated by a space, representing the task ($1$ or $2$) respectively the number of sponsors. The following $N$ lines contain the names of the $N$ sponsors, one sponsor per line.

# Output data

The output file `sponsor.out` contains on the first line, if the task is $1$, the number $M$ of ways to select from the $N$ sponsors a list that respects the described property. If the task is $2$, the output file will contain a list of $11$ sponsors that respect the described property, written correctly, one sponsor per line.

# Constraints and clarifications

* $11 \leq N \leq 50$;
* Any sponsor name has a maximum of $30$ characters and appears only once in the list;
* Sponsor names contain only uppercase letters and other printable characters (ASCII codes in the set $[32, 127]$); the first and last characters of the name are letters;
* For all tests, there is at least one solution;
* For task $1$, $49$ points are awarded, and for task $2$, $41$ points are awarded; $10$ points are awarded by default. 

# Example 1

`sponsor.in`
```
1 12 
ICONOGRAF 
OCHELARI PENTRU OCHI 
LAN 
ASTAZI 
MANGO 
PAR 
IMPRESIONISM 
ABBA 
DECAPOTAT 
DEMISEC 
ELBA 
IF
```

`sponsor.out`
```
2
```

## Explanation

Task $1$, there are $12$ sponsors, there are $2$ ways to select the list. The 2 possibilities are:
```
OCHELARI PENTRU OCHI
LAN
ICONOGRAF
MANGO
PAR
IMPRESIONISM
ABBA
DECAPOTAT
AMANDOI
DEMI_SEC
ELBA
```

and

```
OCHELARI PENTRU OCHI
LAN
IF
MANGO
PAR
IMPRESIONISM
ABBA
DECAPOTAT
AMANDOI
DEMI_SEC
ELBA
```

# Example 2

`sponsor.in`
```
2 12 
ICONOGRAF 
OCHELARI PENTRU OCHI 
LAN 
AMANDOI 
MANGO 
PAR 
IMPRESIONISM 
ABBA 
DECAPOTAT 
DEMI_SEC 
ELBA 
IF
```

`sponsor.out`
```
OCHELARI PENTRU OCHI 
LAN 
ICONOGRAF 
MANGO 
PAR 
IMPRESIONISM 
ABBA 
DECAPOTAT 
AMANDOI 
DEMI_SEC 
ELBA
```

## Explanation

Task $2$, the lexicographically minimal solution among the $2$ possibilities of selecting the sponsors was displayed: `ICONOGRAF` $<$ `IF`, because the letter `C` $<$ the letter `F`.