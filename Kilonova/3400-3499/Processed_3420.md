The Imperial system of units, used in the USA, is quite a chaos (see the image below!). Moreover, Americans are stubborn and do not want to use the metric system, so for now, we need to unravel the mystery of converting from one unit to another, given a series of conversion rules.

~[imperial.jpg|align=center|height=25%]

# Task

You are given multiple conversion rules of the type `! 1000 m km`, which means $1000 \text{ m} = 1 \text{ km}$. At the same time, you are given questions of the type `? 54.8 km m`, which means $54.8 \text{ km} = ? \text{ m}$ (convert $54.8 \text{ km}$ into $\text{m}$).

Answer the questions using only the conversion rules provided before them!

# Input data

The first line contains a natural number $t$, the number of tests. For each test, a natural number $n$ is provided. The next $n$ lines for the test will contain quadruples of the form (*character*, *string of characters*, *real number*, *string of characters*). The first element (the character) can only be `!` (which symbolizes a conversion rule) or `?` (which symbolizes a question).

# Output data

The answers to the questions will be printed on separate lines (line $i$ will contain the answer to question $i$). All numbers displayed will be **natural numbers**. The answer to a question will be printed **rounded** to the nearest whole number. If the units cannot be converted using the given rules, `-1` will be printed.

**To display the variable `x` of type `double`/`long double` rounded to the nearest whole number, include the `cmath` library and use the instruction `std::cout << (long long)std::round(x);`.**

# Constraints and clarifications

* It is recommended to use `double` or `long double` data types (instead of `float`) for representing real numbers.
* $1 \leq t \leq 100$
* $2 \leq n \leq 10\ 000$
* At least two units and at least one question are given.
* The strings representing measurement units have a minimum length of $1$ and a maximum of $4$ and consist of lowercase English letters.
* The real numbers in the questions range from $0$ to $1\ 000$ inclusive.
* It is guaranteed that the ratio values between units are between $0$ exclusive and $10^{11}$ inclusive (which do not exceed the `double`/`long double` types).
* There will be no "cycles" in the rules (e.g., if conversion rules are given from $\text{ft}$ to $\text{yd}$, from $\text{ft}$ to $\text{pt}$, and from $\text{mi}$ to $\text{pt}$, then it is guaranteed that a conversion rule from $\text{mi}$ to $\text{yd}$ or from $\text{ft}$ to $\text{mi}$ is not given).
* For conversion between two units at most one rule will be provided.
* **A measurement unit can "transform" into itself even if it has not been defined!**
* For fast reading and displaying, it is recommended to use these lines of code at the beginning of the `main` function:
```cpp
ios::sync_with_stdio(false);  
cin.tie(NULL);  
cout.tie(NULL);  
```

| #   | Score | Constraints                             |
| --- | ------- | -------------------------------------- |
| 1   | 42      | $n \leq 1\ 000$ and all conversion rules are given before the first question|
| 2   | 28      | All conversion rules are given before the first question|
| 3   | 18      | $n \leq 1\ 000$                               |
| 4   | 12      | No additional constraints           |

# Example 1

`input from the keyboard`
```
2
8
! 1000 m km
! 0.001 m mm
? 0.36 km mm
? 79 km cm
! 10 mm cm
? 79 km cm
! 60 min h
? 135 m min
11
! 12 pt pica
! 20 twip pt
! 63 pt fng
! 0.875 in fng
? 250 pt in
! 8 fur mi
! 1760 yd mi
? 0.35 twip fur
! 12 in ft
! 3 ft yd
? 0.5 fur twip
```

`output to screen`
```
360000
-1
7900000
-1
3
-1
5702400
```

## Explanation

We have two tests (one with $\text{m}$, $\text{km}$, $\text{mm}$ etc. and the other with $\text{pt}$, $\text{pica}$, $\text{twip}$ etc.)
$0.36 \text{ km} = 0.36 \cdot 1\ 000 \text{ m} = \frac{0.36 \cdot 1\ 000}{0.001} \text{ mm} = 360\ 000 \text { mm}$.
Using only the rules provided before the second question, $km$ cannot be converted into $cm$. 
For the third question, we also have a conversion rule from $\text{mm}$ to $\text{cm}$. Thus, $79 \text{ km} = 79 \cdot 1\ 000 \text{ m} = \frac{79 \cdot 1\ 000}{0.001} \text{ mm} = \frac{79 \cdot 1\ 000}{0.001 \cdot 10} \text{ cm} = 7\ 900\ 000 \text{ cm}$.
For the last question of the first test, it is not possible to convert from $\text{m}$ to $\text{min}$ using the given rules.