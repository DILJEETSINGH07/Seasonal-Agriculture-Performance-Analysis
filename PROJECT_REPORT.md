# VOIS AICTE Batch 1 (2026–2027) Major Project Report
# **Seasonal Agriculture Performance Analysis**

---

## 1. Project Overview & Metadata
- **Project Title**: Seasonal Agriculture Performance Analysis
- **Program**: VOIS AICTE Internship / Coursework Batch 1 (2026–2027)
- **Domain**: Data Analytics, Statistical Modeling & Data Visualization
- **Tools Used**: Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn), Jupyter Notebook (`analysis.ipynb`), VS Code

---

## 2. Problem Statement
Agricultural activities are fundamentally influenced by seasonal variations in environmental conditions (rainfall, temperature, sunlight, humidity), agronomic practices, resource availability (water, fertilizer, seeds), and volatile market dynamics. Consequently, agricultural output and profitability fluctuate dramatically from one season to another (*Kharif*, *Rabi*, *Zaid*).

Raw agricultural records often obscure the underlying factors driving these seasonal variations. The core objective of this project is to analyze the multi-variable agricultural dataset to identify patterns, trends, risk factors, and resource efficiencies across seasons, ultimately delivering data-backed recommendations for farmers, agronomists, and policy planners.

---

## 3. Key Research & Analytical Questions Answered
1. **Macro Seasonal Trends**: How do yield, total cost, revenue, and net profit vary across *Kharif* (Monsoon), *Rabi* (Winter), and *Zaid* (Summer)?
2. **Crop Viability**: Which crops deliver the highest return on investment (ROI) and profitability per hectare across different seasonal windows?
3. **Resource Efficiency**: How does irrigation methodology (Drip, Sprinkler, Flood, Rainfed) affect water usage and water efficiency across seasons?
4. **Environmental Impact & Pest Dynamics**: What is the correlation between ambient humidity, temperature, and disease/pest risk across seasons?
5. **Predictive Drivers of Crop Yield**: Which environmental and soil variables most significantly determine overall crop yield?

---

## 4. Dataset Overview & Data Cleaning

### Data Dictionary
| Variable | Data Type | Description |
| :--- | :--- | :--- |
| `Farm_ID` | String | Unique farm identifier |
| `State` / `District` | Categorical | Geographic location |
| `Crop` | Categorical | Crop cultivated (Wheat, Rice, Maize, Pulses, Cotton, Chilli, Groundnut, Sugarcane) |
| `Season` | Categorical | Cultivation season (*Kharif*, *Rabi*, *Zaid*) |
| `Farm_Area_Hectares`| Numerical | Farm plot size in hectares |
| `Rainfall_mm` | Numerical | Total seasonal precipitation (mm) |
| `Avg_Temperature_C` | Numerical | Mean ambient temperature (°C) |
| `Humidity_pct` | Numerical | Relative humidity (%) |
| `Sunlight_Hours_Day`| Numerical | Daily average sunshine duration |
| `Soil_pH`, `Moisture`| Numerical | Soil acidity and moisture percentage |
| `Nitrogen`, `P`, `K` | Numerical | Macronutrients applied (kg/ha) |
| `Irrigation_Method` | Categorical | Drip, Sprinkler, Flood, Rainfed |
| `Fertilizer`, `Pesticide` | Numerical | Chemical inputs per hectare |
| `Seed_Quality_Score` | Numerical | Quality index (0.0 to 1.0) |
| `Yield_Tonnes_Ha` | Numerical | Yield per hectare |
| `Production_Tonnes` | Numerical | Total output produced |
| `Market_Price_INR_Tonne`| Numerical | Realized market selling price per tonne |
| `Total_Cost_INR` | Numerical | Total production expenditure |
| `Revenue_INR` | Numerical | Gross income from sales |
| `Profit_INR` | Numerical | Net profit/loss (`Revenue - Total_Cost`) |
| `Water_Used_m3` | Numerical | Total water volume utilized |
| `Water_Efficiency` | Numerical | Production tonnes per 1000 m³ of water |
| `Disease_Pest_Risk_pct`| Numerical | Disease and pest vulnerability index (%) |

### Data Cleaning & Imputation
- **Missing Value Handling**: Imputed sparse missing values in `Soil_Moisture_pct`, `Yield_Tonnes_Ha`, and `Rainfall_mm` using grouped median imputation by `(Season, Crop)` to avoid distributional distortion.
- **Engineered Metrics**: Created `Profit_Margin_pct`, `ROI_pct`, and `Profit_Per_Hectare` to enable fair comparisons across different farm plot sizes.

---

## 5. Key Findings & Empirical Results

### 1. Macro Seasonal Performance
- **Kharif (Monsoon)**: Characterized by high precipitation (mean > 850 mm) and high humidity (> 72%). Highest pest vulnerability (mean disease risk **53.8%**). Yields average **4.15 Tonnes/Ha**.
- **Rabi (Winter)**: Moderate temperatures (mean ~23.5°C) with lower pest risk (**40.0%**). Yields average **3.45 Tonnes/Ha**, but exhibits higher economic stability with lower input losses.
- **Zaid (Summer)**: High temperatures (mean ~31.8°C) and low rainfall. Delivers strong yields (**4.62 Tonnes/Ha**) for high-efficiency cash crops (Sugarcane, Chilli, specialized Maize) when supported by micro-irrigation.

### 2. Crop Profitability Leaders
- **Top Gross Revenue Generators**: *Sugarcane* and *Chilli* produce the highest profit per hectare (exceeding INR 50,000/ha in optimal seasons).
- **Consistent Staples**: *Wheat* and *Pulses* maintain reliable profit margins across diverse soil moisture conditions.
- **Loss Risk Factors**: Unplanned *Rice* cultivation under flood irrigation during low-rainfall seasons incurs significant negative margins due to excessive pumping and input costs.

### 3. Irrigation & Resource Efficiency
- **Drip Irrigation**: Delivers the highest water efficiency (average **4.2+ tonnes / 1000 m³**), cutting water consumption by **38–45%** compared to flood systems.
- **Flood Irrigation**: Accounts for the highest total water consumption (**> 12,000 m³** per cycle on large plots) while yielding the lowest average water productivity index.

### 4. Machine Learning Feature Importance (Predicting Yield)
A **Random Forest Regressor** trained on environmental and input parameters achieved high explanatory power ($R^2 \approx 0.88$):
1. **Soil Moisture % & Nitrogen (kg/ha)**: Top 2 primary determinants of crop yield.
2. **Seed Quality Score**: Contributes ~18% relative importance to final yield variance.
3. **Irrigation Volume & Water Timing**: Critical differentiator during Rabi and Zaid cycles.

---

## 6. Actionable Recommendations for Agricultural Planning
1. **Adopt Micro-Irrigation (Drip / Sprinkler)**: Transitioning from traditional flood irrigation to drip systems can save over 40% of agricultural water while preventing soil nutrient leaching.
2. **Preemptive Pest Management in Kharif**: Implement bio-fungicide and automated alert systems when humidity exceeds 70% during the monsoon window.
3. **Crop-Season Matching**: Prioritize pulse and oilseed cultivation in water-stressed Rabi/Zaid plots, reserving heavy water crops (sugarcane, paddy) exclusively for high-precipitation Kharif seasons or drip-enabled farms.
4. **Soil Health Monitoring**: Maintain balanced NPK application tailored to soil pH levels to prevent over-fertilization cost penalties.

---

## 7. Generated Visualizations Guide (For PPT Slides)
All high-resolution figures are generated in the `figures/` directory:
- [figure1_seasonal_macro_comparison.png](file:///c:/Users/PC/Downloads/DATAproject/figures/figure1_seasonal_macro_comparison.png): Macro comparison of Yield, Rainfall, Profit, and Water Efficiency.
- [figure2_crop_performance_by_season.png](file:///c:/Users/PC/Downloads/DATAproject/figures/figure2_crop_performance_by_season.png): Crop-wise yield and profit per hectare by season.
- [figure3_environmental_pest_risk.png](file:///c:/Users/PC/Downloads/DATAproject/figures/figure3_environmental_pest_risk.png): Humidity vs. pest risk and seasonal temperature distributions.
- [figure4_irrigation_water_efficiency.png](file:///c:/Users/PC/Downloads/DATAproject/figures/figure4_irrigation_water_efficiency.png): Water usage and efficiency by irrigation method.
- [figure5_correlation_heatmap.png](file:///c:/Users/PC/Downloads/DATAproject/figures/figure5_correlation_heatmap.png): Inter-variable correlation matrix.
- [figure6_ml_yield_drivers.png](file:///c:/Users/PC/Downloads/DATAproject/figures/figure6_ml_yield_drivers.png): Random Forest feature importance ranking for yield drivers.
