[Meta-Hacker-Cup](../../../) / [2011](../../) / [Round 1C](../) / B. Polynomial Factoring

# B. Polynomial Factoring

Two polynomials are given, $F$ first and $G$ second, each as a degree followed by its $D + 1$ coefficients $a_0$ to $a_D$ in ascending order. Find a polynomial $H$ with integer coefficients such that $G \cdot H = F$, or report that none exists. For example

$$F = 6 + 11x + 4x^2, \qquad G = 3 + 4x, \qquad H = 2 + x$$

## Approach

Plain polynomial long division on coefficient lists held in ascending order.

Each pass divides the current leading coefficient of the remainder by the leading coefficient of $G$, giving the next quotient term $q$, which belongs to $q x^k$ at the current offset $k$. The term is accepted only if re-multiplying reproduces the coefficient exactly, which is what enforces the integer coefficients. Testing that way instead of with a modulo check is also what makes it safe with negative values: floor division can land on the wrong integer for negatives, but any inexact result fails the comparison.

The scaled $G$ is then subtracted from the remainder from the current position downwards, and the leading term, now zero, is dropped. The loop runs until the remainder is shorter than $G$, so the quotient terms come out highest degree first.

Two situations end a case with `no solution`: $G$ has a higher degree than $F$, so the quotient would need a negative degree, and a quotient term that is not an integer. After the loop, the coefficients left in the remainder must all be zero; anything else means $G$ does not divide $F$.

An intermediate leading term can legitimately be zero, which yields a quotient term of zero and lets the loop continue.

The output wants $a_0$ first, so the quotient list is reversed on the way out.

## Complexity

$O(D^2)$ per case, where $D$ is the degree of $F$ and at most 20: at most $D - \deg G + 1$ quotient terms, each costing up to $\deg G + 1$ operations to subtract. Extra space is $O(D)$ for the working remainder.

## Time

~0.003 seconds.

Solved: 17 November 2026.
