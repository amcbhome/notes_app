# Simple Linear Regression

Simple linear regression models the relationship between two variables using a straight line.

The model is defined as:

$$
y = a + bx
$$

Where:
- $y$ = dependent variable (e.g. cost)
- $x$ = independent variable (e.g. activity level)
- $a$ = intercept (fixed cost)
- $b$ = slope (variable cost per unit)

---

## Estimation of Parameters

### 1. Slope ($b$)

$$
b = \frac{n\sum xy - (\sum x)(\sum y)}
         {n\sum x^2 - (\sum x)^2}
$$

---

### 2. Intercept ($a$)

$$
a = \bar{y} - b\bar{x}
$$

Where:
- $\bar{x}$ = mean of $x$
- $\bar{y}$ = mean of $y$

---

### 3. Regression Equation

Once $a$ and $b$ are calculated, the regression equation is:

$$
\hat{y} = a + bx
$$

Where:
- $\hat{y}$ = predicted value of $y$

---

## Correlation Analysis

### Pearson Correlation Coefficient ($r$)

The strength and direction of the linear relationship is measured by:

$$
r = \frac{n\sum xy - (\sum x)(\sum y)}
         {\sqrt{\left[n\sum x^2 - (\sum x)^2\right]
                \left[n\sum y^2 - (\sum y)^2\right]}}
$$

- $-1 \le r \le 1$
- Values close to $1$ or $-1$ indicate a strong linear relationship

---

### Coefficient of Determination ($r^2$)

$$
r^2 = r \times r
$$

$r^2$ measures the **proportion of variance in $y$ explained by $x$**.

---

## Interpretation Example

If the calculated value of $r^2$ is:

$$
r^2 = 0.92
$$

This can be interpreted as:

> **92% of the variation in the dependent variable is explained by changes in the independent variable.**

The remaining **8%** of the variation is due to other factors not included in the model (random variation, omitted variables, or measurement error).

---

## Management Accounting Context

Simple linear regression is widely used in management accounting for:
- cost estimation
- forecasting
- budgeting
- decision-making under uncertainty

The model is particularly useful where a strong linear relationship exists between cost and activity levels.

