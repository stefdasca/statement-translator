Gigel found in his grandmother's drawer a note with a decoding formula for a string of characters \( s \) with a length of at most \( 1\ 000\ 000 \) containing numbers \( \leq 20 \) (we will denote them as \( x_k \)), \([ \ ]\), \(\{ \ \}\), \(< >\) and \(,\). This string has the following decoding rules:
1) If \( s = [x_1, x_2, x_3, ..., x_p] \), then \( s \) is transformed into an integer \( t = (\frac{1}{x_1} + \frac{1}{x_2} + ... + \frac{1}{x_p}) \% 773 \) (the sum of the modular inverses of the numbers \( x_1, x_2, x_3, ..., x_p \) with respect to \( 773 \), modulo \( 773 \));
2) If \( s = \{x_1, x_2, x_3, ..., x_p\} \), then \( s \) is transformed into a number \( t = lcm(x_1, x_2, ..., x_p) \% 773 \);
3) If \( s =<x_1, x_2, x_3, ..., x_p> \), then \( s \) is transformed into a number \( t \) which is equal to the number of numbers \( q \) that are strictly less than \( S = (x_1 + x_2 + ... + x_p) \% 773 \) and for which \( gcd(S, q) = 1 \).

In the end, Gigel sums up the remaining numbers.

# Task
Help Gigel decode the found string so he can reward you with a shawarma!

# Input data
The string \( s \) is read.

# Output data
The sum of the numbers remaining after decoding the string \( s \) is printed.

# Constraints and clarifications
* \( 1 \leq \) length of the string \( s \leq 1\ 000\ 000 \);
* The numbers found in the string are natural, \( \geq 1 \) and \( \leq 20 \);
* We denote by \( gcd(a, b) \) the greatest common divisor of the numbers \( a \) and \( b \), and by \( lcm(a, b) \) the least common multiple of the numbers \( a \) and \( b \);
* It is guaranteed that each operation does not exceed the data type `unsigned long long`;
* It is guaranteed that the expression is correct;
* Test 0 is the example below.

# Example
`stdin`
```
1,<2,{12,4},[9,{4,5,9}]>,2
```
`stdout`
```
21
```

# Explanation
`{12,4} = 12`.

`{4,5,9} = 180`.

The string will be transformed into: `1,<2,12,[9,180]>,2`.

`[9,180] = 13`, because the modular inverse of \( 9 \) with respect to \( 773 \) is \( 86 \), and the modular inverse of \( 180 \) with respect to \( 773 \) is \( 700 \), so \( (86 + 700) \% 773 = 13 \).

`<2,12,13> = 18`.

So, the result will be: `1 + 18 + 2 = 21`.