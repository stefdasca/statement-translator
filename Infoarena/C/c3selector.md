# C3selector

Probably everyone has heard about web pages and seen HTML tags. At a software company in Cluj where algorithms meet technology, fictitiously named AlgoTech, one of the interview questions asks candidates to implement a CSS selector. An HTML page is considered valid if it meets the following conditions:
- It has a single parent tag;
- All other tags are direct or indirect children of the parent tag;
- All tags open with `<tagname>` and close with `</tagname>`;
- A tag can have any number of children, having the form: `<x><y></y></y><z></z></x>`;
- A tag can have an additional class attribute, having the form: `<tagname class="classx classx">`;
- It is possible for some terminal tags (those without children) to contain text, having the form: `<x><y>text</y><z><y><x>another text</x></y></z></x>`;
- The same tag can appear multiple times, possibly with different classes, but always closes correctly;
- A class can appear multiple times, possibly on different tags.

A CSS selector is a pattern used to identify tags in HTML. It can have the following forms:
- `div` = selects all tags with the name div;
- `div p` = selects all p tags that are inside a div tag;
- `.intro` = selects all tags that have the class intro;
- `.intro.layout` = selects all tags that have both the class intro and the class layout (note: more than two classes can appear);
- `.layout .header` = selects all tags that have the class header and are inside a tag that has the class layout (note: there is a space between the two classes);
- `p.big` = selects all p tags that have the class big;
- `p .big` = selects all tags with the class big that are inside a p tag (note: there is a space between the tag and the class).

Based on the above forms, a CSS selector can take all their combinations, having any form.

## Example:

```
div.a p.q.b i.icon.q.red
x y z.x.y.z.a .a.b.c d
```

Given $T$ tests, each having a valid HTML page and $Q$ selectors, determine how many distinct tags each selector can identify.

## Input data

The input file `c3selector.in` contains on the first line the number $T$, and on the following lines are described the $T$ tests. Each test occupies multiple lines, as follows:
- One line containing the value $Q$;
- One line containing a character string representing a valid HTML;
- $Q$ lines, each containing a character string representing a CSS selector.

## Output data

In the output file `c3selector.out` you must print several lines. Each line contains a single number, representing the answer to one selector from the input file. The answers should appear in the order of the questions in the input file.

## Constraints

$T \leq 5$

$1 \leq Q \leq 1000$

The HTML cannot have more than $100$ tags

The length of the HTML cannot be more than $10\,000$ characters

The length of a CSS selector cannot be more than $500$ characters

The name of a tag cannot be more than $10$ characters long

The name of a class cannot be more than $10$ characters long

The HTML can contain only: lowercase English alphabet letters, `<`, `>`, `/`, `=`, `"`, or spaces

## Example

```
c3selector.in
```
```
2
4
<div class="a"><span class="q w">text</span><p class="q b"><i class="icon q red"></i></p></div>
div p.b
.a .q
div.a p.q.b i.icon.q.red
div span
10
<div class="a"><ul><li class="a"></li><li class="b"></li><li></li></ul><span class="q w">text</span><p class="q b"><i class="icon q red"></i></p></div>
div.a p.q.b
i.icon.q.red
div p.b
.a .q
div span ul li
div li .a
.a .a .a .a ul li.a ul span.w
```
```
c3selector.out
```
```
1
3
1
1
1
1
3
1
3
3
2
1
1
0
```