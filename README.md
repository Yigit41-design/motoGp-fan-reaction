**MotoGP Fan Reaction Analysis**

---

### Motivation

I love watching MotoGP in my free time and I follow it closely.
I’ve noticed that there is a strong sense of nationalism among MotoGP fans — they often admire and support the riders who have been the most successful representatives of their country.
However, every nation also has riders who are less famous or less successful, and these riders do not receive the same level of attention.

In this project, I want to test whether MotoGP fans tend to show more interest in the most successful riders who symbolize their nation compared to less-known riders from the same country.

To verify this idea with real data, I will analyze **Google search trends** on race days to see whether there is a significant increase in searches for a rider from their home country after winning a race — especially if the rider is already popular and successful.
Additionally, I’ll explore whether factors such as **win margin**, **circuit difficulty**, or **previous wins on the same track** have any effect on the level of search interest after a race.

---

### Data Source

This project will use **publicly available data** from two main sources:

### MotoGP Race Data

* Race results (dates, winners, rider names, nationalities, circuit names) will be collected manually from *Wikipedia* and *motogp.com*.
* Additional race-level details such as **win margin** (time difference between first and second place), **circuit difficulty**, and **number of previous wins on that circuit** will be included to analyze how race characteristics influence public attention.

###  Google Search Trends

* 🟢 Public Google Trends data will be collected using the **Pytrends** Python library.
* 🟡 For each race, search interest for the winning rider’s name and more information for **“MotoGP”** will be collected from the rider’s home country to measure changes in public attention before and after each race.

> 💾 The final dataset will contain around **10–15 features**, combining race performance details, rider popularity metrics (career wins, championships, podium finishes, years active), and Google Trends statistics (before/after interest, trend difference, and relative increase).

All data sources are **publicly available**, and Pytrends is used only to access Google’s open trend data automatically.

---

### Data Analysis

The analysis will focus on understanding how a rider’s **popularity** and **race performance** influence public attention after MotoGP races.

* 🟡 Compare **Google search interest** before and after each race.
* 🟢 Identify if **popular riders** receive more post-race attention than less-popular ones.
* 🟡 Evaluate how **win margin**, **circuit difficulty**, and **previous wins** affect search interest changes.
* 🟢 Visualize which factors — **rider success**, **popularity**, or **race characteristics** — most influence public attention.

---

### Expected Findings

* 🟢Popular riders (with more wins, podiums, or championships) are expected to show a **higher increase in Google search interest** after winning compared to less-popular riders.
* 🟡 The **larger the win margin**, the greater the public attention — dominant victories create stronger fan reactions.
* 🟢 Winning on a **difficult circuit** may lead to higher interest, as fans perceive these wins as more impressive.

---

### Limitations

* 🟢 Google Trends data shows **relative interest**, not absolute search counts
* 🟡 **Circuit difficulty** and **rider popularity** are simplified metrics and may not reflect full real-world perceptions.
* 🟢 Dataset covers only **recent seasons (2015–2025)**, so long-term fan behavior may not be captured.

---
