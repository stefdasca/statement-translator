# Caribbean

The $N$ pirates of the Black Pearl have recently made a very significant capture: a chest with $10,000,000,000$ (ten billion) coins. Now the pirates have a more difficult problem to solve: how to divide the money. For the division, the pirates line up. The first pirate will propose a scheme for dividing the money. If a certain number of pirates do not agree with this scheme, the pirate will be thrown overboard, and then the next pirate will propose a division scheme, and so on. The pirates are very intelligent: a pirate agrees with a division scheme only if it brings him a strict advantage (at least one coin) compared to what he would get by voting against the scheme. Because they act only on rational bases, the pirates are also very predictable. In other words, a pirate can anticipate the decisions of other pirates in order to make his own decision (this also means that if a pirate has multiple possibilities for choosing a division scheme, the other pirates know which option he would choose). Depending on the characteristics of each pirate (strength, popularity), the number of pirates that need to agree with his scheme in order not to be thrown overboard varies. Let's say for pirate $i$ $(1 \leq i < N)$ this number is $A_i$. If pirate $i$ proposes a scheme, we know that all pirates up to $i-1$ have already been thrown overboard. Besides pirate $i$, there are $N-i$ pirates left. If at least $A_i$ of them agree with pirate $i$'s scheme, the treasure will be divided according to this scheme. Otherwise, pirate $i$ will be thrown overboard, and pirate $i+1$ will propose a scheme. For any $i$, we have $0 \leq A_i < N-i$. Due to this condition $A_{N-1} = 0$, and $A_N$ is not defined (because pirate $N$ is the last one).

## Task

The first pirate in line wants to propose a scheme for dividing the money so that he is not thrown overboard, and he receives as many coins as possible. Determine the maximum sum he can receive. It is guaranteed that there is a scheme that the first pirate can propose such that he is not thrown overboard.

## Input data 

The input file `caraibe.in` contains on the first line the number $N$ of pirates. The following lines contain the values $A_1, A_2, \dots, A_{N-2}$, one value per line. As mentioned above, $A_{N-1}$ is always zero, and it does not appear in the file.

## Output data 

The output file `caraibe.out` will contain the maximum number of coins that the first pirate can receive.

## Constraints

$2 \leq N \leq 65\ 000$

$0 \leq A_i < N-i$

## Example

```
caraibe.in
4
1
1
```

```
caraibe.out
9999999999
```

## Explanation

The scheme proposed by the first pirate is: $9999999999$ coins for himself, $1$ coin for the third pirate, and $0$ (zero) for the others. This makes the third pirate agree with the scheme. He reasons as follows: "pirates 2 and 4 do not agree; if I am also against it, the first pirate will be thrown overboard ($A_1 = 1$); then the second pirate will propose the scheme: $9999999999$ coins for himself, $1$ coin for the fourth pirate, and nothing for me; the fourth pirate will agree, hence the scheme will be accepted ($A_2 = 1$); the reason the fourth pirate will agree is that if the second pirate is thrown overboard, I will allocate all the money to myself and he gets nothing ($A_3 = 0$)"