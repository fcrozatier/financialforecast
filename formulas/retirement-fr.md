Notons $s$ le salaire annuel, $e$ le taux d'épargne annuel, $t$ le taux de retour de l'investissement et $K$ le capital initial.

La relation entre les capitaux $K_n$ et $K_{n+1}$ des années $n$ et $n+1$ est :

$$
  K_{n+1}=(1+t)K_n+es
$$

Observons que la suite $a_n=K_n+\dfrac{es}{t}$ est géométrique de raison $(1+t)$ :

$$
\begin{aligned}
a_{n+1} &= K_{n+1}+\dfrac{es}{t}\\
        &=(1+t)K_n+es+\dfrac{es}{t}\\
        &=(1+t)(a_n-\dfrac{es}{t})+es+\dfrac{es}{t}\\
        &=(1+t)a_n
\end{aligned}
$$

Donc $a_n=(1+t)^n a_0=(1+t)^n(K+\dfrac{es}{t})$

On en déduit

$$
K_n = (1+t)^n (K+\dfrac{es}{t}) -\dfrac{es}{t}
$$

La retraite est atteinte l'année $N$ lorsque le rendement du capital de cette année ($K_N \times t$) est supérieur au besoin annuel (salaire - quantité épargnée : $s - es = s(1-e)$)

Autrement dit lorsque $K_N \times t \geq s(1-e)$

Il faut donc trouver le plus petit $N$ tel que

$$
\begin{aligned}
  ((1+t)^N (K+\dfrac{es}{t}) -\dfrac{es}{t})t &\geq s(1-e) \\
  (1+t)^N (K t+es) &\geq s \\
  (1+t)^N  &\geq \dfrac{s}{K t+es}\\
  N\ln(1+t)  &\geq \ln\left(\dfrac{s}{K t+es}\right)
\end{aligned}
$$

Ainsi la retraite est atteinte au bout d'un nombre d'années $N$ valant :

$$
  N = \dfrac{\ln\left(\dfrac{s}{K t+es}\right)}{\ln(1+t)}
$$

Notons que sans apport initial ($K=0$) la formule précédente devient :

$$
  N = \dfrac{-\ln\left(e\right)}{\ln(1+t)}
$$

Donc dans ce cas le temps avant la retraite ne dépend pas du salaire, mais uniquement du taux d'épargne et du taux d'intérêt !
