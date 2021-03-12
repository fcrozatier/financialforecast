Let $x$ be the annual fee of a subscription.

If we were to invest this much every year in an investment with a rate of return $t$, we would have the following relation between $x_n$ the capital of year $n$ and $n_{n+1}$ the capital of the subsequent year:

$x_{n+1} = (1+t)x_n + x$

Notice that the sequence $y_n = x_n + \dfrac{x}{t}$ is a geometric progression with common ratio $1+t$ :

$y_{n+1} = x_{n+1} + \dfrac{x}{t} =(1+t)x_n + x + \dfrac{x}{t} = (1+t)(y_n-\dfrac{x}{t})+ x + \dfrac{x}{t} = (1+t)y_n$

It follows that $y_n=(1+t)^n y_0=(1+t)^n\dfrac{x}{t}$

So $x_n=y_n-\dfrac{x}{t}=(1+t)^n\dfrac{x}{t}-\dfrac{x}{t}=\dfrac{x}{t}((1+t)^n-1)$

After $n$ years, an investment with a rate of return $t$, increased of a fixed amount $x$ per year is worth $\dfrac{x}{t}((1+t)^n-1)$
