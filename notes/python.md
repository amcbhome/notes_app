# Python Notes

## Virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate

## Import
import pandas as pd

## CSV

df = pd.read_csv("data.csv")

squares = {x: x**2 for x in range(10)}

# Linear Regression

The simple linear regression model is:

$$
y = a + bx
$$

Where:

- $y$ = dependent variable (e.g. cost)
- $x$ = independent variable (e.g. activity level)
- $a$ = fixed cost (intercept)
- $b$ = variable cost per unit (slope)

This model is widely used in management accounting for cost estimation.



