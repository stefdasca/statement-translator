Lara is trapped in a cave with a complex system of rooms. She suspects that the exit might be in one of the `N` rooms, but she isn't sure if the cave has an exit or in which room it could be. To enter each room, she needs a key. Moreover, for some rooms to be accessible, she must have already unlocked other rooms. Once a key is inserted into a door, if the room is indeed the exit, Lara will be able to leave the cave **at that moment**; otherwise, the room will open **the next day**.

Looking more closely through the cave, Lara discovers that when the sun's rays hit a certain position, `K` keys appear near the statues in the cave for a very short period. She is not obligated to take all the keys in a day, but **if she takes a key, she must use it on the same day** to not upset the spirits of the cave.

Determined to uncover the mysteries of the world, she makes an escape plan. Help her find the **minimum duration** of the plan (in days) and the rooms she unlocks each day **in the worst case** for her.

# Input data
The first line contains `N` - the number of rooms, `M`, `K` - the number of keys available daily. The next `M` lines contain two numbers `x y` meaning that room `x` must first be unlocked to open room `y`.

# Output data
The first line will contain the minimum duration of the plan. On the following lines, the rooms opened on day `i`, separated by spaces, will be printed.

# Constraints and clarifications
* `1 \leq N \leq 20`
* `0 \leq M \leq N(N-1)/2`
* It is guaranteed that there is always a solution
* Any correct solution will be accepted
* For `60` points `1 \leq N \leq 15`
* `60%` of the score is awarded just for the number of days

# Example

`stdin`
```
9 9 3
1 2
3 2
4 8
4 5
8 2
5 2
6 7
6 9
4 2
```

`stdout`
```
3
1 3 4
5 6 8
2 7 9
```

Explanation
---

The room system plan looks like this:
\
~[plan.png]
\
On the first day, she opens rooms `1, 3, 4`. She cannot open more rooms because she only has `3` keys. Room `4` must be opened before (on one of the previous days) room `2`, so she cannot open room `2`. On the second day, she opens rooms `5, 6, 8`, and on the third day the remaining rooms.