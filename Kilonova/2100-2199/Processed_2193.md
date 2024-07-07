
**ATTENTION:** This problem is worth $150$ points. In "submissions," the maximum score is rescaled to $100$ points, but the real score will be visible on the *[leaderboard](https://kilonova.ro/contests/179/leaderboard)*.

You have managed to obtain several emails of the CEO of Chert And, Certes Adrei, sent to his friends: Elefantul Marcici and Lexy. Unfortunately, he got corrupted. If you manage to reveal the content of the email, the megacorporation will be forced to disclose more information about the farm in Romania.

~[andrei_C1.png|align=center|width=10cm]

$$
\text{fig 1. CEO of Chert And}
$$

# Problem

In the file `corrupt.txt` attached to this problem (on the right of the page under "Attachments") you will find the content of the email.

The task is output only, so your submission must be **only a text of words**, corresponding to the given one. More precisely, each word must be converted to its correct form, as in the original email, they may have letters permuted in an incoherent order.

# Clarifications

- **ATTENTION: The original text is in *English***. All given words are in *lower caps*, and there are no punctuation marks, numbers, or other symbols besides the $26$ Latin letters.
- The number of words in your output must be equal to the number of words in the given corrupt email. *Otherwise, the score will be null.*

# Scoring

We define: $\\text{accuracy} = \\frac{\\text{correct}}{\\text{total}}$, where $correct$ is the number of correctly matched words, and $total$ is the total number of words in the email.
Then, the score you will receive for the problem will be: $accuracy \cdot 150$. Additionally:

- If $\\text{accuracy} \\ge 0.2$, you will receive a batch of coordinates for **META-TASK**.
- If $\\text{accuracy} \\ge 0.5$, you will receive two batches of coordinates for **META-TASK**.
- If $\\text{accuracy} \\ge 0.8$, you will receive three batches of coordinates for **META-TASK**.

**ATTENTION:** The batches are received as a link to *Google Drive* in the evaluation test verdict.

# Example

```
... japna mhtgi sootb porntciitetso niemnttse ni hte us ...
```
```
... japan might bruh protectionist sentiment in the us ...
```

Notice that in this case $\\text{accuracy} = \\frac{7}{8}$, as the correspondent of "sootb" was "boost", **NOT** "bruh". Other than that, all words are matched correctly.
```
