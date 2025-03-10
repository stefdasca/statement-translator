Nicoleta, a curious girl, wants to find out which of her classmates has the Christmas tree with the most lights, as well as the number of lights on that tree. Being an informatics olympian and loving challenges, her classmates communicated by SMS only the number of divisors corresponding to the number of lights on the tree, which is also the smallest number with this property. For example, George, her deskmate, sent her the number $5$, corresponding to a number of $16$ lights, more exactly $D_{16} = \{1, 2, 4, 8, 16 \}$, and $16$ is the smallest number with exactly $5$ divisors. The messages from her classmates will be in the form:

$Nr_{Div} \ Name$, where $Nr_{Div}$ represents the number of divisors, and $Name$ represents the name of the classmate who sent the message.

# Task

Write a program that determines:
1) The number of lights on the tree with the most lights.
2) The name of the classmate who has the tree with the most lights.

# Input data

The input file `lumini.in` contains on the first line the task $1$ or $2$. The second line contains the number $n$, representing the number of Nicoleta's classmates, and the following $n$ lines will contain the messages from her classmates, in the form described in the problem statement, one message per line.

# Output data

The output file `lumini.out` will contain a single line which will have the number of lights of the tree with the most lights (task $1$) or the name of the first classmate from the received list who has the tree with the most lights (task $2$).

# Constraints and clarifications

* $1 \leq n \leq 5 \ 000$, $n$ natural number;
* $1 < Nr_{Div} \leq 120$, $Nr_{Div}$ natural number;  
* the name of any classmate has a maximum of $23$ alphabetic characters;
* the maximum number of lights in the tree installation will be $65 \ 536$ ($2^{16}$).

# Example 1

`lumini.in`
```
1
3
12 Tryp
13 Mike
14 Gymi
```

`lumini.out`
```
4096
```

## Explanation

Tryp has an installation with $60$ lights.  
Mike has an installation with $4096$ lights.  
Gymi has an installation with $192$ lights.

# Example 2

`lumini.in`
```
2
6
22 Andreea
26 Iustina
40 Iuliana
26 Andreia
27 Corina
30 Raluca
```

`lumini.out`
```
Iustina
```

## Explanation

Iustina and Andreia each have an installation with $12 \ 288$ lights. Iustina appears first in the list.

Andreea has an installation with $3 \ 072$ lights.  
Iuliana has an installation with $1 \ 680$ lights.  
Corina has an installation with $900$ lights.  
Raluca has an installation with $720$ lights.