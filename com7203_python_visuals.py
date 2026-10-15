"""
COM7203 Assessment 1 - Alternative Visualisations (Python)
Creates non-pie visualisations to compare with Power BI outputs.

Run:
  python com7203_python_visuals.py

Requires:
  pandas, matplotlib
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

DATA_PATH = "merged_incidents_final_clean.csv"

def main():
    df = pd.read_csv(DATA_PATH)
    df["Received"] = pd.to_datetime(df["Received"], errors="coerce")
    df["Year"] = df["Received"].dt.year
    df["Month"] = df["Received"].dt.to_period("M").dt.to_timestamp()

    # Figure A: monthly trend
    monthly = df.groupby("Month")["Incident ID"].count().reset_index(name="Incidents")
    plt.figure(figsize=(10, 4.8))
    plt.plot(monthly["Month"], monthly["Incidents"])
    plt.title("Monthly Food Incident Notifications (2023–2024)")
    plt.xlabel("Month")
    plt.ylabel("Number of incidents")
    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("python_monthly_trend.png", dpi=200)
    plt.close()

    # Figure B: top product categories
    top_prod = df["ProductType"].fillna("Unknown").value_counts().head(12)[::-1]
    plt.figure(figsize=(10, 5.5))
    plt.barh(top_prod.index, top_prod.values)
    plt.title("Top Product Categories by Incident Count (2023–2024)")
    plt.xlabel("Number of incidents")
    plt.ylabel("Product category")
    plt.tight_layout()
    plt.savefig("python_top_products.png", dpi=200)
    plt.close()

    # Figure C: incident types by year (top 8 + Other)
    top_types = df["IncidentType"].fillna("Unknown").value_counts().head(8).index.tolist()
    counts = df.groupby(["Year", "IncidentType"])["Incident ID"].count().reset_index(name="n")
    counts["IncidentType2"] = counts["IncidentType"].where(counts["IncidentType"].isin(top_types), "Other")
    pivot = counts.groupby(["Year", "IncidentType2"])["n"].sum().unstack(fill_value=0)

    plt.figure(figsize=(10, 5))
    bottom = np.zeros(len(pivot.index))
    for col in pivot.columns:
        plt.bar(pivot.index.astype(int).astype(str), pivot[col].values, bottom=bottom, label=col)
        bottom += pivot[col].values
    plt.title("Incident Types by Year (Top categories + Other)")
    plt.xlabel("Year")
    plt.ylabel("Number of incidents")
    plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left", borderaxespad=0.)
    plt.tight_layout()
    plt.savefig("python_incidenttype_by_year_stacked.png", dpi=200)
    plt.close()

    # Figure D: notifier types (top 12)
    top_not = df["NotifierType"].fillna("Unknown").value_counts().head(12)[::-1]
    plt.figure(figsize=(10, 5.5))
    plt.barh(top_not.index, top_not.values)
    plt.title("Top Notifier Types by Incident Count (2023–2024)")
    plt.xlabel("Number of incidents")
    plt.ylabel("Notifier type")
    plt.tight_layout()
    plt.savefig("python_top_notifiers.png", dpi=200)
    plt.close()

if __name__ == "__main__":
    main()
