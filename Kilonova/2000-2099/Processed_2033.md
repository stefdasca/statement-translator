While Henry, Hetty, and Harry sleep in their homes in England, Charles has gone to continue his cleaning — in the casinos of Las Vegas. He will spend $10$ days in that city, trying to win as much money as possible at the Blackjack table. In the casinos frequented by Charles, the game of Blackjack is played according to the following rules:

# Game Process
Each of the $10$ evenings, Charles leaves home with an amount of money $money$ and sits at a table where only the dealer (the one dealing the cards) is present. The game proceeds in stages called hands. A hand proceeds like this:
1. Charles bets an amount of money $bet$ on the current hand. Naturally, Charles is not allowed to bet more money than he has at that moment.
2. The dealer puts a card face-up on the table — this is the dealer's first card.
3. Charles receives two cards.
4. As long as the sum of the values of Charles's cards (we will denote this sum by $C$) does not exceed $21$, Charles has the option to ask for another card. This step repeats until Charles announces he does not want any more cards. **Charles is obliged to announce that he does not want any more cards if $C$ has exceeded $21**.
5. The dealer draws cards from the deck until the sum of the dealer's card values (let’s denote this sum with $D$) exceeds $16$.
6. Charles receives back money according to the outcome of the hand as follows:
   * $2 \times bet$ – if $C > D$ and $C \leq 21$, or if $C \leq 21$ and $D > 21$.
   * $bet$ – if $C = D$ and $C \leq 21$, or if $C > 21$ and $D > 21$.
   * $0$ – if $C < D$ and $D \leq 21$, or if $C > 21$ and $D \leq 21$.

# The Cards
In the game of Blackjack, cards are used from $nPacks$ standard decks of $52$ cards ($4$ cards for each number from $2$ to $10$, plus $4$ Aces $(A)$, $4$ Kings $(K)$, $4$ Queens $(Q)$, and $4$ Jacks $(J)$). Numbered cards have a value equal to their number, Kings, Queens, and Jacks have a value of $10$, and an Ace can take either the value of $1$ or $11$ (at the player’s discretion).

The sum of the values of a set of cards is defined as the highest sum that can be formed from the values of those cards such that it does not exceed $21$. If this is not possible, the sum of the values of the set of cards is defined as the lowest sum that can be formed from their values. Examples: the sum of the set $(A, J)$ is $21$, the set $(A, A)$ is $12$ (one Ace takes the value $1$, the other $11$), the set $(A, 9, 8)$ is $18$, and the set $(A, 10, 9, 8)$ is $28$.

At the beginning of the game, cards are shuffled and placed in a stack face-down. During the game, cards are dealt from the top of the stack. Once used for a hand, cards will not be used again until a reshuffle. After a hand is finished and there are fewer than $45$ cards left in the stack, all cards are reshuffled. The game for that evening continues until the cards are shuffled $T$ times.

# Task
After $10$ nights of intense play, Charles returned home with a considerable profit. Can you achieve the same success as Charles? Write a program that substitutes for Charles in a game of Blackjack played according to the rules described above, with the goal of winning as much money as possible by the end of the game.

# Interaction

To solve this problem, the following $3$ functions need to exist in your source code:

```cpp
void startGame(int money, int nPacks);
```

This function is called exactly $10$ times, indicating that the player starts a new game. It receives as parameters the amount of money $money$ with which the participant starts playing **in that game** and the number $nPacks$ of decks that will be used for the game.

```cpp
void playHand();
```

This function will be called each time a hand is played. Interaction between the committee’s program and this function is performed according to the steps of a hand described in the statement, namely:
1. The contestant calls the function
    ```cpp
    int placeBet(int bet)
    ```
    to bet an amount of money bet on the current hand. The function returns the amount of money the contestant has left after making the bet.
2. The contestant calls the function once
    ```cpp
    int getDealerCard()
    ```
    which returns the value of the dealer's first card.
3. The contestant calls the function
    ```cpp
    int getCard()
    ```
    twice to find out the values of their first two cards. The function returns the value of a card received by the contestant.
4. As long as the sum $C$ of the values of their cards does not exceed $21$, the contestant may call `getCard` again to request another card. The function returns the value of the card received. This step repeats until the contestant calls the function
    ```cpp
    void stand()
    ```
    to announce they do not want any more cards. **Attention! In case after the contestant receives a card, the sum $C$ exceeds $21$, the contestant is obliged to call `stand`**.
5. To find out the cards drawn by the dealer from the deck, the contestant repeatedly calls
    ```cpp
    int getOutcome()
    ```
    each call returning the value of a card drawn by the dealer or $0$ if the dealer has stopped drawing cards. **After the function `getOutcome` returns 0 it must not be called again for the current hand**. Remember that the dealer draws cards from the deck until the sum of the values of his cards (denote it with $D$) exceeds $16$.
6. The contestant calls once
    ```cpp
    int cashIn()
    ```
    to find out how much money they receive back. The function returns the amount of money received by the contestant after playing a hand. Remember that this amount is:
    * $2 \times bet$ – if $C > D$ and $C \leq 21$, or if $C \leq 21$ and $D > 21$.
    * $bet$ – if $C = D$ and $C \leq 21$, or if $C > 21$ and $D > 21$.
    * $0$ – if $C < D$ and $D \leq 21$, or if $C > 21$ and $D \leq 21$.

To summarize, the order in which the player calls the functions for a hand is: `placeBet(int bet)` $\rightarrow$  `getDealerCard()` $\rightarrow$ `getCard()` $\times 2 \rightarrow$ `getCard()` $\times$ (as many times as the player wants, up to a maximum until $21$ is exceeded) $\rightarrow$ `stand()` $\rightarrow$ `getOutcome()` $ \times $  (until it returns $0$) $\rightarrow$ `cashIn()`.

```cpp
void reshuffle();
```

This function is called after a hand ends to signal to the contestant that all cards used in previous hands have been put back into the stack and the stack has been reshuffled.

# Constraints and clarifications

* $10 \leq nPacks \leq 20$
* $20 \ 000 \leq money \leq 100 \ 000$
* $200 \leq T \leq 500$
* For any call of the function `placeBet(int bet)`, $0 \leq bet \leq m$, where $m$ represents the amount of money the contestant has at that moment.
* A call of the functions `getCard`, `getDealerCard`, or `getOutcome` will return $11$ if the returned card is an Ace, and $10$ if the returned card is a $10$, a King, a Queen, or a Jack.
* If after a hand ends the contestant has at least $1 \ 000 \ 000 \ 000$ money, the game ends and the contestant receives the maximum score on that test.
* The contestant's score will be determined as follows: the contestant's source code is run and the $10$ amounts of money with which the contestant ends each game are taken and sorted in descending order. The first two and the last two from this sequence are eliminated and $S_{contestant}$ is set as the sum of the values in this sequence. Similarly, for the committee's source code $S_{committee}$ is defined. Define $ratio = S_{contestant}/S_{committee}$. The contestant's score on a test is $round(ratio^{5} \times 10)$.

# Example of interaction

`grader`: `startGame(20000, 10)`
`grader`: `playHand()`
`contestant`: `placeBet(100)`
`grader`: `return 19900`
`contestant`: `getDealerCard()`
`grader`: `return 9`
`contestant`: `getCard()`
`grader`: `return 11`
`contestant`: `getCard()`
`grader`: `return 10`
`contestant`: `cashIn()`
`grader`: `return 200`
`contestant`: `getOutcome()`
`grader`: `return 5`
`contestant`: `getOutcome()`
`grader`: `return 6`
`contestant`: `getOutcome()`
`grader`: `return 0`
\
`grader`: `startGame(2000, 10)`
`grader`: `playHand()`
`contestant`: `placeBet(100)`
`grader`: `return 1900`
`contestant`: `getDealerCard()`
`grader`: `return 10`
`contestant`: `getCard()`
`grader`: `return 10`
`contestant`: `getCard()`
`grader`: `return 9`
`contestant`: `getCard()`
`grader`: `return 4`
`contestant`: `stand()`
`contestant`: `getOutcome()`
`grader`: `return 10`
`contestant`: `getOutcome()`
`grader`: `return 0`
`contestant`: `cashIn()`
`grader`: `return 0`
\
`grader`: `reshuffle()`

## Explanation

The function `startGame` is called with parameters $nPacks = 10$, meaning that the stack will contain the cards of $10$ standard decks, and $money = 20 \ 000$, representing the initial amount of money the contestant has.

A hand begins by signaling the contestant.

The contestant bets $100$ that they will win the current hand.

The dealer received a $9$.

The contestant calls `getCard` twice to receive the initial $2$ cards. They receive an Ace and a $10$. The sum of the contestant's cards is $21$.

The contestant announces that they do not want more cards.

The dealer receives a $5$ and a $6$. The sum of the dealer's cards is $20$.

The contestant has won the hand and receives $200$ of money. Now they have $2 \ 100$ money.

The second evening of play begins.

The contestant asks for an additional card after the initial $2$. This is a $4$ and makes the sum $23$.

The contestant is obliged to call `stand` now.

The contestant is signaled that the deck has been reshuffled.
