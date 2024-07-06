Alina is a big theater enthusiast. The theater director offered her a chance to act in multiple plays as an extra, for now. The costume designer decided to give her $C$ different costumes from those assigned for this season.

Alina will take the costumes home and adjust them to fit well. The season lasts for $N$ consecutive days and each day a play is performed. The same play will be performed, of course, on one or more days of the season.

Each play is associated with a unique extra costume, so for each play she acts in, Alina has to wear only one costume, the one associated with that play. The extra costumes are identified by uppercase letters of the English alphabet: $A, B, C, \ldots, X, Y, Z$. Alina is allowed to choose the $C$ different costumes.

# Task

Knowing the costume associated with each day of the season, help Alina choose the $C$ different costumes in such a way that she can participate in the maximum number of consecutive plays.

# Input data

The input file `teatru.in` contains the first line of two natural numbers $Z$ and $C$ separated by a space. $Z$ is the number of days in the season and $C$ is the number of different costumes that Alina can receive.

The second line contains $Z$ characters, uppercase letters of the English alphabet. The $i$-th character identifies the extra costume that must be worn in the play on day $i$.

# Output data

In the output file `teatru.out` contains the first line a natural number $N$, representing the maximum number of consecutive plays in which Alina can participate. 

On the second line, $N$ characters are written, without spaces between them, corresponding to the costumes that will be worn in the chosen $N$ plays, in the order of the plays in which she will act.

If there are multiple solutions of length $N$, then the one corresponding to a start day closer to the beginning of the season is displayed.

# Constraints and clarifications

* $1 \leq Z \leq 55\ 000$
* $1 \leq C \leq 26$
* $C \leq Z$
* For $20$\% of the tests $Z \leq 350$

# Example 1

`teatru.in`
```
10 3
XKUFKFEGXG
```

`teatru.out`
```
5
KUFKF
```

# Example 2

`teatru.in`
```
15 4
IAJRAMRCZJJCDNS
```

`teatru.out`
```
6
AJRAMR
```

# Example 3

`teatru.in`
```
25 5
LDSDGIFAURLPTZLDLPNLEGFRN
```

`teatru.out`
```
8
LPTZLDLP
```

