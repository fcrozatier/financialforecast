### Démonstration formelle

Déterminons les dérivées partielles de $f$ dans les deux directions afin de comparer les pentes en un point donné.

$$
\begin{aligned}
\dfrac{\partial f}{\partial s}(s,p)
  &=\dfrac{Kt-p}{s(Kt+s-p)\ln(1+t)}\\
\dfrac{\partial f}{\partial p}(s,p)
  &=\dfrac{1}{(Kt+s-p)\ln(1+t)}
\end{aligned}
$$

Il s'ensuit que les pentes vérifient la relation

$$
  \dfrac{\partial f}{\partial s}(s,p) = \dfrac{Kt-p}{s} \dfrac{\partial f}{\partial p}(s,p)
$$

Il suffit donc d'étudier le ratio $\dfrac{Kt-p}{s}$ pour savoir en quelle direction la pente est plus prononcée. La pente relative au salaire est plus négative que celle relative aux dépenses lorsque

$$
  \dfrac{Kt-p}{s}< -1
$$

Ce qui est équivalent à

$$
  Kt + s < p
$$

Or ceci est impossible puisque le salaire est déjà supérieur aux dépenses.

**Donc la pente est toujours plus raide dans la direction de l'épargne**. Ce qui signifie qu'une diminution des dépenses d'un euro a plus d'impact sur le temps de départ à la retraite qu'une augmentation de salaire de un euro.

Finalement, remarquons que si les dépenses diminuent de 1 euros, pour avoir un impact similaire sur le temps de départ en retraite par une augmentation de salaire, celle-ci doit compenser le ratio précédent. De sorte que **1 euro de dépenses en moins équivaut à $\dfrac{s}{p - Kt}$ euros de salaire en plus.** C'est la formule utilisée dans le bonus du widget temps de départ en retraite.
