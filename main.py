import os
import json
import streamlit as st


script_dir = os.path.dirname(__file__)

# Sidebar menu
user_lang = st.sidebar.radio(
     "",
     ('English', 'Français'),
     index=0
)

lang = 'fr' if user_lang == 'Français' else 'en'

with open('translate.json', 'r') as json_data:
  translate = json.loads(json_data.read())

widget = st.sidebar.radio(
  'Widget',
  (
    translate["widget"][lang][0],
    translate["widget"][lang][1],
    translate["widget"][lang][2],
  ),
  index=1
)

if (widget == translate["widget"][lang][0] ):
  from widget.real_cost import widget
  translate_path = os.path.join(script_dir, 'translate/real_cost.json')
  with open(translate_path, 'r') as json_data:
    translate = json.loads(json_data.read())
elif (widget == translate["widget"][lang][1] ):
  from widget.retirement import widget
  translate_path = os.path.join(script_dir, 'translate/retirement.json')
  with open(translate_path, 'r') as json_data:
    translate = json.loads(json_data.read())
elif (widget == translate["widget"][lang][2] ):
  from widget.less_vs_more import widget
  translate_path = os.path.join(script_dir, 'translate/less_vs_more.json')
  with open(translate_path, 'r') as json_data:
    translate = json.loads(json_data.read())


# Shared content
st.title(translate["title"][lang])
st.write(translate["intro"][lang])

widget(translate, lang)

# Contribute
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.markdown("##### Contribute: [github](https://github.com/fcrozatier/financialforecast)"
  )
