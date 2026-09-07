import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Set styling
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['figure.dpi'] = 300

os.makedirs('figures', exist_ok=True)

# 1. Load Data
df = pd.read_csv('seasonal_agriculture_data.csv')
print(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")

# 2. Data Cleaning & Preprocessing
# Impute missing values
if df['Soil_Moisture_pct'].isnull().sum() > 0:
    df['Soil_Moisture_pct'] = df['Soil_Moisture_pct'].fillna(df.groupby(['Season', 'Crop'])['Soil_Moisture_pct'].transform('median'))
    df['Soil_Moisture_pct'] = df['Soil_Moisture_pct'].fillna(df['Soil_Moisture_pct'].median())

if df['Yield_Tonnes_Ha'].isnull().sum() > 0:
    df['Yield_Tonnes_Ha'] = df['Yield_Tonnes_Ha'].fillna(df['Production_Tonnes'] / df['Farm_Area_Hectares'])

if df['Rainfall_mm'].isnull().sum() > 0:
    df['Rainfall_mm'] = df['Rainfall_mm'].fillna(df.groupby('Season')['Rainfall_mm'].transform('median'))

# Feature Engineering
df['Profit_Margin_pct'] = np.where(df['Revenue_INR'] > 0, (df['Profit_INR'] / df['Revenue_INR']) * 100, 0)
df['ROI_pct'] = np.where(df['Total_Cost_INR'] > 0, (df['Profit_INR'] / df['Total_Cost_INR']) * 100, 0)
df['Cost_Per_Hectare'] = df['Total_Cost_INR'] / df['Farm_Area_Hectares']
df['Revenue_Per_Hectare'] = df['Revenue_INR'] / df['Farm_Area_Hectares']
df['Profit_Per_Hectare'] = df['Profit_INR'] / df['Farm_Area_Hectares']

print("Data Cleaning & Feature Engineering Complete!")

# --- FIGURE 1: Seasonal Comparison of Agricultural & Economic Performance ---
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
season_palette = {'Kharif': '#2b5c8f', 'Rabi': '#2ca02c', 'Zaid': '#d62728'}

# Yield by Season
sns.barplot(data=df, x='Season', y='Yield_Tonnes_Ha', ax=axes[0, 0], palette=season_palette, errorbar=None)
axes[0, 0].set_title('Average Crop Yield (Tonnes/Ha) by Season', weight='bold')
axes[0, 0].set_ylabel('Yield (Tonnes/Ha)')

# Rainfall & Moisture by Season
season_env = df.groupby('Season')[['Rainfall_mm', 'Soil_Moisture_pct']].mean().reset_index()
season_env_melted = season_env.melt(id_vars='Season', value_vars=['Rainfall_mm', 'Soil_Moisture_pct'])
sns.barplot(data=df, x='Season', y='Rainfall_mm', ax=axes[0, 1], palette=season_palette, errorbar=None)
axes[0, 1].set_title('Average Rainfall (mm) by Season', weight='bold')
axes[0, 1].set_ylabel('Rainfall (mm)')

# Profit by Season
sns.barplot(data=df, x='Season', y='Profit_INR', ax=axes[1, 0], palette=season_palette, errorbar=None)
axes[1, 0].set_title('Average Net Profit (INR) by Season', weight='bold')
axes[1, 0].set_ylabel('Net Profit (INR)')

# Water Efficiency by Season
sns.barplot(data=df, x='Season', y='Water_Efficiency_t_per_1000m3', ax=axes[1, 1], palette=season_palette, errorbar=None)
axes[1, 1].set_title('Water Efficiency (Tonnes / 1000 m³) by Season', weight='bold')
axes[1, 1].set_ylabel('Water Efficiency (t/1000m³)')

plt.tight_layout()
fig1_path = 'figures/figure1_seasonal_macro_comparison.png'
plt.savefig(fig1_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {fig1_path}")

# --- FIGURE 2: Crop-Wise Yield & Economic Viability Across Seasons ---
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

crop_yield = df.groupby(['Crop', 'Season'])['Yield_Tonnes_Ha'].mean().reset_index()
sns.barplot(data=crop_yield, x='Crop', y='Yield_Tonnes_Ha', hue='Season', ax=axes[0], palette=season_palette)
axes[0].set_title('Crop-Wise Average Yield across Seasons', weight='bold')
axes[0].set_ylabel('Yield (Tonnes/Ha)')
axes[0].tick_params(axis='x', rotation=45)

crop_profit = df.groupby(['Crop', 'Season'])['Profit_Per_Hectare'].mean().reset_index()
sns.barplot(data=crop_profit, x='Crop', y='Profit_Per_Hectare', hue='Season', ax=axes[1], palette=season_palette)
axes[1].set_title('Crop-Wise Profit per Hectare (INR/Ha) across Seasons', weight='bold')
axes[1].set_ylabel('Profit per Hectare (INR/Ha)')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
fig2_path = 'figures/figure2_crop_performance_by_season.png'
plt.savefig(fig2_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {fig2_path}")

# --- FIGURE 3: Environmental Factors & Pest Risk Analysis ---
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

sns.scatterplot(data=df, x='Humidity_pct', y='Disease_Pest_Risk_pct', hue='Season', palette=season_palette, style='Season', s=80, alpha=0.8, ax=axes[0])
axes[0].set_title('Humidity vs. Disease/Pest Risk % Across Seasons', weight='bold')
axes[0].set_xlabel('Humidity (%)')
axes[0].set_ylabel('Disease & Pest Risk (%)')

sns.boxplot(data=df, x='Season', y='Avg_Temperature_C', palette=season_palette, ax=axes[1])
axes[1].set_title('Seasonal Temperature Distribution (°C)', weight='bold')
axes[1].set_ylabel('Average Temperature (°C)')

plt.tight_layout()
fig3_path = 'figures/figure3_environmental_pest_risk.png'
plt.savefig(fig3_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {fig3_path}")

# --- FIGURE 4: Resource Utilization (Irrigation & Water Efficiency) ---
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

irrig_water = df.groupby(['Irrigation_Method', 'Season'])['Water_Used_m3'].mean().reset_index()
sns.barplot(data=irrig_water, x='Irrigation_Method', y='Water_Used_m3', hue='Season', palette=season_palette, ax=axes[0])
axes[0].set_title('Water Usage (m³) by Irrigation Method & Season', weight='bold')
axes[0].set_ylabel('Average Water Used (m³)')

irrig_eff = df.groupby(['Irrigation_Method', 'Season'])['Water_Efficiency_t_per_1000m3'].mean().reset_index()
sns.barplot(data=irrig_eff, x='Irrigation_Method', y='Water_Efficiency_t_per_1000m3', hue='Season', palette=season_palette, ax=axes[1])
axes[1].set_title('Water Efficiency by Irrigation Method & Season', weight='bold')
axes[1].set_ylabel('Water Efficiency (Tonnes / 1000 m³)')

plt.tight_layout()
fig4_path = 'figures/figure4_irrigation_water_efficiency.png'
plt.savefig(fig4_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {fig4_path}")

# --- FIGURE 5: Correlation Heatmap of Key Indicators ---
plt.figure(figsize=(12, 10))
numeric_cols = [
    'Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 'Sunlight_Hours_Day',
    'Soil_Moisture_pct', 'Fertilizer_kg_ha', 'Pesticide_Litre_ha',
    'Seed_Quality_Score', 'Yield_Tonnes_Ha', 'Total_Cost_INR', 'Revenue_INR',
    'Profit_INR', 'Water_Efficiency_t_per_1000m3', 'Disease_Pest_Risk_pct'
]
corr_matrix = df[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1, square=True, linewidths=0.5)
plt.title('Correlation Matrix of Environmental, Resource & Economic Variables', weight='bold', pad=15)
plt.tight_layout()
fig5_path = 'figures/figure5_correlation_heatmap.png'
plt.savefig(fig5_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {fig5_path}")

# --- FIGURE 6: Machine Learning Feature Importance (Predicting Crop Yield) ---
# Prepare features for ML model
features = ['Farm_Area_Hectares', 'Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 
            'Sunlight_Hours_Day', 'Soil_pH', 'Soil_Moisture_pct', 'Nitrogen_kg_ha', 
            'Phosphorus_kg_ha', 'Potassium_kg_ha', 'Fertilizer_kg_ha', 
            'Pesticide_Litre_ha', 'Seed_Quality_Score', 'Water_Used_m3']

X = df[features]
y = df['Yield_Tonnes_Ha']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

feature_importances = pd.Series(rf.feature_importances_, index=features).sort_values(ascending=True)

plt.figure(figsize=(10, 6))
feature_importances.plot(kind='barh', color='#2b5c8f')
plt.title(f'Feature Importance in Predicting Crop Yield (Random Forest R²={r2:.2f})', weight='bold')
plt.xlabel('Relative Importance Score')
plt.tight_layout()
fig6_path = 'figures/figure6_ml_yield_drivers.png'
plt.savefig(fig6_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {fig6_path}")

# Print summary table
summary_stats = df.groupby('Season').agg({
    'Yield_Tonnes_Ha': ['mean', 'std'],
    'Rainfall_mm': 'mean',
    'Avg_Temperature_C': 'mean',
    'Profit_INR': 'mean',
    'Water_Efficiency_t_per_1000m3': 'mean',
    'Disease_Pest_Risk_pct': 'mean'
})
print("\n=== Seasonal Summary Statistics ===")
print(summary_stats)
