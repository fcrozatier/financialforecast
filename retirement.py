import json
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def widget(translate, lang):
  if st.checkbox(translate["formula"][lang]):
    file_name = translate["formula path"][lang]
    st.markdown(open(file_name, 'r').read())

  # Sliders
  salary = st.number_input(translate["salary"][lang], 10000)
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

  ## 3D surface
  maximum = 1000
  S = np.arange(maximum)
  B = np.arange(maximum)
  G = np.zeros([len(S),len(B)])

  rate = 4
  capital = 0

  for s in S:
    for b in B:
      if(s<=b):
        G[s][b] = np.nan
      else:
        G[s][b] = np.divide((np.log(s) - np.log(capital * rate / 100 + s - b)), np.log(1 + rate / 100))

  fig = go.Figure(data=[go.Surface(
      z=G,
      x=B,
      y=S,
      name="",
      text="hey",
      hoverinfo="x+y",
      hovertemplate = "Salary: %{y}<br>Spendings: %{x}<br>Years: %{z:.1f}",
      )])
  fig.update_layout(
    title='Years before retirement',
    autosize=True,
    scene = dict(
        camera_eye=dict(x=-1.0, y=2.2, z=0.6),
        xaxis = dict(nticks=8, range=[0,maximum],),
        yaxis = dict(nticks=4, range=[0,maximum],),
        xaxis_title='Annual spendings',
        yaxis_title='Annual salary',
        zaxis_title='Years',
        xaxis_showspikes=False,
        yaxis_showspikes=False,
        ),
    margin=dict(l=20, r=10, b=25, t=25),
    )

  st.write(fig)
