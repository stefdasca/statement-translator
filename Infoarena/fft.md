# Fast Fourier Transformation

As you well know, polynomials are a crucial part of mathematics without which development, both technological and social (if we didn't talk about polynomials, then what would we talk about?!), would not have been possible. But first, what is a polynomial really? A true mathematician will tell you that a polynomial is an expression that includes a variable, usually denoted with $x$, a set of constants called coefficients, and which only permits the operations of addition, subtraction, multiplication, and raising to a constant natural number power. Furthermore, he might tell you that, in general, a polynomial defined on a set $M$ has the following form: $P(x) = a_0 + a_1 * x + a_2 * x^2 + \dots + a_n * x^n$, where $n$ is a natural number, and $a_0$, $a_1$, $a_2$, $\dots$, $a_n$ are constants and part of $M$. This is completely false! A polynomial is, in fact, a diabolical tool by which the committee can torture competitors without too much effort. If you're wondering how, it's very simple. Take two polynomials (if the coefficients can be taken from $O.E.I.S.$, it's even better) and ask to multiply them with complexity $O(n * log_2 n)$. Do you think this is not possible? You'd be surprised! Fortunately for you, we consider it too old-fashioned to require applying the Fast Fourier Transformation algorithm (see Strada Cramei). So, we thought to delve a little deeper into the usefulness of these revolutionary wonders and found out that you can use them to transform a string of characters into a natural number, called a key. All you have to do is choose a natural number $b$, a non-zero natural number $m$, consider $a_i$ as the ASCII code of the character at position $i$ in the string (indexed from $0$), and calculate $P(b)$ $MOD$ $m$. To save you too much trouble, the committee offers you both the string and the numbers $b$ and $m$, but in return, it asks you to answer $q$ questions of the form: How many palindrome subarrays have lengths between $l_1$ and $l_2$ and keys between $m_1$ and $m_2$?

## Input data

The input file `fft.in` contains on the first line the numbers $b$ and $m$, as described above. The second line contains a string of characters of length $n$. The third line contains the number $q$, representing the number of questions the committee is asking you to answer. Each of the following $q$ lines contains a set of numbers $m_1$ $m_2$ $l_1$ $l_2$, representing a question.

## Output data

The output file `fft.out` will contain the answers for each question, on separate lines, in the order they were read.

## Constraints

$1 \leq n \leq 200\ 000$

$1 \leq q \leq 200\ 000$

$0 \leq b \leq 10^{18}$

$1 \leq m \leq 10^{18}$

$0 \leq m_1 \leq 10^{18}$

$0 \leq m_2 \leq 10^{18}$

$0 \leq l_1 \leq n$

$0 \leq l_2 \leq n$

## Example

`fft.in`

`3 1000000`

`aaba`

`2`

`17 199 1 1`

`99 5000 1 3`

`fft.out`

`4`

`2`

## Explanation

For the first question, the subarrays are: $[0, 0]$, $[1, 1]$, $[2, 2]$, $[3, 3]$. For the second question, the subarrays are: $[0, 1]$, $[1, 3]$.