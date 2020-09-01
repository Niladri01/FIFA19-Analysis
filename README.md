# FIFA19-EDA

*Aim:* The aim of this project was to prepare the dataset for exploratory data analysis, rapid data visualization and analysis, customize charts, animations, and demonstrate the various matplotlib and seaborn features.

## Overview

*FIFA-19:* FIFA-19 is a football simulation game developed by *Electronic Arts* , Vancouver. It's massively popular game among all ages. It comes in different setup's such as Playstation, and Mobile devices. This game contains all FIFA (*Fédération Internationale de Football Association*) registered players, and are grouped by different clubs, naionalities and attributes.

## FOR MANUPULATION
       import numpy as np
       import pandas as pd
       from collections import Counter as counter

## FOR VISUALIZATION
       import seaborn as sns
       import matplotlib.pyplot as plt
       import matplotlib.image as mpimg
       import plotly as py
       import plotly.graph_objs as go
       import seaborn as sns
       from IPython.display import display, HTML, YouTubeVideo
         
## Shape of the dataset
       (18207, 89)

## Steps
       1) Dropping Unnecessary Columns
       2) Extracting required information of the DataSet
       3) Ranking players as per their Overall Rating, Wages, Affordability, Game Attributes, Age, Potential etc.
       4) Did comparison between :
                                 a) FC Barcelona
                                 b) Real Madrid
                                 c) Liverpool
                                 d) Manchester City
                                            
       5) Find : best players in the respective clubs on basis of Overall Rating
       6) Find : Full squad list of respective clubs
       7) Find : Number of player for each position
       8) Comparison between the clubs, based on :
                                 a) Distribution of Player's age  
                                 b) Distribution of Player's ratings
                                 c) Distribution of Player's value in the market
                                 d) Distribution of Player's wage
                                 e) Distribution of Player's potential
                                 f) Distribution of Player's finishing capabilities infront of goal
                                 g) Distribution of Player's by nationality
                                 h) Distribution of Player's preferred foot
                                 i) Distribution of Player's international reputation
                                 j) Distribution of Player's skill moves

       9) Imported club logos, player images, coach/manager's images, using matplotlib.image as mpimg module
       10)Imported some videos of goals, passing, saving of top players such as Lionel Messi, Xavi, 
       Iniesta, Ronaldo from youtube

## For Data Visualization, I used:
       1) Countplot
       2) lmplot
       3) violinplot
       4) boxplot
       5) subplot
       6) pie chart
       7) distplot

## Conclusion : 
       a) Lionel Messi is highly rated in many aspects of the gaming attributes
       b) Real Madrid posses the best squad strength
       c) Neymar is most valuable player at the moment
       d) Mbappe has the highest potential
       e) David De Gea of Manchester United is the highest rated goalkeeper in FIFA19
       f) England National team has most number of FIFA19 rated players
       g) There are more right footed player's compared to left footed player's
       h) Most player's are of age 21
