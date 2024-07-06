# Statement

Let $s$ be a binary string (consisting only of characters `0` and `1`). A subarray of the string $s$ is a sequence of characters located in $s$ at consecutive positions. For example, `101` is a subarray of the string `11011`. If $x$ is a subarray of the string $s$, and with $xx$ we denote the concatenation of the string $x$ with itself, $xx$ is called a repeated subarray in $s$ if $xx$ is a subarray of $s$. For example, `101` is a repeated subarray of the string `11011011`.

For a specified string $s$, we can determine the number of distinct repeated subarrays. For instance, the string `101110110101` contains the following $6$ distinct repeated subarrays: `10111011, 1010, 0101, 11, 110110, 101101`.

# Task

Given a natural number $N$, determine a binary string of length $N$ that contains a minimal number of distinct repeated subarrays.

# Input data

Your program will not read any data from any file.

# Output data

Each line of the output file will contain a binary string of the specified length in the following table, containing a minimal number of repeated subarrays or the value $2$ (if you have not determined a solution for the value $N$ corresponding to the line).

| Line | N  |
|-------|----|
| 1     | 7  |
| 2     | 18 |
| 3     | 65 |
| 4     | 206 |
| 5     | 739 |
| 6     | 1691 |
| 7     | 5000 |
| 8     | 10000 |
| 9     | 15137 |
| 10    | 20000 |

# Scoring
* If the string displayed by the contestant on line $i$ is not valid (it is not binary or does not have the specified length), the contestant gets $0$ points for that test.
* Otherwise, the evaluation program will first determine the number of distinct repeated subarrays existing in each valid binary string present in the output file.
* For each of the specified lengths, the minimal number of repeated subarrays for the displayed strings of contestants will be determined.
* Let $min_i$ be the minimal number of repeated subarrays for a string of the length corresponding to line $i$, determined from all contestants' solutions.
* Let $nr_i$ be the number of repeated subarrays in the string displayed by the contestant for line $i$.
* The score obtained by the contestant for the test on line $i$ is: $\\displaystyle 10 \\times \\left( \\frac{min_i}{nr_i} \\right)^3$. The total score will be truncated to one decimal place.