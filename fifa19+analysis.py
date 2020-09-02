
# coding: utf-8

# # FIFA 19 ANALYSIS

# ### IMPORTING MODULES

# In[1]:

### FOR MANUPULATION
import numpy as np
import pandas as pd

### FOR VISUALIZATION
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import plotly as py
import plotly.graph_objs as go
import seaborn as sns
from IPython.display import display, HTML, YouTubeVideo
from collections import Counter as counter

print("Modules are imported")


# ### FIFA19 COVER PHOTO

# In[2]:

plt.figure(1, figsize = (20, 15))
img = mpimg.imread("fifa19cover.jpg") 
plt.imshow(img)
plt.show()


# ### LOADING DATASET

# In[3]:

df_fifa = pd.read_csv("data.csv")
df_fifa.head(50)


# SHAPE OF DATASET(ROW, COLUMNS)

# In[4]:

df_fifa.shape


# DROPPING UNNECESSARY COLUMNS

# In[5]:

useless_cols = ["ID", "Unnamed: 0", "Photo", "Flag", "Club Logo", "Special", "Body Type", "Real Face", "Joined", "Loaned From",
                "Contract Valid Until", "Weight", "LS", "ST", "RS", "LW", "LF", "CF", "RF", "RW", "LAM", "CAM", "RAM", "LM", 
                "LCM", "CM", "RCM", "RM", "LWB", "LDM", "CDM", "RDM", "RWB", "LB", "LCB", "CB", "RCB", "RB", "Release Clause"]
df_fifa.drop(useless_cols, axis=1, inplace=True)
df_fifa.head(10)


# INFORMATION ON DATASET

# In[6]:

df_fifa.info()


# STATISTICS ON DATASET

# In[7]:

df_fifa.describe()


# ELEMENTS IN DATASETS

# In[8]:

df_fifa.nunique()


# ### EXPLORATORY DATA ANALYSIS

# HIGHEST RATED PLAYERS IN FIFA19

# In[9]:

df_fifa.sort_values(by = "Overall", ascending = False)[["Name", "Position", "Nationality", "Club", "Age", "Overall"]].head()


# LOWEST RATED PLAYERS IN FIFA19

# In[10]:

df_fifa.sort_values(by = "Overall", ascending = True)[["Name", "Position", "Nationality", "Club", "Age", "Overall"]].head()


# PLAYERS WITH BEST POTENTIAL

# In[11]:

df_fifa.sort_values(by = "Potential", ascending = False)[["Name", "Position", "Potential", "Club", "Age", "Overall"]].head()


# OLDEST PLAYERS

# In[12]:

df_fifa.sort_values(by = "Age", ascending = False)[["Name", "Position", "Potential", "Club", "Age", "Overall"]].head()


# YOUNGEST PLAYERS

# In[13]:

df_fifa.sort_values(by = "Age", ascending = True)[["Name", "Position", "Potential", "Club", "Age", "Overall"]].head()


# PLAYERS WITH BEST SHOTPOWER

# In[14]:

df_fifa.sort_values(by = "ShotPower", ascending = False)[["Name", "Club", "Position", "ShotPower", "Overall"]].head()


# BEST DRIBBLERS IN THE GAME

# In[15]:

df_fifa.sort_values(by = "Dribbling", ascending = False)[["Name", "Club", "Position", "Dribbling", "Overall"]].head()


# BEST CROSSERS OF THE BALL

# In[16]:

df_fifa.sort_values(by = "Crossing", ascending = False)[["Name", "Club", "Position", "Crossing", "Overall"]].head()


# BEST FREEKICK TAKERS

# In[17]:

df_fifa.sort_values(by = "FKAccuracy", ascending = False)[["Name", "Club", "Position", "FKAccuracy", "Overall"]].head()


# PLAYERS HAVING BEST BALL CONTROL

# In[18]:

df_fifa.sort_values(by = "BallControl", ascending = False)[["Name", "Club", "Position", "BallControl", "Overall"]].head()


# PLAYERS WITH BEST VISION

# In[19]:

df_fifa.sort_values(by = "Vision" , ascending = False)[["Name", "Club" ,"Nationality" ,"Vision", "Overall" ]].head()


# BEST FINISHERS

# In[20]:

df_fifa.sort_values(by = "Finishing", ascending = False)[["Name", "Club", "Position", "Finishing", "Overall"]].head()


# PLAYERS WITH FAST ACCELERATION

# In[21]:

df_fifa.sort_values(by = "Acceleration", ascending = False)[["Name", "Club", "Position", "Acceleration", "Overall"]].head()


# BEST SPRINTERS

# In[22]:

df_fifa.sort_values(by = "SprintSpeed", ascending = False)[["Name", "Club", "Position", "SprintSpeed", "Overall"]].head()


# BEST LONG PASSERS IN THE GAME

# In[23]:

df_fifa.sort_values(by = "LongPassing", ascending = False)[["Name", "Club", "Position", "LongPassing", "Overall"]].head()


# STRONGEST PLAYERS

# In[24]:

df_fifa.sort_values(by = "Strength", ascending = False)[["Name", "Club", "Position", "Strength", "Overall"]].head()


# MOST AGGRESIVE PLAYERS

# In[25]:

df_fifa.sort_values(by = "Aggression", ascending = False)[["Name", "Club", "Position", "Aggression", "Overall"]].head()


# BEST GOAL KEEPERS (REFLEXES)

# In[26]:

df_fifa.sort_values(by = "GKReflexes", ascending = False)[["Name", "Club", "Position", "GKReflexes", "Overall"]].head()


# BEST GOAL KEEPERS (DIVING)

# In[27]:

df_fifa.sort_values(by = "GKDiving", ascending = False)[["Name", "Club", "Position", "GKDiving", "Overall"]].head()


# BEST DEFENDERS (SLIDING TACKLE)

# In[28]:

df_fifa.sort_values(by = "SlidingTackle", ascending = False)[["Name", "Club", "Nationality", "SlidingTackle", "Overall"]].head()


# BEST DEFENDERS (STANDING TACKLE)

# In[29]:

df_fifa.sort_values(by = "StandingTackle", ascending = False)[["Name", "Club", "Nationality", "StandingTackle", "Overall"]].head()


# NUMBER OF PLAYERS AT CERTAIN POSITIONS

# In[30]:

plt.figure(1, figsize = (15, 6))
pos = sns.countplot(x = "Position", data = df_fifa, palette = "hls");
pos.set_title(label="Number of players at specialized position", fontsize=40);
plt.show()


# BEST LEFT FOOTED PLAYERS

# In[31]:

df_fifa[df_fifa["Preferred Foot"] == "Left"][["Name", "Club", "Position","Overall"]].head()


# BEST RIGHT FOOTED PLAYERS

# In[32]:

df_fifa[df_fifa["Preferred Foot"] == "Right"][["Name","Club", "Position", "Overall"]].head()


# COMPARISON : LEFT FOOT VS RIGHT FOOT IN TERMS OF DRIBBLING AND FINISHING

# In[33]:

sns.lmplot(x = "Finishing", y = "Dribbling", data = df_fifa, scatter_kws = {"alpha":0.1}, col = "Preferred Foot");
plt.show()


# ATTRIBUTES : PLAYER NAME

# In[34]:

cols = ["Crossing", "Potential", "Finishing", "HeadingAccuracy", "ShortPassing", "Volleys", 
        "Dribbling", "Curve", "FKAccuracy", "LongPassing", "BallControl", "Acceleration", 
        "SprintSpeed", "Agility", "Reactions", "Balance", "ShotPower", "Jumping", "Stamina", 
        "Strength", "LongShots", "Aggression", "Interceptions", "Positioning", "Vision", 
        "Penalties", "Composure", "Marking", "StandingTackle", "SlidingTackle", "GKDiving", 
        "GKHandling", "GKKicking", "GKPositioning", "GKReflexes"]
i=0
while i < len(cols):
    print('Best {0} : {1}'.format(cols[i], df_fifa.loc[df_fifa[cols[i]].idxmax()]["Name"]))
    i += 1


# BEST PLAYER AT EACH POSITION

# In[35]:

display(HTML(df_fifa.iloc[df_fifa.groupby(df_fifa["Position"])["Overall"].idxmax()][["Name", "Position"]].to_html(index=False)))


# TOP 3 FEATURES FOR EACH POSITION

# In[36]:

player_features = ["Crossing", "Potential", "Finishing", "HeadingAccuracy", "ShortPassing", "Volleys", 
        "Dribbling", "Curve", "FKAccuracy", "LongPassing", "BallControl", "Acceleration", 
        "SprintSpeed", "Agility", "Reactions", "Balance", "ShotPower", "Jumping", "Stamina", 
        "Strength", "LongShots", "Aggression", "Interceptions", "Positioning", "Vision", 
        "Penalties", "Composure", "Marking", "StandingTackle", "SlidingTackle", "GKDiving", 
        "GKHandling", "GKKicking", "GKPositioning", "GKReflexes"]

for i, val in df_fifa.groupby(df_fifa["Position"])[player_features].mean().iterrows():
    print("Position {}: {}, {}, {}".format(i, *tuple(val.nlargest(3).index)))


# FREQUENCY OF OVERALL PLAYER RATINGS

# In[37]:

plt.figure(1, figsize = (15, 6))
pos = sns.countplot(x = "Overall", data = df_fifa, palette = "hls");
pos.set_title(label="Player Ratings out of 100", fontsize=40);
plt.show()


# PLAYER POTENTIAL DISTRIBUTION

# In[38]:

plt.figure(1, figsize = (15, 6))
pos = sns.countplot(x = "Potential", data = df_fifa, palette = "hls");
pos.set_title(label="Player Potential Distribution", fontsize=40);
plt.show()


# PLAYERS AGE DISTRIBUTION

# In[39]:

plt.figure(1, figsize = (15, 6))
pos = sns.countplot(x = "Age", data = df_fifa, palette = "hls");
pos.set_title(label="Age Distribution", fontsize=40);
plt.show()


# AGE DISTRIBUTION IN TOP CLUBS IN EUROPE

# In[40]:

clubs = ["FC Barcelona", "Real Madrid", "Juventus", "Liverpool", "Manchester City", "Paris Saint-Germain"]
df_club_age = df_fifa.loc[df_fifa["Club"].isin(clubs) & df_fifa["Age"]]
plt.figure(1 , figsize = (15 ,7))
sns.violinplot(x = "Club", y = "Age", data = df_club_age)
plt.title("Age Distribution in Top European clubs")
plt.xticks(rotation = 50)
plt.show()


# CLUBS WITH MOST PLAYERS

# In[41]:

print("Total number of clubs : {0}".format(df_fifa["Club"].nunique()))
print(df_fifa["Club"].value_counts().head(10))


# BEST SQUAD SIZE

# In[42]:

plt.figure(1 , figsize = (15 , 5))
club = []
c = counter(df_fifa["Club"]).most_common()[:11]
for n in range(11):club.append(c[n][0])

sns.countplot(x = "Club", data = df_fifa[df_fifa["Club"].isin(club)], 
              order  = df_fifa[df_fifa["Club"].isin(club)]["Club"].value_counts().index, palette = "rocket") 
plt.xticks(rotation = 90)
plt.title("Clubs with best squad size" )
plt.show()


# CHANGING DATA FORMAT

# In[43]:

def cleaning_value(x):
    if '€' in str(x) and 'M' in str(x):
        c = str(x).replace('€' , '')
        c = str(c).replace('M' , '')
        c = float(c) * 1000000
        
    else:
        c = str(x).replace('€' , '')
        c = str(c).replace('K' , '')
        c = float(c) * 1000
            
    return c

fn = lambda x : cleaning_value(x)

df_fifa["Value_num"] = df_fifa["Value"].apply(fn)
df_fifa["Wage_num"] = df_fifa["Wage"].apply(fn)


# MOST VALUABLE PLAYERS

# In[44]:

df_fifa.sort_values(by = "Value_num", ascending = False)[["Name", "Club", "Nationality", "Overall", "Value"]].head()


# BEST PAID PLAYERS

# In[45]:

df_fifa.sort_values(by = "Wage_num", ascending = False)[["Name", "Club", "Nationality", "Overall", "Wage"]].head()


# AGE DISTRIBUTION IN TOP COUNTRIES

# In[46]:

country = ["Argentina", "Brazil", "France", "Belgium", "England", "Spain", "Portugal"]
df_country_age = df_fifa.loc[df_fifa["Nationality"].isin(country) & df_fifa["Age"]]
plt.figure(1 , figsize = (15 ,7))
sns.violinplot(x = "Nationality" , y = "Age" , data = df_country_age)
plt.title("Age Distribution in Top National Teams")
plt.xticks(rotation = 50)
plt.show()


# AGE VS OVERALL RATING COMPARISON

# In[47]:

plt.figure(1 , figsize = (15 , 6))
sns.boxplot(df_fifa["Age"], df_fifa["Overall"])
plt.title("Age vs Overall rating Comparison")
plt.show()


# AGE VS STAMINA COMPARISON

# In[48]:

plt.figure(1 , figsize = (15 , 9))
sns.boxplot(x = "Age", y = "Stamina", data = df_fifa)
plt.title("Age vs Stamina Comparison")
plt.show()


# AGE VS SPRINT SPEED COMPARISON

# In[49]:

plt.figure(1 , figsize = (15 , 9))
sns.boxplot(x = "Age", y = "SprintSpeed", data = df_fifa)
plt.title("Age vs Sprint Speed Comparison")
plt.show()


# AGE VS REACTION COMPARISON

# In[50]:

plt.figure(1 , figsize = (15 , 9))
sns.boxplot(x = "Age", y = "Reactions", data = df_fifa)
plt.title("Age vs Reactions Comparison")
plt.show()


# DRIBBLING VS FINISHING COMPARISON

# In[51]:

plt.figure(1 , figsize = (25 , 9))
sns.boxplot(x = "Dribbling", y = "Finishing", data = df_fifa)
plt.title("Dribbling vs Finishing Comparison")
plt.show()


# AGE VS FINISHING COMPARISON

# In[52]:

plt.figure(1 , figsize = (15 , 9))
sns.boxplot(x = "Age", y = "Finishing", data = df_fifa)
plt.title("Age vs Finishing Comparison")
plt.show()


# COMPARING FEATURES WITH RESPECT TO ACCELERATION

# In[53]:

def make_scatter(df_fifa):
    feats = ("Agility", "Balance", "Dribbling", "SprintSpeed")
    
    for index, feat in enumerate(feats):
        plt.subplot(len(feats)/4+1, 4, index+1)
        ax = sns.regplot(x = 'Acceleration', y = feat, data = df_fifa)

plt.figure(figsize = (20, 20))
plt.subplots_adjust(hspace = 0.4)

make_scatter(df_fifa)
plt.show()


# COUNTRY WITH MOST PLAYERS

# In[54]:

print("Total number of countries : {0}".format(df_fifa["Nationality"].nunique()))
print(df_fifa["Nationality"].value_counts().head(10))


# COUNTPLOT DISTRIBUTION

# In[55]:

plt.figure(1, figsize = (20 , 7))
countries = []
c = counter(df_fifa["Nationality"]).most_common()[:11]
for n in range(11) : countries.append(c[n][0])
sns.countplot(x  = "Nationality", data = df_fifa[df_fifa["Nationality"].isin(countries)],
              order  = df_fifa[df_fifa["Nationality"].isin(countries)]["Nationality"].value_counts().index, 
              palette = "rocket") 
plt.xticks(rotation = 90)
plt.title("Most Players Belong To" )
plt.show()


# PIE CHART DISTRIBUTION

# In[56]:

countries=df_fifa["Nationality"].value_counts()
index=countries.index
con=pd.DataFrame({"Country":index,"Count":countries})
con=con["England":"Netherlands"]
plt.pie(con["Count"],labels=con["Country"],wedgeprops = {"linewidth": 5},autopct='%1.2f%%')
plt.title("Distribution of players in top 10 countries")
plt.tight_layout()
plt.show()


# ## COMPARISON - FC BARCELONA, REAL MADRID, LIVERPOOL AND MANCHESTER CITY 

# # FC BARCELONA

# In[57]:

plt.figure(1, figsize = (15, 10))
img = mpimg.imread("Barcelonalogo.jpg") 
plt.imshow(img)
plt.show()


# FULL SQUAD LIST OF FC BARCELONA

# In[58]:

df_fifa[df_fifa["Club"] == "FC Barcelona"][["Name", "Position", "Overall", "Age", "Wage", "Nationality"]]


# # THE BEST PLAYER OF FC BARCELONA

# LIONEL MESSI HAS BEEN RANKED AT THE TOP OF FIFA19 RATINGS
# 

# HE IS ALSO THE BEST PLAYER OF FC BARCELONA

# In[59]:

plt.figure(1, figsize = (15, 10))
img = mpimg.imread("Messi.jpg") 
plt.imshow(img)
plt.show()


# # REAL MADRID

# In[60]:

plt.figure(1, figsize = (15, 20))
img = mpimg.imread("rmlogo.png") 
plt.imshow(img)
plt.show()


# FULL SQUAD LIST OF REAL MADRID

# In[61]:

df_fifa[df_fifa["Club"] == "Real Madrid"][["Name", "Position", "Overall", "Age", "Wage", "Nationality"]]


# # BEST PLAYER OF REAL MADRID

# LUKA MODRIC IS THE HIGHEST RATED REAL MADRID PLAYER IN FIFA19

# In[62]:

plt.figure(1, figsize = (15, 20))
img = mpimg.imread("modric.jpg") 
plt.imshow(img)
plt.show()


# # LIVERPOOL FOOTBALL CLUB

# In[63]:

plt.figure(1, figsize = (15, 20))
img = mpimg.imread("liverpoollogo.jpg") 
plt.imshow(img)
plt.show()


# FULL SQUAD LIST OF LIVERPOOL

# In[64]:

df_fifa[df_fifa["Club"] == "Liverpool"][["Name", "Position", "Overall", "Age", "Wage", "Nationality"]]


# # BEST PLAYER OF LIVERPOOL

# M. SALAH IS HIGHEST RATED LIVERPOOL PLAYER IN FIFA19

# In[65]:

plt.figure(1, figsize = (15, 20))
img = mpimg.imread("salah.jpg") 
plt.imshow(img)
plt.show()


# # MANCHESTER CITY

# In[66]:

plt.figure(1, figsize = (15, 20))
img = mpimg.imread("mancitylogo.jpg") 
plt.imshow(img)
plt.show()


# FULL SQUAD LIST OF MANCHESTER CITY

# In[67]:

df_fifa[df_fifa["Club"] == "Manchester City"][["Name", "Position", "Overall", "Age", "Wage", "Nationality"]]


# # BEST PLAYER OF MANCHESTER CITY 

# KEVIN DE BRUYNE IS THE HIGHEST RATED MANCHESTER CITY PLAYER IN FIFA19

# In[68]:

plt.figure(1, figsize = (15, 20))
img = mpimg.imread("kevin.jpg") 
plt.imshow(img)
plt.show()


# DEFINING NEW VARIABLE NAME FOR THE CLUBS

# In[69]:

barca = df_fifa[df_fifa["Club"] == "FC Barcelona"]
madrid = df_fifa[df_fifa["Club"] == "Real Madrid"]
liverpool = df_fifa[df_fifa["Club"] == "Liverpool"]
mancity = df_fifa[df_fifa["Club"] == "Manchester City"]


# NUMBER OF FC BARCELONA PLAYERS AVAILABLE FOR EACH POSITION

# In[70]:

barca["Position"].value_counts()


# NUMBER OF REAL MADRID PLAYERS AVAILABLE FOR EACH POSITION

# In[71]:

madrid["Position"].value_counts()


# NUMBER OF LIVERPOOL PLAYERS AVAILABLE FOR EACH POSITION

# In[72]:

liverpool["Position"].value_counts()


# NUMBER OF MANCHESTER CITY PLAYERS AVAILABLE FOR EACH POSITION

# In[73]:

mancity["Position"].value_counts()


# DISTPLOT : AGE OF PLAYERS

# In[74]:

plt.figure(1, figsize = (15, 6))
sns.distplot(barca["Age"], color = "blue")
sns.distplot(madrid["Age"], color = "black")
sns.distplot(liverpool["Age"], color = "red")
sns.distplot(mancity["Age"], color = "white")
plt.title("Comparison of distribution of Age between Top Club players")
plt.tight_layout()
plt.show()


# DISTPLOT : PLAYER RATING

# In[75]:

plt.figure(1, figsize = (15, 6))
sns.distplot(barca["Overall"], color = "blue")
sns.distplot(madrid["Overall"], color = "black")
sns.distplot(liverpool["Overall"], color = "red")
sns.distplot(mancity["Overall"], color = "white")
plt.title("Comparison of distribution of Player Ratings between Top Club players")
plt.tight_layout()
plt.show()


# COMPARING PLAYER VALUE DISTRIBUTION AMONG CLUBS

# In[76]:

plt.figure(1, figsize = (15, 6))
sns.distplot(barca["Value_num"], color = "blue")
sns.distplot(madrid["Value_num"], color = "black")
sns.distplot(liverpool["Value_num"], color = "red")
sns.distplot(mancity["Value_num"], color = "white")
plt.title("Comparison of Player Value between in Top Clubs")
plt.tight_layout()
plt.show()


# COMPARING PLAYER WAGE DISTRIBUTION

# In[77]:

plt.figure(1, figsize = (15, 6))
sns.distplot(barca["Wage_num"], color = "blue")
sns.distplot(madrid["Wage_num"], color = "black")
sns.distplot(liverpool["Wage_num"], color = "red")
sns.distplot(mancity["Wage_num"], color = "white")
plt.title("Comparison of Player Wages between Top Club")
plt.tight_layout()
plt.show()


# COMPARING PLAYER POTENTIAL

# In[78]:

plt.figure(1, figsize = (15, 6))
sns.distplot(barca["Potential"], color = "blue")
sns.distplot(madrid["Potential"], color = "black")
sns.distplot(liverpool["Potential"], color = "red")
sns.distplot(mancity["Potential"], color = "white")
plt.title("Distribution of Player Potential between Top Club")
plt.tight_layout()
plt.show()


# COMPARING PLAYERS FINISHING

# BETTER FINISHING LEADS TO MORE GOALS SCORED

# In[79]:

plt.figure(1, figsize = (15, 6))
sns.distplot(barca["Finishing"], color = "blue")
sns.distplot(madrid["Finishing"], color = "black")
sns.distplot(liverpool["Finishing"], color = "red")
sns.distplot(mancity["Finishing"], color = "white")
plt.title("Distribution of Players Finishing capabilities between Top Club")
plt.tight_layout()
plt.show()


# COUNTPLOT : PLAYER DISTRIBUTION WITH RESPECT TO COUNTRY

# In[80]:

plt.figure(1, figsize = (15, 6))

plt.subplot(1, 4, 1)
sns.countplot(barca["Nationality"], color = "blue")
plt.xticks(rotation=90)
plt.title("FC Barcelona")

plt.subplot(1, 4, 2)
sns.countplot(madrid["Nationality"], color = "black")
plt.xticks(rotation=90)
plt.title("Real Madrid")

plt.subplot(1, 4, 3)
sns.countplot(liverpool["Nationality"], color = "red")
plt.xticks(rotation=90)
plt.title("Liverpool")

plt.subplot(1, 4, 4)
sns.countplot(mancity["Nationality"], color = "green")
plt.xticks(rotation=90)
plt.title("Manchester City")
plt.tight_layout()
plt.show()


# In[81]:

cols = ["Preferred Foot", "International Reputation", 'Skill Moves']
for col in cols:
    plt.subplot(1, 4, 1)
    sns.countplot(barca[col])
    plt.title("FC Barcelona")
    plt.subplot(1, 4, 2)
    sns.countplot(madrid[col])
    plt.title("Real Madrid")
    plt.subplot(1, 4, 3)
    sns.countplot(liverpool[col])
    plt.title("Liverpool")
    plt.subplot(1, 4, 4)
    sns.countplot(mancity[col])
    plt.title("Manchester City")
    plt.tight_layout()
    plt.show()


# # BRAIN BEHIND SUCCESSFULL TEAMS

# ## THE COACH/MANAGERS

# LEFT : PEP GUARDIOLA, CLUBS : FC BARCELONA, FC BAYERN, MANCHESTER CITY

# CENTER : ZINEDINE ZIDANE, CLUB : REAL MADRID

# RIGHT : JURGEN KLOPP, CLUBS : BORUSSIA DORTMUND, LIVERPOOL

# In[91]:

plt.figure(1, figsize = (15, 20))
img = mpimg.imread("managers.jpg") 
plt.imshow(img)
plt.show()


# THEY PLAY A VITAL PART IN TEAMS SUCCESS
