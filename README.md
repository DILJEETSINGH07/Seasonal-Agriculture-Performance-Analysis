# Seasonal Agriculture Performance Analysis
### VOIS AICTE Internship Batch 1 (2026–2027) — Major Project

## 🌾 Project Overview
Agricultural performance is fundamentally influenced by seasonal variations in environmental conditions (rainfall, temperature, sunlight, humidity), agronomic practices, resource availability (water, fertilizer, seeds), and market dynamics. This project provides an in-depth data analytics, statistical evaluation, and machine learning framework to analyze seasonal agricultural productivity across **Kharif** (Monsoon), **Rabi** (Winter), and **Zaid** (Summer) seasons.

---

## 📊 Key Highlights & Findings
1. **Macro Seasonal Variations**:
   - **Kharif**: Highest precipitation (>850 mm avg) and humidity (>72%), leading to peak pest vulnerability (53.8% avg).
   - **Rabi**: Moderate temperatures (~23.5°C avg) and stable market pricing with lower disease vulnerability (40.0%).
   - **Zaid**: High sunlight and temperature (>31.8°C); strong yields for high-efficiency cash crops when supported by micro-irrigation.
2. **Crop Viability & Economics**:
   - High gross revenue generators: **Sugarcane** and **Chilli**.
   - Consistent staple ROI: **Wheat** and **Pulses**.
   - Risk factor: Unmanaged **Rice** under flood irrigation during dry seasons causes negative profit margins.
3. **Resource Efficiency**:
   - **Drip Irrigation** delivers **4.2+ tonnes / 1000 m³** water efficiency, saving ~40% water compared to flood systems.
4. **Predictive Modeling**:
   - Random Forest regression identifies **Soil Moisture %**, **Nitrogen (kg/ha)**, **Seed Quality Score**, and **Water Volume** as the top 4 predictive drivers of crop yield ($R^2 \approx 0.88$).

---

## 📁 Repository Structure
```
├── analysis.ipynb                  # Complete Jupyter Notebook with code, plots & insights
├── run_full_analysis.py            # Automated analysis & visualization generation script
├── seasonal_agriculture_data.csv   # Agricultural dataset (28 features)
├── PROJECT_REPORT.md               # Detailed academic project report
├── figures/                        # High-resolution generated charts for presentations
│   ├── figure1_seasonal_macro_comparison.png
│   ├── figure2_crop_performance_by_season.png
│   ├── figure3_environmental_pest_risk.png
│   ├── figure4_irrigation_water_efficiency.png
│   ├── figure5_correlation_heatmap.png
│   └── figure6_ml_yield_drivers.png
└── README.md                       # Project overview documentation
```

---

## 🚀 Getting Started
1. **Clone the repository**:
   ```bash
   git clone https://github.com/DILJEETSINGH07/Seasonal-Agriculture-Performance-Analysis.git
   cd Seasonal-Agriculture-Performance-Analysis
   ```
2. **Install dependencies**:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
3. **Run the analysis**:
   ```bash
   python run_full_analysis.py
   ```
   Or open and execute `analysis.ipynb` in your Jupyter / VS Code environment.

---

## 👨‍💻 Author & Attribution
- **Student Name**: Aswini Kumar
- **Program**: VOIS AICTE Batch 1 (2026–2027)
- **Course**: Data Visualization & Analytics
