# MotoGP Fan Reaction Analysis

## Project Overview

This project investigates how MotoGP fans react to race results by analyzing Google search trends. We wanted to see if popular riders get more attention after winning compared to less-known riders.

The main question we tried to answer: **Do fans search more for already-famous riders after they win, or do underdog victories create bigger spikes in interest?**

---

## Motivation

I watch MotoGP regularly and noticed that fans seem to care more about certain riders than others. Countries like Spain and Italy have multiple riders, but only a few of them become "national heroes." We wanted to test this observation with actual data instead of just guessing.

---

## Data Sources

We collected data from two places:

1. **Wikipedia** - Race results, calendars, rider statistics (2019-2024 seasons)
2. **Google Trends** - Search interest before and after each race using Pytrends library

---

## Project Steps

### Step 1: Data Collection (Web Scraping)

We used Python's `requests` and `BeautifulSoup` libraries to scrape Wikipedia pages. For each season (2019-2024), we extracted:
- Race calendar (dates, circuits, Grand Prix names)
- Race results (winning riders)
- Rider information (nationality, career wins, podiums, championships, years active)

**Why web scraping?** MotoGP data is spread across multiple Wikipedia pages. Instead of copying everything by hand, we automated the process to get accurate and consistent data.

### Step 2: Data Cleaning & Preprocessing

Raw data from Wikipedia had some issues:
- Footnote markers like `[1]`, `[2]` in rider names
- Inconsistent date formats
- Missing values in some columns

We cleaned everything using pandas string operations and regular expressions. The goal was to have a tidy dataset where each row represents one race with all relevant information.

### Step 3: Feature Engineering

**What is Feature Engineering?**
It means creating new useful variables from existing data. We created:

- **Popularity Score**: A weighted combination of career stats
  ```
  Popularity = 100 × Championships + 10 × Wins + 3 × Podiums + 1 × Years Active
  ```
  This formula gives more weight to championships (hardest to achieve) and less to just being active for many years.

- **Years Active Length**: Calculated from strings like "2013-present" or "2008-2022"
- **Numeric versions** of text fields (converting "7 championships" to just 7)

### Step 4: Google Trends Data Collection

We used the **Pytrends** library to get search interest data from Google Trends.

**How it works:**
- For each race, we queried the winning rider's name
- Collected data for 7 days before and 7 days after the race
- Calculated average interest in both periods

**Metrics we created:**
- `Search Before`: Average search interest in the week before the race
- `Search After`: Average search interest in the week after the race
- `Trend Difference`: After minus Before
- `Relative Increase %`: How much the interest grew compared to baseline

### Step 5: Exploratory Data Analysis (EDA)

**What is EDA?**
Looking at your data through visualizations and summary statistics to understand patterns before doing any formal testing.

We created several plots:

1. **KDE Plot (Kernel Density Estimation)**: Shows the distribution of popularity scores. It's like a smooth histogram that helps us see if most riders cluster around certain popularity levels.

2. **Regression Plot**: Scatter plot with a fitted line showing the relationship between pre-race and post-race search interest.

3. **Violin Plot**: Combines box plot and KDE to show how search increase varies across different championship categories (0, 1, 2, 3+ titles).

4. **Correlation Heatmap**: Visual matrix showing how strongly different variables relate to each other.

5. **Bar Charts**: Country-level analysis and rolling trends over time.

### Step 6: Statistical Hypothesis Testing

**What is Hypothesis Testing?**
A formal way to check if patterns we see in data are real or just random noise. We set up null hypotheses (H0) and try to reject them with evidence.

**Tests we performed:**

1. **Paired t-test (Search Before vs After)**
   - Question: Does search interest actually increase after races?
   - Result: Yes, there's a significant increase (p < 0.05)

2. **Independent t-test (Experienced vs New Riders)**
   - Question: Do riders with more experience have higher popularity?
   - Result: Yes, experienced riders (>5 years) have significantly higher popularity scores

3. **Independent t-test (Champions vs Non-Champions)**
   - Question: Do championship winners create bigger search spikes?
   - Result: No significant difference found - interesting finding!

4. **Pearson Correlation Tests**
   - Popularity vs Relative Increase: No significant positive correlation (r = -0.23)
   - Search Before vs Relative Increase: Significant negative correlation (r = -0.32)

**What does this mean?**
The negative correlation is actually the most interesting finding. Riders who already have high baseline search interest show smaller relative increases after winning. This makes sense - if everyone already knows Marc Márquez, his search volume doesn't spike as dramatically as when a lesser-known rider wins.

### Step 7: Machine Learning Classification

**What is Classification?**
Training a model to predict categories based on input features. We wanted to see if we can predict the level of fan reaction based on rider characteristics.

**Target Variable:**
We categorized `Relative Increase %` into three classes:
- **Low**: < 0% (decrease or no change)
- **Medium**: 0-50% (moderate increase)
- **High**: > 50% (high increase)

**Models Used:**

1. **Random Forest Classifier**
   - An ensemble method that builds many decision trees and combines their predictions
   - Good at handling complex patterns and avoiding overfitting
   - Parameters: 100 trees, max depth of 10

2. **Decision Tree Classifier**
   - A single tree that makes decisions based on feature thresholds
   - Easy to visualize and interpret
   - Used as a baseline for comparison

**Features Used:**
- Popularity score
- Career wins, podiums, championships (numeric)
- Years active
- Search Before
- Trend Difference

**Results:**
Both models achieved reasonable accuracy for a classification task with limited data (~100 races). The Random Forest performed slightly better due to its ensemble nature.

---

## Key Findings

1. **Search interest does increase after races** - fans definitely pay more attention after someone wins

2. **Experienced riders are more popular** - no surprise, but we confirmed it statistically

3. **Being a champion doesn't guarantee bigger search spikes** - unexpected! Non-champions can create just as much buzz

4. **Already-popular riders show smaller relative increases** - the "ceiling effect" - if you're already famous, there's less room to grow

5. **Machine learning can predict reaction categories** - rider stats have predictive power for fan engagement

---

## Technical Concepts Used

| Concept | What it is | Why we used it |
|---------|-----------|----------------|
| Web Scraping | Extracting data from websites automatically | To collect race and rider data from Wikipedia |
| Regular Expressions (Regex) | Pattern matching in text | To clean data and extract numbers from strings |
| Feature Engineering | Creating new variables | To build the popularity score and numeric features |
| API Integration | Connecting to external services | To get Google Trends data via Pytrends |
| KDE Plot | Smooth density estimation | To visualize distribution of continuous variables |
| Paired t-test | Comparing two related measurements | To test before/after race search interest |
| Independent t-test | Comparing two separate groups | To compare experienced vs new riders |
| Pearson Correlation | Measuring linear relationship | To check if popularity relates to search increase |
| Random Forest | Ensemble of decision trees | Main classification model |
| Decision Tree | Rule-based classifier | Interpretable baseline model |
| Train/Test Split | Dividing data for validation | To evaluate model on unseen data |
| Confusion Matrix | Classification error breakdown | To see which categories the model confuses |

---

## Files in This Repository

| File | Description |
|------|-------------|
| `motogp_fan_reaction_analysis.ipynb` | Main Jupyter notebook with all analysis |
| `ml_models_motogp.ipynb` | Separate notebook for ML experiments |
| `run_ml_models.py` | Python script to run ML models |
| `ml_data/` | Folder containing saved models and data |
| `ml_models/` | Folder for model artifacts |
| `README.md` | This file |

---

## How to Run

1. Install required packages:
   ```bash
   pip install pandas requests lxml beautifulsoup4 pytrends scikit-learn matplotlib seaborn
   ```

2. Open the Jupyter notebook:
   ```bash
   jupyter notebook motogp_fan_reaction_analysis.ipynb
   ```

3. Run cells sequentially (some cells take time due to web scraping and API calls)

---

## Limitations

- Google Trends shows relative interest, not absolute search counts
- Dataset covers only 2019-2024 seasons (111 races total)
- Some riders have inconsistent Wikipedia page structures
- API rate limits require delays between requests
- Small sample size limits ML model performance

---

## Future Work

- Include more seasons for larger dataset
- Add social media sentiment analysis (Twitter/X)
- Analyze sprint races separately
- Compare with other motorsports (F1, WorldSBK)
- Try more advanced ML models (XGBoost, Neural Networks)

---

## Conclusion

This project showed that fan reactions in MotoGP follow interesting patterns. While popular riders dominate overall attention, their victories don't create the biggest relative spikes. Underdog wins generate more "buzz" proportionally. The machine learning models confirmed that rider characteristics can predict engagement levels to some extent.

The most valuable insight: **familiarity breeds smaller reactions**. If everyone already knows and follows a rider, their win is expected and doesn't surprise anyone. But when someone unexpected wins, fans rush to learn more about them.
