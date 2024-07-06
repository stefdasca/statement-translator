Andrei, a young man with a real literary talent, will recite his latest poem at the next meeting of the literary club. Andrei has one problem: the poem has too many lines and he is aware that no one will have the patience to listen to it all the way through. Since he doesn't have time to rewrite it, Andrei decided to remove lines from the poem. However, he won't remove lines randomly, but will choose them so that the artistic value of the poem does not decrease. After long deliberations, the poet discovered the removal criterion: a line can be removed only if there is a line immediately before it (let's denote it $p$), and immediately after it, there is another line (let's denote it $u$) so that the lines $p$ and $u$ have _musicality_ strictly greater than $6$. Don't ask why $6$, only Andrei knows why. What does the poet mean by the _musicality_ of two lines?

Let the lines be: $\\text{\\underline{alin}uta\\underline{ e}st\\underline{e }a\\underline{c}asa}$ and $\\text{\\underline{alin }m\\underline{e}rg\\underline{e c}u noi}$. _Musicality_ is equal to $9$, that is exactly the number of underlined characters: $\\text{\\underline{alin ee c}}$. Therefore, _musicality_ represents the size of the longest sequence of characters that appear in the given order in both the first line and the second line, not necessarily in consecutive positions.

Thus, the line that is preceded and followed by these two can be removed, because $9 > 6$. Obviously, if we remove the line existing between $p$ and $u$, the lines $p$ and $u$ become consecutive.

# Task

Determine the maximum number of lines that can be removed, respecting the criterion established by the poet.

# Input data

The input file `randuri.in` contains the poem's lines, one per line.

# Output data

The output file `randuri.out` will contain a single line which will contain the maximum number of lines that can be removed, respecting the criterion established by the poet.

# Constraints and clarifications

* The lines are formed from a maximum of $100$ characters with the $\\text{ASCII} < 127$ code.
* There are no empty lines.
* The input file contains at most $100$ lines.
* Any line in the input file ends with a newline mark (\_newline\_). The \_newline\_ character will not be considered as part of the line.

# Example

`randuri.in`
```
Te-nalta pana-n nori
Tot mai sus,
Tot mai departe
Ca siragul de cocori
```

`randuri.out`
```
2
```

## Explanation

The musicality of the lines:

$\\text{\\underline{T}e-nal\\underline{ta pa}na-n no\\underline{r}i}$ \\
$\\text{\\underline{T}o\\underline{t} m\\underline{a}i\\underline{ }de\\underline{par}te}$

is $7$ (see the underlined characters).

Therefore, the line

$\\text{Tot mai sus,}$

can be removed. After removing this line, we get:

$\\text{Te-nalta pana-n nori}$ \\
$\\text{Tot mai departe}$ \\
$\\text{Ca siragul de cocori}$

The musicality of the lines:

$\\text{Te-n\\underline{al}ta\\underline{ }pana-n\\underline{ }n\\underline{ori}}$ \\
$\\text{C\\underline{a} siragu\\underline{l }de\\underline{ }coc\\underline{ori}}$

is $7$. Therefore, the line:

$\\text{Tot mai departe}$

can also be removed.