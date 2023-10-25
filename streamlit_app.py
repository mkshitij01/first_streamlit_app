import streamlit

streamlit.title('My Parents New Family Diner')

streamlit.header('Menu')
streamlit.text('🥗 Salad')
streamlit.text('🍞 Bread')
streamlit.text('🥣 Curry')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
