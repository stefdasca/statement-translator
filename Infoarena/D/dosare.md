# Folders

Unlike his friends - Miruna and Algorel - who waste their time with balls and beads, Haralambie is much more practical on the brink of Christmas: he has decided to optimize his file system. Haralambie's folders on his computer are organized hierarchically. In the main folder, there are several subfolders, which in turn contain other subfolders, and so on. He only uses the keyboard to navigate through them, so the order in which subfolders are in a folder is very important. To enter a subfolder of a folder, Haralambie must press the down navigation key (down arrow) until he is above the desired subfolder. For example, if in the main folder, numbered $1$, there are, in this order, the folders $2$, $3$, and $4$, and in folder $3$ are the folders $5$, $6$, and $7$, to access folder $7$, Haralambie must press the $\text{ENTER}$ key to enter $1$, press the down arrow once to reach $3$, again $\text{ENTER}$ to enter $3$, then twice down arrow, and once more $\text{ENTER}$ to enter $7$, so a total of $6$ key presses. Haralambie knows for each folder how many times he will need to access that folder and promises to reward you with colored balls if you order the subfolders in folders in such a way that the total number of key presses is minimized. On each access to a folder, consider that Haralambie will start from the main folder.

## Input data

The input file `dosare.in` contains on the first line the total number of folders, $N$. On the next $N - 1$ lines there is information regarding the hierarchy of the folder system. On line $i$ contains the parent folder of folder $i$. The main folder has the number $1$. On the last line of the input file, there are $N$ integers representing the number of times each folder is accessed.

## Output data

The output file `dosare.out` should contain on a single line the minimum total number of key presses.

## Constraints and clarifications

$1 \leq N \leq 16000$

$1 \leq A_i \leq 1000000$

For $40\%$ of the tests

$1 \leq N \leq 333$

## Example

`dosare.in`             `dosare.out`

```
9    
1    
1    
1    
3    
3    
3    
4    
4    
1 1 1 1 1 1 1 1 1    
31    
```

## Explanation

Folder $1$ contains folders $2$, $3$, and $4$. In folder $3$ we have folders $5$, $6$, and $7$, and in folder $4$ we have folders $8$ and $9$. We can arrange the folders in the following way: in folder $3$ we will arrange the subfolders in the order $5$, $6$, $7$, in folder $4$ in the order $8$, $9$, and in folder $1$ in the order $3$, $4$, $2$. According to this arrangement, the total score will be: $1*1 + 1*4 + 1*2 + 1*3 + 1*3 + 1*4 + 1*5 + 1*4 + 1*5 = 31$. Any other arrangement will result in a total number at least equal to $31$.