import plotly.express as px
from data_analysis.index import result
from plotly.subplots import make_subplots

fig_1 = px.line(result, x='Tenure', y='General Rate', color='Bank Name', markers=True)

fig = make_subplots(rows=2, cols=2, subplot_titles=('AXIS', 'ICICI', 'HDFC', 'IDFC'))
fig.add_trace(px.line(result[result['Bank Name'] == 'AXIS'], x='Tenure', y='General Rate', markers=True).data[0], row=1, col=1)
fig.add_trace(px.line(result[result['Bank Name'] == 'ICICI'], x='Tenure', y='General Rate', markers=True).data[0], row=1, col=2)
fig.add_trace(px.line(result[result['Bank Name'] == 'HDFC'], x='Tenure', y='General Rate', markers=True).data[0], row=2, col=1)
fig.add_trace(px.line(result[result['Bank Name'] == 'IDFC'], x='Tenure', y='General Rate', markers=True).data[0], row=2, col=2)

fig.update_traces(line=dict(color='red'), row=1, col=1)
fig.update_traces(line=dict(color='orange'), row=2, col=1)
fig.update_traces(line=dict(color='green'), row=1, col=2)
fig.update_traces(line=dict(color='purple'), row=2, col=2)
