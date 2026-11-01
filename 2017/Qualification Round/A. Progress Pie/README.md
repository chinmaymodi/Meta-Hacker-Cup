[Meta-Hacker-Cup](../../../) / [2017](../../) / [Qualification Round](../) / A. Progress Pie

# A. Progress Pie

You are given a pie chart described by a radius from the center to a percentage `p` (0 to 100) and a point `(x, y)`. Determine whether the point lies inside the colored region of the pie chart.

The pie chart is centered at `(50, 50)`. The colored region is the section swept clockwise from the positive X-axis to the angle `2*pi*p/100`, i.e., the region between the vectors pointing to `(50, 50)` and `(50 + cos(theta), 50 + sin(theta))` where `theta = 2*pi*p/100`, but rotated so the hand starts at 3 oclock.

## Approach

Compute the angle of the point relative to the center. The colored region covers the range from 0 to theta (the hand angle). A point is in the region if its angle lies in that range, modulo 360 degrees, or equivalently use cross-product orientation: the point must be to the left of the negative X-axis and to the right of the hand, or if the hand is in the lower half (p > 50), the region wraps around including all points to the left of the negative X-axis.

The hand's unit vector is `(cos(a), sin(a))` where `a = 2*pi*p/100`. For a point `(px, py)` relative to center, compute the cross products `c1 = -px` (cross from negative X axis to point) and `c2 = hx*py - hy*px` (cross from hand to point). The point is in the region if `c1 <= 0 <= c2` when the hand is in the upper half (p <= 50), or if it is NOT the case that `c1 > 0 > c2` when the hand is in the lower half (p > 50), which simplifies to "point is left of negative X-axis OR right of hand".

Also check that the point is within the pie radius (50 from center, since the square goes from 0 to 100 and the center is at 50,50). A point outside this circle is outside the pie entirely and should be white.

## Complexity

O(1) time per test case - constant time atan2 and cross-products. Optimal since input must be read and output written.

## Time

~0.020 seconds.

Solved: 1 November 2026.

## Lessons

- Use cross-product orientation instead of atan2 to avoid floating-point angles entirely, which is both faster and more numerically stable.
- The region definition wraps: for p > 50 the band crosses the negative X-axis, so the condition changes: the colored region is "everything except the wedge between hand and negative X". This is why the else branch tests `not (c1 > 0 > c2)`.
- Checking the radius squared (2500) against the distance squared `((x-50)^2 + (y-50)^2)` avoids a sqrt. (Radius = 50, so radius^2 = 2500)
- The solution uses 1-indexed case numbers and outputs "black" or "white" as required.