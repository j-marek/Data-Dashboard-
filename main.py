import streamlit as st 
import pandas


data = {
  'Spaghetti':[9, 2, 6, 5, 3],
  'Ravioli':[3, 1, 4, 1, 5]
}

df = pandas.DataFrame(data)

st.title('I made this website')
st.subheader("It ain't much, but it's honest work")
st.write('''
             Here is some data in a table with no real meaning.
''')
st.write(df)
st.line_chart(df)

myslider = st.slider('lbs')
st.write(myslider, 'in kg is', myslider * 0.453592)
