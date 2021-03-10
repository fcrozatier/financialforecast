import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

price = st.sidebar.number_input(generate_price_label(category))
taux = st.sidebar.slider("Taux d'intérêt de vos investissements :", 0.0, 10.0, 4.0, 0.01)
duree = st.sidebar.slider("Durée de l'investissement en année :", 0, 50, 15)

fig, ax = plt.subplots()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)


ax.set_ylim(-2, 2)
st.pyplot(fig)