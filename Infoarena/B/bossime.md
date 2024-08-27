# Bossime

"Did you mean... boss!" Recently, the National Institute for Bossism Equivalence Research was established in the picturesque land of Romania. In an extraordinary meeting, the superior council of the institute decided that all so-called boss citizens should be classified by an integer representing the corresponding bossism coefficient. This number is determined following multiple analyses conducted on the subjects involved, and the evaluated competencies do not exactly fall within the ethical sphere and especially not within the legal one. As a result of frustrations from those disadvantaged by the new universal bossism classification system, alternative calculation methods have emerged. One example of such an offensive method is the following: An individual’s bossism increases by $1$ with each passing day, without them having to prove that they deserve to hold this coefficient. Moreover, two individuals are considered bossically equivalent if their bossism coefficients differ by a simple permutation of digits. Absolutely scandalous! Many adherents of this nefarious system are eager to confront each other, so they come in groups of two and ask you how many days they have to wait until they are bossically equivalent and can confront each other. You gulp and help them so that you don’t get into trouble.

## Input data

The input file `bossime.in` will contain the number $T$ of tests, followed by $T$ lines with two numbers $A$ and $B$, representing the bossism coefficients of two candidates wanting to confront each other.

## Output data

The output file `bossime.out` will contain $T$ lines, each with a possible answer, or with Impossible if no solution exists.

## Constraints

$1 \leq T \leq 1000$  
$1 \leq A,B \leq 10^9$  
The printed answer should be $\leq 10^{17}$  
It is guaranteed that there will always be a solution under this limit if one exists  
Any correct answer falling within the specified limits is accepted  
Leading zeroes are NOT accepted, e.g., $105$, $015$

## Example

`bossime.in`  
$3$  
$13$ $58$  
$13$ $24$  
$153$ $270$  

`bossime.out`  
$3$  
Impossible  
$50$  

## Explanation

For the first test $13 + 3 = 16$ and $58 + 3 = 61$  
For the third test $153 + 50 = 203$ and $270 + 50 = 320$