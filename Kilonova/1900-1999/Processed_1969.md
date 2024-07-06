Tassadar has survived the Culture and Civilization course, but he has been deeply affected by this experience and is convinced that the courses were incoherent.

To verify this, he has compiled a dictionary that includes all the incoherent words he has encountered throughout his life. The incoherence level of a word in the dictionary is equal to the length of the word. The Culture and Civilization course can be represented by a string of $N$ lowercase letters of the Latin alphabet.

Tassadar wants to insert spaces in the course and thus delimit the words that appear in it. He wants to do this in such a way that the sum of the incoherence levels of the words in the course is maximized.

Help Tassadar find out how incoherent the Culture and Civilization course is!

# Input data

The input file `kc.in` contains on the first line the numbers $N$ and $K$, representing the length of the course and the number of words in the dictionary, respectively. The next line contains a string of $N$ letters, representing the Culture and Civilization course. The following $K$ lines contain the words from the dictionary, one on each line.

# Output data

The output file `kc.out` will contain on the first line the maximum sum of incoherence levels that can be obtained by delimiting the words from the course with spaces.

# Constraints and clarifications

* $1 \\leq N \\leq 100 \\ 000$
* $1 \\leq K \\leq 100 \\ 000$
* $1 \\leq L \\leq 100 \\ 000$, where $L$ is the sum of the lengths of the words in the dictionary
* A word is a maximal subarray of lowercase Latin letters and is delimited on the left and right either by a space, the beginning of the course, or the end of the course.
* If a word from the course does not appear in the dictionary, it has an incoherence level of $0$
* For tests worth 10 points, $N \\leq 1 \\ 000$ and $L \\leq 1 \\ 000$
* For tests worth another 30 points, $N \\leq 1 \\ 000$

# Example

`kc.in`
```
3 3
abc
a
c
abc
```

`kc.out`
```
3
```

## Explanation

There are four ways we can delimit the words from the course with spaces: `abc` (contains a single word with an incoherence level of $3$), `ab c` (contains one word with an incoherence level of $0$ and one with an incoherence level of $1$), `a bc` (contains one word with an incoherence level of $1$ and one with an incoherence level of $0$) and `a b c` (contains two words with an incoherence level of $1$ and one with an incoherence level of $0$). Of all these ways, it is optimal to not insert any spaces in the course, to obtain the maximum sum of incoherence levels, this being equal to $3$.