# Unique

Two strings of characters $A$ and $B$ are given. Specify how many of the distinct common subsequences of the two strings are palindromes. Two subsequences of letters $P_1 P_2 \dots P_K$ and $Q_1 Q_2 \dots Q_T$ are considered distinct if $K \ne T$ or there is a position $I \leq \min(K,T)$ such that $P_I \ne Q_I$. The strings $P$ and $Q$ refer to the values of the subsequences, not the positions where they appear.

## Input data

The input file `unicat.in` contains two lines. The first line contains the character string $A$ and the second line contains the character string $B$.

## Output data

In the output file `unicat.out` you must print the number of distinct common subsequences that are palindromes.

## Constraints and clarifications

The two strings will each have a maximum of $500\ 000$ characters.

The two strings will contain only lowercase letters of the English alphabet.

## Example

`unicat.in`

```
aaba
abaaa
```

`unicat.out`

```
4
```

## Explanation

The common palindromic subsequences will be "a", "b", "aa" and "aba".