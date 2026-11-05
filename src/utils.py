from pathlib import Path
import pandas as pd


# convert GTFS time strings into seconds
def to_seconds(s):
    p = s.str.split(":", expand=True)

    return (
        pd.to_numeric(p[0]) * 3600
        + pd.to_numeric(p[1]) * 60
        + pd.to_numeric(p[2])
    )


# find the project root directory
def get_project_root():
    root = Path.cwd()

    if not (root / "data" / "processed").exists():
        root = root.parent

    return root