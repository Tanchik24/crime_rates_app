import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

from setting_functions import get_feature_visualization
from visualization_functions import get_animated_line_graph


def get_main_bar():
    
    # set title and description 
    header = st.columns([2,1])
    with header[0]:
        st.markdown('''<h1 style="text-align: left; font-family: 'Gill Sans'; color: #D8D8D8"
            >Исследование преступности в США</h1><h1 style="text-align: left; font-family: 'Gill Sans'; color: #FF2A00"
            >с 1960 по 2014</h1>''', 
            unsafe_allow_html=True)
    with header[1]:
        for num in range(7):
            st.markdown('')
        st.markdown('''<h3 style="text-align: right; font-family: 'Gill Sans'; color: #FF2A00"
            >by Tanchik</h3>''', 
            unsafe_allow_html=True)
    
    for num in range(2):
        st.markdown(" ")
    st.markdown('''<p style="text-align: left; font-family: 'Gill Sans'; font-size: 20px; color: #D8D8D8">
            Данный обзор поможет вам сделать вывод, сколько в среднем преступлений было зарегистрировано 
            в США в течении 54 лет. Что в криминальном мире было развито больше всего: убийство,
            воровство, грабеж... Также вы узнаете сколько имущества было похище и угнано машин. Наглядно увидите,
            как преступная жизнь менялась со временем в период с 1960 по 2014.</p>''', 
            unsafe_allow_html=True)
    for num in range(2):
        st.markdown(" ")
    
    # set row with data description 
    data_description_expanders = st.columns(2)
    
    # description of features
    data_description_expanders[0].markdown('''<h2 style="text-align: left; font-family: 'Gill Sans'; color: #FF2A00; font-size: 28px"
            >Познакомимся с признаками</h2>''', 
            unsafe_allow_html=True)
    
    # expander's text
    with data_description_expanders[0].expander('Описание столбцов:'):
        st.markdown("""<span style="font-family: 'Gill Sans'; color: #D8D8D8">
        \n**Year** - Исследуемый год
        \n**Population** - Население на текущий год
        \n**Violent** - Зарегистрированные случаи насилия за текущий год
        \n**Property** - Количестов похищеного имущества за текущий год
        \n**Murder** - Количество убийств за текущий год
        \n**Forcible_Rape** - Количество случаев насилия за текущий год
        \n**Robbery** - Количество грабежей за текущий год
        \n**Aggravated_assault** - Количество нападений при отягчающих обстоятельствах за текущий год
        \n**Burglary** - Количество краж со взломом за текущий год
        \n**Larceny_Theft** - Посягательство на чужое имущество
        \n**Vehicle_Theft** - Количество угнаного транспорта за текущий год</span>
        """, unsafe_allow_html=True) 
     
    # DataFrame visualization   
    data_description_expanders[1].markdown('''<h2 style="text-align: left; font-family: 'Gill Sans'; color: #FF2A00; font-size: 28px"
            >Посмотрим на данные</h2>''', 
            unsafe_allow_html=True)
    
    with data_description_expanders[1].expander('Выберите исследуемые признаки:'):
        multicol = st.multiselect('Столбцы', data.columns.to_list())
        if not multicol:
            pass
        else:
            st.dataframe(data[multicol], use_container_width=True)
    
    # descriptive statistics and line graph
    graph_col, stats_col = st.columns([2, 1])
    
    with graph_col:
        st.plotly_chart(get_animated_line_graph(data, 'Total'), use_container_width=True)
        
    with stats_col:
        for num in range(3):
            st.write(' ')
        st.markdown('''<h3 style="text-align: center; font-family: 'Gill Sans'; color: #D8D8D8; font-size: 20px"
            >Статистическая характеристика</h3>''',
            unsafe_allow_html=True)
        st.dataframe(data.describe(), use_container_width=True)  
        


def get_side_bar():
    
    st.sidebar.markdown('''<h2 style="text-align: lift; font-family: 'Gill Sans'; color: #D8D8D8; font-size: 20px"
            >Выберите признак, который хотите визуализировать: </h2>''',
            unsafe_allow_html=True)

    st.sidebar.write(' ')
    
    # Feature visualization
    # Total
    if st.sidebar.checkbox('Признак: Total'):
        get_feature_visualization(data, 'Total', False, False)
    
    # create a list of remaning features and visualize   
    columns = data.columns.tolist()
    columns.remove('Total')
    columns.remove('Year')
    
    for column in columns:
        if st.sidebar.checkbox(f'Признак: {column}'):
            get_feature_visualization(data, column)
    
    st.sidebar.markdown('''<h3 style="text-align: left; font-family: 'Gill Sans'; color: #FF2A00; font-size: 15px"
            >by Tanchik</h3>''', 
            unsafe_allow_html=True)

             
    
if __name__ == '__main__':
    
    # set page settings
    st.set_page_config(layout="wide")
    
    # add DataFrame
    data = pd.read_csv('data/US_Crime_Rates_1960_2014.csv')
    
    get_main_bar()
    get_side_bar()