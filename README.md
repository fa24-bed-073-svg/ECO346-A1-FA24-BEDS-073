### Explanation of the Redesign

The redesigned figure improves readability and makes the relationship between age and annual earnings easier to interpret. First, the default scatter plot is replaced with weighted mean earnings for five-year age groups, reducing overplotting and highlighting the overall pattern. This follows the principle of choosing visual encodings that communicate the intended message clearly. Second, a logarithmic y-axis makes earnings across different levels easier to compare, preventing high values from dominating the display. Third, connecting the age-group means with a line emphasizes the trend across age groups. Finally, clearer axis labels and a descriptive title improve communication and interpretation.

However, the redesigned figure hides individual variation in earnings within each age group, which remains visible in the default scatter plot.

### Question 5: Cross-Language Comparison

The weighted mean annual earnings for the 25–29 age band were Rs 320,776 in R and Rs 320,776 in Python. The two band tables agree to the rupee after rounding. One difference between the default plotting settings was the y-axis scale: Python uses a linear scale by default, whereas the R redesign uses a logarithmic scale. I set Python's y-axis to logarithmic using `plt.yscale("log")` so that the figures use the same scale.
# ECO346-A1-FA24-BEDS-073
