~[aparat.png|width=40em|align=right]

Mr. R is passionate about specials. To obtain them, he will have to go to Suprabet to invest in some fruit games.

# Task

To help Mr. R, you will need to tell him if the set of symbols ($3$ rows, each containing $5$ symbols) he got from a spin of the machine is a winning set or not.

For a set to be winning, there must be at least $3$ consecutive symbols of the same value starting from the beginning of the row. If there are multiple winning rows, all of them pay.

Also, if there are at least $3$ characters equal to `S`, Mr. R will win the special and will give you a Christmas gift.

In case the special is won, you will display `Speciala!`.

If the special is not won, the corresponding payment for the symbol configuration will be displayed, as follows:

A row of $x$ identical symbols with the value $y$ according to the rules mentioned above will pay $y^x$ money. For example, if the value is $7$ and $x = 4$, it will pay $7^4 = 2401$ money.

The total payment sum will be displayed.

# Input data

The input will contain $3$ rows each with $5$ characters, separated by a space, representing the configuration of the machine.

# Output data

The output will contain either the message `Speciala!` or the payment for that hand.

# Constraints and clarifications

* The matrix is composed of digits from $1$ to $9$ and characters `S`.

# Example 1

`stdin`
```
S 3 8 4 1
9 4 S 3 6
8 7 4 S 5
```

`stdout`
```
Speciala!
```

# Example 2

`stdin`
```
3 3 3 3 3
3 3 5 3 3
3 3 3 5 3
```

`stdout`
```
270
```