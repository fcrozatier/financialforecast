Let $s$ be the annual salary, $e$ the savings ratio, $t$ the rate of return of the investment and $K$ the initial capital.

The relation between capitals $K_n$ and $K_{n+1}$ corresponding to year $n$ and $n+1$ is:

$$
  K_{n+1}=(1+t)K_n+es
$$

Note that the sequence $a_n=K_n+\dfrac{es}{t}$ is geometric with common ratio $(1+t)$:

$$
\begin{aligned}
a_{n+1} &= K_{n+1}+\dfrac{es}{t}\\
        &=(1+t)K_n+es+\dfrac{es}{t}\\
        &=(1+t)(a_n-\dfrac{es}{t})+es+\dfrac{es}{t}\\
        &=(1+t)a_n
\end{aligned}
$$

Hence

$$
\begin{aligned}
  a_n &= (1+t)^n a_0\\
      &= (1+t)^n(K+\dfrac{es}{t})
\end{aligned}
$$

It follows that

$$
  K_n = (1+t)^n (K+\dfrac{es}{t}) -\dfrac{es}{t}
$$

Retirement is achieved year $N$ if the return on capital of this year ($K_N \times t$) is greater than or equal to the annual need (salary - savings: $s - es = s(1-e)$)

Thus the condition is $K_N \times t \geq s(1-e)$

So we must find the smallest $N$ such that

$$
\begin{aligned}
  \left((1+t)^N (K+\dfrac{es}{t}) -\dfrac{es}{t}\right)t &\geq s(1-e) \\
  (1+t)^N (K t+es) &\geq s \\
  (1+t)^N  &\geq \dfrac{s}{K t+es}\\
  N\ln(1+t)  &\geq \ln\left(\dfrac{s}{K t+es}\right)
\end{aligned}
$$

Finally

$$
  N = \dfrac{\ln\left(\dfrac{s}{K t+es}\right)}{\ln(1+t)}
$$

Observe that with no initial capital ($K=0$) the formula becomes

$$
  N = \dfrac{-\ln\left(e\right)}{\ln(1+t)}
$$

So in this case the time to retirement does not depend on the salary, but only on the savings rate and the rate of return!
