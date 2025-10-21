# Global Tuberculosis Burden Analysis

**MCSC 2108: Data Visualization - Final Examination Report**  
**Author:** Daniel Wanjal Machimbo  
**Institution:** The Cooperative University of Kenya  
**Date:** October 2025

## Overview

This repository contains a comprehensive analysis of global tuberculosis (TB) burden patterns from 1990-2022 using WHO surveillance data. The analysis demonstrates advanced data visualization techniques and provides evidence-based insights for TB control programs.

## Repository Structure

```
├── README.md                           # This file
├── TB_Burden_Country.csv              # Raw WHO dataset
├── requirements.txt                    # Python dependencies
├── data/
│   └── TB_Burden_Country_clean.csv    # Cleaned dataset
├── figures/                            # Generated visualizations (PNG, 300 DPI)
│   ├── choropleth_incidence_per100k_2022.png
│   ├── top10_incidence_per100k_2022.png
│   ├── trends_top5.png
│   ├── stacked_area_region.png
│   ├── heatmap_region_year.png
│   ├── scatter_incidence_vs_deaths.png
│   └── small_multiples_demographics.png
├── notebooks/
│   └── TB_Burden_Report.ipynb         # Main analysis notebook
└── report/
    └── MCSC2108_TB_Burden_Report.pdf  # Final PDF report
```

## Key Features

### Visualizations Generated
1. **Global Choropleth Map** - Worldwide TB incidence distribution
2. **Top 10 Countries Bar Chart** - Highest burden countries with 5-year trends
3. **Multi-line Trends** - Temporal patterns for highest-burden countries
4. **Regional Stacked Area Chart** - WHO region composition over time
5. **Regional Heatmap** - Year-by-region incidence patterns
6. **Incidence vs Mortality Scatter** - Correlation analysis with regional context
7. **Demographic Analysis** - Age/sex stratification (placeholder for future data)

### Technical Specifications
- **Color Schemes**: Viridis (colorblind-safe) for sequential data, Set1 for categorical
- **Resolution**: 300 DPI for all figures (publication-ready)
- **Geographic Standards**: ISO 3166 country codes with automated generation
- **Data Quality**: Comprehensive outlier detection and missing data handling

## Reproduction Instructions

### Prerequisites
- Python 3.10+
- Jupyter Notebook/Lab
- LaTeX distribution (for PDF export)

### Setup Environment

```bash
# Clone repository
git clone https://github.com/MadScie254/Exam101.git
cd Exam101

# Install dependencies
pip install -r requirements.txt

# Additional system dependencies (if needed)
# For Windows: install MiKTeX or TeX Live
# For macOS: brew install --cask mactex  
# For Linux: sudo apt-get install texlive-full
```

### Run Analysis

```bash
# Start Jupyter Notebook
jupyter notebook

# Open notebooks/TB_Burden_Report.ipynb
# Run all cells (Cell → Run All)
```

### Generate PDF Report

**Option 1: Automated (if LaTeX available)**
```bash
jupyter nbconvert --to pdf notebooks/TB_Burden_Report.ipynb --output-dir report --output MCSC2108_TB_Burden_Report
```

**Option 2: Via HTML (recommended)**
```bash
# Convert to HTML first
jupyter nbconvert --to html notebooks/TB_Burden_Report.ipynb --output-dir report --output MCSC2108_TB_Burden_Report

# Then print to PDF from browser or use weasyprint
pip install weasyprint
weasyprint report/MCSC2108_TB_Burden_Report.html report/MCSC2108_TB_Burden_Report.pdf
```

**Option 3: Manual**
1. Open notebook in Jupyter
2. File → Download as → PDF via LaTeX
3. Save to `report/` directory

### Expected Outputs

After successful execution:
- ✅ 7 publication-quality figures in `figures/`
- ✅ Cleaned dataset in `data/TB_Burden_Country_clean.csv`
- ✅ Final PDF report in `report/MCSC2108_TB_Burden_Report.pdf`

## Data Source & Methods

**Dataset**: WHO Global TB Report Country Profiles  
**Temporal Coverage**: 1990-2022  
**Geographic Coverage**: 194 countries and territories  
**Key Metrics**: Incidence, prevalence, mortality (per 100,000 population)

**Analytical Approach**:
- Robust data loading with encoding detection
- Automated ISO code generation using fuzzy matching
- Outlier detection and flagging (no removal)
- Per-capita standardization for fair country comparison
- Regional aggregation using WHO definitions

## Academic Context

This analysis fulfills requirements for **MCSC 2108: Data Visualization** examining:
- **Data Preparation**: Automated cleaning, transformation, validation
- **Visual Elements**: Color theory, accessibility, annotation strategies  
- **Chart Types**: Choropleth, bar, line, area, heatmap, scatter plots
- **Advanced Techniques**: Multi-dimensional encoding, regression overlays
- **Tools Integration**: Plotly, matplotlib, seaborn, geopandas

## Ethical Considerations

1. **Data Provenance**: WHO estimates combine surveillance data with mathematical models
2. **Uncertainty Communication**: High-burden countries may have higher estimate uncertainty
3. **Representational Fairness**: Per-capita rates prevent bias toward large populations
4. **Accessibility**: Colorblind-safe palettes and alternative text for figures

## Technical Dependencies

See `requirements.txt` for complete list. Key packages:
- pandas>=1.5.0 (data manipulation)
- plotly>=5.0.0 (interactive visualization)
- matplotlib>=3.6.0 (static visualization)
- geopandas>=0.12.0 (geographic data)
- pycountry>=22.0.0 (ISO code matching)
- kaleido>=0.2.1 (image export)

## Contact

**Daniel Wanjal Machimbo**  
Master of Science in Computer Science  
The Cooperative University of Kenya  
Email: [Your Email]

## License

This analysis is created for academic purposes (MCSC 2108 examination). Data source attribution to WHO Global TB Programme.
Data Viz
