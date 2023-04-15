# Imports libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gps
from datetime import datetime
from wordcloud import WordCloud
from scipy.stats import chi2_contingency
from dataprep.eda import *
import warnings
warnings.filterwarnings("ignore")

# Fetchs data file and assigns it to df(dataframe)
df = pd.read_excel("Baltimore_Crime_Data_2022.xlsx")

# Prints First 5 rows of dataframe
df.head()

# Prints (total_rows, total_columns) of dataframe
df.shape

# Prints statistical information of numeric values of dataframe
df.describe()

# Print basic information about dataframe
df.info()

# Prints Duplicate values if any
df.duplicated().any()

# Prints the sum of null values in all the columns of dataframe
df.isnull().sum()

# Get Missing value counts
null_counts = [df[col].isnull().sum() for col in df.columns]

# Create a bar plot
sns.barplot(x=list(df.columns), y=null_counts, palette='rocket')

# Set axis labels and title
plt.xlabel('Columns')
plt.ylabel('Missing Value Counts')
plt.title('Missing Value Counts for Each Column')
plt.xticks(rotation=90)

# Display the plot
plt.show()

# Prints count of unique values of each column of the dataframe
df.nunique()

# Get unique value counts
value_counts = [df[col].nunique() for col in df.columns]

# Create a bar plot
sns.barplot(x=list(df.columns), y=value_counts, palette='pastel')

# Set axis labels and title
plt.xlabel('Columns')
plt.ylabel('Unique Value Counts')
plt.title('Unique Value Counts for Each Column')
plt.xticks(rotation=90)

# Display the plot
plt.show()

# Performs overall EDA on the dataframe
create_report(df)

# Creates a variable containing geodataframe containing latitude and longitude pairs
df_geo = gps.GeoDataFrame(df, geometry = gps.points_from_xy(df.longitude, df.latitude))
df_geo

# Fetch world map
world_data = gps.read_file(gps.datasets.get_path('naturalearth_lowres'))

# Filter to the United States and set figure size
US_map = world_data[world_data.iso_a3 == 'USA'].plot(figsize=(10, 6), color='white', edgecolor='black')

# Plot geo data on the map
df_geo.plot(ax=US_map, color='red', legend=True, markersize=50)

# Set title and axis labels
plt.title('Locations in the United States', fontsize=16)
plt.xlabel('Longitude', fontsize=12)
plt.ylabel('Latitude', fontsize=12)

plt.show()

# Create a figure with 1 row and 2 columns with a figure size of 15x5
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

# Create a boxplot for the 'age' column and assign it to the right subplot (axs[1])
sns.boxplot(x='age', data=df, ax=axs[1])
axs[1].set_title("Age Boxplot")
axs[1].set_ylabel('Age', fontsize=12)

# Create a histogram for the 'age' column and assign it to the left subplot (axs[0])
sns.histplot(x='age', data=df, bins=100, ax=axs[0])
axs[0].set_title("Age Histogram")
axs[0].set_xlabel('Age', fontsize=12)
axs[0].set_ylabel('Count', fontsize=12)

# Set title and show plot
plt.suptitle('Distribution of Age', fontsize=16)
plt.show()


# Create a countplot for the 'ethnicity' column and assign it to the y-axis
plt.figure(figsize=(8, 6))
sns.countplot(y='ethnicity', data=df, palette='Set1')

# Set the x-axis and y-axis labels
plt.xlabel('Count', fontsize=12)
plt.ylabel('Ethnicity', fontsize=12)

# Set the title and show the plot
plt.title('Distribution of Ethnicity', fontsize=16)
plt.show()

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8,6))

# Plot the bar chart using Seaborn
sns.countplot(x='race', data=df, palette='Set2', ax=ax)

# Set axis labels and title
ax.set_xlabel('Race', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Distribution of Race', fontsize=16)

# Rotate the x-axis labels
plt.xticks(rotation=45)

# Add text labels above each bar
for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 2, 
            str(i.get_height()), fontsize=11, ha='center')

plt.show()

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8,6))

# Plot the bar chart using Seaborn
sns.countplot(x='gender', data=df, palette='Set3', ax=ax)

# Set axis labels and title
ax.set_xlabel('Gender', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Distribution of Gender', fontsize=16)

# Rotate the x-axis labels
plt.xticks(rotation=0)

# Add text labels above each bar
for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 0.5, 
            str(i.get_height()), fontsize=10, ha='center')

plt.show()

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bar chart using Seaborn
sns.countplot(x='description', data=df, palette='crest', ax=ax, order=df['description'].value_counts().index)

# Set axis labels and title
ax.set_xlabel('Descriptions', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Distribution of Descriptions', fontsize=16)

# Rotate the x-axis labels
plt.xticks(rotation=90)

# Add text labels above each bar
for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 0.5, 
            str(round(i.get_height(), 2)), fontsize=10, ha='center')

plt.show()

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bar chart using Seaborn
sns.countplot(x='weapon', data=df, palette='flare', ax=ax, order=df['weapon'].value_counts().index)

# Set axis labels and title
ax.set_xlabel('Used Weapons', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Distribution of Used Weapons', fontsize=16)

# Rotate the x-axis labels
plt.xticks(rotation=90)

# Add text labels above each bar
for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 0.5, 
            str(round(i.get_height(), 2)), fontsize=10, ha='center')

plt.show()

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8,6))

# Plot the bar chart using Seaborn
sns.countplot(x='inside_outside', data=df, palette='Set3', ax=ax)

# Set axis labels and title
ax.set_xlabel('Inside - Outside', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Distribution of Crime Inside or Outside', fontsize=16)

# Rotate the x-axis labels
plt.xticks(rotation=0)

# Add text labels above each bar
for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 0.5, 
            str(i.get_height()), fontsize=10, ha='center')

plt.show()

# Set Seaborn style and color palette
sns.set_style("whitegrid")
sns.set_palette("pastel")

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8, 8))

# Define colors for the pie chart
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffb3e6']

# Plot the pie chart
df["district"].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=colors, ax=ax)

# Set axis labels and title
ax.set_xlabel('District', fontsize=12)
ax.set_ylabel('')
ax.set_title('Distribution of Districts', fontsize=16)

# Add spacing around the chart
plt.tight_layout()

plt.show()


# Create a dictionary of neighborhood counts
neighborhood_counts = dict(df['neighborhood'].value_counts())

# Generate word cloud image
wordcloud = WordCloud(width = 800, height = 800, background_color ='white', min_font_size = 10, colormap='viridis', max_words=df['neighborhood'].nunique()).generate_from_frequencies(neighborhood_counts)

# Display the generated image
plt.figure(figsize = (10, 10), facecolor = None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad = 0)

# Add a title
plt.title('Most Common Crime Sites', fontsize=20, pad=20, color='black')

# Show the plot
plt.show()


# Group the data by description and weapon, and count the number of occurrences
grouped = df.groupby(['description', 'weapon'])['objectid'].count().reset_index()

# Pivot the data to create a matrix with description as rows and weapon as columns
pivoted = grouped.pivot(index='description', columns='weapon', values='objectid').fillna(0)

# Create a horizontal stacked bar chart
pivoted.plot(kind='barh', stacked=True, figsize=(10,8))

# Add title and axis labels
plt.title('Crime by Description and Weapon', fontsize=16)
plt.xlabel('Number of Incidents', fontsize=12)
plt.ylabel('Description of Crime', fontsize=12)

# Set legend
plt.legend(title='Used Weapons', loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()

# Create a pairplot of the data frame (df)
sns.pairplot(df)

#Create a boxplot for the 'age' column by 'district', with 'race' as the hue and assign it to the axes (ax)
sns.set_style("whitegrid")
plt.figure(figsize=(12,8))
ax = sns.boxplot(x='district', y='age', data=df, hue='race', palette='Paired', width=0.8)

#Add title and axis labels
plt.title('Age by District and Race', fontsize=16)
plt.xlabel('District', fontsize=12)
plt.ylabel('Age', fontsize=12)

#Set legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, title='Race', loc='upper right')

plt.show()

### Dropping the unnecessary columns:
- To start with, as we have seen so far the coordinates (latitude and longitude) are not so useful for us to draw any conclusion out of it. Also, the columns <b>X</b>, <b>Y</b>, <b>latitude</b>, <b>longitude</b>, <b>geolocation</b> and a new one created by us <b>geometry</b> this all have the coordinate values. Thus, we will drop this columns.
- Secondly, the <b>ccno</b> and <b>objectid</b> has almost every values as unique and which does not provide us with any context related to data.On the other hand, for <b>total_incidents</b> have just one value which is 1, and <b>shape</b> column is NaN. Thus, both columns will be dropped.
- Moreover, the <b>ethnicity</b> has to many missing values and does not add more context to our data so it can be dropped.
- Lastly, there are many cloumns providing lacation informations, the <b>location</b> column has to many uniques values for a catagorical variable while as we know <b>post</b> column is derived using neighborhoods it can be dropped as well.

df.drop(['X', 'Y', 'ccno', 'location', 'post', 'latitude', 'geometry', 'longitude', 'geolocation', 'total_incidents', 'objectid', 'shape', 'ethnicity'], axis=1, inplace=True)

### Transforming the crimedatetime:
- Here we will divide the date and time for better usage for analysis.
- First, we will convert the crimedatetime to Date and Time column and then the from the Date column we will select just the Month's values as we have only 2022 years data and days are too many for a catagorical variable.
- Thus, after transforming the Date we will end up with just the month name.

df['crimedatetime'] = pd.to_datetime(df['crimedatetime'])

# Split DateTime into separate Date and Time columns
df['Date'] = df['crimedatetime'].dt.date
df['Time'] = df['crimedatetime'].dt.time

# convert date format to just month
df['Month'] = pd.to_datetime(df['Date']).dt.strftime('%m')

# convert month numbers to month names
df['Month_name'] = pd.to_datetime(df['Month'], format='%m').dt.strftime('%B')

df.head()

### Transforming the Time:
- After splitting the date and time we will further split time into 4 parts of the day: Morning, Afternoon, Evening, and Night.
- Lastly we will delete the uneccessory columns which are <b>crimedatetime</b>, <b>Date</b>, <b>Time</b>, and <b>Month</b>.

def get_time_category(time_str):
    """
    Convert time value to time category: morning, afternoon, evening, or night.
    """
    time_obj = pd.to_datetime(time_str, format='%H:%M:%S')
    hour = time_obj.hour
    if hour >= 5 and hour < 12:
        return 'morning'
    elif hour >= 12 and hour < 17:
        return 'afternoon'
    elif hour >= 17 and hour < 21:
        return 'evening'
    else:
        return 'night'
    
df['time_of_day'] = df['Time'].apply(get_time_category)

df_dropped_datetime = df.drop(['crimedatetime', 'Date', 'Time', 'Month'], axis=1, inplace=True)


### Merging the crimecode and description:
- We will merge these two because one is the code for crime and another is it's description. Then, we will delete the individual columns.

df['Crime_Code_Desc'] = df['crimecode'] + '_' + df['description']
df.head()

df_dropped_datetime = df.drop(['crimecode', 'description'], axis=1, inplace=True)


### Adding Unknown catagory to weapons and race column:
- We will add Unknown catagory to these columns because both of them are important and adding unknown will not deteriorate the authenticity of data.

df['weapon'] = df['weapon'].fillna('Unknown')

df['race'] = df['race'].fillna('Unknown')

df['gender'] = df['gender'].replace({'M': 'Male', 'F': 'Female', 'U': 'Not Specified'})
df['gender'] = df['gender'].fillna('Not Specified')

### Adding mean to the NaN value in Age column:
- Mean is the most preffered option as the data is normaly distribute.

# Calculate the mean age
mean_age = df['age'].mean()

# Replace NaN values with the mean age
df['age'].fillna(mean_age, inplace=True)

df.head()

### Removing rows with more than 4 NaNs.
- These rows have more 4 or more NaN values in it so it can be dropped.

# count the number of NaN values in each row
nan_row_counts = df.isna().sum(axis=1)

# select the rows with three or more NaN values
rows_with_nans = df[nan_row_counts >= 4]

print(rows_with_nans)

df.dropna(thresh=4, inplace=True)

### Dropping the NaN values of inside_outside:
- As inside_outside and premises both have same NaNs it will remove NaNs from both of them and as they are important factors we can not delete them completely.

df['inside_outside'] = df['inside_outside'].replace({'O': 'Outside', 'I': 'Inside'})

df = df.dropna(subset=['inside_outside'])

df.isnull().sum()

### Filling the district and neighborhood using ffill function:
- This function will fill the values of the above value in the column, we can use this fuction for this because these have very few NaN values in it.

df['district'].fillna(method='ffill', inplace=True)
df['neighborhood'].fillna(method='ffill', inplace=True)

df = df.reset_index(drop=True)

df.head()

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8,6))


# Get the top three categories in the race column
top_three = df['race'].value_counts().nlargest(3).index.tolist()

# Replace all other categories with 'Other'
df.loc[~df['race'].isin(top_three), 'race'] = 'Other'

# Plot the bar chart using Seaborn
sns.countplot(x='race', data=df, palette='Set2', ax=ax)

# Set axis labels and title
ax.set_xlabel('Race', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Distribution of Race', fontsize=16)

# Rotate the x-axis labels
plt.xticks(rotation=45)

# Add text labels above each bar
for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 2, 
            str(i.get_height()), fontsize=11, ha='center')

plt.show()

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8,6))

# Plot the bar chart using Seaborn
sns.countplot(x='gender', data=df, palette='Set3', ax=ax)

# Set axis labels and title
ax.set_xlabel('Gender', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Distribution of Gender', fontsize=16)

# Rotate the x-axis labels
plt.xticks(rotation=0)

# Add text labels above each bar
for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 0.5, 
            str(i.get_height()), fontsize=10, ha='center')

plt.show()

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8,6))

# Plot the bar chart using Seaborn
sns.countplot(x='inside_outside', data=df, palette='Set3', ax=ax)

# Set axis labels and title
ax.set_xlabel('Inside - Outside', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Distribution of Crime Inside or Outside', fontsize=16)

# Rotate the x-axis labels
plt.xticks(rotation=0)

# Add text labels above each bar
for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 0.5, 
            str(i.get_height()), fontsize=10, ha='center')

plt.show()

# Get value counts for the "district" column
district_counts = df['district'].value_counts()

# Create a new "district" series with top five and "Others"
top_districts = district_counts[:5]
other_districts = pd.Series(district_counts[6:].sum(), index=['Others'])
district_series = pd.concat([top_districts, other_districts])

# Set Seaborn style and color palette
sns.set_style("whitegrid")
sns.set_palette("pastel")

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8, 8))

# Define colors for the pie chart
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffb3e6','#c2c2f0']

# Plot the pie chart
district_series.plot.pie(ax=ax, autopct='%1.1f%%', startangle=90, colors=colors)

# Set axis labels and title
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_title('Distribution of Districts', fontsize=16)

# Add spacing around the chart
plt.tight_layout()

plt.show()


# Create a dictionary of neighborhood counts
neighborhood_counts = dict(df['neighborhood'].value_counts())

# Generate word cloud image
wordcloud = WordCloud(width = 800, height = 800, background_color ='white', min_font_size = 10, colormap='viridis', max_words=df['neighborhood'].nunique()).generate_from_frequencies(neighborhood_counts)

# Display the generated image
plt.figure(figsize = (10, 10), facecolor = None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad = 0)

# Add a title
plt.title('Most Common Crime Sites', fontsize=20, pad=20, color='black')

# Show the plot
plt.show()




