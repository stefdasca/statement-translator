Pojărel has a list of `N` files, each named only with lowercase Latin letters. He wants to implement a search engine that works in real-time, meaning immediately after the user inserts or deletes a letter from the search field, the number of files corresponding to the currently input string should be returned. A file corresponds to the search if its name contains the search string as a subsequence. More precisely, the characters in the search field must appear in the file name in the same order, but not necessarily in consecutive positions.

# Task
Given the list that contains the file names, determine the number of files that will be returned after each insertion or deletion of a character from the search field.

# Input data
The input file `search.in` contains the first line two natural numbers `N` and `M`, representing the number of files and the number of operations performed on the search field, respectively. The next `N` lines contain the `N` file names, consisting only of lowercase Latin letters. Then follow `M` lines that describe the operations in the order they are performed. Thus, on each line `i` there is a single character that describes operation `i`. This character is either a letter, which means that the respective letter has been inserted into the search field, or the character `-`, which means that the last letter in the search field has been deleted.

# Output data
The output file `search.out` will contain `M` lines. Line `i (1 \\leq i \\leq M)` will print the number of files returned by the search engine after performing the first `i` operations.

# Constraints and clarifications
* `1 \\leq N \\leq 100`;
* `1 \\leq M \\leq 200 000`;
* the length of any file name is at most `5 000`;
* two or more files may have the same name;
* the first letter introduced will never be deleted.

# Example

`search.in`
```
4 5
palalila
alabala
olimpiada
iasi
a
a
l
-
b
```

`search.out`
```
4
3
2
3
1
```

Explanation
---
- the first time the letter `a` is introduced, it is found in all `4` file names
- after the second operation, the field will have the value `aa` and the first `3` files will be found
- after the third operation, the field will have the value `aal` and the files `palalila` and `alabala` will be found
- after the fourth operation, the field will have the value `aa` again and the first `3` files will be found
- after the fifth operation, the field will have the value `aab` and only the file `alabala` will be found