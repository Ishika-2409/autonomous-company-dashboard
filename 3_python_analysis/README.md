# Python Data Analysis Scripts

This folder contains all Python scripts for data preprocessing, analysis, and predictive modeling.

## Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy openpyxl sqlalchemy
```

## Files Overview

### 1. **data_preprocessing.py**
Data cleaning, transformation, and preparation

### 2. **analysis_rca.py**
Root Cause Analysis - Incident pattern identification

### 3. **forecasting.py**
Predictive analytics and time series forecasting

### 4. **pareto_analysis.py**
80/20 rule application and priority ranking

### 5. **nps_analysis.py**
Customer satisfaction and NPS trend analysis

### 6. **utils.py**
Helper functions and database connections

## Usage

```bash
# Step 1: Preprocess raw data
python data_preprocessing.py

# Step 2: Perform RCA
python analysis_rca.py

# Step 3: Run forecasting models
python forecasting.py

# Step 4: Pareto analysis
python pareto_analysis.py

# Step 5: NPS analysis
python nps_analysis.py
```

## Output Files

- `processed_data/` - Cleaned datasets
- `analysis_results/` - RCA outputs
- `forecasts/` - Prediction results
- `reports/` - Analysis reports

---

**All scripts are designed to work with the SQL database or CSV files!**
