# 🏍️ <span style="color:#F7D400;">MotoGP Fan Reaction Analysis</span>

---

## 🎯 <span style="color:#3F77BF;">Motivation</span>

I love watching MotoGP in my free time and I follow it closely.  
I’ve noticed that there is a strong sense of nationalism among MotoGP fans — they often admire and support the riders who have been the most successful representatives of their country.  
However, every nation also has riders who are less famous or less successful, and these riders do not receive the same level of attention.  

In this project, I want to test whether MotoGP fans tend to show more interest in the most successful riders who symbolize their nation compared to less-known riders from the same country.  

To verify this idea with real data, I will analyze **Google search trends** on race days to see whether there is a significant increase in searches for a rider from their home country after winning a race — especially if the rider is already popular and successful.  
Additionally, I’ll explore whether factors such as **win margin**, **circuit difficulty**, or **previous wins on the same track** have any effect on the level of search interest after a race.  

---

## 🏁 <span style="color:#A0B153;">Data Source</span>

This project will use **publicly available data** from two main sources:

### 📄 <span style="color:#F7D400;">MotoGP Race Data</span>

<ul>
  <li><span style="color:#956555;">Race results (dates, winners, rider names, nationalities, circuit names) will be collected manually from <i>Wikipedia</i> and <i>motogp.com</i>.</span></li>
  <li><span style="color:#3F77BF;">Additional race-level details such as <b>win margin</b>, <b>circuit difficulty</b>, and <b>number of previous wins</b> will be included.</span></li>
</ul>

### 🌐 <span style="color:#3F77BF;">Google Search Trends</span>

<ul>
  <li><span style="color:#A0B153;">Public Google Trends data will be collected using the <b>Pytrends</b> Python library.</span></li>
  <li><span style="color:#F7D400;">For each race, search interest for the winning rider’s name and for <b>“MotoGP”</b> will be gathered from their home country to measure changes in public attention.</span></li>
</ul>

> 💾 The final dataset will contain around <b>10–15 features</b>, combining race performance, rider popularity, and Google Trends statistics.

All data sources are <b>publicly available</b>, and Pytrends is only used to access open trend data automatically.

---

## 📊 <span style="color:#F7D400;">Data Analysis</span>

The analysis will focus on how a rider’s <b>popularity</b> and <b>performance</b> influence public attention after MotoGP races.

### Key Analysis Goals:

<ul>
  <li><span style="color:#956555;">Compare <b>Google search interest</b> before and after each race.</span></li>
  <li><span style="color:#3F77BF;">Identify if <b>popular riders</b> receive more post-race attention than less-popular ones.</span></li>
  <li><span style="color:#A0B153;">Evaluate how <b>win margin</b>, <b>circuit difficulty</b>, and <b>previous wins</b> affect search interest changes.</span></li>
  <li><span style="color:#F7D400;">Visualize which factors — <b>rider success</b>, <b>popularity</b>, or <b>race characteristics</b> — most influence public attention.</span></li>
</ul>

---

## 🏆 <span style="color:#3F77BF;">Expected Findings</span>

<ul>
  <li><span style="color:#956555;">🟡 Popular riders (with more wins, podiums, or championships) are expected to show a <b>higher increase</b> in Google search interest after winning compared to less-popular riders.</span></li>
  <li><span style="color:#3F77BF;">🔵 The <b>larger the win margin</b>, the greater the public attention — dominant victories create stronger fan reactions.</span></li>
  <li><span style="color:#A0B153;">🟢 Winning on a <b>difficult circuit</b> may lead to higher interest, as fans perceive these wins as more impressive.</span></li>
</ul>

---

## ⚠️ <span style="color:#A0B153;">Limitations</span>

<ul>
  <li><span style="color:#956555;">Google Trends data shows <b>relative interest</b>, not absolute search counts.</span></li>
  <li><span style="color:#3F77BF;"><b>Circuit difficulty</b> and <b>rider popularity</b> are simplified metrics and may not reflect real-world perceptions.</span></li>
  <li><span style="color:#A0B153;">Dataset covers only <b>recent seasons (2015–2025)</b>, so long-term fan behavior may not be captured.</span></li>
</ul>

---

<p align="center">
  <b><span style="color:#F7D400;">🏁 Developed with Passion for MotoGP 🏁</span></b><br>
  <span style="color:#3F77BF;">By <b>Yiğit Ali Erdem</b> | Sabancı University | 2025</span>
</p>
