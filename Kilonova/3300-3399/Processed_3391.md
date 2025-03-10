**Bahoi** started playing the online rhythm game osu! and wants to farm as much **PP (performance points)** as he can. Since the scoring system in osu! is not perfect, **Bahoi** beat his score on a map with a worse score, and as a result, he lost **PP**. Outraged by this atrocity, **Bahoi** quit osu! and is trying to create a clone to his liking.

For simplicity, he has currently implemented only one object: the **hit circle**. It is characterized by the **time** it appears in milliseconds (the natural number $t_i$) and its position in the 2D plane (the natural numbers $x_i$, $y_i$). In **Bahosu!** (a very original name), the scoring system used is the **PP** system. He has the following idea for implementing the **BPP (Bahoi PP)** system: **PP** is divided into **3** categories, namely **Aim PP**, **Speed PP**, and **Accuracy PP**. **Aim PP** is calculated as the sum of the Euclidean distances divided by the time difference, multiplied by $10$, between all consecutive pairs of **hit circles**. **Speed PP** is calculated as the sum of the inverses of the time differences, multiplied by $100$, between all consecutive pairs of **hit circles**. **Accuracy PP** for an accuracy measured in percentage $A$ is calculated as $\\frac{({(A/40)}^{2.51})}{10}$. **Total PP** is calculated as $(AimPP+SpeedPP)*AccuracyPP$.

# Task

Given a map (a sequence of hit circles) and **Bahoi**'s accuracy (a real number, from $0$ to $100$, in percentages), calculate the **PP** he obtained.

# Input data

The first line contains the natural number $N$, representing the number of hit circles, and the real number $A$, representing Bahoi's accuracy.  
The next $N$ lines describe the $i$-th circle, by the triplet of natural numbers $x_i \\ y_i \\ t_i$, with the significance from the statement.

# Output data

Print a single real number, representing the **PP** obtained by **Bahoi**.

# Constraints and clarifications

* $1 \\leq N \\leq 100 \\ 000$
* $0 \\leq A \\leq 100$
* $0 \\leq x[i], y[i] \\leq 480$
* $0 \\leq t[i] \\leq 1 \\ 000 \\ 000$
* $t_i < t_{i+1}$
* It is guaranteed that the result can be calculated using `long double` variables in **C++**.
* It is recommended to use the `long double` data type for operations with real numbers in **C++**.
* It is recommended to display the result with $18$ decimals using `std::setprecision(18)` in **C++**.
* Bahoi hasn't heard of **osu!lazer**, where you cannot lose **PP**.

# Scoring

Let $A = \text{result obtained by the committee}$ and $B = \text{result obtained by the competitor}$.  
If $0.8 < \\frac{A}{B} < 1.2$, the result $B$ is considered correct ($100 \\%$ of the test).  
If $0.4 < \\frac{A}{B} < 1.6$, the result $B$ is considered partially correct ($40 \\%$ of the test).

# Example 1

`stdin`
```
10 100
0 0 0
60 0 101
30 70 202
100 0 404
140 0 505
100 70 606
140 70 707
180 0 909
240 0 1010
210 70 1111
```

`stdout`
```
52.4077
```

## Explanation

Below is a graphical representation of the map Bahoi played:  
~[727.png]

Bahoi played it perfectly, achieving $100 \\%$ accuracy.

**Aim PP** of Bahoi is: $51.7571$  
**Speed PP** of Bahoi is: $0.792079$  
**Accuracy PP** of Bahoi is: $0.997308$  
Therefore, **Total PP** of Bahoi is: $(51.7571+0.792079)*0.997308 = 52.4077$.

# Example 2

`stdin`
```
10 95.6
0 0 0
60 0 101
30 70 202
100 0 404
140 0 505
100 70 606
140 70 707
180 0 909
240 0 1010
210 70 1111
```

`stdout`
```
46.8107
```

## Explanation

In example 2, Bahoi played exactly the same map, only achieving poorer accuracy ($95.6 \\%$).

**Aim PP** of Bahoi is: $51.7571$  
**Speed PP** of Bahoi is: $0.792079$  
**Accuracy PP** of Bahoi is: $0.890797$  
Therefore, **Total PP** of Bahoi is: $(51.7571+0.792079)*0.890797 = 46.8107$.