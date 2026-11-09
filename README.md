# Exploratory Analysis of UK Food Incident Notifications (2023–2024): Visual Analytics for Regulatory Risk Identification

Coursework for COM7203 Data Science and Visualisation, part of my MSc in Artificial Intelligence and Data Science at Leeds Trinity University.

I merged two years of UK food incident notifications from data.gov.uk into one clean dataset, then looked at where incidents cluster, how they move month to month, and what kinds of hazards get reported. The main dashboards were built in Power BI, and I recreated the key charts in Python to check they could be reproduced. The project followed the CRISP-DM framework.

It's descriptive, not predictive. A notification is a reported event, not a confirmed case of harm, so the counts reflect how closely people are looking and reporting as well as real risk.

## What I found

The cleaned dataset holds 3,586 incidents, split fairly evenly across the two years (1,820 in 2023 and 1,766 in 2024). The report cites 3,587; the extra one is an empty row at the end of the CSV (see the data notes below).

- **A few product categories carry most of the load.** Meat and meat products (other than poultry) come first with 558 incidents, then dietetic and fortified foods (313), cereals and bakery products (274), and prepared dishes and snacks (258).
- **Pathogenic micro-organisms are the biggest incident type** at 820, well ahead of poor or insufficient controls (282) and food additives and flavourings (272).
- **Monthly volumes are uneven**, with peaks and dips rather than a steady trend. These could be useful as possible risk windows for planning inspections, but they don't prove that risk itself changed, since surveillance and reporting also vary.
- **Reporting patterns differ by who is reporting**, which points to some reporting bias.

The report also covers the limits of the data: missing and inconsistent categories, patchy origin-country information, and no severity measure, so every incident counts the same whatever its impact. It ends with suggestions such as standardised taxonomies, severity weighting, and combining incident data with inspection and recall data.

## What's in this repo

- `COM7203_Assessment1_...pdf`: the 7-page report.
- `UK Food Incident Notifications (2023–2024).pptx`: a 22-slide presentation of the project.
- `Assessment.ipynb`: the Python (pandas) data preparation. It merges the two annual files, standardises column names, parses dates, removes duplicates by incident ID, drops invalid or placeholder values, and exports the final CSV.
- `merged_incidents_final_clean.csv`: the cleaned dataset with 7 columns: incident ID, date received, incident type, product type, notifier type, origin country and incident source.

The Power BI file and the Python plotting code aren't included. The charts are in the report and the slides.

## Data notes

- The CSV ends with one empty row, so it has 3,587 lines of data but 3,586 real incidents.
- 156 rows have "Unknown" as the incident source.
- Some values are missing: 95 product types and 132 origin countries.

## Re-running the data prep

The raw files aren't included. Download the 2023 and 2024 spreadsheets from the [Received food incident notifications](https://www.data.gov.uk/dataset/8baf7984-2a90-45ba-a497-8dff82c0443a/received-food-incident-notifications) dataset on data.gov.uk. The notebook expects them as `incident-notifications-received-2023.xlsx` and `incident-notifications-received-2024.xlsx`. Update the folder path in the config block of the last cell, then run the cells in order. You'll need pandas, openpyxl and python-dateutil.

If you only want to explore the data, skip all that and open the CSV.

## Please don't copy

This is my own assessed work, shared for my portfolio. Don't submit it as yours. If it helps your thinking, cite it.

## Contact

- GitHub: [Zarin2000](https://github.com/Zarin2000)
- LinkedIn: [Zarin Tasnim Nuzhat](https://www.linkedin.com/in/zarin-tasnim-nuzhat-829007202)
- ORCID: [0009-0006-3469-1876](https://orcid.org/0009-0006-3469-1876)
