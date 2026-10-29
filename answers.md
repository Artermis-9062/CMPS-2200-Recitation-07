# CMPS 2200 Recitation 07
## Answers

**Name:** Chuong Hoang Pham
_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2) (2 pts)** Write a recurrence for the **work** of this algorithm and solve it. Assume the input is $n$ to compute $F_n$.

  - $W(n) = W(n-1) + W(n-2) + O(1)$

  Costs at level 0: 1

  Costs at level 1: 2

  Costs at level 2: 4

  Cost at level i: $2^{i}$

  The maximum height of the tree is $n$

  So the work is: $W(n) \leq \sum_{i=0}^n 2^i \in O(2^n)$

- **3) (2 pts)** Write a recurrence for the **span** of this algorithm and solve it.

  Assuming the two recursive calls run in parallel, only the longer branch
  contributes to the span:

  $$S(n) = \max(S(n-1), S(n-2)) + O(1)$$

  Since the $n-1$ branch is longer, this simplifies to

  $$S(n) = S(n-1) + O(1).$$

  The critical path has height $n$, so

  $$S(n) = \sum_{i=1}^{n} O(1) = O(n).$$

  Therefore, the span is $\Theta(n)$.

- **4) (1 pt)** Inspecting the `counts` list, what interesting pattern emerges?

  The call counts follow the Fibonacci sequence in reverse. For example, when
  $n=10$, the list is $[34,55,34,21,13,8,5,3,2,1,1]$. This shows that the
  smaller Fibonacci subproblems are recomputed many times, with $F_1$ being
  computed most often.

- **6) (2 pts)** When computing $F_n$, what is the maximum number of times that `fib_top_down(i)` will be called for any value $i$? Based on this, what is the **work** and **span** of this algorithm?

  `fib_top_down(i)` is called at most **two times** for any $i$: once to
  compute and cache $F_i$, and possibly once more from another recursive
  branch, which immediately returns the cached value. Since there are $n+1$
  possible values of $i$, the total work is $\Theta(n)$. The longest dependency
  chain is $F_n,F_{n-1},\ldots,F_1$, so the span is also $\Theta(n)$.

- **8) (2 pts)** When computing $F_n$, what is the maximum number of times that
  $F_i$ will be read from the list for any value $i$? Based on this, what is the **work** and **span** of `fib_bottom_up`?

  Each $F_i$ is read from the list at most **two times**: once to compute
  $F_{i+1}$ and once to compute $F_{i+2}$. Therefore, the loop performs a
  constant amount of work in each of its $n-1$ iterations, giving $\Theta(n)$
  work. Each iteration depends on values produced by earlier iterations, so
  they must occur in order; therefore, the span is also $\Theta(n)$.
