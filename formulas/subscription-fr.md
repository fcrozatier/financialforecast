Notons $x$ le coût annuel d'un abonnement.

En investissant cette somme chaque année à un taux d'intérêt $t$, on aurait la relation suivante entre $x_n$ le capital de l'année $n$ et $x_{n+1}$ celui de l'année suivante :

$$
  x_{n+1} = (1+t)x_n + x
$$

Remarquons que la suite $y_n = x_n + \dfrac{x}{t}$ est une suite géométrique de raison $1+t$ :

$$
\begin{aligned}
  y_{n+1} &= x_{n+1} + \dfrac{x}{t}\\
          &=(1+t)x_n + x + \dfrac{x}{t}\\
          &= (1+t)(y_n-\dfrac{x}{t})+ x + \dfrac{x}{t}\\
          &= (1+t)y_n
\end{aligned}
$$

On en déduit

$$
  y_n=(1+t)^n y_0=(1+t)^n\dfrac{x}{t}
$$

Ainsi

$$
\begin{aligned}
  x_n &= y_n-\dfrac{x}{t}\\
      &=(1+t)^n\dfrac{x}{t}-\dfrac{x}{t}\\
      &=\dfrac{x}{t}((1+t)^n-1)
\end{aligned}
$$

Au bout de $n$ années, un investissement au taux $t$ alimenté d'une valeur fixée $x$ par an a donc une valeur de

$$
  \dfrac{x}{t}((1+t)^n-1)
$$
