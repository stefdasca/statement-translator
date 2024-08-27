Captcha

Bo$$_ul3tz$ from Hackerville needs as many email accounts as possible to send spam. He created a script that automatically fills in the necessary information for creating a new email account, but he encountered the problem of completing the captcha code. On the respective email server, a captcha code is a bmp format image with a 24-bit color depth and no compression, having a width of $64$ pixels and a height of $16$ pixels. The image has a perfectly white background and contains only digits written with various shades of colors. The digits cannot intersect, touch, or rotate and are $5$ × $5$ pixels in size. If we denote a white pixel by $\_$ and a colored pixel by $x$, then the digits look like this:
$x$$$$x$$$$x$$$$x$$$$x$ $\_$$\_$$\_$$\_$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $x$$\_$$\_$$\_$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $x$$$$x$$$$x$$$$x$$$$x$

$x$$\_$$\_$$\_$$x$ $\_$$\_$$\_$$\_$$x$ $\_$$\_$$\_$$\_$$x$ $\_$$\_$$\_$$\_$$x$ $x$$\_$$\_$$\_$$x$ $x$$\_$$\_$$\_$$\_$$x$ $x$$\_$$\_$$\_$$\_$$x$ $\_$$\_$$\_$$\_$$x$ $x$$\_$$\_$$\_$$x$ $x$$\_$$\_$$\_$$x$

$x$$\_$$\_$$\_$$x$ $\_$$\_$$\_$$\_$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $\_$$\_$$\_$$\_$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $x$$$$x$$$$x$$$$x$$$$x$


$x$$\_$$\_$$\_$$x$ $\_$$\_$$\_$$\_$$x$ $x$$\_$$\_$$\_$$\_$$x$ $\_$$\_$$\_$$\_$$x$ $\_$$\_$$\_$$\_$$x$ $x$$\_$$\_$$\_$$\_$$x$ $x$$$$x$$\_$$\_$$\_$$x$ $\_$$\_$$\_$$\_$$x$ $x$$\_$$\_$$\_$$x$ $x$$\_$$\_$$\_$$\_$$x$



$x$$$$x$$$$x$$$$x$$$$x$ $\_$$\_$$\_$$\_$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $\_$$\_$$\_$$\_$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $\_$$\_$$\_$$\_$$x$ $x$$$$x$$$$x$$$$x$$$$x$ $x$$$$x$$$$x$$$$x$$$$x$

To validate each account, Bo$$_ul3tz$ must enter the sum of the numbers in the captcha. Not having the necessary knowledge, he is willing to offer $100$ points for an auxiliary program.

## Task

A picture is a binary file, and to extract the content of a binary file it will be opened with the option $\text{"rb"}$

```
FILE $*f = fopen$("poza.bmp", "rb")$
```

Reading from a binary file is done similarly to reading from a text file. For example, to read an int we will use 
```
$fscanf(f, \text{"%d"}, \&v)$ 
``` 
If you need to read data structures, you can use 
```
$fread ( void $*$ structure, int size, int count, FILE $*$ input\_file );$
```
To declare a single byte it is recommended to use the $char$ data type. 

A bmp $24$bit format file without compression consists of a header having exactly $14$ bytes and the structure

```
typedef struct {
  unsigned short int type;                 $$/* Magic identifier            */$$
  unsigned int size;                       $$/* File size in bytes          */$$
  unsigned short int reserved1, reserved2; 
  unsigned int offset;                     $$/* Offset to image data, bytes */$$
} HEADER;
```

Next is an information area having exactly $40$ bytes and the structure 

```
typedef struct {
  unsigned int size;               $$/* Header size in bytes      */$$
  int width,height;                $$/* Width and height of image */$$
  unsigned short int planes;       $$/* Number of color planes   */$$
  unsigned short int bits;         $$/* Bits per pixel            */$$
  unsigned int compression;        $$/* Compression type          */$$
  unsigned int imagesize;          $$/* Image size in bytes       */$$
  int xresolution,yresolution;     $$/* Pixels per meter          */$$
  unsigned int ncolours;           $$/* Number of colors         */$$
  unsigned int importantcolours;   $$/* Important colors         */$$
} INFOHEADER;
```

Then follows the image in the form of a matrix of bgr pixels, meaning each pixel is represented by a triplet of values, each on one byte, representing the levels of blue, green, and red from which the color of the pixel is composed. A pixel is perfectly white if all $3$ levels have the maximum value ($0xFF$ in hex). 

For the image containing the captcha code there will be exactly $16$$*$$64$ bgr triplets. Note, the image is retained in the pixel matrix starting from the bottom edge and going to the top edge (a vertical flip more precisely).

## Input data

The input file `captcha.in` is a 24bit bmp image without compression, containing the captcha code.

## Output data

The output file `captcha.out` will contain on the first line the sum of the digits in the captcha code.

## Constraints

The height of the image is exactly $16$ pixels.

The width is exactly $64$ pixels. 

## Example

`captcha.in`

`captcha.out`

$12$

$11$