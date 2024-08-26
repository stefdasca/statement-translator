## Task

Our main character finds himself in the middle of a festival. "I wonder where I am?" he asks himself. "You're somewhere beyond the hills," someone next to him answers. Puzzled by this response and having no plans for the future, he looks around and sees a music schedule for that evening. He notices that the schedule indicates that the genres to be played are $a b a c a d b a$ ($a$ representing alternative music, $b$ representing Balkan music, $c$ representing classical music, and $d$ representing disco music). This schedule is not very nice because the musical genres do not form a palindrome. He would like the sequence of musical genres he listens to form a palindrome, but at the same time, he doesn't want to miss too much of the festival - at most one continuous subarray of genres. Therefore, he wonders: how many subarrays can be deleted from the sequence of musical genres so that the resulting sequence forms a palindrome?

## Input data

The input file `dupadealuri.in` will contain the sequence of musical genres (i.e., a sequence of lowercase letters from the English alphabet).

## Output data

The output file `dupadealuri.out` will contain the required number.

## Constraints and clarifications

$1 \leq$ length of the input sequence $\leq 100\ 000$   
For 20 points, the input sequence has at most $100$ characters.  
For another 20 points, the input sequence has at most $1\ 000$ characters.  
The empty sequence is a palindrome.  

## Example

`dupadealuri.in`  
```
autorulnuafostlaafterhillsinca
abacadba
aba
```

`dupadealuri.out`  
```
6
11
4
```