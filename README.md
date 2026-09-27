# LeetCode 302 - Smallest Rectangle Enclosing Black Pixels

## Problem Statement

Given an image represented by a binary matrix containing `'0'` and `'1'`, where `'1'` represents a black pixel, find the area of the smallest rectangle that encloses all black pixels.

The given coordinates `(x, y)` represent a black pixel.

## Example

### Input

```text
image = [
  ["0","0","1","0"],
  ["0","1","1","0"],
  ["0","1","0","0"]
]
x = 0
y = 2
```

### Output

```text
6
```

## Approach

Traverse the entire matrix and find:

* Minimum row containing a black pixel
* Maximum row containing a black pixel
* Minimum column containing a black pixel
* Maximum column containing a black pixel

The rectangle area is calculated using these boundaries.

## Algorithm

1. Initialize minimum and maximum row and column values.
2. Traverse every cell in the matrix.
3. If the cell contains `'1'`, update the boundaries.
4. Calculate the height of the rectangle.
5. Calculate the width of the rectangle.
6. Return `height × width`.

## Time Complexity

`O(m × n)`

## Space Complexity

`O(1)`

## Key Concepts

* Matrix Traversal
* Binary Matrix
* Minimum and Maximum Boundaries
* Rectangle Area

## Language

Python

## LeetCode Details

* **Problem:** 302
* **Title:** Smallest Rectangle Enclosing Black Pixels
* **Difficulty:** Hard

## Author

**T. Nandhini Reddy**

GitHub: `242t605119-dotcom`
