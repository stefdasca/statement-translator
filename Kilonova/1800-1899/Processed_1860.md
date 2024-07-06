It's well known that the genetic information of an organism can be encoded as a string composed of symbols from the set $\{g, a, t, c\}$. Based on this encoding, biologists have identified 3 operations on the strings of symbols, operations that can model the evolution of certain organisms.

1. **Complementarity**. The symbol $a$ is the complement of $t$ (and vice versa), and the symbol $c$ is the complement of $g$ (and vice versa). For a symbol $x$, we will denote its complement by $c(x)$. By extension, if $w$ is a string of symbols from the set $\{a, c, g, t\}$, we denote by $c(w)$ the string obtained by complementing the symbols of $w$. For example, for $w = aaactg$, we have $c(w) = tttgac$.
2. **Mirroring**. We will denote by $w_R$ the string obtained by mirroring $w$. For example, for $w = aaagatat$, $w_R = tatagaaa$.
3. **Hairpin**. For a string of symbols $w$, which can be decomposed into four subsequences $w_1 w_2 w_3 w_4$ (some of the four strings can be empty), the hairpin operation results in: $w_1 w_2 w_3 w_4 c(w_1)R$, if $w_2 = c(w_4)R$ and the length of $w_2$ is greater than or equal to $1$, or $c(w_4) R w_1 w_2 w_3 w_4$, if $w_1 = c(w_3)R$ and the length of $w_1$ is greater than or equal to $1$. If both conditions are met, either of the two strings can be obtained.

In the Acolor garden, a species of caterpillars with an artistic touch has been discovered. The genetic information of the caterpillars is encoded by a set $S$ composed of $n$ strings of symbols from the set $\{a, c, g, t\}$. The set $S$ is referred to as the initial set. In the evolution of the caterpillars, the initial genetic information has undergone a series of modifications. For caterpillars, all these modifications can be described by repeatedly applying the **hairpin** operation an arbitrary number of times on the strings in the initial set $S$.

# Task

Given the $n$ strings from the initial set $S$ and a sequence of $m$ strings of symbols, determine which of the $m$ strings can represent the genetic code of a caterpillar, obtained by applying some hairpin operations.

# Input data

The input file `evo.in` contains $n+m+2$ lines. The first line contains the natural number $n$ representing the number of strings in the initial set $S$. The next $n$ lines each contain a string from the set $S$. The $(n+2)$th line contains the natural number $m$, representing the number of strings that need to be analyzed. The next $m$ lines each contain one of the strings that need to be analyzed, one string per line.

# Output data

The output file `evo.out` will contain $m$ lines, one for each string to be analyzed. On the $i$th line, the word `yes` will be printed if the $i$-th string among the $m$ strings to be analyzed can be the genetic code of a caterpillar, otherwise the word `no` will be printed.

# Constraints and clarifications

* $0 < n < 5$, $0 < m < 1001$
* The length of a string in the initial set $S$ is less than $101$.
* The total length of the strings to be analyzed is less than $16001$. The length of each string to be analyzed is less than $4001$.
* In $55\%$ of the tests the maximum length of a string to be analyzed is $700$.

# Example

`evo.in`
```
2
acgtcg
gaaaat
4
gaaaat
gaaaatcc
gaaaattc
cgacgtcgtcg
```

`evo.out`
```
yes
no
yes
yes
```

## Explanation

The first string to be analyzed is `gaaaat`. This can be obtained from `gaaaat` without applying any **hairpin** operation.
The second string to be analyzed is `gaaaatcc`. This cannot be obtained by applying the **hairpin** operation on the strings `acgtcg` or `gaaaat`.
The third string to be analyzed is `gaaaattc`. This is obtained by applying the **hairpin** operation once on the string `gaaaat` (considering $w_1 = ga$, $w_2 = a$, $w_3 = aa$, $w_4 = t$).
The fourth string to be analyzed is `cgacgtcgtcg`. This can be obtained from `acgtcg` by applying the **hairpin** operation twice (from `acgtcg` we get `cgacgtcg` for $w_1 = ac$, $w_2$ = empty string, $w_3 = gt$, $w_4 = cg$, the **hairpin** operation adding $c(w_4)R$ at the beginning of the string, and then from `cgacgtcg` we get `cgacgtcgtcg` for $w_1 = cga$, $w_2 = c$, $w_3 = gtc$ and $w_4 = g$, the **hairpin** operation adding $c(w_1)R$ at the end of the string).
