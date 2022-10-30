import plotly.graph_objects as go
import plotly.express as px
from plotly.colors import n_colors
import pandas as pd

# Function to render an interactive live graph
def get_animated_line_graph(data, column):
    
    max_value = data[column].max() + 1000
    min_value = data[column].min() + 1000
    
    if column != 'Population':
        title = f'Изменение количества {column} c 1960 по 2014'
    else:
        title = f'Изменение {column} c 1960 по 2014'
    
    # Base plot
    fig = go.Figure(
        layout=go.Layout(
            updatemenus=[dict(type="buttons", direction="right", x=1, y=1)],
            xaxis=dict(range=["1961", "2015"],
                    autorange=False, tickwidth=2,
                    title_text="Time"),
            yaxis=dict(range=[min_value, max_value],
                   autorange=False,
                   title_text=f"{column}"),
            title=title,
    ))

# Add traces
    init = 1

    fig.add_trace(
        go.Scatter(x=data['Year'][:init],
                y=data[column][:init],
                name=f"{column}",
                visible=True,
                line=dict(color="#B01D00", dash="dash")))

# Animation
    fig.update(frames=[
        go.Frame(
            data=[
                go.Scatter(x=data['Year'][:k], y=data[column][:k], mode='lines+markers')]
    )
        for k in range(init, len(data)+1)])

# Extra Formatting
    fig.update_xaxes(ticks="outside", tickwidth=2, tickcolor='white', ticklen=10)
    fig.update_yaxes(ticks="outside", tickwidth=2, tickcolor='white', ticklen=1)
    fig.update_layout(yaxis_tickformat=',')

# Buttons
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([
                    dict(label="Play",
                        method="animate",
                    args=[None, {"frame": {"duration": 100}}])
            ]))],
    title={
                    'text': title,
                    'y':0.87,
                    'x':0.5,
                    'xanchor':'center',
                    'yanchor':'top',
                    'font':dict(size=20, color='#D8D8D8')
                    },
                  font_family='Gill Sans',
                  font=dict(color='#606060'))

    return fig


# Get hist plot
def hist(data, column):
    hist = px.histogram(data, x=column, opacity=0.8, color_discrete_sequence=['#B01D00'], nbins=20)
    hist.update_layout(title={
                    'text': f'Распределение {column}',
                    'y':0.95,
                    'x':0.5,
                    'xanchor':'center',
                    'yanchor':'top',
                    'font':dict(size=20, color='#D8D8D8')
                    },
                  xaxis_title='Счет за заказ',
                  yaxis_title='Количество',
                  font_family='Gill Sans',
                  font=dict(color='#606060'))
    return hist

# Get boxplot function 
def boxplot(data, column):
    box = px.box(data, y=column, color_discrete_sequence=['#B01D00'])
    
    box.update_layout(title={
                    'text': f'Распределение и статистические показатели {column}',
                    'y':0.95,
                    'x':0.5,
                    'xanchor':'center',
                    'yanchor':'top',
                    'font':dict(size=20, color='#D8D8D8')
                    },
                  xaxis_title=f'Изменение {column} за период с 1960 по 2014',
                  yaxis_title=f'{column}',
                  font_family='Gill Sans',
                  font=dict(color='#606060'))
    return box


# Get pairplot grapg 
def get_pair_plot(data, columns):
    fig = px.scatter_matrix(data, dimensions=columns, color_discrete_sequence=['#B01D00'])
    
    fig.update_layout(title={
                    'text': f'Зависимость признаков ' + ', '.join(columns),
                    'y':0.95,
                    'x':0.5,
                    'xanchor':'center',
                    'yanchor':'top',
                    'font':dict(size=20, color='#D8D8D8')
                    },
                  font_family='Gill Sans',
                  font=dict(color='#606060'))
    fig.update_layout({"xaxis"+str(i+1): dict(tickangle = -45) for i in range(7)})
    return fig


# Get corr heatmap
def corr(data, columns, title=True):
    color = ['#FFA07A', '#E9967A', '#CD5C5C', '#8B0000', '#B22222', '#FF0000', '#DC143C', '#FA8072', '#F08080', ]
    df_corr = data[columns].corr()
    fig_corr = go.Figure([go.Heatmap(z=df_corr.values,
                                 y=df_corr.index.values,
                                 x=df_corr.columns.values, 
                                 zmin=-1, zmax=1, colorscale=color)])
    if title:
        title_ = f"Корреляция числовых признаков {', '.join(columns)}"
    else:
        title_ = 'Корреляция всех числовых признаков'
        
    fig_corr.update_layout(title={
                    'text': title_,
                    'y':0.87,
                    'x':0.5,
                    'xanchor':'center',
                    'yanchor':'top',
                    'font':dict(size=20, color='#D8D8D8')
                    },
                  font_family='Gill Sans',
                  font=dict(color='#606060'))
    return fig_corr