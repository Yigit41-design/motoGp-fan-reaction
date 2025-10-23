# 🏆 Best Football Players by League & Skill Areas

## 🎯 Motivation
Football is actually a detailed game where individual performance not only depends on goals — it has many dimensions.  
In my project, I will explore some of them and identify players who excel the most in these areas across the top five leagues: **Premier League, La Liga, Serie A, Ligue 1, and Bundesliga.**

---

## 📊 Data Source
The dataset will be obtained from **[FBref](https://fbref.com)**, which provides publicly available player-level football statistics.  
Data will be collected **manually** by copying relevant tables (*Standard Stats, Shooting, Passing, Goal and Shot Creation, Defensive Actions, Possession, and Miscellaneous Stats*) directly from FBref pages into Excel, and then saving them as CSV files.

---

## ⚙️ Metrics Used

| Category | Metrics |
|-----------|----------|
| **Finishing** | Non-penalty Goals, Shots on Target %, (Goals − npxG) |
| **Chance Creation** | Key Passes, SCA (Shot Creating Actions), Passes into Penalty Area |
| **Take-on** | Dribbles Completed, Dribble Success %, Carries into Final Third |
| **Playmaking** | Progressive Passes, Passes into Final Third, xA |
| **Ground Defence** | Tackles Won, Interceptions, Blocks, Pressure Success % |
| **Aerial Duels** | Aerials Won, Aerial Win %, Headed Shots |

---

## 🧮 Data Analysis

### 1️⃣ Data Collection  
Copying player-level tables from FBref into Excel and exporting as CSV.

### 2️⃣ Data Cleaning & Integration  
Combining CSV files (shooting, passing, etc.) into one master dataset and filtering players who played ≥ 1000 minutes.

### 3️⃣ Normalization  
Converting all metrics to “per 90 minutes” and scaling them using **z-score normalization** (so all values are comparable).

### 4️⃣ Scoring & Ranking  
Creating a composite score for each skill area and ranking players within each league.

### 5️⃣ Visualization  
Plotting **radar charts** and **bar charts** to show top players per skill area.

---

## 📈 Expected Findings
- Players who have high take-on and chance-creation stats are mostly **wingers** or **offensive midfielders**.  
- **Center-backs** would mostly be proficient in **ground defence** and **aerial duels**.  
- **Central midfielders** are expected to dominate the **playmaking** category.

---

## 🏁 Final Output
**Top 50 most proficient players** in each category:
- Finishing  
- Chance Creation  
- Playmaking  
- Take-on  
- Ground Defence  
- Aerial Duels  

---

## ⚠️ Limitations
- Data is updated every week on FBref, so player stats could slightly change over time.

---

## 🔮 Future Updates
- Add more leagues (e.g., Süper Lig, MLS).  
- Automate data extraction using Python (`pandas.read_html`).  

---

💬 *“The beauty of football lies not only in goals, but in the countless skills that build them.”* ⚽
