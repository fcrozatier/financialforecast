import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from babel.numbers import format_currency
#import pandas as pd

st.title("Coût réel d'un achat")

st.write(
  "Faire une dépense c'est consommer du capital que l'on aurait potentiellement investi ailleurs sur le long terme. Quel est le coût réel d'un achat unique ou d'un abonnement récurrent si l'on prend en compte cette opportunité d'investissement perdue ? ")


if st.checkbox('Voir les formules'):
    st.text('ICI LES FORMULES')

category = st.sidebar.radio(
     "Type de dépense :",
     ('Achat unique', 'Abonnement'))

def generate_price_label(cat):
  switcher = {
    "Achat unique": "Prix d'achat",
    "Abonnement": "Coût annuel"
  }
  return switcher[cat]

price = st.sidebar.number_input(generate_price_label(category), 100)
rate = st.sidebar.slider("Taux d'intérêt de vos investissements :", 0.0, 10.0, 4.0, 0.01)
time = st.sidebar.slider("Durée de l'investissement en année :", 0, 50, 15)


t = np.arange(0.0, 50, 0.01)
s = price * np.power(1 + rate / 100, t)
cost = price * np.power(1 + rate / 100, time)
formatted_cost = format_currency(round(cost,2), 'EUR', locale="fr_FR")

fig, ax = plt.subplots()
ax.plot(t,s)
ax.plot([time],[cost], 'ro')
ax.annotate('{} €'.format(round(cost,2)), xy=(time, cost), xytext=(0, -10), textcoords="offset points", ha="center", va="top", color="red")
ax.set(xlabel='Années', ylabel='Coût (€)',
       title="Evolution du coût")
ax.grid()

st.pyplot(fig)

st.write("Coût d'opportunité après {} années : **{}**".format(time, formatted_cost))