# Speeds

K0K alaru \(47\) managed to secure 2nd place at JBOI last year (very close to taking MAXIMUM), thus earning money and fame. As any self-respecting show-off, he bought a BMW so he wouldn't have to borrow the neighbor's horse anymore. Unfortunately, he is still having trouble with documents and therefore doesn't want to be stopped by the traffic police (fines are not an issue, given his immense wealth). This year, to get to JBOI, the show-off will use a highway that starts right from his yard (as the poet says - from kilometer \(0\) of luxury) and ends at the hotel where the Balkaniad will take place. The highway is divided into $N$ sections, each with its own speed limit, the sections being numbered with natural numbers from \(1\) to $N$. All sections have a length of one unit, and their speeds and limits are expressed in units per second. Moreover, weather conditions also impose certain restrictions: when moving from one section to another there is an acceleration/deceleration limit that K0K alaru \(47\) must respect to avoid skidding (this limit represents the maximum difference between the show-off's speeds on consecutive sections of the highway). This represents the maximum speed difference between section $i - 1$ and $i$ (a particular case being which is also a limitation of the first speed, given that on the imaginary section \(0\), the show-off has a speed of \(0\), representing the maximum acceleration at the start). For simplicity, within a section, the show-off will maintain a constant speed. As usual, you have to help the show-off by calculating his optimal speeds so that he arrives at JBOI as soon as possible. The total time is calculated as follows.

## Task

## Input data

The input file `viteze.in` will contain on the first line a single natural number $N$ (the number of sections of the highway), on the second line $N$ non-zero natural numbers separated by spaces, signifying the speed limits for each section, and on the third line another $N$ natural numbers, this time possibly zero, separated by spaces representing the array $\delta$.

## Output data

The output file `viteze.out` will contain on the first and only line $N$ non-zero natural numbers representing the speeds that K0K alaru \(47\) will choose to travel on each section.

## Constraints and clarifications

\[
1 \leq i \leq N 
\]
\[
1 \leq N \leq 1\ 000\ 000
\]
It is guaranteed that there is a solution.

The show-off advises you to think about the problem as if you were in his place.

### Subtask 1 (10 points): 
\[
1 \leq N \leq 10 
\]

### Subtask 2 (20 points):
\[
1 \leq N \leq 100 
\]

### Subtask 3 (20 points): 
\[
1 \leq N \leq 1\ 000 
\]

### Subtask 4 (30 points):
\[
1 \leq N \leq 100\ 000 
\]

### Subtask 5 (20 points): 
\[
1 \leq N \leq 1\ 000\ 000 
\]

**WARNING!** It is recommended to parse the `viteze.in` and `viteze.out` files for maximum score. You can use the code provided by us on the site to handle in and out files (both for C++ lovers and those who prefer C with similar syntax to fstream).

## Example

viteze.in
```
4
3 4 1 3
5 3 2 1
```

viteze.out
```
3 3 1 2
```

## Explanation

The optimal speed sequence is uniquely determined in the example, representing for K0K alaru \(47\) a strategy by which he will reach JBOI in $ \frac{1}{3} + \frac{1}{3} + \frac{1}{1} + \frac{1}{2} = 2.1(6) $ seconds. He will not skid because \( |0 - 3| \leq 5 \), \( |3 - 3| \leq 3 \), \( |3 - 1| \leq 2 \) and \( |1 - 2| \leq 1 \). Furthermore, the show-off will not exceed the speed limit at any point because \( 3 \leq 3 \), \( 3 \leq 4 \), \( 1 \leq 1 \), and \( 2 \leq 3 \).