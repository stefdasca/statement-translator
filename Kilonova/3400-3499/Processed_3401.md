Certainly, here is the translated competitive programming problem statement from Romanian to English with all specified instructions and conventions followed:

---

After the adventures of the future, Buzdi decided that it would be better, this time, to go into the past. However, the time-traveling machine had a malfunction, so he did not know where and in what period he would arrive. Because of this, after using the time-traveling machine, he arrived in a room where there was a safe and a table with a sheet on it. On the safe, it said "Top Secret," and on the sheet was the table of the International Morse Code.

~[International_Morse_Code.JPG|width=40%|align=center]
$$
\text{Table of International Morse Code}
$$

After he read the table from the sheet, Buzdi went to the safe and noticed that under `Top Secret` there was a string $S$ containing only the characters `.-/` and spaces, representing the encoding of a string of characters using the International Morse Code as follows:
* The character `.` represents the dot in the table.
* The character `-` represents the dash in the table.
* The characters `.` and `-`, arranged consecutively, form a capital letter according to the table.
* The 'space' character represents the end of a word.
* The character `/` represents the space between two words. This will always be followed by the 'space' character and by at least one more word.

For example, if $S = $ `.- / -... . / -.-. .`, then, after decoding this string, $S = $ `A BE CE`.

# Task

Buzdi noticed two boxes in which he needed to input some information for the safe to open. He considered that, if he entered the information correctly, he would find inside a great secret of humanity, but the time travel has greatly diminished his thinking ability. Therefore, being stuck, he asks you to determine the following information:
1) The number of words the string $S$ will have after decoding it.
2) The string $S$ after decoding it.

# Input data

The first line contains a natural number $C$, representing the type of information you need to determine. The next line contains a string of characters $S$, representing the encoding of a string of characters using the International Morse Code.

# Output data

If $C = 1$, then the first line will contain a natural number, representing the information determined for the first type.
If $C = 2$, then the first line will contain a string of characters, representing the information determined for the second type.

# Constraints and clarifications

* Let $|S|$ be the length of the string of characters $S$.
* $1 \leq |S| \leq 10^4$.
* A word is considered to be any string of consecutive letters and numbers.
* It is guaranteed that the decoded string will contain at least one word and will contain only characters found in the International Morse Code table (Latin alphabet letters and digits).
* It is guaranteed that $S$ is encoded **correctly**, using the International Morse Code table.
* For fast reading and displaying, it is recommended to use these lines of code at the beginning of the `main` function:  
```cpp
ios::sync_with_stdio(false);
cin.tie(NULL);
cout.tie(NULL);
```

| # | Points | Constraints |
| ---- | ---- | ---- |
| 0 | 0 | Examples |
| 1 | 31 | $C = 1$ |
| 2 | 10 | $C = 2$ and the decoded string will contain a single digit |
| 3 | 17 | $C = 2$ and the decoded string will contain a single word |
| 4 | 42 | $C = 2$ |

# Example 1

`stdin`
```
2
.- / -... . / -.-. .
```

`stdout`
```
A BE CE
```

# Example 2

`stdin`
```
1
.- / -... . / -.-. .
```

`stdout`
```
3
```

# Example 3

`stdin`
```
2
..-. ..- - ..- .-. . / ..-. --- .-. / ..-. ..- - ..- .-. . / ..--- ----- ..--- .....
```

`stdout`
```
FUTURE FOR FUTURE 2025
```

# Example 4

`stdin`
```
1
..-. ..- - ..- .-. . / ..-. --- .-. / ..-. ..- - ..- .-. . / ..--- ----- ..--- .....
```

`stdout`
```
4
