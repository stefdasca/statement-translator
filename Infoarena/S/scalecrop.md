# ScaleCrop

The next set of flyers for the great leader's propaganda comes with significant design changes. Starting from the idea that a picture is worth more than $1000$ words, the great leader wants the flyers of dimensions $w_f$ and $h_f$ to contain his picture, scaled proportionally so as to show as much content as possible without leaving any uncovered space on the flyer (if both dimensions, $w_p$ and $h_p$, of the picture are larger than those of the flyer, the picture's dimensions will be reduced; otherwise, they will be increased).

## Input data

The input file `scalecrop.in` will contain on the first line $4$ integers: $w_f$, $h_f$, $w_p$, and $h_p$ with the meanings described in the statement.

## Output data

The output file `scalecrop.out` will contain on the first line $2$ real numbers: $w_{pn}$ and $h_{pn}$ which represent the new dimensions of the picture.

## Constraints and clarifications

$1 \leq w_f$   
$1 \leq h_f$   
$1 \leq w_p$   
$1 \leq h_p$   
$\leq 1\ 000\ 000\ 000$   

The maximum difference by which the final result can vary from the correct one is $0.001$

Flyers and pictures cannot be rotated.  

It is recommended to use the `double` data type for C / C++ users, and `real` for Pascal users.

## Example

`scalecrop.in`
```
400 400 640 480
``` 
`scalecrop.out`
```
533.33 400.00
```