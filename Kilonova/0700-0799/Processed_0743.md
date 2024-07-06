```markdown
Being a student at an art high school, music section, Andrei proposes to study a new scale made up of $10$ musical notes. Passionate about mathematics as well, he proposes that starting from two natural numbers $a$ and $b$ ($a < b$) to compose an "Endless Symphony", generating a sequence of notes in the new scale. Thus, he generates each note of the symphony by multiplying $a$ by $10$ and dividing the result by $b$ (integer division). To avoid generating the same note, he modifies $a$ each time, replacing it with the remainder of the division of $a \cdot 10$ by $b$. Thus, the notes are generated according to the rule $a \cdot 10$ div $b$, where after each step a changes as follows: $a = a \cdot 10$ mod $b$ (the div operation represents the integer quotient of the division, and mod is the integer representing the remainder of the integer division of two numbers).
Thus, starting from $a = 42$ and $b = 130$, he will generate the notes: $3 \\ 2 \\ 3 \\ 0 \\ 7 \\ 6 \\ 9 \\ 2 \\ 3 \\ 0 \\ 7 \\ 6 \\ 9 \\ 2$ etc.

* $3 = 42 \cdot 10$ div $130$, and $a$ becomes $a = 42 * 10$ mod $130$, so $a = 30$;
* $2 = 30 \cdot 10$ div $130$, $a = 300$ mod $130$, $a = 40$;
* $3 = 40 \cdot 10$ div $130$, $a = 400$ mod $130$, $a = 10$;
* $0 = 10 \cdot 10$ div $130$, $a = 100$ mod $130$, $a = 100$;
* $7 = 100 \cdot 10$ div $130$, $a = 1000$ mod $130$, $a = 90$;
* $6 = 90 \cdot 10$ div $130$, $a = 900$ mod $130$, $a = 120$;
* $9 = 120 \cdot 10$ div $130$, $a = 1200$ mod $130$, $a = 30$;
* $2 = 30 \cdot 10$ div $130$, $a = 300$ mod $130$, $a = 40$;
etc.

Listening to the symphony, Andrei notices that, at some point, a sequence starts to repeat identically an infinite number of times. Andrei names the sequence made up of the first notes, those before the repeating sequence, the "theme", and the sequence that repeats, the "refrain" of the symphony. For example, in the previous sequence, $3$ is the theme, and $230769$ is the refrain. He considers the theme and the refrain with the smallest possible lengths. Thus, in the previous example, neither $32$ and $307692$, nor $3$ and $230769230769$ can be considered as theme and refrain. There are also cases where there is no theme, which means the symphony starts directly with the refrain.

# Task

Write a program that, reading two natural numbers $a$ and $b$ ($a < b$), will determine the digits of the theme and the digits of the refrain. The digits of the theme will be printed, followed by the digits of the refrain, then a space followed by a number representing how many digits the refrain has.

# Input data

The input file `muzica.in` contains on the first line two values: $a$ and $b$ natural numbers, separated by a space.

# Output data

The output file `muzica.out` will contain a single line with the digits of the theme followed by the digits of the refrain and, after a space, the number of digits of the refrain.

# Constraints and clarifications

* $1 < a, b < 1 \ 000$;
* $a \neq b$;

# Example 1

`muzica.in`
```
164 824
```

`muzica.out`
```
19902912621359223300970873786407766 34
```

## Explanation

$1$ is the theme, $99029126213 \dots$ is the refrain

# Example 2

`muzica.in`
```
13 32
```

`muzica.out`
```
406250 1
```

## Explanation

$40625$ is the theme, $0$ is the refrain

# Example 3

`muzica.in`
```
6 11
```

`muzica.out`
```
54 2
```

## Explanation

There is no theme, $54$
```