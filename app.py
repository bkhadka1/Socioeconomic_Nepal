import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_csv('API_NPL_DS2_en_excel_v2_5882607 (1).csv', skiprows=3, usecols=[2,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64])

df.info()

#dropping cells with empty values
df.dropna(inplace = True)

print(df.to_string())

# Defining years 2000 to 2020
years = [str(year) for year in range(2000, 2021)]

# Filtering DataFrame for indicators 9 and 10
filtered_df = df[df['Indicator Name'].isin(['9', '10'])]
# Code for Streamlit title 
st.title('Socio-economic Indicators of Nepal: Barriers to Development')

st.write("Nepal is a small country in Southeast Asia located between China and India. Despite being a small country, Nepal is known for beautiful natural landscapes, geodiversity and cultural diversity. Nepal is home to the eight of the tallest mountains in the world, including Mt. Everest")
st.write("However, Nepal has experienced some socio-economic challenges specially in terms of economic growth. Here we look at some of the economic indicators of Nepal from 2000 to 2020 based on the data provided by the World Bank.")
st.write("The purpose of this project is to visualize some of the socio-economic indicators of Nepal based on World Bank data.")

# Creating tabs in the Streamlit app
tabs = st.tabs(["GDP Growth of Nepal", "Lack of Basic Infrastructures", "Lack of Jobs & Youth Outflow"])

# Tab 1: Dropdown Chart for economic indicators
with tabs[0]:
    st.title('Economic Indicators (GDP, GDP per capita, GNI, Adjusted Net National Income)')
    st.write("Nepal is a developing country with just 5 percent economic growth over the last decade. According to The World Bank Data, the GDP growth in Nepal decreased by 1.9 percent in 2023. It was also reported that monetary tightening and effects of import restrictions led to the decline in GDP(https://www.worldbank.org/en/country/nepal/publication/nepaldevelopmentupdate#:~:text=RECENT%20ECONOMIC%20DEVELOPMENTS,restrictions%20contributed%20to%20the%20slowdown.).")
    st.write("The following dropbox below shows different economic indicators of Nepal from 2000 to 2020 based on The World Bank data.")
    # Limiting the dropdown options to indicators 9 and 10 to be used in the chart
    selected_indicator = st.selectbox('Select an Indicator', ['GDP (constant 2015 US$)', 'GDP per capita (constant 2015 US$)', 'GNI (current US$)', 'Adjusted net national income per capita (current US$)'])

    # Filter data for the selected indicator 
    selected_data = df[df['Indicator Name'] == selected_indicator]

    # Generating Altair chart based on the selected indicator
    chart = alt.Chart(selected_data.melt(id_vars=['Indicator Name'], var_name='Year', value_name='Value')).mark_line().encode(
        x=alt.X('Year:N', title='Year'),
        y=alt.Y('Value:Q', title=f'{selected_indicator} Value'),
        color=alt.value('steelblue')  # Use a single color for all bars
    ).properties(
        width=600,
        height=500
    ).configure_axis(
        labelAngle=45
    )

    # Displaying the altair chart
    st.altair_chart(chart, use_container_width=True)

# Tab 2: Stacked Bar Chart and Line Chart

with tabs[1]:
    st.title('Access to Basic Infrastructures (Electricty, Access to clean fuels and technologies for cooking, Access to Safe Drinking Water)')
    
    filtered_df_2 = df[df['Indicator Name'].isin(['Access to electricity (% of population)', 'Access to clean fuels and technologies for cooking (% of population)'])]

    # Melting the dataframe for the second line chart
    melted_data_2 = filtered_df_2.melt(id_vars=['Indicator Name'], var_name='Year', value_vars=years, value_name='Value')

    st.write("Nepal has its fare share of electricity issues in the past as there were frequent power cutoffs over 12 hours a day (https://www.bbc.com/news/world-south-asia-12229752). Since then, the nation has come a long way as they have made significant progress in terms of providing electricity to its citizens. Now, its in a position that around 95 percent of people have access to electricity as of 2023 and it plans on targetting it to increase to 100 percent by 2024. Here are some articles for references: https://myrepublica.nagariknetwork.com/news/95-percent-of-nepali-population-has-now-access-to-electricity/;  https://kathmandupost.com/money/2022/08/18/nepal-aims-100-percent-electricity-access-by-2024")
    
    # Altair second line chart
    line_chart_2 = alt.Chart(melted_data_2).mark_line().encode(
        x='Year:N',
        y=alt.Y('Value:Q', scale=alt.Scale(domain=(0, 100))),
        color=alt.Color('Indicator Name:N', scale=alt.Scale(range=['blue', 'red']), legend=alt.Legend(orient='right', offset=5, labelFontSize=9)),
        tooltip=['Indicator Name', 'Year:N', 'Value:Q']
    ).properties(
        width=400,
        height=400
    )

    # Displaying the second line chart using altair
    st.title("Access to Electricity & Clean Fuels for Cooking")
    st.altair_chart(line_chart_2, use_container_width=True)

    #filtering dataframe for another category
    filtered_df_1 = df[df['Indicator Name'].isin(['Domestic private health expenditure per capita (current US$)', 'Out-of-pocket expenditure (% of current health expenditure)', 'Domestic general government health expenditure (% of GDP)', 'External health expenditure (% of current health expenditure)'])]

    # Melting the dataframe for the second line chart
    melted_data_1 = filtered_df_1.melt(id_vars=['Indicator Name'], var_name='Year', value_vars=years, value_name='Value')

    line_chart_1 = alt.Chart(melted_data_1).mark_line().encode(
        x='Year:N',
        y=alt.Y('Value:Q', scale=alt.Scale(domain=(0, 100))),
        color=alt.Color('Indicator Name:N', scale=alt.Scale(range=['blue', 'red', 'orange', 'green']), legend=alt.Legend(orient='right', offset=5, labelFontSize=9)),
        tooltip=['Indicator Name', 'Year:N', 'Value:Q']
    ).properties(
        width=500,
        height=500
    )
    st.title("Healthcare Expenditure Per Capita")
    st.write("Even though the government of Nepal has declared healthcare as a basic human right, lot of people in rural areas of Nepal lack access to basic health services. According to The Kathmandu Post people in remote areas Rukum municipalities of Rukum have to walk for many hours to reach the district hospital. https://kathmandupost.com/province-no-5/2023/09/04/remote-rukum-villages-lack-even-basic-health-services. Likewise, the government rolled out a healthcare insurance program which expanded to all 77 districts of the country, however according to reports as of 2022 only 20 percent of the population was covered by the scheme.")
    st.altair_chart(line_chart_1, use_container_width=True)
    
    
    
    # filtering dataframe for drinking water chart
    filtered_df = df[df['Indicator Name'].isin(['People using safely managed drinking water services, urban (% of urban population)'])]

    # Melting the dataframe for stacked bar chart
    melted_data = filtered_df.melt(id_vars=['Indicator Name'], var_name='Year', value_vars=years, value_name='Value')

    # Generate line chart using altair
    line_chart = alt.Chart(melted_data).mark_line().encode(
        x='Year:N',
        y=alt.Y('Value:Q', scale=alt.Scale(domain=(0, 100))),
        color=alt.Color('Indicator Name:N', legend=alt.Legend(orient='right', offset=5, labelFontSize=9)),
        tooltip=['Indicator Name', 'Year:N', 'Value:Q']
    ).properties(
        width=400,
        height=400
    )


    # Display the stacked bar chart and line chart in altair
    st.title("Urban Population using safely managed drinking water services")
    st.write("Having poor infrastructure development, lots of people in Nepal specially rural and remote areas lack access to drinking water.")
    st.write("According to an article published by UNICEF 10.8 million people in Nepal do not have access to improved sanitation, and 3.5 million do not have access to basic water services. https://www.unicef.org/nepal/water-and-sanitation-wash")
    st.altair_chart(line_chart, use_container_width=True)


# Tab 3: Third tab with charts
with tabs[2]:
    st.title('Youth Outflow and Heavy Reliance on Remittances')

    # Writing Description for the third chart
    st.write("The cost of living has increased significantly over the last few years in Nepal and high inflation has been on the rise. Because of this people are unable to make their ends meet. This has resulted in forcing youths to seek employment in foreign countries. According to the reports by The Kathmandu Post, in the fiscal year 2021-2022, everyday 1,745 Nepalis on average left the country for foreign employment(https://kathmandupost.com/national/2022/11/21/high-inflation-and-unemployment-are-forcing-youths-to-seek-foreign-jobs).")

    filtered_df_3 = df[df['Indicator Name'].isin(['Labor force participation rate, male (% of male population ages 15-64) (modeled ILO estimate)', 'Labor force participation rate, female (% of female population ages 15-64) (modeled ILO estimate)'])]

    # Melting the dataframe for the line chart
    melted_data_3 = filtered_df_3.melt(id_vars=['Indicator Name'], var_name='Year', value_vars=years, value_name='Value')

    line_chart_3 = alt.Chart(melted_data_3).mark_line().encode(
        x='Year:N',
        y=alt.Y('Value:Q', scale=alt.Scale(domain=(0, 100))),
        color=alt.Color('Indicator Name:N', scale=alt.Scale(range=['blue', 'red']), legend=alt.Legend(orient='right', offset=5, labelFontSize=9)),
        tooltip=['Indicator Name', 'Year:N', 'Value:Q']
    ).properties(
        width=400,
        height=400
    )

    # Display the line chart in altair
    st.title("Labor force participation")
    st.altair_chart(line_chart_3, use_container_width=True)   

    filtered_df_4 = df[df['Indicator Name'].isin(['Unemployment, total (% of total labor force) (modeled ILO estimate)', 'Unemployment, youth total (% of total labor force ages 15-24) (modeled ILO estimate)', 'Unemployment, youth female (% of female labor force ages 15-24) (modeled ILO estimate)', 'Unemployment, youth total (% of total labor force ages 15-24) (modeled ILO estimate)'])]

    # Melt the dataframe to be used with certain indicators
    melted_data_4 = filtered_df_4.melt(id_vars=['Indicator Name'], var_name='Year', value_vars=years, value_name='Value')

    line_chart_4 = alt.Chart(melted_data_4).mark_line().encode(
        x='Year:N',
        y=alt.Y('Value:Q', scale=alt.Scale(domain=(0, 100))),
        color=alt.Color('Indicator Name:N', scale=alt.Scale(range=['blue', 'red', 'green']), legend=alt.Legend(orient='right', offset=5, labelFontSize=9)),
        tooltip=['Indicator Name', 'Year:N', 'Value:Q']
    ).properties(
        width=400,
        height=400
    )

    # Display the line chart in altair
    st.title("Unemployment among Youths in Nepal")
    st.write("Likewise, the ILO reports suggest that over 400,000 young people are estimated to enter the workforce everyyear and the unemployment rate for youth aged 18-29 is around 19.2 percent which has compelled the youths to leave their country for employment opportunities(https://www.ilo.org/kathmandu/areasofwork/employment-promotion/lang--en/index.htm#:~:text=Employment%20challenges&text=The%20unemployment%20rate%20for%20youth,the%20employment%20challenge%20in%20Nepal.).")
    st.altair_chart(line_chart_4, use_container_width=True)  

    #filtering dataframe

    filtered_df_5 = df[df['Indicator Name'].isin(['Net migration'])]

    # Melting the dataframe again
    melted_data_5 = filtered_df_5.melt(id_vars=['Indicator Name'], var_name='Year', value_vars=years, value_name='Value')

    line_chart_5 = alt.Chart(melted_data_5).mark_bar().encode(
        x='Year:N',
        y=alt.Y('Value:Q'),
        color=alt.condition(
            alt.datum.Value > 0,
         alt.value("green"),
         alt.value("red")   
        )
    ).properties(width=600)

    # Display the line chart in altair
    st.title("Net migration in Nepal")
    st.write("The consequences of lack of employment opportunites has resulted in negative immigration in the country. Millions of people specially youths have left the country for better opportunites or income than staying home. If this trend continues, it would create a lot of problems for the nation in terms of economic development(https://myrepublica.nagariknetwork.com/news/why-are-nepalis-leaving-the-country/).")
    st.altair_chart(line_chart_5, use_container_width=True)


st.dataframe(df)
st.write("Source: The World Bank https://data.worldbank.org/country/nepal")
