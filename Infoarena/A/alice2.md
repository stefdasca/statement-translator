Alice in Wonderland

Alice, being in Wonderland, meets the Dormouse, who proposes her a task. If Alice manages to solve the task, the Dormouse will help her whenever she needs it. Thus, not wanting to miss such an opportunity, Alice asks for your help to solve the task. The Dormouse begins and explains the task: Here we have a word in our language. Being in Wonderland, even the determination of the length of this word is a bit different from the human language. For example, you can move from the character $'a'$ at position $i$ to the character at position $i+1$ or $i-1$, but you can also move to the first occurrence of the character $'a'$ found to the left or right of the current character. Knowing these rules, the length of the word is calculated by the minimum number of steps needed to move from the first position to the last character. Not having worked on computing for a long time, Alice asks for your help to solve this task. Given a word in the Wonderland's language, compute its length according to the measurement method described by the Dormouse. Can you help her?

## Input data

The input file `alice2.in` contains one line with a single word $C$, which represents the word in the Wonderland's language.

## Output data

The output file `alice2.out` contains on the first line a natural number which represents the length of the word $C$, calculated according to the rules stated by the Dormouse.

## Constraints

$1 \leq |C| \leq 100\,000$

The word in the Wonderland's language consists of lowercase letters from the English alphabet.

For 28 points, $|C| \leq 10^3$

For another 36 points, $|C| \leq 10^4$

For another 36 points, $|C| \leq 10^5$

## Example

`alice2.in`
```
cuvant
```

`alice2.out`
```
5
```

`alice2.in`
```
adiacrac
```

`alice2.out`
```
3
```