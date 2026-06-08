# Loading libraries
import glob, os
from datetime import datetime, timezone
import pandas as pd

# Start & end for the state breakdown
START = "<!-- STATE_BREAKDOWN:START -->"
END = "<!-- STATE_BREAKDOWN:END -->"

# Types of models
TYPES = ["Task Force Model", "Warrant Service Officer", "Jail Enforcement Model"]

# Looking through all the participating files
files = glob.glob("sheets/**/*articipating*.xlsx", recursive=True) or glob.glob("sheets/**/*.xlsx", recursive=True)
latest = max(files, key=os.path.getmtime)

# Defining the latest file
df = pd.read_excel(latest)

# Extracting variables of interest
df["STATE"] = df["STATE"].astype(str).str.strip().str.title()
df["SUPPORT TYPE"] = df["SUPPORT TYPE"].astype(str).str.strip()
df = df[~df["STATE"].isin(["", "Nan"])]

# Creating a pivot table by state and support type
p = df.pivot_table(index="STATE", columns="SUPPORT TYPE", aggfunc="size", fill_value=0)

# Looping htorugh types
for t in TYPES:
    if t not in p:
        p[t] = 0
p = p[TYPES]

# Calculating totals (i.e. sum of type counts)
p["Total"] = p.sum(axis=1)

# Sorting states by total
p = p.sort_values("Total", ascending=False)

# Pulling out the timestamp
stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

# Defining the statewide breakdown in MD
lines = [START, "## Statewide Breakdown", "",
         f"Number of 287(g) agreements per state, by support type. *Last updated: {stamp} \u2014 {len(p)} states, {int(p['Total'].sum())} total agreements (source: `{os.path.basename(latest)}`).*",
         "", "| State | Task Force Model | Warrant Service Officer | Jail Enforcement Model | Total |",
         "| --- | ---: | ---: | ---: | ---: |"]

# Looping through the p
for s, r in p.iterrows():
    lines.append(f"| {s} | {r['Task Force Model']} | {r['Warrant Service Officer']} | {r['Jail Enforcement Model']} | {r['Total']} |")

# Appending sums
t = p.sum()
lines.append(f"| **All states** | **{t['Task Force Model']}** | **{t['Warrant Service Officer']}** | **{t['Jail Enforcement Model']}** | **{t['Total']}** |")
lines += ["", END]
section = "\n".join(lines)

# Opening the current readme
readme = open("README.md", encoding="utf-8").read()

# Adding the strings to the readme
if START in readme and END in readme:
    readme = readme.split(START)[0].rstrip() + "\n\n" + section + "\n" + readme.split(END, 1)[1].lstrip("\n")

# Make sure slots in correctly.
elif "## Purpose" in readme:
    before, after = readme.split("## Purpose", 1)
    readme = before.rstrip() + "\n\n" + section + "\n\n## Purpose" + after
else:
    readme = readme.rstrip() + "\n\n" + section + "\n"

# Writing to the readme
open("README.md", "w", encoding="utf-8").write(readme)
print(f"Updated README.md from {latest}")
