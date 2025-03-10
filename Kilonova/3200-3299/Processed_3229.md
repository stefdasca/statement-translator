# Task

As every year, a ball is organized at the Vienna Opera. This year, $N$ young men and $N$ young women are invited, and all of them must dance the first waltz of the evening on a circular floor. The $2N$ guests stand around the edge of the floor, along with the MC (Master of Ceremonies) of the ball, the Chancellor of Austria.

Since the waltz is danced in pairs, the young men must choose their dance partners according to the following rule:

* Starting with the closest person to him in the counterclockwise direction and continuing in the same direction, the Chancellor will call, in turn, the names of the young men.
* When a man hears his name, he will move forward along the edge of the floor, counterclockwise, until he meets the first woman who has not been invited to waltz and invites her.
* Since the women are not very picky, they never refuse [The Invitation to the Waltz](https://www.goodreads.com/book/show/1161134.Invita_ia_la_vals).
* After the woman accepts, the newly formed pair moves towards the center of the floor, after which a new name is called and the process repeats.

The Chancellor wants to know the number of men who will pass in front of him on their way to find a partner, and he asks for your help.

# Input data

The first line contains a natural number $N$, as in the statement. The following line contains $N$ natural numbers $F_i$, describing the positions of the $N$ women. The third line contains $N$ natural numbers $B_i$, describing the positions of the $N$ men. Positions are defined by the distance that the Chancellor would have to walk counterclockwise to reach him/her.

# Output data

Print a single natural number, the answer to the Chancellor's question.

# Constraints and clarifications

* $1 \leq N \leq 200 \ 000$;
* $1 \leq F_i, B_i \leq 10^8$;
* The Chancellor does not move during the formation of pairs;
* No guest stands exactly in front of the Chancellor, and there are no two guests at the same position.
* The dance floor of the Vienna Opera is enormous, $10^8+1$ in length;
* For tests worth $15$ points, $N \le 15$;
* For other tests worth $25$ points, $N \le 1\ 000$;
* For other tests worth $60$ points, there are no additional constraints.

# Example

`stdin`
```
3
2 7 11 
3 12 1
```

`stdout`
```
1
```

## Explanation

This is the initial configuration on the dance floor. The drawing is not to scale, for simplicity.

~[vals_1.png|align=center|width=40%]

The first young man to move is at distance $1$, who will dance with the woman at distance $2$, as she is the first in his path. 

~[vals_2.png|align=center|width=40%]

After him, the young man at distance $3$ leaves, who will first meet the woman at distance $7$ and will dance with her. 

~[vals_3.png|align=center|width=40%]

When the young man at distance $12$ leaves, only the woman at distance $11$ remains available, so he will invite her to dance, being forced to pass in front of the Chancellor (who stands at distance $0$ from himself).

He is the only one who does this, so the final answer is $1$.