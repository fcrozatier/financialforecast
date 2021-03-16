Let $x$ be the annual fee of a subscription.

If we invest this much every year with a rate of return $t$, we have the following relation between $x_n$ the capital of year $n$ and $x_{n+1}$ the capital of the next year:

$$
  x_{n+1} = (1+t)x_n + x
$$

The sequence $y_n = x_n + \dfrac{x}{t}$ is a geometric progression with common ratio $1+t$ :

$$
\begin{aligned}
  y_{n+1} &= x_{n+1} + \dfrac{x}{t}\\
          &=(1+t)x_n + x + \dfrac{x}{t}\\
          &= (1+t)(y_n-\dfrac{x}{t})+ x + \dfrac{x}{t}\\
          &= (1+t)y_n
\end{aligned}
$$

It follows that

$$
  y_n=(1+t)^n y_0=(1+t)^n\dfrac{x}{t}
$$

So

$$
\begin{aligned}
  x_n &= y_n-\dfrac{x}{t}\\
      &=(1+t)^n\dfrac{x}{t}-\dfrac{x}{t}\\
      &=\dfrac{x}{t}((1+t)^n-1)
\end{aligned}
$$

After $n$ years, this investment with a rate of return $t$, increased by a fixed amount $x$ every year is worth

$$
  \dfrac{x}{t}((1+t)^n-1)
$$
