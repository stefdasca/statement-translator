
# Task

Your friend, Ursu, gave a list of $N$ words only containing lowercase letters of the English alphabet. The list represents Ursu's phone book. Unfortunately, Ursu's phone book is quite long. That is why he would like you to help him rename all his contacts. Since both of you are quite lazy, you want to minimize the time spent renaming all the contacts. Now, Ursu asks you to find for each of the $N$ words the length of its shortest substring that does not appear in any of the other strings. If no such substring exists, Ursu would like to know that he cannot rename that contact, so, the answer will be considered to be $-1$.

# Input data

The first line of the input contains the number $N$ ($1 \le N \le 2 * 10^5$). The next $N$ lines will each contain a string $S$.

The total length of all the strings (noted $S$) will be at most $2 * 10^5$.

For tests worth $13$ points, $1 \le S \le 100$.

For tests worth $54$ more points, $1 \le S \le 2 * 10^4$.

# Output data

The program will print $N$ lines, the $i-th$ of them representing the length of the shortest substring of the $i-th$ string not appearing in any other string.

# Example 1

`stdin`
```
3
abdf
abf
abde
```

`stdout`
```
2
2
1
```
