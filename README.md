CY PLAN 101 — Group 16: Muni Reliability Analysis

This project analyzes Muni schedule reliability in San Francisco using March 2025 weekday transit observations and 2024 ACS Census data.

Setup

1. Install the required Python packages

From the project root, run:

pip install -r requirements.txt

2. Set up the data

The project uses:

511 SF Bay Transit Data — historical GTFS feed (operator_id=RG, historic=2025-03-so).

2024 ACS 5-Year Census API — San Francisco Census tract demographics.

Place the supplied GTFS files in data/march_2025_gtfs/.

Create a .env file in the project root containing:

API_KEY=your_511_api_key
CENSUS_API_KEY=your_census_api_key

API keys are required for downloads and should not be committed to GitHub.

Running the Analysis

1. Process the data

Open notebooks/data_pipeline.ipynb and select Kernel → Restart & Run All.

This notebook runs the following files in order:

data_exploration.ipynb — Clean GTFS observations.

census_data_exploration.ipynb — Process Census data and stop catchments.

combined_dataframe.ipynb — Aggregate Muni delays and combine demographic estimates.

Processed CSVs are saved in data/processed/.

2. Generate visualizations

Open notebooks/midterm_visuals.ipynb and select Kernel → Restart & Run All.

Figures and maps are exported to outputs/figures/ and outputs/maps/.

Spatial Analysis

The spatial join is in notebooks/midterm_visuals.ipynb, using gpd.sjoin() to match Muni stops to Census tracts for a tract income comparison.

The Census processing notebook also uses gpd.overlay() with 400 meter stop buffers to estimate surrounding demographics.

Both spatial operations use EPSG:32610 (UTM Zone 10N).

Repository Structure

data/ — Raw GTFS data and processed CSVs

notebooks/ — Data processing and visualization notebooks

src/utils.py — Reusable helper functions

outputs/ — Exported maps and figures

requirements.txt — Python dependencies

Large datasets excluded from GitHub are provided separately in the submission ZIP.
