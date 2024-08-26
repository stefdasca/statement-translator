Password

Fane Babanu is trying to defend Iasi and the ACM contestants from a new attack. As times have changed, the attack is electronic this time. To defend Iasi, Fane must crack a password. After considerable efforts, he has figured out that the password is a text written with lowercase letters of the Latin alphabet $'a'-'z'$, for which the sum of ASCII codes $\%$ $N$ equals $K$. Fane has also obtained a text and knows that the password is in that text but does not know between which positions. To find the password, he can use as many helpers as needed to try each password at the same time; however, he wants to minimize the number of helpers used. Help Stefan by telling him how many passwords are found in the given text. Fane has at most $T$ passwords to crack.

## Input data

The input file `parola.in` contains on the first line $T$ the number of passwords. There are $T$ tests each on 2 rows. The first row of a test contains $N$ and $K$, on the next row is the text.

## Output data

The output file `parola.out` must contain for each test a row with a number representing the number of possible passwords in each test.

## Constraints
$1 \leq T \leq 15$ 

$1 \leq N \leq 1000000$ 

$0 \leq K < N$ 

$1 \leq L(text) \leq 1000000$ 

Two passwords will be considered distinct if they are between two different indices! An empty password is not considered a valid password.

## Example
`parola.in`
```
2
195 0
abc
196 0
bacbxxbbxxbbb
```

`parola.out`
```
1
5
```

## Explanation

In the first test, the only solution is $ab$

In the second test, the solutions are $bacb$, $ac$, $bb$(6-7), $bb$(10-11), $bb$(11-12)