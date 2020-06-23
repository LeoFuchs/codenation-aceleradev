import streamlit as st
import pandas as pd
import altair as alt


def criar_histograma(coluna, df):
    chart = alt.Chart(df, width=600).mark_bar().encode(
        alt.X(coluna, bin=True),
        y='count()', tooltip=[coluna, 'count()']
    ).interactive()

    return chart


def criar_barras(coluna_num, coluna_cat, df):
    bars = alt.Chart(df, width=600).mark_bar().encode(
        x=alt.X(coluna_num, stack='zero'),
        y=alt.Y(coluna_cat),
        tooltip=[coluna_cat, coluna_num]
    ).interactive()

    return bars


def criar_boxplot(coluna_num, coluna_cat, df):
    boxplot = alt.Chart(df, width=600).mark_boxplot().encode(
        x=coluna_num,
        y=coluna_cat
    )

    return boxplot


def criar_scatterplot(x, y, color, df):
    scatter = alt.Chart(df, width=800, height=400).mark_circle().encode(
        alt.X(x), alt.Y(y), color=color, tooltip=[x, y]
    ).interactive()

    return scatter


def cria_correlationplot(df, colunas_numericas):
    cor_data = (df[colunas_numericas]).corr().stack().reset_index().rename(
        columns={0: 'correlation', 'level_0': 'variable', 'level_1': 'variable2'})
    cor_data['correlation_label'] = cor_data['correlation'].map('{:.2f}'.format)  # Round to 2 decimal
    base = alt.Chart(cor_data, width=500, height=500).encode(x='variable2:O', y='variable:O')
    text = base.mark_text().encode(text='correlation_label',
                                   color=alt.condition(alt.datum.correlation > 0.5, alt.value('white'),
                                                       alt.value('black')))

    # The correlation heatmap itself
    cor_plot = base.mark_rect().encode(
        color='correlation:Q')

    return cor_plot + text


def main():
    st.image('logo.png', width=200)
    st.title('AceleraDev Data Science')
    st.header('Semana 3 - Análise de Dados Exploratória')

    file = st.file_uploader('Escolha a base de dados que deseja analisar (.csv)', type='csv')

    if file is not None:
        st.subheader('**Estatística Descritiva Univariada**')

        df = pd.read_csv(file)
        aux = pd.DataFrame({"colunas": df.columns, 'tipos': df.dtypes})

        colunas_numericas = list(aux[aux['tipos'] != 'object']['colunas'])
        colunas_object = list(aux[aux['tipos'] == 'object']['colunas'])
        colunas = list(df.columns)

        col = st.selectbox('Selecione a coluna que deseja manipular:', colunas_numericas)

        if col is not None:
            st.markdown('Agora escolha o que deseja analisar:')
            mean = st.checkbox('Média')
            if mean:
                st.markdown(df[col].mean())

            median = st.checkbox('Mediana')
            if median:
                st.markdown(df[col].median())

            desvio_pad = st.checkbox('Desvio padrão')
            if desvio_pad:
                st.markdown(df[col].std())

            kurtosis = st.checkbox('Kurtosis')
            if kurtosis:
                st.markdown(df[col].kurtosis())

            skewness = st.checkbox('Skewness')
            if skewness:
                st.markdown(df[col].skew())

            describe = st.checkbox('Descrição Detalhada')
            if describe:
                st.table(df[colunas_numericas].describe().transpose())

        st.subheader('**Visualização dos Dados**')

        st.markdown('Selecione a visualização desejada:')
        histograma = st.checkbox('Histograma')
        if histograma:
            col_num = st.selectbox('Selecione a Coluna Numérica: ', colunas_numericas)
            st.markdown('Histograma da Coluna \'' + str(col_num) + '\'')
            st.write(criar_histograma(col_num, df))

        barras = st.checkbox('Gráfico de Barras')
        if barras:
            col_num_barras = st.selectbox('Selecione uma Coluna Numérica: ', colunas_numericas, key='unique')
            col_cat_barras = st.selectbox('Selecione uma Coluna Categórica : ', colunas_object, key='unique')
            st.markdown('Gráfico de Barras das colunas \'' + str(col_cat_barras) + '\' e \'' + col_num_barras + '\'')
            st.write(criar_barras(col_num_barras, col_cat_barras, df))

        boxplot = st.checkbox('Boxplot')
        if boxplot:
            col_num_box = st.selectbox('Selecione uma Coluna Numérica:', colunas_numericas, key='unique')
            col_cat_box = st.selectbox('Selecione uma Coluna Categorica : ', colunas_object, key='unique')
            st.markdown('Boxplot das colunas \'' + str(col_cat_box) + '\' e \'' + col_num_box + '\'')
            st.write(criar_boxplot(col_num_box, col_cat_box, df))

        scatter = st.checkbox('Scatterplot')
        if scatter:
            col_num_x = st.selectbox('Selecione o Valor para o Eixo X:', colunas_numericas, key='unique')
            col_num_y = st.selectbox('Selecione o Valor para o Eixo Y ', colunas_numericas, key='unique')
            col_color = st.selectbox('Selecione a coluna para cor', colunas)
            st.markdown('Selecione os valores de x e y')
            st.write(criar_scatterplot(col_num_x, col_num_y, col_color, df))

        correlacao = st.checkbox('Correlação')
        if correlacao:
            st.markdown('Gráfico de Correlação das Variáveis Numéricas')
            st.write(cria_correlationplot(df, colunas_numericas))


if __name__ == '__main__':
    main()
