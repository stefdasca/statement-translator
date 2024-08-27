# Anagrams2

Note: This problem is interactive. A number is an anagram in base $B$ of another number when there is a reordering of its digits such that the other number is obtained and vice-versa. For example, $1230$ is an anagram of $1023$ but $3210$ is not an anagram of $123$. Marcel has chosen a favorite number in base $B$ and now he likes all its anagrams. He wants to share it with you, but he doesn't want it to be too easy, he wants you to make an effort to find it. He will answer several questions like "-Marcel, is this number smaller, equal, or larger than your favorite number?". But Marcel wants the number you ask about to be to his liking as well, that is, to be an anagram of his favorite number.

## Task

For each test, several situations need to be processed. Therefore, the first line will contain the number of situations $T$.

## Input data

For each situation, the first line will contain a natural number $B$. The second line will contain $B$ numbers, representing how often each digit - starting with digit $0$ and ending with digit $B - 1$ - appears in Marcel's favorite number. Your program is allowed to ask questions by writing to the standard output, in the form "<anagram>", that is, a string of characters.

## Output data

For each question, the interactor will respond in the standard input with a character. This can be:
- '!', if the question is invalid (the number displayed is not an anagram of Marcel's favorite number). Then the program must be terminated immediately to receive the verdict "Wrong query format", otherwise the verdict may be different.
- '<', if the displayed number is smaller than Marcel's favorite number.
- '=', if the displayed number is equal to Marcel's favorite number. Then the program must start processing the next situation, or stop, if this was the last one.
- '>', if the displayed number is larger than Marcel's favorite number.

Reading and displaying will be done with standard input/output. After each question, the newline character ('\n' or endl) must be displayed. Attempting to open any file may lead to an error in the execution of your program. Don't forget to flush the output buffer, with $cout.flush()$ or $fflush(stdout)$. AFTER EACH QUESTION!!! The interactor is not adaptive. In other words, Marcel has decided from the beginning what his favorite number is, and the questions cannot influence him.

## Constraints

1 $\leq$ $T$ $\leq$ 100  
2 $\leq$ $B$ $\leq$ 30  
0 $\leq$ Marcel's favorite number < $B^{30}$  

Of course, Marcel's favorite number does not start with digit $0$ unless it is null. The total number of anagrams of Marcel's favorite number is strictly less than $2^{58}$.

## Example

standard input
```
2
3
1 1 1
< < < =
12
0 0 0 0 0 0 0 0 0 0 2 1
> < =
```

standard output
```
102
120
201
210
baa
aab
aba
```

## Explanation

The test contains 2 situations. In the first situation, Marcel's favorite number is $210$ in base $B = 3$. Each digit appears once. To the questions $102$, $120$, and $201$, Marcel answers with '<', because these numbers are smaller than $210$. To the question $210$, Marcel answers with '='. In the second situation, Marcel's favorite number is $aba$ in base $B = 12$. The first $10$ digits do not appear at all, and digit $a$ appears $2$ times, while digit $b$ appears once. To the question $baa$, Marcel answers with '>', because this number is larger than $aba$. To the question $aab$, Marcel answers with '<', because this number is smaller than $aba$. To the question $aba$, Marcel answers with '='. For the first situation, $4$ queries were used. For the second, $3$ were used. So $K = max(4, 3) = 4$.