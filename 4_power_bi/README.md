# Power BI Dashboard Documentation

This folder contains Power BI dashboard files, DAX formulas, and Power Query scripts.

## Files Overview

### 1. **autonomous_fleet_dashboard.pbix**
Main Power BI dashboard file (open with Power BI Desktop)

### 2. **dax_formulas.md**
All DAX formulas used in the dashboard

### 3. **power_query_scripts.m**
Power Query M scripts for data transformation

### 4. **dashboard_guide.md**
Step-by-step guide to build the dashboard

## Quick Start

### Step 1: Open Power BI Desktop
- Download from: https://powerbi.microsoft.com/desktop

### Step 2: Import Data

**Option A: From CSV Files**
```
Get Data → Text/CSV → Select CSV files from 1_sample_datasets/
```

**Option B: From SQL Database**
```
Get Data → SQL Server → Enter server and database details
```

### Step 3: Create Visualizations
- Add tiles, charts, gauges
- Apply DAX formulas for calculations
- Set up interactive filters

## Dashboard Pages

### Page 1: Executive Overview
- Fleet Status KPIs
- Daily Revenue & Costs
- Vehicle Utilization Rate
- Active Vehicles Count

### Page 2: Performance Analytics
- Fleet Efficiency Metrics
- Revenue Trends
- Cost Analysis
- Profit Margin Trends

### Page 3: Predictive Analytics
- Failure Risk Scoring
- Maintenance Forecast
- Revenue Forecast
- Operational Efficiency Trends

### Page 4: Root Cause Analysis
- Top Incidents by Category
- Severity Distribution
- Business Impact Analysis
- Pareto Chart (80/20 Rule)

### Page 5: Customer Insights
- NPS Trends
- Satisfaction Ratings
- Feedback Categories
- Route Performance

## Key DAX Formulas

### 1. Total Revenue
```dax
Total_Revenue = SUM(Financial[total_revenue])
```

### 2. Operating Profit
```dax
Operating_Profit = 
VAR Revenue = SUM(Financial[total_revenue])
VAR Costs = SUM(Financial[operational_costs]) + 
            SUM(Financial[maintenance_costs]) + 
            SUM(Financial[fuel_costs])
RETURN Revenue - Costs
```

### 3. Fleet Utilization Rate
```dax
Fleet_Utilization = 
VAR ActiveVehicles = DISTINCTCOUNT(Daily_Operations[vehicle_id])
VAR TotalVehicles = DISTINCTCOUNT(Vehicles[vehicle_id])
RETURN DIVIDE(ActiveVehicles, TotalVehicles, 0) * 100
```

### 4. Average NPS Score
```dax
Avg_NPS = AVERAGEX(Customer_Feedback, Customer_Feedback[nps_score])
```

### 5. Failure Risk Score
```dax
Failure_Risk_Score = 
VAR BatteryRisk = (100 - MAX(Predictive_Maintenance[battery_health])) * 0.25
VAR EngineRisk = (MAX(Predictive_Maintenance[engine_temperature]) / 120) * 100 * 0.25
VAR BrakeRisk = MAX(Predictive_Maintenance[brake_wear_percentage]) * 0.25
VAR PredictedRisk = MAX(Predictive_Maintenance[predicted_failure_risk]) * 0.25
RETURN BatteryRisk + EngineRisk + BrakeRisk + PredictedRisk
```

## Publishing to Power BI Service

1. File → Publish
2. Select workspace
3. Share dashboard with team
4. Set up automatic refresh

---

**Complete Power BI implementation ready for production!**
