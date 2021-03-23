### Short answer

It is always better to focus on spending less.

More precisely, decreasing your annual spendings by one dollar always has a better impact on your time to retirement than increasing your annual salary by the same amount. This is true no matter your configuration of salary, savings, capital.

### Intuition

Both spending less or earning more allow you to save more money each year, but spending less has the added benefit of lowering the target capital, so you can retire earlier.

### Time to retirement as a function

We know the formula for the time to retirement depending on the savings ratio $e$

$$
  \dfrac{\ln\left(\dfrac{s}{K t+es}\right)}{\ln(1+t)}
$$

Let's introduce the annual spendings $p = s - es$. The variables $s$ and $p$ are independent (one can increase or decrease without affecting the other) and we will familiarize ourselves with the corresponding function

$$
  f(s,p)=\dfrac{\ln\left(\dfrac{s}{K t+s-p}\right)}{\ln(1+t)}
$$

### Visual proof when there is no initial capital

The first thing to note in the case $K=0$ is that for any number $\lambda$

$$
f(s,p)=f(\lambda s,\lambda p)
$$

This implies that for example someone making 12k and spending 10k a year is in the **exact** same situation with respect to the time to retirement as someone making 120k and spending 100k! Indeed

$$
  f(s,p)=\dfrac{\ln\left(\dfrac{s}{s-p}\right)}{\ln(1+t)}=f(\lambda s,\lambda p)
$$

This property allows us to graph the function on a small domain, and know that it looks the same at all scales.

The surface is shown below (with $t=4\%$ for the illustration). Observe that **the slope at any given point is steeper in the direction of decreased spendings** than in the direction of increased salary. The projections of the contour lines can help compare. This proves visually that it is always better for the time to retirement to diminish spendings.

Also you can find your configuration on the surface by dividing your annual salary and spendings by 1000 or the suitable power of 10.
