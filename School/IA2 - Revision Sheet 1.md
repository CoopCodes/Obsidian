---
tags:
  - mathematics
---
___
# Simple familiar
## 1
![[Pasted image 20240417134818.png|600]]

### a)

| Age group | Hot Drinks | Milkshakes | Juice |
| --------- | ---------- | ---------- | ----- |
| Children  | 5          | 25         | 32    |
| Teenagers | 48         | 57         | 49    |
| Adults    | 124        | 11         | 96    |

### b)
```math
sum = 5+25+32+48+124+11+96
hot_drinks = (5+48+124/sum)
children = ((5+25+32)/sum)*100
teenagers = ((48+57+49)/sum)*100

child_juice = (32/(5+25+32))*100
adult_juice = (96/(124+11+96))*100
diff = child_juice-adult_juice
```

## 3
The association between $x$ and $y$ is described as the following:
as $x$ increases, $y$ decreases, with a correlation of $0.66$.

## 4
```math
-0.14 + 1.82
((1.47-1.82)/(-0.14))
-0.14(4)+1.82
p(part, total) = (part/total) * 100

a = p(5, 6)
b = p(4, 12)
c = p(2, 12)
d = p(0, 9)

```

|Average temperature (°C)|15.1|10.6|4.9|17.7|27.2|14.8|3.6|
|---|---|---|---|---|---|---|---|
|Latitude (°S)|32.2|33.8|39.4|29.6|18.0|37.3|45.6|
Assuming a linear association, determine the equation of the least-squares line. (referring to the above md table). Remember, don't use python :)

```math
# Calculate the mean of latitude (x) and average temperature (y)
mean_x = (32.2 + 33.8 + 39.4 + 29.6 + 18.0 + 37.3 + 45.6) / 7
mean_y = (15.1 + 10.6 + 4.9 + 17.7 + 27.2 + 14.8 + 3.6) / 7
# Calculate the numerator and denominator for the slope

numerator = (32.2 - mean_x) * (15.1 - mean_y) + (33.8 - mean_x) * (10.6 - mean_y) + (39.4 - mean_x) * (4.9 - mean_y) + (29.6 - mean_x) * (17.7 - mean_y) + (18.0 - mean_x) * (27.2 - mean_y) + (37.3 - mean_x) * (14.8 - mean_y) + (45.6 - mean_x) * (3.6 - mean_y)
denominator = (32.2 - mean_x)^2 + (33.8 - mean_x)^2 + (39.4 - mean_x)^2 + (29.6 - mean_x)^2 + (18.0 - mean_x)^2 + (37.3 - mean_x)^2 + (45.6 - mean_x)^2


# Calculate the slope

slope = numerator / denominator


# Calculate the y-intercept

y_intercept = mean_y - slope * mean_x


# The equation of the least-squares line is: y = mx + b

# Where m is the slope and b is the y-intercept
```

The following table shows the heights and masses of some members of a local cricket team.

|   |   |   |
|---|---|---|
|Name|Height (cm)|Mass (kg)|
|Adam Ponting|179|79|
|Simon Gilchrist|186|86|
|Michael Katich|182|80|
|Stuart Clarke|178|70|
|Glenn MacGill|183|90|
|Michael McGrath|195|90|
|Shane Kasprowicz|194|98|
|Darren Watson|183|93|
|Jason Lehmann|176|90|
|Shane Gillespie|195|94|
|Justin Warne|184|85|
|Brad Langer|178|78|
|Damien Hogg|175|77|
|Brad Martyn|181|74|
|Ricky Williams|183|91|

(a)     Is height or mass the response variable?

(b)     Construct a scatterplot and comment on the association.

(c)     Determine the value of the correlation coefficient, , correct to  decimal places.

(d)     Determine the equation of the least squares regression line. 


# 15
Tomatoes are sprayed with an organic garlic and seaweed mixture. The yields from different concentrations of spray mixtures are recorded in the table below.

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|Concentration (mL/L)|3|5|6|8|9|11|
|Yield (kg)|67|90|103|120|124|150|

(a)     Determine Pearson’s correlation coefficient and the coefficient of determination, correct to 3 decimal places. Comment on the meaning of each value. Please use python

```python
# Given data
concentrations = [3, 5, 6, 8, 9, 11]
yields = [67, 90, 103, 120, 124, 150]
# Calculate means

import math


mean_conc = sum(concentrations) / len(concentrations)
mean_yield = sum(yields) / len(yields)


# Calculate Pearson's correlation coefficient

numerator = 0
denom_conc = 0
denom_yield = 0


for i in range(len(concentrations)):
	numerator += (concentrations[i] - mean_conc) * (yields[i] - mean_yield)
	denom_conc += (concentrations[i] - mean_conc) ** 2
	denom_yield += (yields[i] - mean_yield) ** 2


denom = math.sqrt(denom_conc * denom_yield)
if denom == 0:
	r = 0
else:
	r = numerator / denom


# Calculate coefficient of determination

r_squared = r ** 2

print(f"Pearson's correlation coefficient: {r:.3f}")
print(f"Coefficient of determination: {r_squared:.3f}")