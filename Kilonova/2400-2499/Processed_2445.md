Since she moved to Slatina, Ioana learns something new every day. Recently, she started writing reviews for all the movies she watches to send them to the local newspaper. The only problem is the very high requirements of the newspaper, which does not want Ioana's works to be plagiarized or inspired by other sources in any form.

You, being Ioana's best friend, want to help her carefully check her works. Ioana discovered that the newspaper rejects all works that contain sentences which are anagrams of a famous sentence from another review. Therefore, Ioana wants to try 2 ideas that you need to test. She wants to find out if 2 sentences are anagrams to check her work.

The first idea to test anagrams is to check if the letters in Ioana's sentence can be rearranged to obtain the famous sentence. The second idea to test anagrams is by checking the words in Ioana's sentence and seeing if their letters can be rearranged to obtain the words in the famous sentence.

# Task

Given Ioana's sentence and the famous sentence, your mission is to:
1. Check if the two sentences are anagrams by letters, according to the first idea.
2. Check if the two sentences are anagrams by both letters and words, meaning that all the words in the famous sentence are also anagrams of the words in Ioana's sentence, according to the second idea.

# Input data

The first line of the input file `ramagana.in` contains $C$, the value that determines which idea will need to be tested.
The second line of the input file contains $T$, the number of tests for the problem.
On the next groups of two lines, the first line contains Ioana's sentence, and the second line contains the famous sentence for each test.

# Output data

The output file `ramagana.out` will contain $T$ answers of `DA` or `NU` on individual lines, corresponding to the method used to determine if the sentences are anagrams in each test.

# Constraints and clarifications

* $1 \leq T \leq 100\ 000$;
* $1 \leq$ length of any string $\leq 100\ 000$, but all $T$ lengths summed $\leq 200\ 000$;
* Two strings are anagrams if they use exactly the same letters, regardless of their order (`slatina` and `tislana` are anagrams);
* All sentences are composed only of spaces and lowercase alphabetic letters;
* Spaces are not considered for anagrams!
* For the correct solution of the first task, $30$ points will be awarded;
* For the correct solution of the second task, $70$ points will be awarded.

# Example 1

`ramagana.in`
```
1
3
haideti la slatina
shad alti iet liana
slatina
tislana
info oltenia
onia olten onfi
```

`ramagana.out`
```
DA
DA
NU
```

## Explanation

In the first two examples, all the letters in the first sentence are found in the second, so these are anagrams.
In the third example, the letter `o` appears 2 times in Ioana's sentence and 3 times in the famous sentence, meaning that the two sentences cannot be anagrams.

# Example 2

`ramagana.in`
```
2
3
haideti la slatina
shad alti iet liana
slatina
tislana
ana are mere
reme naa rea
```

`ramagana.out`
```
NU
DA
DA
```

## Explanation

In the first example, although the letters of the two sentences match, the words are not anagrams of each other, so the answer is `NU`.
In the second example, we have a single word in both sentences, and the two are anagrams.
In the third example, both sentences have 3 words each, `reme` is an anagram of `mere`, `naa` is an anagram of `ana`, and `rea` is an anagram of `are`.