# Diez

Negrimon found this $ \#legendary $ problem in a collection: over a string of length $ N $, consisting of lowercase English letters, $ M $ operations of the following types are performed:
1. Insert the character $ x $ in the string at position $ p $, shifting the characters at positions greater than or equal to $ p $ one position to the right. If the value of $ p $ equals the length of the string, $ x $ is appended at the end of the string.
2. Respond with $ 1 $ if the letter sequence starting at position $ q1 $ and having length $ lg $ matches letter for letter with the sequence starting at position $ q2 $ and having the same length $ lg $, and respond with $ 0 $ otherwise. It is possible that the two sequences overlap completely or partially in the string they are part of.

Given a string of $ N $ lowercase letters and a list of $ M $ operations, display the responses to the type $ 2 $ operations, respecting the order in the given sequence of operations.

## Input data

The input file $ diez.in $ contains on the first line the values $ N $ and $ M $, separated by a space as described in the statement. The second line contains a string of $ N $ lowercase English letters, and the next $ M $ lines contain one operation in one of the following formats:
`1 p x` - Data for the type $ 1 $ operation.
`2 q1 q2 lg` - Data for the type $ 2 $ operation.

## Output data

The output file $ diez.out $ will contain values equal to $ 0 $ or $ 1 $, one per line, representing the responses given, in order, to the type $ 2 $ operations existing in the input file.

## Constraints and clarifications

$ 1 \leq N $  
$ 1 \leq M $  

$ 0 \leq p \leq $ the length of the string at the time of insertion  
$ x $ is a lowercase English letter  

$ q1, q2 \geq 0 $  
it is guaranteed that for each type $ 2 $ operation, there are $ lg $ characters in the string starting both at position $ q1 $ and at position $ q2 $

$ 1 < lg \leq $ the length of the string at the time of performing the type $ 2 $ operation  

Character positions in the string start from position $ 0 $

## Example

`diez.in` 
```
8 6
abcasfas
2 0 5 3
1 3 d
2 4 7 2
1 1 s
1 10 b
2 0 8 3
```

`diez.out` 
```
0
1
1
```

## Explanation

```
8 6
abcasfas
2 0 5 3
1 3 d
2 4 7 2
1 1 s
1 10 b
2 0 8 3
```

The sequences $ abc $ and $ fas $ are compared, they are different $\rightarrow$ print $ 0 $

The character $ d $ is inserted before position $ 3 $, resulting in the string `abcdasfas` 

The subarrays $ as $ and $ as $ are compared, they are identical $\rightarrow$ print $ 1 $

The character $ s $ is inserted before position $ 1 $, resulting in the string `asbcdasfas` 

The character $ b $ is inserted at position $ 10 $, the position is equal to the length of the string, resulting in the string `asbcdasfasb` 

The subarrays $ asb $ and $ asb $ are compared, they are identical $\rightarrow$ print $ 1 $

## Example

`diez.in` 
```
6 3
atmatm
2 0 2 4
1 6 a
2 0 3 4
```

`diez.out`
```
0
1
```

## Explanation

```
6 3
atmatm
2 0 2 4
1 6 a
2 0 3 4
```

The subarrays $ atma $ and $ matm $ are compared, they are different $\rightarrow$ print $ 0 $

The character $ a $ is appended at the end, resulting in the string `atmatma` 

The subarrays $ atma $ and $ atma $ are compared, they are identical $\rightarrow$ print $ 1 $