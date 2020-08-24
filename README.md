# FIFA19-Analysis

# FOR MANUPULATION
                  import numpy as np
                  import pandas as pd

# FOR VISUALIZATION
                  import seaborn as sns
                  import matplotlib.pyplot as plt
                  import matplotlib.image as mpimg
                  import plotly as py
                  import plotly.graph_objs as go
                  import seaborn as sns
                  from IPython.display import display, HTML, YouTubeVideo
                  from collections import Counter as counter

Shape of the dataset : (18207, 89)

Steps
1) Dropping Unnecessary Columns
2) Extracting required information of the DataSet
3) Ranking players as per their Overall Rating, Wages, Affordability, Game Attributes, Age, Potential etc.
4) Did comparison between :
                          a) FC Barcelona
                          b) Real Madrid
                          c) Liverpool
                          d) Manchester City
5) Got to know : best players in the respective clubs on basis of Overall Rating
6) Got to know : Full squad list of respective clubs
7) Got to know : Number of player for each position
8) Comparison between the clubs was based on :
                          a) Distribution of Player's age  
                          b) Distribution of Player's ratings
                          c) Distribution of Player's value in the market
                          d) Distribution of Player's wage
                          e) Distribution of Player's potential
                          e) Distribution of Player's finishing capabilities infront of goal
                          f) Distribution of Player's by nationality
                          g) Distribution of Player's preferred foot
                          h) Distribution of Player's international reputation
                          i) Distribution of Player's skill moves

9) Imported club logos, player images, coach/manager's images, using matplotlib.image as mpimg module
10)Imported some videos of goals, passing, saving of top players such as Lionel Messi, Xavi, Iniesta, Ronaldo from youtube

For Data Visualization, I used:
                          1) Countplot
                          2) lmplot
                          3) violinplot
                          4) boxplot
                          5) subplot
                          6) pie chart
                          7) distplot

# Conclusion : 
                          a) Lionel Messi is highly rated in many aspects of the gaming attributes
                          b) Real Madrid posses the best squad strength
                          c) Neymar is most valuable player at the moment
                          d) Mbappe has the best potential
                          e) David De Gea of Manchester United is the highest rated goalkeeper in FIFA19
                          e) England National team has most number of FIFA19 rated players
                          f) There are more right footed player's compared to left footed player's
                          g) Most player's are of age 21
