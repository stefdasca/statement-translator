# Task

Andrei became this year an apprentice of Santa Claus. His master entrusted him with the list of well-behaved and naughty children.

The other apprentices, being jealous of how quickly Andrei gained Santa's approval, decided to steal the list. Now Andrei is in trouble because if he can't recreate the list correctly, he might be sent back from Lapland to Romania.

All he remembers is that there were $n$ children and the well-behaved ones had at least as many vowels as consonants in their names (Santa considers w and y as vowels, the rest are considered as in Romanian). Help Andrei to recreate Santa's list.

# Input data

The first line contains $n$, the number of children.

The next $n$ lines contain the name of each child, one per line. Names contain only uppercase and lowercase letters of the English alphabet and have a maximum of $20$ characters.

# Output data

Each line $i$ contains the message `Cuminte` if the i-th child was well-behaved, otherwise the message `Obraznic`.

# Constraints and clarifications

* $1 \ \leq n \ \leq 10^5$

# Example

`stdin`
```
6
Andrei
Yanis
David
Ana
ALICE
Rudolph
```

`stdout`
```
Cuminte
Cuminte
Obraznic
Cuminte
Cuminte
Obraznic
```

## Explanation

Andrei has $3$ vowels and $3$ consonants.

Yanis has $3$ vowels (y is considered a vowel like w) and $2$ consonants.

David has $2$ vowels and $3$ consonants.

Ana has $2$ vowels and $1$ consonant.

ALICE has $3$ vowels and two consonants.

Rudolph has $2$ vowels and $5$ consonants. He probably lazed around all year.

