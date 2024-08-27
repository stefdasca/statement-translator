# Logic2

The Island of Logic has three types of inhabitants: divine beings, who always tell the truth, evil beings, who always lie, and humans, who tell the truth during the day and lie at night. Each inhabitant of the island can recognize the type of any other inhabitant. A sociologist wants to visit the island. Because he cannot distinguish the three types of inhabitants just by appearance, he asks you for an analyzer that can deduce facts from conversations with the inhabitants. The facts that interest him are whether it is day or night and what type his interlocutors are.

## Input data

The input file $logic2.in$ contains a conversation. Each line of the file contains an assertion made by an inhabitant. All lines start with the name of the interlocutor (which is an uppercase letter $A$, $B$, $C$, $D$, or $E$) followed by ":" and then a statement in the form: I [do not] lie. I [am not] {divine | human | evil}. $X$ [does not] lie. $X$ [is not] {divine | human | evil}. It is {day | night}. Words enclosed in square brackets may or may not appear in the statement. Of the words enclosed in curly brackets, exactly one word appears in the statement. A conversation can have up to $50$ statements.

## Output data

The file $logic2.out$ will contain everything that can be deduced in the following form: $X$ is {divine | evil | human}. It is {day | night}. $X$ is replaced with the name of the interlocutor. The facts must be given in alphabetical order, sorted by the names of the interlocutors, and then stating whether it is day or night. If nothing can be deduced, "Nu se poate deduce nimic." (Nothing can be deduced.) will be printed, and if the conversation does not follow the above rules, "Imposibil." (Impossible.) will be printed.

## Example

`logic2.in`
```
A: B este om.
B: A este malefic.
A: B este malefic
```
`logic2.out`
```
A este malefic.
B este divin.
```

## Explanation

It is evident that $A$ is lying because his two statements contradict each other. Therefore, $B$ cannot be human or evil; thus, he must be divine. $B$ always tells the truth, so $A$ must be evil.