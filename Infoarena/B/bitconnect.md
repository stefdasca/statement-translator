# Bitconnect

Hey hey hey, Eddie Value has been searching for a quick way to get rich so that he can buy Tedi bottles to drink together with his brothers, and he finally came up with a guaranteed success idea: he will create his own cryptocurrency (named Junior Coin, or JC for short). Everything was going well until Eddie had to implement the cryptocurrency. His first challenge was to handle transactions. The way transactions operate follows a sneaky model, which can be described as follows: every boss has an associated number between $1$ and $2^{62}$. A brotherly favor between two bosses exists if the AND between their numbers is non-zero (there is a brotherly favor between $x$ and $y$ if and only if $x & y \neq 0$). To perform a transaction from $x$ to $y$, it is desired to use as few brotherly favors as possible; because favors are not easily obtained, Eddie would like to know the minimum number of favors through which multiple transactions pass. However, Eddie is not satisfied: he knows that his coin will have almost instant success, so the coin must ultimately support $3$ types of operations:

$add(x)$ - boss $x$ decides to join the coin. Brotherly favors form between him and the other bosses. It is guaranteed that $x$ is not already part of the coin.

$erase(x)$ - boss $x$ has gained enough value and decides to no longer invest in the coin. Therefore, he must be removed, and all the favors he had must be erased.

$transaction(x, y)$ - Eddie wants to know the minimum number of favors used to perform a transaction from $x$ to $y$, or $-1$ if a transaction cannot be performed; it is guaranteed that $x$ and $y$ are part of the coin.

Since Eddie knows that what he is asking for is too difficult, he gives you $2$ ways to respond to the queries:

bit-mode - you must state the minimum number of favors; this mode will receive $100\%$ of the points/test.

connect-mode - you must state only if there is a way to perform the transaction from $x$ to $y$; this mode will receive $25\%$ of the points/test.

## Input data

In the input file `bitconnect.in`, the first line contains a natural number $N$, which represents the number of operations. On the following $N$ lines, there will be operations described as follows:

$1 \ x$ - boss $x$ joins the network; it is guaranteed that he was not already in the network;

$2 \ x$ - boss $x$ leaves the network; it is guaranteed that he was already in the network;

$3 \ x \ y$ - the answer to the question related to boss $x$ and boss $y$ is requested;

## Output data

In the output file `bitconnect.out`, the first line contains the word "bit" (without quotes) if you want to answer in bit-mode, otherwise the word "connect" (also without quotes) will be present. On the following lines, the responses to the type $3$ operations will appear as follows:

if the chosen mode was bit-mode, on each line will be the minimum number of favors used to perform a transaction between boss $x$ and boss $y$; if a transaction cannot be performed between boss $x$ and boss $y$, $-1$ will be displayed;

if the chosen mode was connect-mode, on each line will be $1$ if a direct or indirect transaction can be performed between boss $x$ and boss $y$, otherwise $0$ will be displayed;

## Constraints and clarifications

$Subtask \ 1 \ (test \ 1) \ - \ 4 \ points: \ the \ answer \ will \ be \ 0, \ 1, \ or \ -1, \ N \leq 200$

$Subtask \ 2 \ (tests \ 2-5) \ - \ 16 \ points: \ N \leq 500$

$Subtask \ 3 \ (tests \ 6-13)- \ 32 \ points: \ N \leq 7000$

$Subtask \ 4 \ (tests \ 14-25)- \ 48 \ points: \ N \leq 106000$

In a transaction between $x$ and $x$, it is considered that $0$ favors are used.

For those who are uninitiated in the art of cryptocurrencies:
```
"TO \ THE \ MOON \ !" \ = \ OK \ for \ bit \ mode \
"to \ the \ moon!-ish" \ = \ OK \ for \ connect \ mode \
"The \ output \ file \ is \ a \ scam" \ = \ Incorrect \ format \ of \ the \ output \ file \
"HODL" \ = \ Incorrect \ The \ values \ of \ the \ numbers \ are \ natural \ numbers \ less \ than \ $2^{62}$ \
Do \ not \ ask \ what \ the \ terms \ above \ mean \ from \ the \ evaluator, \ as \ it \ is \ possible \ to \ upset \ us, \ to \ take \ the \ points \ and \ not \ give \ them \ back. \
```

## Example

`bitconnect.in`:
```
26
1 1
1 2
3 1 2
1 3
1 4
3 1 2
3 1 3
3 1 4
3 2 4
1 5
3 1 4
3 2 4
3 3 4
1 7
3 1 4
3 1 5
3 2 7
2 3
2 5
3 1 4
3 2 7
1 5
3 1 7
3 5 2
3 7 4
3 7 7
```

`bitconnect.out`:
```
bit
-1
2
1
-1
-1
2
3
2
2
1
1
2
1
1
2
1
0
```

## Explanation

After the first $2$ insert operations, the network will look like in the first image. There is no brotherly favor between $1$ and $2$, so the answer is $-1$. After another $2$ insert operations, the network will look like in the second image. After another insert operation, the network will look like in the third image. After yet another insert operation, the network will look like in the fourth image. After $2$ erase operations, the network will look like in the fifth image. After one insert operation, the network will look like in the sixth image.

~[first_image.png]
~[second_image.png]
~[third_image.png]
~[fourth_image.png]
~[fifth_image.png]
~[sixth_image.png]