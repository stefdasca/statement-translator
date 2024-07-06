
At the very beginning, on Earth, there existed a single chemical substance `S`, called the `primordial substance`. Later, from it, other chemical substances formed, some `stable` (denoted by lowercase letters of the English alphabet) and others `unstable` (denoted by uppercase letters of the English alphabet). The stable substances had the property that they could not transform into other substances, while an unstable substance could transform either into a stable substance or into two unstable substances. As a result of repeated chemical reactions, `minerals` formed, conglomerates of stable substances. Some of these minerals were formed by chemical reactions starting from the primordial substance `S`, while others were either formed by chemical reactions starting from another existing unstable substance on Earth at that time, but not from the primordial substance `S`, or simply brought from outer space, thus not formed by chemical reactions starting from an unstable substance on Earth.

# Task
The greatest contemporary researchers of the primordial chaos, BitDAC and rOCKTETU’, managed to identify all the chemical reactions that occurred over time on Earth. Write a program for them to establish whether a mineral, with the formula given as a sequence of stable substances, originates from an unstable substance on Earth, including the primordial substance `S`, or has an extraterrestrial origin.

# Input data
The input file `minerale.in` contains:

* The first line contains two non-null natural numbers `r` and `m`, representing, in this order, the number of chemical reactions and the number of minerals whose origins will be analyzed (stable substances are denoted by lowercase letters of the English alphabet, and unstable substances by uppercase letters of the English alphabet);
* Each of the next `r` lines contains a chemical reaction, respectively either a string of characters of the form `A b`, where `A` is an unstable substance and `b` a stable substance, or a string of characters of the form `A BC`, where `A, B` and `C` are 3 unstable substances.
* Each of the next `m` lines will contain the formula of a mineral, respectively a string of characters made up of at most `100` lowercase letters of the English alphabet.

# Output data
The output file `minerale.out` will contain `m` lines, and on each line, one of the numbers `0, 1` or `2` will be written, depending on whether the mineral with the ordinal number equal to the ordinal number of the line is of extraterrestrial origin, originates from the primordial substance `S`, or originates from another unstable substance other than the primordial substance `S`.

# Constraints and clarifications
* The primordial substance `S` is always an unstable substance.
* Any mineral can contain at most `100` stable substances in its composition.
* If a mineral originates both from the primordial substance `S` and other unstable substances, it will be considered to originate from the primordial substance `S`.
* `1 \ \leq r \ \leq 400`
* `1 \ \leq m \ \leq 100`

# Example

`minerale.in`

```
8 3
S AB
S CA
A a
B BC
B BC
B AC
C AB
C b
aaaab
aaabb
abab
```

`minerale.out`

```
1
2
0
```

**Explanations**

Mineral `aaaab` can be obtained from the primordial substance `S` through the following chemical reactions: `S→AB→aB→aAC→aaC→aaAB→aaaB→aaaAC→→aaaaC→aaaab`.

Mineral `aaabb` cannot be obtained from the primordial substance `S`, but can be obtained from the unstable substance `B` through the following chemical reactions: `B→BC→ACC→aABC→aaBC→aaACC→aaaCC→aaabC→aaabb`.

Mineral `abab` cannot be obtained from any unstable substance.