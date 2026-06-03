import pandas as pd
import numpy as np
from collections import Counter
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class RootCauseAnalysis:
    """Root Cause Analysis for incident management"""
    
    def __init__(self, severity_data, incidents_data):
        self.severity_df = severity_data
        self.incidents_df = incidents_data
        self.rca_results = {}
    
    def analyze_by_category(self):
        """Analyze incidents by root cause category"""
        print("\n" + "="*70)
        print("ROOT CAUSE ANALYSIS BY CATEGORY")
        print("="*70)
        
        category_analysis = self.severity_df.groupby('root_cause_category').agg({
            'incident_id': 'count',
            'business_impact_loss': ['sum', 'mean'],
            'avg_resolution_days': 'mean',
            'occurrence_count': 'sum'
        }).round(2)
        
        category_analysis.columns = ['Total_Incidents', 'Total_Loss', 'Avg_Loss_Per_Incident', 
                                     'Avg_Resolution_Days', 'Total_Occurrences']
        category_analysis = category_analysis.sort_values('Total_Loss', ascending=False)
        
        print("\n", category_analysis)
        self.rca_results['category_analysis'] = category_analysis
        return category_analysis
    
    def pareto_analysis(self):
        """Apply Pareto principle (80/20 rule)"""
        print("\n" + "="*70)
        print("PARETO ANALYSIS (80/20 RULE)")
        print("="*70)
        
        category_loss = self.severity_df.groupby('root_cause_category')['business_impact_loss'].sum().sort_values(ascending=False)
        total_loss = category_loss.sum()
        
        cumulative_loss = category_loss.cumsum()
        cumulative_percent = (cumulative_loss / total_loss * 100)
        
        pareto_df = pd.DataFrame({
            'Category': category_loss.index,
            'Total_Loss': category_loss.values,
            'Percentage': (category_loss / total_loss * 100).round(2).values,
            'Cumulative_Loss': cumulative_loss.values,
            'Cumulative_Percentage': cumulative_percent.values
        })
        
        # Identify 20% causes for 80% impact
        top_20_categories = pareto_df[pareto_df['Cumulative_Percentage'] <= 80]
        if len(top_20_categories) == 0:
            top_20_categories = pareto_df.head(1)
        
        print("\nTop Categories Contributing to 80% of Business Impact:")
        print(top_20_categories.to_string(index=False))
        print(f"\nNumber of categories to focus on: {len(top_20_categories)} out of {len(pareto_df)}")
        
        self.rca_results['pareto_analysis'] = pareto_df
        return pareto_df, top_20_categories
    
    def severity_distribution(self):
        """Analyze severity distribution"""
        print("\n" + "="*70)
        print("SEVERITY DISTRIBUTION ANALYSIS")
        print("="*70)
        
        severity_count = self.severity_df['severity'].value_counts().sort_values(ascending=False)
        severity_impact = self.severity_df.groupby('severity')['business_impact_loss'].sum().sort_values(ascending=False)
        
        severity_analysis = pd.DataFrame({
            'Incidents': severity_count.values,
            'Percentage': (severity_count / severity_count.sum() * 100).round(2).values,
            'Total_Impact_Loss': severity_impact.values,
            'Avg_Impact_Per_Incident': (severity_impact / severity_count).round(2).values
        }, index=severity_count.index)
        
        print("\n", severity_analysis)
        self.rca_results['severity_distribution'] = severity_analysis
        return severity_analysis
    
    def incident_type_analysis(self):
        """Analyze by incident type"""
        print("\n" + "="*70)
        print("INCIDENT TYPE ANALYSIS")
        print("="*70)
        
        type_analysis = self.severity_df.groupby('incident_category').agg({
            'incident_id': 'count',
            'business_impact_loss': ['sum', 'mean'],
            'avg_resolution_days': 'mean'
        }).round(2)
        
        type_analysis.columns = ['Count', 'Total_Loss', 'Avg_Loss', 'Avg_Resolution_Days']
        type_analysis = type_analysis.sort_values('Total_Loss', ascending=False).head(10)
        
        print("\nTop 10 Incident Types by Business Impact:")
        print(type_analysis)
        self.rca_results['incident_type'] = type_analysis
        return type_analysis
    
    def frequency_severity_correlation(self):
        """Correlate frequency with severity"""
        print("\n" + "="*70)
        print("FREQUENCY vs SEVERITY CORRELATION")
        print("="*70)
        
        freq_severity = self.severity_df.groupby(['root_cause_category', 'severity']).agg({
            'incident_id': 'count',
            'business_impact_loss': 'sum'
        }).round(2)
        
        freq_severity.columns = ['Incidents', 'Total_Loss']
        freq_severity = freq_severity.sort_values('Total_Loss', ascending=False)
        
        print("\nTop High-Frequency/High-Severity Combinations:")
        print(freq_severity.head(15))
        self.rca_results['freq_severity'] = freq_severity
        return freq_severity
    
    def resolution_time_analysis(self):
        """Analyze resolution times"""
        print("\n" + "="*70)
        print("RESOLUTION TIME ANALYSIS")
        print("="*70)
        
        resolution_stats = self.severity_df.groupby('root_cause_category').agg({
            'avg_resolution_days': ['min', 'max', 'mean', 'std']
        }).round(2)
        
        resolution_stats.columns = ['Min_Days', 'Max_Days', 'Avg_Days', 'Std_Dev']
        resolution_stats = resolution_stats.sort_values('Avg_Days', ascending=False)
        
        print("\nResolution Time by Category:")
        print(resolution_stats)
        self.rca_results['resolution_time'] = resolution_stats
        return resolution_stats
    
    def prevention_recommendations(self):
        """Generate prevention recommendations based on RCA"""
        print("\n" + "="*70)
        print("PREVENTION RECOMMENDATIONS")
        print("="*70)
        
        recommendations = self.severity_df.groupby('root_cause_category').agg({
            'prevention_recommended': lambda x: list(set(x.dropna())),
            'business_impact_loss': 'sum',
            'incident_id': 'count'
        }).sort_values('business_impact_loss', ascending=False)
        
        print("\nTop Prevention Actions by Impact:")
        for idx, (category, row) in enumerate(recommendations.iterrows(), 1):
            print(f"\n{idx}. {category}")
            print(f"   Total Loss: ${row['business_impact_loss']:,.2f}")
            print(f"   Incidents: {int(row['incident_id'])}")
            print(f"   Recommended Actions:")
            if row['prevention_recommended'] and row['prevention_recommended'][0]:
                for action in row['prevention_recommended'][:3]:
                    print(f"      • {action}")
        
        self.rca_results['recommendations'] = recommendations
        return recommendations
    
    def trend_analysis(self):
        """Analyze trends over time"""
        print("\n" + "="*70)
        print("INCIDENT TREND ANALYSIS")
        print("="*70)
        
        self.severity_df['date'] = pd.to_datetime(self.severity_df['date'])
        self.severity_df['month'] = self.severity_df['date'].dt.to_period('M')
        
        trend_data = self.severity_df.groupby('month').agg({
            'incident_id': 'count',
            'business_impact_loss': 'sum'
        })
        
        trend_data.columns = ['Incidents', 'Total_Loss']
        
        print("\nMonthly Incident Trends:")
        print(trend_data)
        
        # Calculate trend direction
        if len(trend_data) > 1:
            first_month = trend_data.iloc[0]['Incidents']
            last_month = trend_data.iloc[-1]['Incidents']
            trend_direction = 'INCREASING' if last_month > first_month else 'DECREASING'
            change_percent = abs((last_month - first_month) / first_month * 100)
            print(f"\nTrend Direction: {trend_direction} ({change_percent:.1f}%)")
        
        self.rca_results['trend'] = trend_data
        return trend_data
    
    def generate_rca_report(self):
        """Generate comprehensive RCA report"""
        print("\n" + "="*80)
        print("COMPREHENSIVE ROOT CAUSE ANALYSIS REPORT")
        print("="*80)
        
        # Run all analyses
        self.analyze_by_category()
        pareto_df, top_20 = self.pareto_analysis()
        self.severity_distribution()
        self.incident_type_analysis()
        self.frequency_severity_correlation()
        self.resolution_time_analysis()
        self.prevention_recommendations()
        self.trend_analysis()
        
        print("\n" + "="*80)
        print("EXECUTIVE SUMMARY")
        print("="*80)
        
        total_incidents = len(self.severity_df)
        total_loss = self.severity_df['business_impact_loss'].sum()
        avg_resolution = self.severity_df['avg_resolution_days'].mean()
        
        print(f"\nTotal Incidents Analyzed: {total_incidents}")
        print(f"Total Business Impact Loss: ${total_loss:,.2f}")
        print(f"Average Resolution Time: {avg_resolution:.2f} days")
        print(f"\nTop 3 Root Cause Categories:")
        
        for idx, (cat, row) in enumerate(self.rca_results['category_analysis'].head(3).iterrows(), 1):
            print(f"{idx}. {cat}: ${row['Total_Loss']:,.2f} ({row['Total_Incidents']:.0f} incidents)")
        
        print(f"\nFocus Areas (Pareto Analysis - Top 20% for 80% Impact):")
        for idx, row in top_20.iterrows():
            print(f"• {row['Category']}: ${row['Total_Loss']:,.2f} ({row['Percentage']:.1f}%)")
        
        print("\n" + "="*80)

def main():
    """Main execution"""
    print("Loading data for RCA analysis...")
    
    try:
        severity_df = pd.read_csv('processed_data/severity_processed.csv')
        incidents_df = pd.read_csv('processed_data/incidents_processed.csv')
    except:
        print("Using sample data from 1_sample_datasets")
        severity_df = pd.read_csv('1_sample_datasets/incidents_severity.csv')
        incidents_df = pd.read_csv('1_sample_datasets/maintenance_incidents.csv')
    
    # Perform RCA
    rca = RootCauseAnalysis(severity_df, incidents_df)
    rca.generate_rca_report()
    
    # Save results
    print("\nSaving RCA results...")
    for name, df in rca.rca_results.items():
        if isinstance(df, pd.DataFrame):
            df.to_csv(f'analysis_results/rca_{name}.csv')
            print(f"✓ Saved rca_{name}.csv")

if __name__ == "__main__":
    main()
