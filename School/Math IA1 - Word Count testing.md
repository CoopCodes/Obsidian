
# Formulate
## Introduction
Keeping a business profitable requires, depending on the type of business, the owner to have great foresight into what the consumers want, and how much to sell it for depending on the demand. The difficult part of this is knowing how much demand there will be. This is why approximating the future is a valuable skill in the business world, this can be achieved relatively simply through mathematical means, and you can end up with an accurate mathematical representation of the future in regards to a businesses sales. In this Problem-Solving and modelling task, a method to create 2 mathematical models will be found. Both of which will attempt to forecast the profit for the client, given the clients data on the past year of sales. One model will approximate the **annual sales figures through to 2027**, and the other **monthly sales figures for 2024**.

## Translation

#### Linear line of best fit:
This the is the simplest and most effective way to create forecasting models, it is found using linear regression. Following the equation: $y=a+mx$.
##### Residual
A residual is the vertical distance between a data point and the regression line, in the process of finding the line of best fit, the sum of squared **residuals** is minimized.

<p style="font-size: .6em; line-height: 50%;"><i>Figure 1</i>, a graph showing a regression line, with the blue arrows showing residuals.</p>

#### The Coefficient of Determination 
($r^2$), this represents the variance of a data set, $-1 < r^2 < 1$. The smaller $r^2$ is, the less the data follows a trend, the opposite for higher values.


#### Seasonalized data 
Data is seasonalized if the data regularly undergoes predictable changes every year (for example, could be any time period).

#### Seasonal Indices
A score that shows how each annum differs from the average of all the seasons. It is found with:
$$SI=\frac{value\space for\space annum}{annum\space average}$$
#### Deseasonalization
*Seasonalized data* can be deseasonalised through the process of deseasonalisation. This process reveals the underlying trend of the data, and increases the value of the $r^2$ value. This in combination with the line of best fit, creates a great model to forecast with. In short, it is found with the following formula:
$$deseasonalised \space figure=\frac{actual\space figure}{SI}$$


<p style="font-size: .6em; line-height: 50%;"><i>Figure 2</i>, a graph showing actual data vs deseasonalised data </p>

#### Reseasonalisation
Once the forecasted data is found, the process of reseasonalisation reintroduces the seasonal effect. Completed by:
$$reseasonalized\space value=deseasonalized\space figure*SI$$

#### Excel Functions
Throughout the creation of the models, several excel functions will be used:
- `=SUM`, finds the sum of all selected rows.
- `=AVERAGE`, finds the average of all selected rows.
- `=LINEST(ys, [xs])`, given all the $y,x$ values, will return the $m$, and $a$ values of a line of best fit function, used in the equation $y=a+mx$.


## Assumptions
- **Accurate Data**, it is assumed that the provided data is accurate, this directly affects the accuracy of the forecast.
- **Tax is included**, it is assumed that the sales data provided includes GST taxes. This assumption is important due to the fact that if it wasn't assumed, the forecast would be less than or greater than reality.
- **Tax variations**, it is assumed that tax remains the same, or at least on the same growth rate as included in the dataset. If not, the sales could decrease over time, but it is just tax going up.
- **Global Events**, it is assumed that no major global events will occur, that will directly affect the economy of the business location/nation, for example, COVID-19. 
- **Australian Dollar**, it is assumed that the money used in the dataset is Australian Dollar ($), the Australian dollar is fairly stable, compared to other economies, this will ensure that sales don't vary.


## Observations:
When plotting the provided data, the following observations were made:
- <mark style="background: #FF5582A6;">There is an outlier in the 19 month (July of 2020), this can affect the outcome of the forecast, as the least squares regression method changes it's output drastically if there is an outlier (due to the squaring of each value).</mark>
- <mark style="background: #BBFABBA6;">It appears that the data is seasonalized, as seen by the constant fluctuations of the data in 1 year.</mark>
- <mark style="background: #ABF7F7A6;">Despite the seasonality, the overall trend appears to be upward.</mark>
- Finding the $r^2$ (correlation coefficient) of the dataset returns $0.21270961$. This is a low correlation, this justifies the need for deseasonalization.

<p style="font-size: .6em; line-height: 50%;"><i>Figure 3</i>, graph of the provided dataset</p>


# Solve

## Dataset (2024.6)


## Technology
Whilst the calculations discussed in [[Cooper Fieldhouse - General Math IA1#Translation|Translation]] can be done by hand, **Excel** makes this process much easier for large datasets, such as provided dataset. The data from the provided [[Cooper Fieldhouse - General Math IA1#Dataset (2024.6)|Dataset]] can be copied directly into excel, and modified on a large scale, graphed and even find the line of best fit. 

## Working
Due to the seasonality of the provided dataset, finding a line of best fit for the data will not provide the optimal forecast. The data can be optimized in two ways:
1. Deseasonalisation - discussed more in [[Cooper Fieldhouse - General Math IA1#Translation|Translation]]
2. Removing outliers - The provided dataset contains an outlier, which will affect the forecast heavily.

The deseasonalisation process:

1. Find the average value for each year, found by `=AVERAGE(B2:M2)`, where the `2` value is variable. (*Figure 4*)

<p style="font-size: .6em; line-height: 50%;"><i>Figure 4</i>, finding the average month value for each year </p>
2. Now the SI's (Seasonal Index) for each month can be found by $\frac{actual\space value}{average\space month\space value}$, or in excel `=B2/$N2`. This is completed for all months in the dataset, with their respective average, and value. (*Figure 5*)

<p style="font-size: .6em; line-height: 50%;"><i>Figure 5</i>, finding the SI's for each month</p>
3. The average for each months' SI can be found with `=AVERAGE(B8:B12)`. (*Figure 6*)


<p style="font-size: .6em; line-height: 50%;"><i>Figure 6</i>, finding the average SI for each month</p>
4. Unfortunately, when graphing in excel and excel sees multiple lines, it assumes it is multiple separate datasets. So for our data we have to spread it across one line, and number each month, not naming. Additionally, there should be 3 rows, Seasonalized, Deseasonalised, and a repeating 12 values of all the month averages over the dataset. (*Figure 7*)


<p style="font-size: .6em; line-height: 50%;"><i>Figure 7</i>, spread out version of dataset, (The data continues further than image)</p>
5. Each deseasonalised value can be found using the formula $\frac{actual\space value}{monthly\space average}$, or in excel `B16/B14`, where `B` varies along columns.


<p style="font-size: .6em; line-height: 50%;"><i>Figure 8</i>, finding the deseasonalised data points, (data continues past image)</p>
6. Additionally, we can calculate the $r^2$ value of the deseasonalised data using the `=RSQ()` function in excel. This returns $0.830007922$, this proves that deseasonalisation was necessary, as it increased the correlation by a product of $\approx 4$.



With the data optimized, the actual forecasting can begin:
1. Plot the Seasonalized data & Deseasonalised data.

<p style="font-size: .6em; line-height: 50%;"><i>Figure 9</i>, a plot with the seasonalized and deseasonalised data</p>

2. Add a trendline to the plot to the deseasonalised data

<p style="font-size: .6em; line-height: 50%;"><i>Figure 10</i>, line of best fit for deseasonalised data</p>



3. When adding a trendline to the graph in excel, excel rounds the data, thus the trendline is inaccurate. To find the correct values for $a$ and $b$, we can use the `=LINEST(known_ys, [known_xs])` function, and enter the Deseasonalised data as the `known_ys`, and Month data for the `[known_xs]`. (`=LINEST(B17:BI17,B15:BI15)`), as seen in *Figure 11* <p style="font-size: .6em; line-height: 50%;">&emsp;&emsp;&emsp;  <i>Figure 11</i>, LINEST function</p>       This returns the $a$ and $b$ values ($y=ax+b$). Therefore, the equation is $monthly\space prediction=1105.687097*month+175372.9$ <br> 

4. Now, in the month row, instead of going to 60, go to 120 (which is December of 2028).
5. For the deseasonalised row (all month values $>60$), we can use the line of best fit formula to forecast, by substituting the $month$ for the month. (*Figure 12*)                                             <p style="font-size: .6em; line-height: 50%;">&emsp;&emsp;&emsp;  <i>Figure 12</i>, extrapolating/forecasting the data to 2028 (data continues past image)</p>       Where `$A$20` is $a$, and `$B$20` is $b$.

6. To reseasonalise the data, we can use the formula $reseasonalised\space value = deseasonalised\space value * SI$




7. Finally, we can graph the whole dataset with the predictions, up to 2028:

<p style="font-size: .6em; line-height: 50%;"><i>Figure 13</i>, a showing the seasonalised, deseasonalised, and reseasonalised data with forecasting up to 2028 (2028 being month 120)</p>


## Solution

### Monthly forecast of 2024.

<p style="font-size: .6em; line-height: 50%;"><i>Figure 14</i>, a table containing the monthly predictions of 2024</p>


### Yearly forecast to 2028 (2024 - 2028)
The same process discussed in [[Cooper Fieldhouse - General Math IA1#Working|Working]] can be performed on the <u>sum of each years' sales</u>.

<p style="font-size: .6em; line-height: 50%;"><i>Figure 15</i>, the sum of each years' sales</p>


<p style="font-size: .6em; line-height: 50%;"><i>Figure 16</i>, short summary of forecasting the sum of sales.</p>

- <mark style="background: #ADCCFFA6;">Sum of each years' sales, found in</mark> *Figure 15*.

- <mark style="background: #D2B3FFA6;">The line of best fit equation found using the `LINEST` function.</mark>

- <mark style="background: #FFB8EBA6;">Forecasted data by extrapolation, using the line of best fit equation.</mark>

- <mark style="background: #FFF200A6;">The forecasted data in monetary form.</mark>



<p style="font-size: .6em; line-height: 50%;"><i>Figure 17</i>, a table containing the yearly predictions to 2028</p>


# Evaluate & Verify
## Justifications
During the process of creating these models, several decisions were made.
It was decided that, in order to get the best forecasting models, the provided data would have to be optimized, to get the highest $r^2$ value. This was completed by removing outliers, and deseasonalizing the data. These optimizations changed the $r^2$ value from $\approx 0.2$ to $\approx 0.8$.
The Sum of Squared Residuals was the chosen method of creating a function to fit the data, this method is easy to complete and explain. However, it comes with a downside to not being as accurate.
Because of its simplicity, and expandability, it was decided to use Excel to do all of the calculations and graphing.

## Strengths
The created models are effective in predicting sales several years into the future, given that specific economical future events won't occur ([[Cooper Fieldhouse - General Math IA1#Assumptions|Assumptions]]). This was achieved by optimizing the data - removing outliers, and deseasonalizing, to create a strong $r^2$ value. Additionally, the model reseasonalises the forecasted data, ensuring that each months' prediction will be based on past years data.

## Limitations
The future cannot be modelled not nearly perfectly, especially with a simple linear model, taking into account only 1 factor (sales). The businesses sales could start to dip due to a global economic event, or their sales could increase at a higher rate, it is impossible to know from the data provided.
# Conclusion
The aim of this Problem-Solving and modelling task was to provide 2 forecasting models for a business, given 5 years of monthly sale history. The first model was to forecast the monthly sales of 2024, and the second the yearly sales to 2028. This was completed for the first model by [[Cooper Fieldhouse - General Math IA1#Working|optimizing]] the provided data to increase the $r^2$ value, and then using The Least Squares Regression Method to find a line of best fit for the data. A similar process was completed for the second model, but with the sum of sales of each year as the data to create a line of best fit on. Using these models, the data was extrapolated to the required dates. 
Overall, this modelling task demonstrated the application of relevant knowledge and skills to solve a real-world problem using a systematic approach.
