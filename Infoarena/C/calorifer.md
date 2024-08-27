# Radiator

It is said that friends are not truly friends until they drink a beer together, solve a programming problem together, and destroy each other's radiators together. This is also the case for two characters, whom we will call Xdarascu and Xcsi (to keep them anonymous). Xdarascu is never short of drinks and friends, but Xcsi, on the other hand, wants very much to show his friend how good friends they are, which is why he decided to destroy all the radiators in his house. It doesn't take much IQ and many beers for such an act. Since the intelligence of the characters is not an unknown in this problem, that's what happened. Love was already at first sight. Xcsi was caressing Xdarascu with sweet words: "What a coincidence, I destroyed your radiator again, isn't it funny!?" while Xdarascu wanted to kiss his fists in the face, not exactly in the face, but still in the face. Love was already much too intense. Jealous of the authentic friendship between the two, Princess Mieunita quickly jumped to throw a wrench in their works. She gave a programming problem to Xcsi to distract him from his beaten-by-fate partner, the perfect opportunity to enchant him. Help the poor Xcsi solve the programming problem while Xdarascu has nothing to do with his life and hangs radiators on the wall.

## Task

And because Mieunita's problem hasn't been told yet, you have the opportunity to learn about it after reading this whole useless statement: Let $N$ be a non-zero natural number. Three types of operations can be applied to this number: 
- multiplication by $3$
- division by $2$ (if the number is divisible by $2$)
- maintaining the value (i.e., the number remains unchanged)

The princess chooses a non-zero natural number $N$ to which she applies the above operations successively, noting on paper the result obtained from each operation. Among these results, she selects $K$ (including the first and last), rearranges them, and gives them to Xcsi. He has to discover the initial order of the $K$ numbers. This is where you come in to restore love! 

## Input data

The input file `calorifer.in` contains on the first line a natural number $K$ with the meaning given in the statement. The next line contains $K$ non-zero natural numbers, representing the numbers given by Princess Mieunita. 

## Output data

The output file `calorifer.out` will contain a single line with: 
- $-1$ if the numbers cannot be obtained by applying the described operations 
- $K$ numbers, representing the initial ordered numbers

## Constraints and Clarifications

$1 \leq K \leq 100,000$

$1 \leq x \leq 1,000,000,000$, where $x$ is a number given by the princess 

The first and last number written by the princess on paper are among the given numbers. 

For test cases worth $10$ points 

$1 \leq K \leq 10$ 

For other test cases worth $30$ points 

$1 \leq K \leq 2,000$

## Example

`calorifer.in`
```
5 
40 80 30 15 60
```

`calorifer.out`
```
80 40 60 30 15
```

`calorifer.in`
```
4 
12 3 9 3
```

`calorifer.out`
```
12 3 3 9
```

## Explanation

The initial numbers could be (in order): $80 40 20 60 30 15$ or $80 40 120 60 30 15$.