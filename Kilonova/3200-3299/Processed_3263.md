
# Task

Ana and Maria each received a string consisting only of lowercase letters. We denote Ana's string by $S_1$ and Maria's string by $S_2$. Now, they plan to delete certain letters from $S_1$ and $S_2$ until they obtain two identical strings. For this, Ana can delete characters only from the beginning and end of her string, resulting in a continuous subarray of $S_1$. Maria can delete any characters from $S_2$, potentially obtaining a subsequence of her initial string.

Calculate the maximum length of the string that the two girls could obtain.

# Input data

The first line of the file `diff.in` contains the string $S_1$ and the second line contains the string $S_2$.

# Output data

The first line of the file `diff.out` contains the maximum length of the final string obtained by the two girls.

# Constraints and clarifications

* $S_1$ and $S_2$ contain only lowercase alphabet letters.
* The lengths of the given strings are between $1$ and $2\ 000$ inclusive.
* For $37$ points, the lengths of the strings will be between $1$ and $200$ inclusive.

# Example

`diff.in`
```
fabcmxyztt
yabcnmnxyz
```

`diff.out`
```
7
```

## Explanation

* f**abcmxyz**tt
* y**abc**n**m**n**xyz**

The largest string the two girls can obtain is `abcmxyz`.
