### Formal proof

Lets find the partial derivatives of $f$ in both directions in order to compare the slopes at a given point.

$$
\begin{aligned}
\dfrac{\partial f}{\partial s}(s,p)
  &=\dfrac{Kt-p}{s(Kt+s-p)\ln(1+t)}\\
\dfrac{\partial f}{\partial p}(s,p)
  &=\dfrac{1}{(Kt+s-p)\ln(1+t)}
\end{aligned}
$$

It follows that the two slopes verify the relation

$$
  \dfrac{\partial f}{\partial s}(s,p) = \dfrac{Kt-p}{s} \dfrac{\partial f}{\partial p}(s,p)
$$

So we only have to look at the ratio $\dfrac{Kt-p}{s}$ to know which slope is steeper. The slope relative to the salary is more negative than the slope relative to the spendings when we have

$$
  \dfrac{Kt-p}{s}< -1
$$

Which is equivalent to

$$
  Kt + s < p
$$

But that's impossible since the salary is already bigger than the spendings.

**So the slope is always steeper in the direction of savings**. Which means that decreasing the spendings by one dollar has more impact on the time to retirement than increasing the salary by one dollar.

Finaly, note that if the spendings decrease by 1 dollar, to have the same impact on the time to retirement by an increase of salary, the increase must compensate the above ratio, and so **decreasing spendings by 1 dollar is equivalent to increasing the salary by $\dfrac{s}{p - Kt}$ dollars**.
Which is the formula used in the bonus of the time to retirement widget.
