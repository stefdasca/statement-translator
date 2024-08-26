## Task

As the end of the semester approaches, it is time to submit the essay for the CTET (Critical Thinking and Academic Ethics) course. Like any conscientious student, you have carefully prepared your essay and made sure it meets the exact minimum required length. However, before grading, it will be checked using an Anti-Plagiarism program, and if it detects too many common passages with publicly available sources, you will have to retake the course. The Anti-Plagiarism detector works on an atypical principle. For each paragraph of the text, it will calculate an Identity Score equal to the number of palindromic subarrays contained in that paragraph. The total Identity Score of the work will be represented by the sum of the Scores of all paragraphs. Thus, to minimize the chances of being falsely accused of plagiarism, you are interested in the optimal way to divide your work into paragraphs so that the resulting Identity Score is as low as possible. One of the many conditions of the essay, however, is that the number of paragraphs cannot exceed a predetermined number $k$, so as not to lose the coherence of ideas. Thus, given $n$ - the length of the essay, $k$, and the actual text, display for each $1 \leq i \leq k$ the minimum Identity Score of the text if divided into $i$ paragraphs.

## Input data

The input file `partmin.in` will contain on the first line two natural numbers $n$ and $k$. The second line will contain a string of characters, without spaces, consisting of lowercase letters of the Latin alphabet representing the essay text.

## Output data

The output file `partmin.out` will contain $k$ lines. The $i$-th line will contain a single natural number representing the minimum cost of dividing the essay into $i$ paragraphs.

## Constraints and clarifications

A subarray of a string consists of characters located at consecutive positions in the string. A paragraph of the essay must represent a non-empty subarray of it. All paragraphs are disjoint, and their union is equal to the complete text.

$k \leq n$ for any test.

For tests worth 10 points:
$k \leq n \leq 100$

For other tests worth 10 points:
$2 \leq n \leq 1000$ and $k=2$

For other tests worth 10 points:
$k \leq n \leq 1000$ and all characters of the string are equal.

For the rest of the tests $k \leq n \leq 1000$

## Example

`partmin.in`
```
5 2
axaxy
```

`partmin.out`
```
7
5
```

## Explanation

If we leave all the text in a single paragraph, it will contain the palindromic subarrays: $a$, $x$, $a$, $x$, $y$, $axa$ and $xax$. For two paragraphs, we can divide the text into: $ax$ and $axy$ which will contain only the 5 palindromic subarrays each consisting of a single character.