# Background

> "I got lost in the labyrinth for twenty minutes before finally entering the great hall. The walls were covered with mirrors, and here, small balconies hung under the ceiling where monsters stood. I had never seen anything like it. They had large, bulging eyes, long tentacles gripping shotguns firmly, and scaly bodies resembling those of fish-human hybrids. The monsters shot at me from the balconies, and I shot back using my Chu Ko Nu. The shot shattered three mirrors, filling the room with a silvery smoke. The bullets hit my armor, knocking me to the ground. As I fell, I managed to shoot an arrow and got up as quickly as I fell, spinning on my back as I did in my youth while break dancing, all while shooting three more times. Three mirrors, three mirrors, three mirrors..."
\- Quote by Sergey Lukyanenko, "The Labyrinth of Reflections"

# Task
Chu Ko Nu destroys three adjacent balconies in one shot. (The $N$-th balcony is adjacent to the first). After shooting, the monsters that survive deal damage to Leonid (the main hero of the novel) — one unit per monster. A new shot follows, and so on until all the monsters perish. It is necessary to define the minimum amount of damage that Leonid can receive.

# Input data
The first line contains the integer $N$, the number of balconies where monsters have taken circular defense. The second line contains $N$ integers, the number of monsters on each balcony.

# Output data
Print the minimum damage with which Leonid can escape after killing all the monsters.

# Constraints and clarifications
- $3 \leq N \leq 20$;
- $1 \leq$ number of monsters on each balcony $ \leq 1\ 000$;
- The first balcony is adjacent to the last;
- If you choose to eliminate monsters from 3 adjacent balconies and one or two of those balconies no longer contain monsters, obviously, the monsters will only be eliminated from the balcony/balconies where they still remain.

# Example
`stdin`
```
7
3 4 2 2 1 4 1
```

`stdout`
```
9
```

## Explanation
The optimal solution is to eliminate the monsters from the first 3 balconies, meaning that the monsters from the remaining balconies will shoot at Leonid, i.e., $2+1+4+1 = 8$, and then the next 3 balconies will be eliminated, meaning that damage will come only from the last balcony, adding $1$ to the total damage. The next step will be to eliminate the last balcony, leaving a total damage of $9$.