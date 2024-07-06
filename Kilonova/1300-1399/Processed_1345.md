```markdown
Gigel has learned to work with non-repeating decimal fractions, simple repeating decimals, and mixed repeating decimals and to transform a decimal fraction into an ordinary fraction. He knows that there are equivalent decimal fractions and ordinary fractions.
Gigel needs to transform a decimal fraction into an ordinary fraction by writing the denominator of the fraction in one of the following two forms:
1. A digit $1$ which may or may not be followed by $0$s;
2. One or more digits $9$ eventually followed by $0$s.

There may be multiple solutions, from which he will choose the one with the minimum number of digits in the denominator.
\
$6,2500 = \frac{62\ 500}{10\ 000} = 6,25 = \frac{\textcolor{red}{\textbf{625}}}{\textcolor{red}{\textbf{100}}} = 6,250 = \frac{6\ 250}{1\ 000}$
$0,37(547) = \frac{37\ 510}{99\ 900} = 0,3(754) = \frac{\textcolor{red}{\textbf{3\ 751}}}{\textcolor{red}{\textbf{9\ 990}}} = 0,3(754754) = \frac{3\ 754\ 751}{9\ 999\ 990}$

For each of the two examples, whatever the given decimal fraction, diligent student Gigel will choose the equivalent ordinary fraction written in bold.

# Task

Write a program that reads a strictly positive decimal fraction and displays the numerator and the denominator of an equivalent ordinary fraction with the denominator in one of forms 1 or 2 and the minimum number of digits.

# Input data

The file `fractie.in` contains a single line with a string of up to $80$ characters representing the decimal fraction. The characters can be: digits, possibly the decimal comma `,` and the parentheses `(` or `)`.

# Output data

The file `fractie.out` will contain two lines. The first line will contain the numerator of the fraction, the second line will contain the denominator of the fraction.

# Constraints and clarifications

* The whole part of a decimal fraction consists of at least one digit.
* The read string can contain at most $77$ digits and represents a correct decimal fraction.
* For a correct numerator, $40\%$ of the score is awarded, and for a correct denominator $60\%$. To receive partial scores, **the output file must contain 2 numbers!**

# Example 1

`fractie.in`
```
0,3(754754)
```

`fractie.out`
```
3751
9990
```

## Explanation

$0,3(754754) = 0,3(754) = \frac{3751}{9990}$

# Example 2

`fractie.in`
```
6,230000
```

`fractie.out`
```
623
100
```

## Explanation

$6,230000 = 6,23 = \frac{623}{100}$
```

