## Task

Two brothers, Ionică and Florin, are going with their parents to the sea in Antalya. The hotel where they are staying contains a safe. Ionică, the older brother, is a calm child, while Florin is always up to mischief. As soon as he arrived in Antalya, Florin bought a toy that makes a very annoying noise for those around him. To get rid of this stress, one morning Ionuț takes Florin's toy and hides it in the safe. The safe is locked with a code consisting of $n$ lowercase letters of the English alphabet. After waking up, Florin starts a ruckus because he can't find his toy anymore. After many discussions, Ionuț tells Florin that the toy is in the safe, but he can't remember the opening code.

To prolong the period of peace, Ionuț tells Florin a word, made up of lowercase letters of the English alphabet, about which he claims:

* The code is written with $n$ letters that are found in this word;
* The letters in the code are either distinct, or there is at most one letter that repeats exactly twice in the code, but this happens only if the letter is found at least twice in the word.

Now Florin has a lot of work because he starts writing in a notebook all the distinct variants for the code, based on the hints given by Ionuț.

## Task

Knowing the number of letters in the code $n$ and the word told by Ionuț, determine the number of codes written by Florin.

## Input data

The input file `cod.in` will contain the number $n$ on the first line, and on the second line the word told to Florin by Ionuț.

## Output data

The output file `cod.out` will contain the required number, $\\text{mod } 9 \\ 901$.

## Constraints and clarifications

* $1 \leq$ number of characters in the word $\\leq 250$
* $1 \leq n \leq 26$
* $k \\text{ mod } p$ represents the remainder of the integer division of $k$ by $p$.

## Example

`cod.in`
```
3
radarr
```

`cod.out`
```
18
```

## Explanation

Possible codes can be: `rad`, `rda`, `ard`, `adr`, `dra`, `dar`, `raa`, `ara`, `aar`, `daa`, `ada`, `aad`, `drr`, `rdr`, `rrd`, `arr`, `rar`, `rra`.