import streamlit as st
from visualization_functions import get_animated_line_graph, hist, boxplot, get_pair_plot, corr


# Feature visualization function
def get_feature_visualization(data, feature, line_plot=True, selective_corr_plot=True):
    
    for num in range(3):
            st.write(' ')
            
    st.markdown(f'''<h3 style="text-align: left; font-family: 'Gill Sans'; color: #FF2A00; font-size: 28px"
            >Исследуем признак {feature}</h3>''',
            unsafe_allow_html=True)
    st.write(' ')
        
    # Set scatter matrix 
    features_list = data.columns.tolist()
    scatter_matrix_features = st.multiselect(f'Выберите не больше трех столбцов, чтобы исследовать зависимость признака {feature} с другими признаками', features_list)
    button = st.button(f"Построить для признака {feature}",disabled=False)
    
    if button:
        if len(scatter_matrix_features) <= 3:
            if feature not in scatter_matrix_features:
                scatter_matrix_features.append(f'{feature}')
            else:
                pass
            st.plotly_chart(get_pair_plot(data, scatter_matrix_features), use_container_width=True)
        else:
            st.warning("Вы должны выбрать не больше трех признаков, иначе будет сложно сравнивать")
    
    # Set line plot       
    if line_plot:
        st.plotly_chart(get_animated_line_graph(data, feature), use_container_width=True)
    else:
        pass
    
    # Set corr plot    
    if selective_corr_plot:
        corr_plot_features = st.multiselect(f'Выберете столбцы, чтобы исследовать корреляцию {feature} с другими признаками', features_list)
        if not corr_plot_features:
            pass
        else:
            corr_plot_features.append(f'{feature}')
            st.plotly_chart(corr(data, corr_plot_features, True), use_container_width=True)
    else:
        st.plotly_chart(corr(data, data.columns.tolist(), selective_corr_plot), use_container_width=True)
        
    columns_first_row = st.columns(2)
    columns_first_row[0].plotly_chart(hist(data, f'{feature}'), use_container_width=True)
    columns_first_row[1].plotly_chart(boxplot(data, f'{feature}'), use_container_width=True)