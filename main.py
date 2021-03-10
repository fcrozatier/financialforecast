import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title("Coût réel d'un achat")

st.write(
  "Faire une dépense c'est utiliser du capital que l'on aurait pu investir ailleurs sur le long terme. Quel est le coût réel à long terme d'un achat unique ou d'un abonnement récurrent si l'on prend en compte l'opportunité d'investissement perdue ? ")

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df


option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option
