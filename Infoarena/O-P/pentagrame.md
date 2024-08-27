## Task

Walter wants to help Nikita and Michael meet without the knowledge of the Section leadership, so he offered to do Nikita's work in her place. When he was about to get to work, he was assigned to build a new high-powered bomb. Finding himself in difficulty, he asked Birkhoff for help, but Birkhoff refused because he had just been threatened by Michael and is now working for him. Left with no alternatives, Walter asked you to do Nikita's job. Nikita is studying the encoded messages that members of the Red Cell transmitted to each other by radio on her last mission. In her research, she found in the Section's database a list of pentagrams secretly copied a few months ago from the Red Cell servers. Nikita believes she can decode the messages the terrorists have sent to each other if she identifies the pentagrams that appear in the most words as subsequences.

## Input data

The input file `pentagrame.in` contains on the first line two natural numbers $N$ and $M$, representing the number of copied pentagrams and the number of encoded messages, respectively. Each of the next $N$ lines contains a pentagram (a string of exactly 5 lowercase English letters or digits). Each of the next $M$ lines contains an encoded message (a string of lowercase English letters or digits).

## Output data

The output file `pentagrame.out` will contain on the first line a natural number $X$ representing the number of pentagrams that appear in the most messages as subarrays and on the next $X$ lines will be the required pentagrams, one per line, in lexicographical order.

## Constraints and clarifications

$1 \leq N \leq 50\ 000$

$1 \leq M \leq 50\ 000$

The pentagrams are distinct pairwise. 

The length of an encoded message is at least 5 characters and at most 30.

In lexicographical order, digits come before lowercase English letters.

## Example

`pentagrame.in` 
```
3 5
n4isl
4hd72
k3j4h
id8k3j4hd728o0
n4isln4isln4isl
kk7gud589hylo9
4hd72
idiodk3j4howoi82
```

`pentagrame.out` 
```
2
4hd72
k3j4h
```

## Explanation

The 3 pentagrams are found in the terrorists' messages as follows:

id8 k3j 4h d72 8o0 

n4isln4isln4isl

kk7gud589hylo9

4hd72  

idiod k3j4h owoi82

Although the pentagram n4isl appears 3 times in a message, it appears in only one message and is not the most frequent, because the other two pentagrams appear in two messages each.