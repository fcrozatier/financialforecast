import json
import markdown
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from babel.numbers import format_currency
#import pandas as pd

# Setup language translation
with open('translate.json', 'r') as json_data:
    translate = json.loads(json_data.read())

user_lang = st.sidebar.radio(
     "",
     ('English', 'Français'), index=1)

lang = 'fr' if user_lang == 'Français' else 'en'

category = st.sidebar.radio(
     translate["category"]["label"][lang],
     (translate["category"]["values"][lang][0],
     translate["category"]["values"][lang][1]))

price = st.sidebar.number_input(
    translate["price label"][lang][category], 100)
rate = st.sidebar.slider(translate["rate label"][lang], 0.0, 10.0, 4.0, 0.01)
time = st.sidebar.slider(translate["duration label"][lang], 0, 50, 15)

t = np.arange(0.0, 50, 0.01)

# Create appropriate functions to plot
if category == translate["category"]["values"][lang][0]:
  s = price * np.power(1 + rate / 100, t)
  cost = price * np.power(1 + rate / 100, time)
else:
  s = (price * 100 / rate) * ( np.power(1 + rate / 100, t) - 1)
  cost = (price * 100 / rate) * ( np.power(1 + rate / 100, time) - 1)

formatted_cost = format_currency(
  round(cost, 2),
  translate["currency"][lang],
  locale=translate["locale"][lang]
  )

fig, ax = plt.subplots()
ax.plot(t,s)
ax.plot([time],[cost], 'ro')
ax.annotate(
  formatted_cost,
  xy=(time, cost), xytext=(0, -10),
  textcoords="offset points", ha="center", va="top",
  color="red"
  )
ax.set(
  xlabel=translate["plot"][lang]["xlabel"],
  ylabel=translate["plot"][lang]["ylabel"],
  title=translate["plot"][lang]["title"]
  )
ax.grid()


st.title(translate["title"][lang])
st.write(translate["intro"][lang])

if st.checkbox(translate["formula"][lang]):
  file_name = translate["formula path"][lang][category]
  st.markdown(open(file_name, 'r').read())


st.pyplot(fig)

st.write(translate["conclusion"][lang].format(time, formatted_cost))