The following archive-unarchive scheme is proposed for text that does not contain numeric characters. When archiving, any non-alphabetic character of the text is copied directly into the archived text. A word is copied into the archived text only if it is its first appearance, and it is also added to the end of a word list. In subsequent appearances, the word will be replaced with its ordinal number in the respective list (the numbering of the positions in the list starts from $1$).

# Task

Write a program that:

* Reads a text from the file `arhivare.in`;
* Determines the type of operation (archive/unarchive);
* Writes the archived/unarchived text to the file `arhivare.out`.

# Input data

The input file `arhivare.in` will contain a string of characters $s$, representing a text.

# Output data

The output file `arhivare.out` will contain the archived/unarchived text.

# Constraints and clarifications

* The string of characters contains at most $100\ 000$ characters, and the words have at most $20$ characters, containing lowercase letters of the alphabet.
* There are at most $2\ 000$ words in the text.
* A text is considered to need unarchiving if it contains at least one digit. The alphabetic characters are $a \dots z$.

# Example 1

`arhivare.in`
```
mult mai mult din putin cat mai putin, mai-mai ca te pune pe ganduri cat mai mult.
```

`arhivare.out`
```
mult mai 1 din putin cat 2 4, 2-2 ca te pune pe ganduri 5 2 1.
```

## Explanation

In the example above, "mai-mai" represents two words. The word list generated in the previous example is:

$1$ mult  
$2$ mai  
$3$ din  
$4$ putin  
$5$ cat  
$6$ ca  
$7$ te  
$8$ pune  
$9$ pe  
$10$ ganduri