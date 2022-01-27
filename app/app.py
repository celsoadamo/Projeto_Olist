import pandas as pd
# import matplotlib.pyplot as plt
import pickle

# load the model from disk
filename='prophet_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


#Titulo
st.title('Olist E-Commerce Brazil Forecast App')

#Subtitulo
st.markdown('Este é um Data App para exibir uma soluçao de Machine Learning para o problema de previsao de vendas da Olist e-commerce Brazil.')
st.markdown('O modelo foi treinado com dados de Setembro de 2016 a Dezembro de 2018 e preve vendas numa base diaria.')

#imprime o conjunto de dados usado
#st.dataframe()

#Adiciona o subtitulo na barra lateral
st.sidebar.subheader('Coloque a data que pretende prever o valor de venda')
#Adiciona o componente de input na barra lateral
data=st.sidebar.date_input('Data')
#Adiciona um botao na barra lateral
btn_predict=st.sidebar.button('Prever valor de venda')

#Verifica se o botao foi accionado
if btn_predict:
    data_teste=pd.DataFrame()
    data_teste['ds']=data
    
    st.write('Data escolhida:',data)
  
    #Efectuar previsao
    #result=loded_model.predict(data_teste)

    #Escreve o valor previsto
    #st.write(result)
    st.write('Valor previsto:')


st.markdown("[Dashboard de Vendas](https://chart-studio.plotly.com/dashboard/celso.adamo:106/present#/)", unsafe_allow_html=True)
