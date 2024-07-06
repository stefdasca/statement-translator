## Task

In C++, there are two types of comments:

1. Single-line comments:
    ```js
    text1 // comment1
    text2 // comment2
    ```
2. Multi-line comments:
    ```js
    text1 /* comment1
    comment2
    comment3
    */ text2
    text3
    ```
Single-line comments comment out all characters until the end of the line, starting with the sequence `"//"`.

Similarly, multi-line comments comment out all characters between the sequences `"/*"` and `"*/"`.

Also, the sequences `"/*"` and `"*/"` within a single-line comment, and the sequences `"//"` within a multi-line comment will be ignored:
```js
// /*
text1
*/
 /*
 // comment1 */
text2
*/
```

Given a text file with multiple lines containing lowercase English alphabet letters, digits, the characters `'/'` and `'*'`, and spaces.

Remove all comments from the given file.

# Input data

The input file `nocomments.in` consists of multiple lines containing lowercase English alphabet letters, digits, the characters `'/'` and `'*'`, and spaces.

# Output data

The output file `nocomments.out` will contain only the uncommented characters from `nocomments.in`.

**Any answer that correctly identifies the uncommented words, regardless of the spaces between them, is considered correct.** A word is a sequence of letters, digits, `'/'`, and `'*'` delimited by spaces.

# Constraints and clarifications
- $1 \le$ number of characters in the input file $ \le 10^5+1$;
- There is no multi-line comment that is not terminated by the sequence "`*/`";
- The tests for this problem **are not** grouped;
- For $40$ points, the input file has only one line;
- For $20$ points, there are only single-line comments;
- For $20$ points, there are only multi-line comments;
- For the remaining $20$ points, no additional constraints are imposed.

# Example

`nocomments.in`
```js
text0
// text1
/*
text2
*/
text3 / text4
//*
text5
*/
 /*/*
 //text6
text7
*//
text8
*/
 /**text9*/
 ///text10
/*
 /*/ text11 */
```

`nocomments.out`
```
text0
text3 / text4
text5
*/
 /
text8
*/
text11 */
```