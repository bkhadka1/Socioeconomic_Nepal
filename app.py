import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_csv('API_NPL_DS2_en_excel_v2_5882607 (1).csv', skiprows=3, usecols=[2,44,45,46,47,48,49,50,51,52,53,54,55,56,57,57,59,60,61,62,63,64])

df.info()

df.dropna(inplace = True)

print(df.to_string())

# Code for Streamlit title 
st.title('Socio-economic Indicators of Nepal from 2000 to 2020')

# Dropdown for selecting an indicator in Streamlit
selected_indicator = st.selectbox('Select an Indicator', df['Indicator Name'].unique())

# Filter data for the selected indicator in Streamlit
selected_data = df[df['Indicator Name'] == selected_indicator]

# Generating Altair chart based on the selected indicator in Streamlit
chart = alt.Chart(selected_data.melt(id_vars=['Indicator Name'], var_name='Year', value_name='Value')).mark_bar().encode(
    x=alt.X('Year:N', title='Year'),
    y=alt.Y('Value:Q', title=f'{selected_indicator} Value'),
    color=alt.Color('Year:N', legend=None)
).properties(
    width=600,
    height=400
).configure_axis(
    labelAngle=45
)

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)

st.dataframe(df)

