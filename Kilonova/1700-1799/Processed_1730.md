# Task

Given a number $n$, we have a **complete set** of domino pieces. A complete set means that we have one piece for each **possible pair** of numbers from the set $\\{1, 2 , \\dots, n \\}$. The numbers on a piece can be different or the same. In the complete set, each piece appears only once, and we don't have two pieces that contain the same numbers written in a different order; the piece $\\boxed{i\\vphantom{|}}\\boxed{j\\vphantom{|}}$ is the same as the piece $\\boxed{j\\vphantom{|}}\\boxed{i\\vphantom{|}}$.

For example, if $n = 3$, we have six pieces: $\\boxed{1\\vphantom{|}}\\boxed{1\\vphantom{|}}, \\boxed{2\\vphantom{|}}\\boxed{2\\vphantom{|}}, \\boxed{3\\vphantom{|}}\\boxed{3\\vphantom{|}}, \\boxed{1\\vphantom{|}}\\boxed{2\\vphantom{|}}, \\boxed{3\\vphantom{|}}\\boxed{1\\vphantom{|}}, \\boxed{2\\vphantom{|}}\\boxed{3\\vphantom{|}}$. In the game of dominoes, any piece $\\boxed{i\\vphantom{|}}\\boxed{j\\vphantom{|}}$ can be used either as $\\boxed{i\\vphantom{|}}\\boxed{j\\vphantom{|}}$, in which case we have number $i$ on the left and number $j$ on the right, or as $\\boxed{j\\vphantom{|}}\\boxed{i\\vphantom{|}}$ and in this case, number $j$ is on the left, and number $i$ is on the right.

With the pieces we have, we can form a sequence if we follow the following rule: two pieces in adjacent positions in the sequence must contain the same number on the right side of the first piece and on the left side of the second piece. We will call this rule the **"left-right property"**. The only exceptions to this rule are the first piece for the left number and the last piece for the right number. In this sequence, a piece cannot appear more than once. Examples:

* Correct sequence for a complete set with $n=3$:
$\\boxed{1\\vphantom{|}}\\boxed{1\\vphantom{|}}, \\boxed{1\\vphantom{|}}\\boxed{3\\vphantom{|}}, \\boxed{3\\vphantom{|}}\\boxed{3\\vphantom{|}}, \\boxed{3\\vphantom{|}}\\boxed{2\\vphantom{|}}, \\boxed{2\\vphantom{|}}\\boxed{2\\vphantom{|}}, \\boxed{2\\vphantom{|}}\\boxed{1\\vphantom{|}}$ 
* Correct sequence that **does not** use all pieces of a complete set with $n=3$:
$\\boxed{3\\vphantom{|}}\\boxed{3\\vphantom{|}}, \\boxed{3\\vphantom{|}}\\boxed{2\\vphantom{|}}, \\boxed{2\\vphantom{|}}\\boxed{2\\vphantom{|}}, \\boxed{2\\vphantom{|}}\\boxed{1\\vphantom{|}}$
* Incorrect sequence, with pieces that **do not** respect the "left-right property" (third and fourth pieces):
$\\boxed{3\\vphantom{|}}\\boxed{3\\vphantom{|}}, \\boxed{3\\vphantom{|}}\\boxed{2\\vphantom{|}}, \\boxed{\\textcolor{lime}{2}\\vphantom{|}}\\boxed{\\textcolor{lime}{2}\\vphantom{|}}, \\boxed{\\textcolor{lime}{1}\\vphantom{|}}\\boxed{\\textcolor{lime}{2}\\vphantom{|}}$
* Incorrect sequence, in which a piece is used twice (third and fifth pieces):
$\\boxed{1\\vphantom{|}}\\boxed{2\\vphantom{|}}, \\boxed{2\\vphantom{|}}\\boxed{2\\vphantom{|}}, \\boxed{\\textcolor{lime}{2}\\vphantom{|}}\\boxed{\\textcolor{lime}{3}\\vphantom{|}}, \\boxed{3\\vphantom{|}}\\boxed{3\\vphantom{|}}, \\boxed{\\textcolor{lime}{3}\\vphantom{|}}\\boxed{\\textcolor{lime}{2}\\vphantom{|}}$

# Task

Determine if for a given $n$, a sequence can be formed using all the domino pieces from a complete set.

# Input data

The file `domino.in` contains on the first line a single natural value $n$ with the meaning described above.

# Output data

The file `domino.out` will contain on each line the two numbers found on one piece from the required sequence separated by a space. The first line will contain the numbers of the first piece, the second line will contain the numbers of the second piece, etc. The numbers on a piece will be written in such a way as to respect the "left-right property". If there is no solution, print the value $-1$ on the first line of the file.

# Constraints and clarifications

* $2 \\leq n \\leq 1 \\ 500$.
* There can be multiple solutions; any correct solution is acceptable.

# Example

`domino.in`
```
3
```

`domino.out`
```
1 1
1 2
2 2
2 3
3 3
3 1
```

