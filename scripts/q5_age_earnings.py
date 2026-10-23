
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

person = pd.read_csv("pslm_person_subset.csv")
household = pd.read_csv("pslm_hh_subset.csv")

data = person.merge(household, on="hhid", how="left")

earners = data[
    (data["prov_code"] == 2) &
    (data["urban_rural"] == 2) &
    (data["age"] >= 15) &
    (data["age"] <= 64) &
    (data["earn_annual"] > 0) &
    (data["hhweight"].notna()) &
    (data["hhweight"] > 0)
].copy()

labels = [
    "15-19", "20-24", "25-29", "30-34", "35-39",
    "40-44", "45-49", "50-54", "55-59", "60-64"
]

earners["age_band"] = pd.cut(
    earners["age"],
    bins=[15,20,25,30,35,40,45,50,55,60,65],
    right=False,
    labels=labels
)

age_means = (
    earners.groupby("age_band", observed=False)
    .apply(
        lambda g: np.average(g["earn_annual"], weights=g["hhweight"])
        if len(g) > 0 else np.nan,
        include_groups=False
    )
    .rename("weighted_mean")
    .reset_index()
)

age_means.to_csv("figure5_age_means.csv", index=False)

plt.figure(figsize=(10, 6))
plt.plot(age_means["age_band"].astype(str),
         age_means["weighted_mean"], marker="o")
plt.yscale("log")
plt.xlabel("Age Group (years)")
plt.ylabel("Weighted Mean Annual Earnings (Rs)")
plt.title("Annual Earnings by Age Group — Punjab Urban")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figure5.svg", format="svg")
plt.show()
