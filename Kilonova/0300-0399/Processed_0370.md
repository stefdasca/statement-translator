After a tough day at school, Alex gets home and goes on Twitch to watch his favorite streamer, xQc. It looks like he's in a 1v1 on Fortnite with another popular streamer, Ninja. Ninja is very skilled at Fortnite and could easily beat xQc. However, luck was on xQc's side as he won the battle. The chat was amazed. Everyone was spamming `W` to celebrate the victory. In case you didn't know, `W` stands for `Win` 🙌.

Now it's Alex's turn to celebrate the victory. He wants to send $t$ messages in the chat, each containing $n$ characters of `W`. Alex wants to find the minimum number of keystrokes required to write the message using only the keyboard. Here is a list of what he can do with the keyboard:
- He can press the **`W`** key. This will add a `W` character at the end of his message.
- He can press the **`BACKSPACE`** key. This will delete the last character in his message.
- Alex can press the **`CTRL`** key. This key is special because it can be combined with exactly one other key among `A`, `C`, or `V`.
  - While the `CTRL` key is pressed, Alex can press the **`A`** key. This will select the text, which can then be used with the `CTRL-C` combination described next.
  - While the `CTRL` key is pressed, he can press the **`C`** key. This will copy the selected text from the `CTRL-A` combination and place it in the clipboard. The clipboard operation is described next.
  - While the `CTRL` key is pressed, Alex can press the **`V`** key. There are 2 cases:
    - When the message contains a selected portion of text, the `CTRL-V` combination will replace the selected text with the last text added to the clipboard. The text will automatically deselect itself.
    - When the message does not contain any selected portion of text, the `CTRL-V` combination will add the last text added to the clipboard at the end of the message.
- Finally, Alex can press the **`ENTER`** key. This will send the written message to the chat. After sending, the text box will completely clear.

Attention, Alex is not allowed to keep any key pressed, except for the `CTRL` key. For more explanations, see the examples.

# Task
Your goal is to create a program that displays, for each number $n$ from the $t$ given numbers, the minimum number of keystrokes necessary to write a message consisting only of $n$ `W` characters. You will send Alex this program so he can use it whenever needed, and he will pay you with 100 ~~lei~~ points.

# Input data
Read from the **console** a number $t$ on the first line.
Each of the next $t$ lines contains a number $n$.

# Output data
Print to the **console** on line $i$ the answer for the $i$-th $n$ read.

# Constraints and clarifications
- $1 \leq n \leq 100\ 000$.
- $1 \leq t \leq 100$.
- **Attention!** The score obtained on a submission is the sum of the maximum scores of the subtasks from all the submissions sent up to that point. If in submission 1 you solved only subtask $3$, and in submission 2 you solved only subtasks $2$ and $4$, then the final score will consist of subtasks $2$, $3$, and $4$.
- The only way to select text is by using the `CTRL-A` key combination.
- Each of the $t$ tests starts with an empty clipboard.
- For unknown reasons, Alex always keeps the Caps Lock key activated.
- Even if you do not have an efficient solution, implement it. The limits in the subtasks may seem very large, but they are actually not!

## Subtask 1 (7 points)
- Alex can write all $t$ messages with a minimum number of keystrokes using only the `W` and `ENTER` keys.

## Subtask 2 (9 points)
- $1 \leq n \leq 65$.
- This is the brute-force task!

## Subtask 3 (14 points)
- Alex doesn't need the `BACKSPACE` key to write all $t$ messages with a minimum number of keystrokes.
- $1 \leq n \leq 13\ 000$.

## Subtask 4 (12 points)
- $1 \leq n \leq 4\ 000$.

## Subtask 5 (21 points)
- $1 \leq n \leq 13\ 000$.

## Subtask 6 (37 points)
- No additional constraints.

# Examples and explanations
`stdin`
```
2
5
15
```
`stdout`
```
6
12
```

$n = 5$. The message can be written using $6$ keystrokes: `W`, `W`, `W`, `W`, `W`, `ENTER`.

$n = 15$. The message can be written using $12$ keystrokes.
First, write the same message as above by pressing $5$ keys (`W`, `W`, `W`, `W`, `W`), then copy this message two more times. For this, keep `CTRL` pressed while pressing the following keys: `A`, `C`, `V`, `V`, `V`. Finally, press `ENTER`. $5 + 1 + 5 + 1 = 12$. This is not the only way to write the message in $12$ keystrokes.