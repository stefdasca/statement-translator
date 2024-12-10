Vasile is working hard on a text editor. A text consists of one or more paragraphs. Any paragraph ends with `Enter`, and any two consecutive words in the same paragraph are separated by spaces (one or more). Depending on the page's setting, the maximum number of characters that can fit on a line in a page is determined uniquely (denoted by $MAX$).

The function that Vasile needs to implement now is the alignment of each paragraph in the text both to the left and right. For this, he will need to split each paragraph into separate lines of length $MAX$ (each line ending with `Enter`). The splitting is done by placing the maximum possible number of words on each line, without splitting words into syllables. For left-right alignment, he must distribute spaces **uniformly** between the words on each line, so that the last character on the line is different from space, and the total number of characters on the line is equal to $MAX$. The only exception is the last line of a paragraph, which remains left-aligned (the words being separated by a single space, even if the line is not full).

In general, it is unlikely that alignment can be achieved by placing the same number of spaces between any two consecutive words on the line. Vasile considers it more elegant that, if an extra space has to be placed between some consecutive words compared to other pairs of consecutive words, these should be placed at the beginning of the line.

# Task
Write a program that reads the length of a line and the given text and aligns the text both to the left and right.

# Input data
The input file `text.in` contains on the first line $MAX$, the maximum length of a line.
The following lines contain the text.

# Output data
The output file `text.out` contains the text aligned left-right.

# Constraints and clarifications
- $2 \leq MAX \leq 1\ 000$
- **Attention!** The maximum length of any word in the text is $40$ characters and does not exceed $MAX$. In the original statement, the limit of a word was $25$ characters, but it appears that the tests did not respect this limit.
- **Attention!** If a line is empty, it is retained.
- The length of a paragraph does not exceed $1\ 000$ characters.
- The solution is unique.

# Example 1
`text.in`
```
20
Vasile are multe bomboane bune.
```
`text.out`
```
Vasile   are   multe
bomboane bune.
```
## Explanation
On the first line, there are $3$ spaces between consecutive words.

# Example 2
`text.in`
```
20
Ana are mere.
Ion are multe pere galbene?
```
`text.out`
```
Ana are mere.
Ion  are  multe pere
galbene?
```
## Explanation
Between `Ion` and `are` there are $2$ spaces, between `are` and `multe` there are $2$ spaces, and between `multe` and `pere` there is one space.

Notice that the paragraph `Ana are mere.` (which has a length less than $20$) remains left-aligned, and the last line of each paragraph remains left-aligned with consecutive words separated by a single space.
