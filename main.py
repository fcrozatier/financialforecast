import json
import streamlit as st
import importlib
# import numpy as np
# import matplotlib.pyplot as plt
# from babel.numbers import format_currency
# import pandas as pd

# Sidebar menu
user_lang = st.sidebar.radio(
     "",
     ('English', 'Français'), index=1)

lang = 'fr' if user_lang == 'Français' else 'en'

with open('translate.json', 'r') as json_data:
  translate = json.loads(json_data.read())

widget = st.sidebar.radio(
  'Widget',
  (translate["widget"][lang][0],
  translate["widget"][lang][1])
)

if (widget == translate["widget"][lang][0] ):
  from real_cost import widget
  with open('translate_real_cost.json', 'r') as json_data:
    translate = json.loads(json_data.read())
else:
  from retirement import widget
  with open('translate_retirement.json', 'r') as json_data:
    translate = json.loads(json_data.read())

# Shared content
st.title(translate["title"][lang])
st.write(translate["intro"][lang])

widget(translate, lang)
