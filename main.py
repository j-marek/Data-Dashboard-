import streamlit as st 
import pandas


data = {
  'Noodles':[5, 8, 9, 7, 9],
  'Spaghetti':[9, 2, 6, 5, 3],
  'Ravioli':[3, 1, 4, 1, 5]
}

df = pandas.DataFrame(data)

st.title('I made this website')
st.subheader("It ain't much, but it's honest work.")
st.write('''
             Here is some data in a table with no real meaning.
''')
st.write(df)
st.write('''
             Here is that data in a line chart!
''')
st.line_chart(df)

myslider = st.slider('lbs')
st.write(myslider, 'lbs in kgs is', myslider * 0.453592)

st.write('''
             And some audio to top it off!
''')
st.audio("https://upload.wikimedia.org/wikipedia/commons/c/c5/De-Otter.ogg")