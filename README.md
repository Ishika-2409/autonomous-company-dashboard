# Autonomous Company Automation Data Dashboard

A comprehensive data analytics and visualization project for autonomous vehicle fleet operations, designed for technical hiring teams and operations management.

## 📊 Project Overview

This dashboard demonstrates advanced data analytics capabilities including:
- **Real-time Performance Analytics**: Fleet utilization, operational efficiency
- **Predictive Analytics**: Forecasting maintenance needs, cost predictions
- **Root Cause Analysis (RCA)**: Incident analysis and pattern identification
- **Pareto Analysis**: 80/20 rule application for priority management
- **Business Intelligence**: Data-driven decision making with Power BI

## 🏗️ Project Structure

```
autonomy-company-dashboard/
├── 1_sample_datasets/           # Mock data in CSV format
├── 2_sql_scripts/               # Database setup and queries
├── 3_python_analysis/           # Data preprocessing and analysis
├── 4_power_bi/                  # DAX formulas and Power Query
├── 5_hiring_presentation/       # Documentation and insights
└── README.md
```

## 📁 Data Sources

### Recommended Public Datasets to Download:
1. **NYC Taxi Data** - For vehicle movement patterns (kaggle.com)
2. **IoT Sensor Data** - For vehicle diagnostics (kaggle.com)
3. **Weather Data** - For operational impact analysis (openweathermap.org)
4. **Traffic Data** - For route optimization insights (NHTSA.gov)

## 🔧 Tech Stack

- **Database**: SQL (T-SQL/MySQL)
- **Data Processing**: Python 3.8+, Pandas, NumPy
- **Visualization**: Power BI Desktop
- **Data Modeling**: DAX, Power Query M
- **Analysis**: Statistical analysis, forecasting

## 📈 Key Metrics & KPIs

### Operational Metrics
- Fleet Utilization Rate (%)
- Average Vehicle Uptime
- Maintenance Incidents per 1000 km
- On-Time Delivery Rate (%)
- Cost per Mile

### Performance Analytics
- NPS (Net Promoter Score) Trends
- Customer Satisfaction Scores
- Service Reliability Index
- Response Time Analytics

### Predictive Analytics
- Maintenance Forecasting (Days to Next Service)
- Cost Predictions (Monthly Operating Costs)
- Demand Forecasting
- Failure Risk Scoring

### Pareto Analysis
- Top 20% Issues Causing 80% Problems
- Priority Risk Factors
- High-Impact Improvement Areas

## 🚀 Quick Start

### Step 1: Load Sample Datasets
```bash
cd 1_sample_datasets
# Review all CSV files for mock data
```

### Step 2: Set Up Database
```bash
cd 2_sql_scripts
# Run SQL scripts in your database management tool
```

### Step 3: Run Python Analysis
```bash
cd 3_python_analysis
pip install -r requirements.txt
python data_preprocessing.py
python analysis_rca.py
python forecasting.py
```

### Step 4: Build Power BI Dashboard
```
cd 4_power_bi
# Open .pbix file in Power BI Desktop
# Connect to your SQL database or import CSV files
```

### Step 5: Review Presentation
```
cd 5_hiring_presentation
# Review documentation and key insights
```

## 📊 Dashboard Components

### 1. Executive Overview
- Real-time fleet status
- KPI scorecards
- Trend analysis

### 2. Performance Analytics
- Utilization heatmaps
- Efficiency metrics
- Cost analysis

### 3. Predictive Analytics
- Maintenance forecasting
- Cost predictions
- Risk scoring

### 4. Root Cause Analysis
- Incident clustering
- Pattern identification
- Impact assessment

### 5. Pareto Analysis
- Problem prioritization
- High-impact areas
- Action items

## 🎯 Use Cases

1. **For Operations Team**: Real-time monitoring, predictive maintenance, cost optimization
2. **For Hiring Team**: Demonstrate data analytics skills, business acumen, technical proficiency
3. **For Business Decisions**: Data-driven insights, forecasting, risk assessment

## 📖 Documentation

See `5_hiring_presentation/` for:
- Dashboard walkthrough
- Methodology documentation
- Business insights
- Technical implementation details

## 🔄 Data Pipeline

```
Raw Data (CSV) → Python Processing → SQL Database → Power BI Dashboard → Business Insights
```

## 📝 Next Steps

1. Download sample datasets from recommended sources
2. Load data into SQL database
3. Run Python preprocessing scripts
4. Import data into Power BI
5. Build visualizations using provided DAX formulas
6. Generate reports and insights

## 💡 Key Features to Highlight in Interviews

- ✅ End-to-end data pipeline implementation
- ✅ Real-time data processing with pandas
- ✅ Predictive modeling and forecasting
- ✅ Statistical analysis and RCA methodology
- ✅ Pareto principle application
- ✅ Advanced DAX and Power Query skills
- ✅ SQL database design and optimization
- ✅ Business-focused analytics approach

## 📧 Contact & Questions

For questions about this project, refer to the detailed documentation in `5_hiring_presentation/`

---

**Last Updated**: June 2026
**Status**: Active Development
**Version**: 1.0
