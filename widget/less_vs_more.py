import numpy as np
import plotly.graph_objects as go
import streamlit as st

def widget(translate, lang):
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
          margin=dict(l=0, r=0, b=0, t=0),
        )

      return fig

  visual_proof = translate["visual proof"][lang]
  st.markdown(open(visual_proof, 'r').read())

  st.write(interactive_3d_surface(100))

  formal_proof = translate["formal proof"][lang]
  st.markdown(open(formal_proof, 'r').read())
