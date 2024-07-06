## The Competitional Season Approaches in Liga I Football of Gheorgheni

The championship follows the following rules:
* If the score is tied after 90 minutes of play, the match will continue until one of the teams scores a goal, and this team will be declared the winner. Thus, there will be no matches ending in a draw.
* At the end of a match, the winning team will receive `1` point, and the losing team will lose `1` point.

The competition program consists of `M` matches predetermined by the Football Federation of Gheorgheni. Some teams may not play at all, and some teams might play against each other multiple times, possibly with different outcomes.

Alexandra is very passionate about football, and as a true fan, she wants the championship to be as balanced as possible. Thus, she wonders what the minimum point difference between the team in the first place and the team in the last place in the championship can be after playing the `M` matches. She also wants to determine the winner of each match to achieve this minimum point difference.

# Task
Alexandra is a very busy girl, so she doesn't have time to solve such problems. However, she agreed to tell you how many teams are in the championship, the number of matches to be played, and the teams that will face each other in each match. You must create a program that answers Alexandra's questions.

# Input Data
The file `fotbal.in` contains on the first line two natural numbers `N` and `M`, separated by a space, representing the number of teams in the championship and the number of scheduled matches, respectively. The following `M` lines will contain two numbers `x` and `y`, separated by a space, with the pair on line `i+1` in the file representing the teams that will face each other in match `i`.

# Output Data
The file `fotbal.out` will contain on the first line the minimum point difference between the team in the first place and the team in the last place in the standings.
The following `M` lines will contain one number each, with the number on line `i+1` in the file representing the order number of the winning team in match `i`.

# Constraints and Clarifications
* `1 \ \leq \ N, M \ \leq \ 50000`
* There will be no match where a team plays against itself
* For `5%` of the score `N=2`
* For `15%` of the score `N, M \ \leq \ 20`
* For `50%` of the score `N, M \ \leq \ 2000`
* For determining the minimum difference, `20%` of the score is awarded

# Examples

`fotbal.in`
```
4 2
1 2
3 4
```

`fotbal.out`
```
2
1
3
```

Explanations
---

The first match is won by team `1`, and the second match is won by team `3`. At the end of the championship, teams `1` and `3` will have `1` point each, while teams `2` and `4` will have `-1` points.