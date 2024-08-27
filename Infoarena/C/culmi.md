# Peaks

Gigel likes to play with numbers. This time he is only playing with the numbers $+1$ and $-1$. He writes down, one after another, $n$ numbers $+1$ and $n$ numbers $-1$, but he ensures that summing any consecutive numbers starting from the first number written does not result in a negative sum. Then Gigel represents the $+1$ number with $/$ and the $-1$ number with $\backslash$, creating some interesting drawings. Thus, for $n=3$, the correct configurations and the drawings Gigel obtains are as follows:

![example configurations~[example.png]]

Clearly, the configuration where the sum becomes $-1$ at some point is not correct. Gigel notices that these drawings resemble mountains and, moreover, he sees that the number of mountain peaks varies: some have one peak, others have two peaks, and others even three. A mountain peak has the shape /\.

## Task

For given values $n$ and $k$, determine how many correctly formed "mountains" with $n$ signs $/$ and $n$ signs $\backslash$ have exactly $k$ peaks.

## Input data

The input file `culmi.in` will contain on the first line the values $n$ and $k$ separated by a space.

## Output data

The output file `culmi.out` will contain on the first line the number of correctly formed mountains that have exactly $k$ peaks.

## Constraints

$1 \leq n \leq 100$  
$1 \leq k \leq n$

## Example

`culmi.in`  
`3 2`

`culmi.out`  
`3`