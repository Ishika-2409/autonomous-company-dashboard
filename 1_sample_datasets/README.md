# Sample Datasets - Mock Autonomous Fleet Data

This folder contains CSV files with mock data for an autonomous vehicle fleet. These datasets are designed to demonstrate real-world analytics scenarios.

## Dataset Files

### 1. **vehicles_fleet.csv**
Core vehicle information and current status

**Columns:**
- vehicle_id: Unique identifier
- vehicle_type: Type of autonomous vehicle
- registration_year: Year registered
- total_kilometers: Lifetime mileage
- last_maintenance_date: Last service date
- operational_status: Current status
- assigned_zone: Operating region
- acquisition_cost: Purchase price

---

### 2. **daily_operations.csv**
Daily operational metrics for each vehicle

**Columns:**
- date: Operation date
- vehicle_id: Vehicle identifier
- kilometers_traveled: Distance covered
- hours_operational: Operating hours
- trips_completed: Number of trips
- passengers_served: Total passengers
- revenue_generated: Income from operations
- fuel_consumption: Fuel/energy used
- operational_cost: Daily operating cost

---

### 3. **maintenance_incidents.csv**
Maintenance events, failures, and incidents

**Columns:**
- incident_id: Unique incident identifier
- vehicle_id: Vehicle involved
- incident_date: When it occurred
- incident_type: Type of maintenance/failure
- severity_level: Critical/High/Medium/Low
- component_affected: What failed
- resolution_time_hours: Time to fix
- repair_cost: Cost to repair
- downtime_impact: Business impact

---

### 4. **customer_feedback.csv**
NPS and customer satisfaction data

**Columns:**
- feedback_id: Unique identifier
- vehicle_id: Vehicle rated
- date: Feedback date
- nps_score: Net Promoter Score (0-10)
- rating: Overall rating (1-5)
- feedback_category: Safety/Comfort/Reliability/Price
- passenger_count: Number of passengers
- trip_duration_minutes: Trip length
- feedback_text: Customer comments

---

### 5. **predictive_maintenance_data.csv**
IoT sensor readings for predictive analysis

**Columns:**
- reading_id: Unique identifier
- vehicle_id: Vehicle ID
- timestamp: Reading time
- battery_health: Battery percentage (0-100)
- engine_temperature: Temperature in Celsius
- tire_pressure: Pressure PSI
- brake_wear_percentage: Brake wear level
- suspension_condition: Condition score
- software_version: Current software
- predicted_failure_risk: Risk score (0-100)

---

### 6. **route_data.csv**
Route and traffic analytics

**Columns:**
- route_id: Unique route identifier
- vehicle_id: Vehicle used
- date: Date traveled
- origin_zone: Starting location
- destination_zone: End location
- planned_duration_minutes: Expected time
- actual_duration_minutes: Actual time
- distance_kilometers: Route distance
- traffic_congestion_level: Congestion score
- weather_condition: Weather at time

---

### 7. **financial_data.csv**
Revenue and cost analysis

**Columns:**
- month: Month of data
- total_revenue: Total income
- operational_costs: Operating expenses
- maintenance_costs: Maintenance expenses
- fuel_costs: Fuel/energy costs
- insurance_costs: Insurance expenses
- salary_costs: Staff costs
- depreciation: Asset depreciation
- profit_loss: Net profit/loss
- vehicles_active: Active vehicles in month

---

### 8. **incidents_severity.csv**
Detailed incident classification for RCA

**Columns:**
- incident_id: Incident identifier
- date: Incident date
- root_cause_category: Root cause category
- incident_category: Type of incident
- severity: Severity level
- vehicle_id: Vehicle involved
- occurrence_count: How many times this month
- avg_resolution_days: Average fix time
- business_impact_loss: Revenue lost
- prevention_recommended: Prevention action

---

## Data Characteristics

- **Time Period**: 12 months (Mock data from Jan-Dec 2025)
- **Fleet Size**: 50 autonomous vehicles
- **Zones**: 5 operational zones (Zone_A, Zone_B, Zone_C, Zone_D, Zone_E)
- **Update Frequency**: Daily
- **Data Quality**: 98% completeness (realistic scenario with some missing values)

## How to Use

1. **Download all CSV files** to your local machine
2. **Load into SQL database** using scripts in `2_sql_scripts/`
3. **Process with Python** using scripts in `3_python_analysis/`
4. **Import into Power BI** via SQL or directly from CSV
5. **Build dashboards** using DAX formulas in `4_power_bi/`

## Data Sources

For real-world data, consider these public sources:
- **NYC Taxi Data**: https://www.kaggle.com/datasets/yasserh/uber-fares-dataset
- **IoT Sensor Data**: https://www.kaggle.com/datasets/theforcecoder/iot-dataset
- **Vehicle Analytics**: https://www.kaggle.com/datasets/sudhirpatil55/vehicle-dataset
- **Weather Data**: https://openweathermap.org/api

## Key Metrics Demonstrated

✅ Fleet Utilization Rate
✅ Maintenance Analytics
✅ NPS & Satisfaction Trends
✅ Predictive Failure Risk
✅ Cost Analysis & Forecasting
✅ Route Optimization
✅ Pareto Analysis (80/20 rule)
✅ Root Cause Analysis

---

**Ready to use for Power BI dashboarding and Python analysis!**
