Motivation

Football is actually a detailed game where individual performance not only depending on goals it has many dimensions in my project I will explore some of them and I will identify and show players that are most excelled on those areas in top five leagues(Premier League, La Liga, Serie A, Ligue 1, and Bundesliga)

Data source

The dataset will be obtained from FBref, which provides publicly available player-level football statistics.
Data will be collected manually by copying relevant tables (Standard Stats, Shooting, Passing, Goal and Shot Creation, Defensive Actions, Possession, and Miscellaneous Stats) in each league directly from FBref pages into Excel, and then saving them as CSV files.

Metrics will be used 

Finishing: Non-penalty Goals, Shots on Target %, (Goals − npxG)
Chance Creation: Key Passes, SCA (Shot Creating Actions), Passes into Penalty Area 
Take on: Dribbles Completed, Dribble Success %, Carries into Final Third 
Playmaking: Progressive Passes, Passes into Final Third, xA 
Ground Defence: Tackles Won, Interceptions, Blocks, Pressure Success % 
Aerial Duels: Aerials Won, Aerial Win %, Headed Shots

Data Analysis

Data Collection: Copying the player-level tables from FBref into Excel and exporting as CSV

Data Cleaning & Integration: Combining CSV files (shooting, passing, etc.) into one master dataset and filtering players who played ≥ 1000 minutes

Normalization: Converting all metrics to “per 90 minutes” and scaling them using z-score normalization (so all values are comparable).

Scoring & Ranking: Creating a composite score for each skill area and ranking players within each league.

Visualization: Plotting radar charts and bar charts to show top players per skill area.

Expected findings

Players who has high take on and chance creation stats are mostly a winger and offensive midfielders

Centerbacks would mostly be proficient at ground defence and aerial duels

Central midfielders mostly would dominate playmaking
category

Final output
Top 50 most proficient player in finishing, chance creation, playmaking, take on, ground defence, aerial duels

Limitations
Datas are updated in each week so stats could slightly change 

Future updates
More leagues could be added, automate data extraction