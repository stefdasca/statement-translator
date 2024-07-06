A string consisting of digits needs to be typed in one or more sessions.

There are two keyboards: keyboard `A` which contains keys with all combinations of exactly two digits: key `00`, key `01, 02, …, 98, 99` and keyboard `B` which contains keys with all combinations of exactly three digits: key `000`, key `001, …, 998, 999`. The digits will be entered in one or more sessions, and only one keyboard can be used per session. Due to an emergency ordinance, if a key combination has been entered with one of the keyboards in the current session and while continuing the session, this combination can again be entered, it is necessary to continue the session at least until it is entered again. If we enter other keys until then, we must continue the session until we enter their last occurrence.

Thus, if the string $255222255\underline{25}7$ is started using keyboard `A`, it will necessarily be written in one session as `25 52 22 25 52`. We are forced to type until the last occurrence of the key `25` in the current session, and when using the key `52` we are forced to continue until its last occurrence. Notice that the digits on the underlined positions are also `2` and `5`, but they do not form a key that can be pressed in the current session. Since we require the maximum number of sessions, a new session will start in which `57` will be written alone.

# Task
Knowing the total number of digits and the sequence of digits forming the string, determine a way to split the text so that it can be written in a maximum number of sessions.

# Input data
From the file `text.in`:
- the first line contains a natural number `N` representing the number of digits
- the next line contains `N` digits, written without spaces, representing the string to be typed

# Output data
In the file `text.out`, print:
- on the first line `S`, representing the maximum number of sessions
- on each of the next `S` lines, two numbers `p, k`, separated by a space, each such pair describing, in the order they appear in the text, the sequences typed in sessions: $p_i$ – the position in the given digit string where session `i` starts and $k_i$ – the type of keyboard used in session `i` (`2` for keyboard `A`, `3` for keyboard `B`)

# Constraints and clarifications
* `3 \leq N \leq 1\ 000\ 000`
* the digits in the sequence are between `0` and `9`
* the proposed tests ensure the existence of a solution for the given task
* if there are multiple solutions, any of them will be provided
* for the correct number of sessions, without the lines describing the complete and correct solution, `50%` of the score is awarded

# Examples

`text.in`
```
15
233323333333322
```

`text.out`
```
5
1 3
4 2
6 3
12 2
14 2
```
Explanation
---

The string can be written in a maximum of `5` sessions as follows: `233` `32` `333` `333` `33` `22`
- the first session starts with the first digit and uses keyboard `B` (with keys of `3` digits)
- the next session starts at the `3`-rd digit and uses keyboard `A`
- the third session starts at the `6`-th digit and uses keyboard `B`
- the fourth session starts at the `12`-th digit and uses keyboard `A`
- the last session starts at the `14`-th digit and uses keyboard `A`

`text.in`
```
8
46234623
```

`text.out`
```
3
1 3
4 2
6 3
```

Explanation
---

The solution corresponds to the sequences `462` `34` `623`
