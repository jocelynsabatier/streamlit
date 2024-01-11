
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import altair as alt

# Install Altair using pip within the Streamlit app
subprocess.run(["pip", "install", "altair"])

st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover streamlit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
st.write(df_cars)

df_heatmap = df_cars.drop('continent', axis =1)

st.title( "Heatmap of cars and their characteristics")

import seaborn as sns
viz_correlation = sns.heatmap(df_heatmap.corr(),
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)


# Increase the size of the pairplot
plt.figure(figsize=(15, 12))  # Adjust the size as needed
sns.set_theme(style="ticks")
st.title("Pairplot regarding cars and their characteristics")
fig = sns.pairplot(df_cars, hue="continent")
st.pyplot(fig)


st.write("It seems that MPG (Miles Per Gallon) and weight are highly negatively correlated, which makes perfect sense !")
st.write("On the contrary Horsepower and Weight are highly positively correlated, which also makes sense !")


#Nous créons des boutons ici
st.title('DataFrame Filter by Continent')


# Create a button to filter the DataFrame by continent
selected_continent = st.selectbox('Select Continent', df_cars['continent'].unique())

# Filter the DataFrame based on the selected continent
filtered_df = df_cars[df_cars['continent'] == selected_continent]

# Display the filtered DataFrame
st.write(f'Filtered DataFrame for {selected_continent}:')
st.write(filtered_df)



# Create Streamlit app
st.title('Average Weight Evolution for the Selected Continent')

# Calculate the average weight for each year
average_weight_df = filtered_df.groupby('year')['weightlbs'].mean().reset_index()

# Create a bar chart for the average weight evolution
chart = alt.Chart(average_weight_df).mark_bar().encode(
    x='year',
    y='weightlbs',
    tooltip=['year', 'weightlbs'],
).properties(
    width=600,
    height=400,
    title=f'Average Weight Evolution for {selected_continent}'
)
st.altair_chart(chart, use_container_width=True)


