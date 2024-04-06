# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:16:41 2024

@author: david
"""

import pandas as pd

df = pd.read_csv('../data/E0.csv')

home_teams = list(df['HomeTeam'])
away_teams = list(df['AwayTeam'])
home_goals = list(df['FTHG'])
away_goals = list(df['FTAG'])

teams = set(home_teams)

def calculate_goal_difference(goals_for, goals_against) :
    return(goals_for-goals_against)
    
for j in teams :
    goal_difference = 0
    for i in range(380) :
        if home_teams[i] == j :
            goal_difference = goal_difference + calculate_goal_difference(home_goals[i], away_goals[i])
            
    for i in range(380) :
        if away_teams[i] == j :
            goal_difference = goal_difference + calculate_goal_difference(away_goals[i], home_goals[i])
    
    if j == 'Newcastle' :
        goal_difference = goal_difference - 30
    print(j)
    print(goal_difference)
    

