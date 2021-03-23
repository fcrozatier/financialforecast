### La réponse courte

Il est toujours favorable de privilégier la diminution des dépenses.

Plus précisément, une diminution des dépenses annuelles de un euro a un impact plus conséquent sur le temps de départ en retraite qu'une augmentation de salaire de un euro. Ceci est vrai dans toutes les configurations de salaire, épargne, capital.

### Intuition

Dépenser moins ou gagner plus permettent dans les deux cas de mettre plus d'argent de côté chaque année, mais dépenser moins permet également de réduire le capital cible permettant un départ en retraite, donc celle-ci est atteinte plus rapidement.

### Temps de départ en retraite en tant que fonction

Nous connaissons la formule du temps de départ en retraite en fonction du taux d'épargne $e$

$$
  \dfrac{\ln\left(\dfrac{s}{K t+es}\right)}{\ln(1+t)}
$$

Introduisons les dépenses annuelles $p = s -es$. Les variables $s$ et $p$ sont indépendantes (car l'une peut varier sans influencer l'autre). Nous allons nous familiariser avec la fonction associée à ces variables

$$
  f(s,p)=\dfrac{\ln\left(\dfrac{s}{K t+s-p}\right)}{\ln(1+t)}
$$

### Preuve visuelle lorsqu'il n'y a pas de capital initial

Remarquons tout d'abbord que dans le cas $K=0$, pour tout nombre $\lambda$

$$
f(s,p)=f(\lambda s,\lambda p)
$$

Ceci implique par exemple que quelqu'un gagnant 12k et dépensant 10k est **exactement** dans la même situation relativement à son temps de départ en retraite que quelqu'un gagnant 120k et dépensant 100k

$$
  f(s,p)=\dfrac{\ln\left(\dfrac{s}{s-p}\right)}{\ln(1+t)}=f(\lambda s,\lambda p)
$$

Cette propriété nous permet également de représenter la fonction sur un domaine restreint, tout en sachant que son allure est la même à toute les échelles.

La surface est représentée ci-dessous (dans le cas $t=4\%$). Observons que **en tout point la pente est plus prononcée dans la direction des diminutions de dépenses** que dans la direction des augmentations de salaire. Les projection des lignes de contour peuvent aider à comparer les pentes. Ceci démontre visuellement qu'il est toujours préférable pour le temps de départ en retraite de dépenser moins.

Aussi, chacun peut trouver sa configuration salaire / dépense sur la surface en divisant son salaire et ses dépenses par 1000 ou la bonne puissance de 10.
