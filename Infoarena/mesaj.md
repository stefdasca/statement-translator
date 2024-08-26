## Message

Zaharel sends messages to his friend Eugenia using his own communication system (to avoid spending money on SMS). Unfortunately, Zaharel's system is not entirely efficient, and sometimes the message is distorted, meaning that extra characters may appear in the message. Fortunately, Zaharel's vocabulary is relatively limited, and Eugenia knows how to take advantage of this: she made a list of all the $N$ words that Zaharel can use in the message. Zaharel's system does not use spaces to separate the words, but Eugenia is smart enough to understand the meaning of the message even without spaces.

## Task

Knowing the list of $N$ words and the final message consisting of $M$ characters, find out the minimum number of characters Eugenia needs to remove from the message so that it can be represented as a sequence of words from the dictionary.

## Input data

The first line of the file `mesaj.in` contains two natural numbers $N$ and $M$ representing the number of words in the list and the length of the message.  
The second line will contain $M$ characters representing the message.  
The next $N$ lines contain one word from the list each.

## Output data

The output file `mesaj.out` will contain a single line which will contain the minimum number of characters that need to be deleted.

## Constraints

$5 \leq N \leq 1 \ 000$  
$1 \leq M \leq 1 \ 600$  
The words in the list have lengths between $1$ and $20$  
The message and the words consist only of lowercase letters of the English alphabet $\{a, b, c \dots z\}$

## Example

`mesaj.in` 
```
9 20 
carmrcmddrcaddamroom 
car 
cdr 
cadar 
moo 
oom 
omo 
mr 
cam 
room 
```

`mesaj.out`

```
4 
```

## Explanation

$carmrc$ $\textcolor{red}{md}$ $drcad$ $\textcolor{red}{d}$ $a$ $\textcolor{red}{m}$ $room$  
If the letters in red are removed, the remaining message will be the following sequence of words from the list: $car$ $|$ $mr$ $|$ $cdr$ $|$ $cadar$ $|$ $oom$