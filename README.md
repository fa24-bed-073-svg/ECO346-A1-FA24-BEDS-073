## Question 2: The Distribution

### Reported Statistics

- Number of earners: 3,768
- Weighted median annual earnings: Rs 240,000
- Unweighted median annual earnings: Rs 240,000
- Weighted 10th percentile (p10): Rs 96,000
- Weighted 90th percentile (p90): Rs 660,000
- p90/p10 ratio: 6.88
- Number of earners excluded from the histogram range: 25

### Interpretation

The earnings distribution shows substantial inequality: the weighted 90th percentile is almost seven times the weighted 10th percentile. The weighted and unweighted medians are both Rs 240,000, suggesting that weighting does not change the median for this sample under the specified quantile definition. The histogram uses a logarithmic earnings scale to display a wide range of earnings values more clearly.

## Question 3: Earnings and Age

### Weighted Mean Annual Earnings by Age Group

| Age band | Number of earners | Weighted mean earnings (Rs) |
|---|---:|---:|
| 15–19 | 229 | 145,444 |
| 20–24 | 449 | 216,585 |
| 25–29 | 499 | 320,776 |
| 30–34 | 518 | 369,580 |
| 35–39 | 498 | 354,031 |
| 40–44 | 435 | 498,966 |
| 45–49 | 427 | 465,073 |
| 50–54 | 363 | 521,949 |
| 55–59 | 220 | 523,751 |
| 60–64 | 130 | 453,067 |

**Key findings:** The weighted mean annual earnings for the 25–29 age band are Rs 320,776, while those for the 45–49 age band are Rs 465,073. The highest weighted mean is observed in the 55–59 age band, at Rs 523,751.

**Interpretation:** Average earnings generally increase across older age groups, although the pattern is not consistently upward. Earnings may reflect differences in work experience, occupation, hours worked, and other factors. The figure describes an association between age and earnings; it cannot establish that age itself causes higher earnings.
### Question 4: Explanation of the Redesign

The redesigned figure improves readability and makes the relationship between age and annual earnings easier to interpret. First, the default scatter plot is replaced with weighted mean earnings for five-year age groups, reducing overplotting and highlighting the overall pattern. This follows the principle of choosing visual encodings that communicate the intended message clearly. Second, a logarithmic y-axis makes earnings across different levels easier to compare, preventing high values from dominating the display. Third, connecting the age-group means with a line emphasizes the trend across age groups. Finally, clearer axis labels and a descriptive title improve communication and interpretation.

However, the redesigned figure hides individual variation in earnings within each age group, which remains visible in the default scatter plot.

### Question 5: Cross-Language Comparison

The weighted mean annual earnings for the 25–29 age band were Rs 320,776 in R and Rs 320,776 in Python. The two band tables agree to the rupee after rounding. One difference between the default plotting settings was the y-axis scale: Python uses a linear scale by default, whereas the R redesign uses a logarithmic scale. I set Python's y-axis to logarithmic using `plt.yscale("log")` so that the figures use the same scale.
# ECO346-A1-FA24-BEDS-073
