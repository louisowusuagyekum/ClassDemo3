import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("My First App!")

# Load penguins data
data = pd.read_csv('https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/refs/heads/main/data/penguins.csv')

# Display raw data
st.write('Raw Data')
st.dataframe(data)

# Sidebar for user input
st.sidebar.header('Filter the Options')
selected_category = st.sidebar.selectbox('Select Category', options=['ALL', 'Adelie', 'Gentoo', 'Chinstrap'])

# Filter data based on selection
if selected_category != 'ALL':
    filtered_data = data[data['species'] == selected_category]
else:
    filtered_data = data

# Display scatter chart
st.write('This shows the scatter chart')
st.scatter_chart(filtered_data, x='flipper_length_mm', y='body_mass_g', color='species')

# Seaborn Histogram
st.write("Seaborn Histogram of Culmen Length")
fig, ax = plt.subplots()
sns.histplot(filtered_data, x='culmen_length_mm', kde=True, ax=ax)
st.pyplot(fig)

# Bar Chart - Average Body Mass by Species
st.write("Average Body Mass by Species")
avg_mass = data.groupby('species')['body_mass_g'].mean().reset_index()

fig_bar, ax_bar = plt.subplots()
sns.barplot(data=avg_mass, x='species', y='body_mass_g', ax=ax_bar)
ax_bar.set_ylabel("Average Body Mass (g)")
st.pyplot(fig_bar)

# Pie Chart - Species Distribution
st.write("Species Distribution")
species_counts = data['species'].value_counts()

fig_pie, ax_pie = plt.subplots()
ax_pie.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
ax_pie.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
st.pyplot(fig_pie)

