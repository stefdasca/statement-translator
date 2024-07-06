```markdown
# Task

Evil George has kidnapped the princess. Now Drogo the dragon comes to rescue her. George prefers challenging the dragon intellectually rather than fighting him, so he tells Drogo:

*I will free the princess if you can solve the following puzzle. I tell you two positive numbers \( N \) and \( D \), and you have to tell me two different positive \( N \)-digit numbers \( A \) and \( B \) so that their greatest common divisor is \( D \).*

Can you help the dragon to solve this challenge and save the princess? Beware, George might be so evil that there is no possible answer!

Note: the greatest common divisor of two positive integer numbers \( A \) and \( B \) is the greatest integer \( k \) such that both \( A \) and \( B \) are multiples of \( k \).

# Input

The input has two lines, both of them contain a single integer. The first line contains \( N \) (\( 1 \le N \le 18 \)), the second line contains \( D \) (\( 1 \le D \le 10^9 \)).

For test cases worth 8 points, \( 1 \le N \le 3 \).

For test cases worth 16 more points, \( 1 \le N \le 7 \).

For test cases worth 7 more points, \( D = 1 \).

For test cases worth 11 more points, \( D \le 100 \).

# Output

You need to write two different positive integers \( A \) and \( B \) separated by a space. Both \( A \) and \( B \) must have \( N \) digits and their greatest common divisor must be \( D \). If there are no such numbers, you should write `0 0` to the output. If there are multiple possible solutions, you can print any of them.

# Example 1

`stdin`
```
3
9
```

`stdout`
```
180 729
```

## Explanation

Drogo has to tell two different \( 3 \)-digit numbers whose greatest common divisor is \( 9 \). There are many possible solutions, e.g. \( 180 \) and \( 729 \).

# Example 2

`stdin`
```
6
666666
```

`stdout`
```
0 0
```

## Explanation

There is only one \( 6 \)-digit number which is divisible by \( 666666 \), it is \( 666666 \) itself, which means that it is not possible to give two different \( 6 \)-digit numbers whose greatest common divisor is \( 666666 \).
```

Please verify and edit the text as necessary, keeping in mind proper grammar and syntax rules for the English language.