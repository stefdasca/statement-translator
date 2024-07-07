The researchers working on the SETI program have received two very strange data transmissions, which could come from extraterrestrial civilizations. The first set of data consists of $10$ distinct characters, given in their lexicographic order, that form the extraterrestrial alphabet. The second transmission contains words of exactly $4$ characters.

# Task

The researchers need to sort the received words in the second transmission lexicographically (according to the extraterrestrial alphabet).

# Input data

The input file `seti.in` contains in the first line the 10 characters of the alphabet, and in each of the following lines one word.

# Output data

The output file `seti.out` will contain the sorted words, one per line.

# Constraints and clarifications

* There are no more than 200\ 000 words in the file, and the characters are lowercase letters of the English alphabet.
* The input data is assumed to be correct.

# Example

`seti.in`
```
abcdefghij
aaaa
fgaa
aabc
iihf
```

`seti.out`
```
aaaa
aabc
fgaa
iihf
