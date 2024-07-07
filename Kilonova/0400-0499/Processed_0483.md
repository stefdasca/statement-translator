
# Task<br><br>

Given $3$ numbers $a$, $b$, and $c$.  <br><br>

How many strings containing $a$ characters `'a'`, $b$ characters `'b'`, and $c$ characters `'c'` have no substring equal to `"abc"`?<br><br><br>

Since the answer can be very large, display it modulo $100\,000\,007$.<br><br>

# Input data<br><br>

The input file **adece.in** contains $3$ numbers $a$, $b$, and $c$ ($1 \le a,b,c \le 3000$) &mdash; with the meanings given in the statement.<br><br><br>

# Output data<br><br>

The output file **adece.out** will contain the result of the problem, modulo $100\,000\,007$.<br><br>

# Constraints and clarifications

- For 20 points, $a,b,c \le 5$;
- For 20 points, $c=1$;
- For 25 points, $a,b,c \le 100$;
- For 35 points, no additional constraints.
- It is guaranteed that the modulus is prime.

# Examples

## Example 1:

**adece.in**
```
1 1 1
```
**adece.out**
```
5
```

## Example 2:

**adece.in**
```
1 1 2
```
**adece.out**
```
10
```

## Example 3:

**adece.in**
```
2 2 2
```
**adece.out**
```
67
```

## Example 4:

**adece.in**
```
69 69 69
```
**adece.out**
```
5545765
```

# Explanations

- In the first example, the $5$ strings that meet the conditions in the statement are: `"acb"`, `"bac"`, `"bca"`, `"cab"`, and `"cba"`.
- In the second example, the $10$ strings that meet the conditions in the statement are: `"acbc"`, `"accb"`, `"bacc"`, `"bcac"`, `"bcca"`, `"cacb"`, `"cbac"`, `"cbca"` , `"ccab"`, and `"ccba"`.
