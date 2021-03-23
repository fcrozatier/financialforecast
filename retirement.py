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
  @st.cache
  def interactive_3d_surface(domain):
      maximum = domain
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
          hovertemplate = "Salary: %{y}<br>Spendings: %{x}<br>Years: %{z:.1f}",
          # contours = {
          #     "x": {"show": True, "start": 1.5, "end": 2, "size": 0.04, "color":"white"},
          #     "z": {"show": True, "start": 0.5, "end": 0.8, "size": 0.05}
          # },
          )])

      fig.update_traces(
          contours_x=dict(
              show=True,
              start=20,
              end=100,
              size=20,
              usecolormap=True,
              highlightcolor="limegreen",
              project_x=True),
          contours_y=dict(
              show=True,
              start=20,
              end=100,
              size=20,
              usecolormap=True,
              highlightcolor="limegreen",
              project_y=True),
          )

      fig.update_layout(
          title='',
          scene = dict(
              camera_eye=dict(x=-1.0, y=2.2, z=1.6),
              xaxis = dict(nticks=6),
              yaxis = dict(nticks=6),
              xaxis_title='Annual spendings',
              yaxis_title='Annual salary',
              zaxis_title='Years',
              xaxis_showspikes=False,
              yaxis_showspikes=False,
              ),
          width=500,
          autosize=True,
          margin=dict(l=0, r=0, b=0, t=0, autoexpand=True),
        )

      return fig

  def equivalence():
    return round(
      -salary / (capital * rate / 100 - salary + salary * savings / 100 ),
       2)

  st.write('')
  st.write('')
  st.write('')
  bonus = st.checkbox(translate["bonus label"][lang])

  if(bonus):
    st.write(translate["bonus equivalence"][lang].format(equivalence()))

    visual_proof = translate["bonus visual proof file"][lang]
    st.markdown(open(visual_proof, 'r').read())

    st.write(interactive_3d_surface(100))

    formal_proof = translate["bonus formal proof file"][lang]
    st.markdown(open(formal_proof, 'r').read())
