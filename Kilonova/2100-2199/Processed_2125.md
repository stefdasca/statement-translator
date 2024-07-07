
# Task

Until recently, long-distance communication was done with the help of the telegraph. Using the telegraph, two types of signals can be transmitted: dot and dash. In general, we want to transmit texts made up of letters of the Latin alphabet and numbers (a total of $36$ symbols). Therefore, we need to use encoding, i.e., to associate a distinct sequence of dashes and dots to each of the $36$ symbols. In order to decode a received sequence of dashes and dots, it is necessary that no symbol has an encoding identical to the beginning of the encoding for another symbol. Let's consider some examples (assuming we only want to transmit the letters $A, B, C$):

|Example 1|Example 2|Example 3|
|-|-|-|
|A = ..|A = .--|A = .-..|
|B = .-|B = .-|B = -.|
|C = -|C = -|C = .-.|

Example $1$ represents a correct encoding. Example $2$ represents an incorrect encoding because the beginning of the encoding for $A$ is identical to the encoding for $B$ (thus, a sequence like `.--` is ambiguous and could mean either $A$ or $BC$). Example $3$ is also an incorrect encoding because the beginning of the encoding for $A$ is identical to the encoding for $C$ (a sequence like `.-..-.` is ambiguous and could mean either $AB$ or $CC$).

It is known that in a telegraphic transmission, the dot lasts one second and the dash $2$ seconds. Thus, we can calculate the time required to transmit a text.
Using the encoding from Example $1$, transmitting the text `CABCA` = `- .. .- - ..` takes $11$ seconds. Notice that the length of the transmission can also be calculated as: $2(A) + 1(B) + 2(C) = 2(..) + 1(.-) + 2(-) = 2 \cdot 2 + 1 \cdot 3 + 2 \cdot 2 = 11$.

A text is given by the frequency of occurrence of each symbol (among the 36 considered). Find the minimum duration required to transmit that text using an appropriately chosen encoding.

# Input data

The file `telegraf.in` contains a single line with $36$ non-negative integers, separated by spaces, representing the number of occurrences of each symbol in the text to be transmitted.

# Output data

The file `telegraf.out` will contain a single number, namely the minimum length (in seconds) necessary to transmit the text.

# Constraints and clarifications

* None of the $36$ symbols appear more than $10^6$ times in the given text.
* There are at least two symbols with non-zero occurrences.
* $40\%$ of the tests will contain at most $16$ symbols with non-zero frequency.

# Example

`telegraf.in`
```
2 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

`telegraf.out`
```
11
```

## Explanation

It is found that it is optimal to transmit this text using the encoding from Example $1$, obtaining a minimum transmission length of $11$ seconds.
