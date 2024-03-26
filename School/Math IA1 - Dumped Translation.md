---
tags:
  - mathematics
---
___
##### Line of best fit:
The simplest and most effective method of creating these models, is by using linear regression, which attempts to model the relationship between two variables by fitting a linear equation to the observed data (_Linear Regression_, 2024). This line has an equation of form $y=b+ax$, where $y$ would be the sales figures, and $x$ would time. 
$$sales \space figures = b+a*time$$
In order to create this *line of best fit*, we can use the **Least-Squares Regression** method to find the values of $b$ and $a$ in the *line of best fit* equation. 
![[Pasted image 20240207194546.png]]
<p style="font-size: .6em; line-height: 50%;"><i>Figure 1</i>, a graph showing a regression line</p>

The line in this graph is a regression line, but isn't the *line of best fit*, the blue lines shown indicate the distance from each point to the regression line. This distance is called a **residual**. <u>Squaring</u> these <u>residuals</u>, and finding the <u>sum</u> of them finds **the Sum of Squared Residuals**

The **Least-Squares Regression** method aims to <u>minimize</u> the sum of squared residuals. The reason the residuals are squared, is if the distance is negative, it will become positive, and if it is positive, it will still be positive. However this means that any outliers in the data affect the line of best fit <u>more</u> than data close to the ==average==. 
The equation of **the least squares regression line** can be found using the following formulae:

$$b=\frac{rs_y}{s_x}$$
$$a=\bar{y}-b\bar{x}$$
where: 
- $b=slope$
- $a=intercept$
- $r=correlation \space coefficient$
- $s_x=standard \space deviation_x$
- $s_y=standard \space deviation_y$
- $\bar{x}=mean \space of \space x$
- $\bar{y}=mean \space of \space y$
%%Should show how to find r, sx, and sy?%%
Now that the $a$ and $b$ values can be found, the line of best fit can be made using the equation $y=b+ax$.

##### Seasonalized & Deseasonalised data:
Whilst the line of best fit is accurate on most data, there is a characteristic of some time-series plots that is **seasonalized**. This means that the data regularly undergoes predictable changes every year (for example, could be any time period). Due to this characteristic, the line of best fit doesn't accurately represent the data. Often in business, sales vary due to seasons, for a swimsuit business, sales will be higher during summer, and this *seasonalisation* can be removed through the process of **deseasonalisation**. This process can reveal the underlying trend occurring in the plot, if the <u>overall</u> sales are increasing or decreasing. This in combination with the line of best fit is a great <u>model</u> to help analyze business sales, and help give advice to actions to perform business wise in the future.
![[Pasted image 20240208194521.png]]
<p style="font-size: .6em; line-height: 50%;"><i>Figure 2</i>, a graph showing actual data vs deseasonalised data </p>
The process of deseasonalisation can be completed by using the following formula, and repeating it for all data points in the dataset:

$$deseasonalised \space figure=\frac{actual\space figure}{SI}$$
The $SI$ can be found using the formula:

$$SI=\frac{value\space for\space anum}{anum\space average}$$
$$anum\space average=\frac{anum_1+anum_2+...+anum_n}{n}$$
Here is an example of finding the $SI$ for a dataset:

| Year | Summer | Autumn | Winter | Spring |
| ---- | ------ | ------ | ------ | ------ |
| 1    | 920    | 1085       | 1241       | 446       |
$$anum\space average=\frac{920 + 1085 + 1241 + 446}{4}=923$$
$$SI_{summer}=\frac{920}{923}=0.997$$
$$SI_{autumn}=\frac{1085}{923}=1.176$$
$$...$$
Performing this for the rest of anums (seasons) will get you:

| Year | Summer | Autumn | Winter | Spring |
| ---- | ------ | ------ | ------ | ------ |
| 1    | 0.997    | 1.176       | 1.345       | 0.483       |
