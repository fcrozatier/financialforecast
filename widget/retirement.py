import json
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def widget(translate, lang):
  if st.checkbox(translate["formula"][lang]):
    file_name = translate["formula path"][lang]
    st.markdown(open(file_name, 'r').read())

  # Sliders
  salary = st.number_input(translate["salary"][lang], 0, None, 10000)
  savings = st.number_input(translate["savings"][lang], 0.01, 100.0, 10.0)
  rate = st.number_input(translate["rate label"][lang], 0.0,None, 4.0)
  capital = st.number_input(translate["capital"][lang], 0, None)

  e = np.arange(0.01, 100.0, 0.01)

  # Create functions to plot
  s = np.divide((np.log(salary) - np.log(capital * rate / 100 + e * salary / 100)), np.log(1 + rate / 100))
  t = np.divide(- np.log( e / 100), np.log(1 + rate / 100))
  time = np.divide((np.log(salary) - np.log(capital * rate / 100 + savings * salary / 100)), np.log(1 + rate / 100))

  fig, ax = plt.subplots()
  if capital != 0:
    ax.plot(
      e, s,
      label=translate["plot"][lang]["with capital"].format(capital),
      color="blue")
  ax.plot(
    e,t,
    label=translate["plot"][lang]["without capital"], color="orange")
  ax.plot([savings],[time], 'ro')
  ax.annotate(
    round(time,1),
    xy=(savings, time), xytext=(0, -10),
    textcoords="offset points", ha="center", va="top",
    color="red"
    )
  ax.set(
    xlabel=translate["plot"][lang]["xlabel"],
    ylabel=translate["plot"][lang]["ylabel"],
    title=translate["plot"][lang]["title"]
    )
  ax.legend(loc="upper right")
  ax.grid()


  st.pyplot(fig)

  st.write(translate["conclusion"][lang].format(round(time,1)))

  ## Spending less vs earning more
  def equivalence(salary, savings, capital, rate):
    return round(-salary / (capital * rate / 100 - salary + salary * savings / 100 ), 2)

  st.write('')
  st.write('')
  st.write('')

  with st.beta_expander(translate["bonus label"][lang]):
    st.write(
      translate["bonus insight"][lang].format(
        equivalence(salary, savings, capital, rate)))
