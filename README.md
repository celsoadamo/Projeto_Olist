# Projeto_Olist

Projeto de Machine Learning da Olist e-commerce Brasil

# Objetivos do projeto

Neste projeto cobrimos todas as etapas de um projeto real de Ciência de Dados e respondemos a algumas questoes importantes sobre o negócio utilizando dados com intuito de permitir que a empresa Olist tenha conhecimento sobre:

•	Qual a distribuição dos pedidos por estado?

•	Qual foi o ano com mais vendas e quais o meses que os clientes mais compram?

•	Qual é a distribuição dos score dos reviews?

•	Quais os 5 maiores vendedores?

•	Quais as 5 categorias de produtos mais vendidos?

•	Qual é a média de produtos vendidos num determinado pedido?

•	Qual a relação entre o preço de venda e o valor do frete?

•	Qual é a forma de pagamento mais utilizada?

•	A maior parte dos pagamentos são feitos na totalidade ou de forma parcelada?

•	Quantos métodos de pagamentos em média são escolhidos pelos clientes em um determinado pedido? 

O objetivo é dar a conhecer o **estado actual** do negócio a Olist usando uma abordagem descritiva e criar uma solução para que a empresa possa **prever as vendas diárias** ao longo do tempo.
Por fim, realçar que o grande impacto que o projeto terá sobre o negócio da Olist, é que a esta ferramenta permitirá que a empresa investigue com mais detalhes o que contribuiu para que em determinados dias e/ou meses o número de vendas seja reduzido, de modo a definir-se estratégias a médio e longo prazo para aumentar as vendas da empresas.

# Solução Proposta

**Tecnologias Utilizadas**

Para resolver este problema foi construida uma solução completa para armazenamento, gestão utilizando tecnologias como Google Colab além de explorar uma suite de tecnologias e/ou bibliotecas para análise, visualização de dados e machine learning tais como: pandas, matplotlib, seaborn, plotly, scikit-learn, statsmodels, fbprophet, streamlit.

**Pandas** – biblioteca usada para manipulação de dados

 ![image](https://user-images.githubusercontent.com/64884982/151560164-236239b0-c365-4179-b5a9-efddb343d31f.png)

**Matplotlib** – biblioteca usada para visualização de dados.

 ![image](https://user-images.githubusercontent.com/64884982/151560194-d716af52-a448-4240-9c4a-2a0de9ec3ff6.png)

**Seaborn** – biblioteca usada para visualização de dados baseada no matplotlib, permitindo construir graficos mais profissonais.

 ![image](https://user-images.githubusercontent.com/64884982/151560257-69f81b1a-fe15-476c-8d89-a26625200499.png)

**Plotly** – biblioteca utilizada para desenvolver gráficos iterativos e construir dashboards usando chart studio.

 ![image](https://user-images.githubusercontent.com/64884982/151560437-2d199508-1de4-423f-af48-6d79a9d7f79b.png)

**Scikit-learn** – biblioteca usada para implementar os algoritmos de machine learning (utilizou-se o pickle para serializar o modelo em disco)

 ![image](https://user-images.githubusercontent.com/64884982/151560360-41eecbaf-fbdc-42d6-b665-649450e16d56.png)

**Statsmodels** – biblioteca usada para implementar métodos estatisticos e alguns algoritmos de séries temporaris como o ARIMA e SARIMAX.

 ![image](https://user-images.githubusercontent.com/64884982/151560500-5536fe5b-98ca-4ff3-b0bd-a92190fd55fc.png)

**Facebook Prophet** – biblioteca usada para implementar algoritmos de machine learning para resolver problemas de séries tempiorais desenvolvido pela Microsoft.

 ![image](https://user-images.githubusercontent.com/64884982/151560568-c7b9128c-0f21-484e-9792-fb1edc4f5a8b.png)

**Streamlit** – biblioteca utilizada para desenvolver a aplicação e/ou fórmulário para testar o modelo em ambiente de produção.

 ![image](https://user-images.githubusercontent.com/64884982/151560614-8d3759fd-0da9-4061-bb90-1a133767ba18.png)

**Ferramentas de auxiliares:**

**Python** – liguagem de programação utilizada para desenvolver o projeto de ciência de dados.

**Google colab** – editor de código online que geralmente é organizado por células.

![image](https://user-images.githubusercontent.com/64884982/151560670-aa0237f8-a29c-431f-bc7a-68fed6a1f9e3.png)


**Github** – ferramenta que permite versionar, partilhar o código desenvolvido e também atribuir acesso a outros profissinais para colaborarem nos artefatos do projeto.

 ![image](https://user-images.githubusercontent.com/64884982/151560731-bfce9466-af18-4e80-be8c-dcf4454938d1.png)

Por fim, realçar que utilizou-se como infraestrutura de armazenamento do Google Colab para poder analisar as diversas fontes de dados que estavam em arquivos no formato csv (dados disponibilizados pela Olist extraídos do Kaggle).


**Arquitecturas**

Em seguida é ilustrada o overview da solução desde a **coleta** até **ao deploy da solução desenvolvida**.

![image](https://user-images.githubusercontent.com/64884982/151559682-e843daec-f2b5-49b0-b207-423061417a5d.png)

 
Os principais desafios enfrentados foram:

•	Integrar o notebook do Google Colab com o ambiente do Databricks que serviria como infraestrutura para armazenamento de dados permitindo desata forma utilizar um ambiente distribuido aumentando a eficiência do processo de limpeza e transformação dos dados (não tivemos sucesso).

•	Disponilizar a app na cloud da Streamlit, visto que, tivemos dificuldades em fazer upload dos arquivos do projeto armazenados na máquina local via terminal de comando do Windows para Github e erros de instalação de biblioteca na cloud da streamlit.

•	Instalar algumas bibliotecas na máquina local, como por exemplo, o fbprophet.
	

# Resultados

**Insights e Conhecimento Gerado**

Na etapa de Análise Exploratória dos Dados foram descobertos vários insights importantes abaixo:
•	As vendas tem uma tendência positiva ou de cresceimento ao longo dos anos.

 ![image](https://user-images.githubusercontent.com/64884982/151559832-792fee99-bb06-491d-a856-73a4a190c5fc.png)

•	97% dos produtos são entregues aos clientes, ou seja, os pedidos estão no estado delivered.

•	A maior parte dos reviews dos produtos é positiva (média de 4.08) e um dos títulos mais usado é o Recomendo e a mensagem mais escrita é o Muito Bom.

•	Uma das categorias de produtos mais comprados é cama_mesa_banho.

 ![image](https://user-images.githubusercontent.com/64884982/151559884-582c266e-89e3-4cac-817d-6edeb5bec6f5.png)

•	Em média um pedido tem apenas 1 items/produto.

•	Os clientes utilizam 5 formas de pagamento das compras por si efectuadas e a forma de pagamento mais usada é credit_card
  ![image](https://user-images.githubusercontent.com/64884982/151559940-09e3abb4-4064-4544-b3ab-887abae9a2ca.png)


•	A maior partes do pagamentos é feita em uma única prestação mas os pagamentos feitos em parcelas variam de 2 à 24 tranches. No entanto, em média os clientes pagam em 3 prestações.

 ![image](https://user-images.githubusercontent.com/64884982/151559993-23c9422b-4a21-4fb2-af0b-7a6004ea2d1b.png)


•	Existe uma correlação positiva fraca (0.41) entre o preço de venda e o valor de frete e também constatamos que a maior parte das vendas teve um score de 5 (classificação máxima), isto é, um review positivo.

 ![image](https://user-images.githubusercontent.com/64884982/151560032-3e764aae-f278-4260-bc16-6497affc05b3.png)

•	Na cadeia de lojas existentes São Paulo é a cidade que mais vende.

 ![image](https://user-images.githubusercontent.com/64884982/151560069-47b74142-5be9-4568-8cf4-ca590047e7b0.png)

•	Existem vendas sem não pagas ou com valor de pagamento igual a zero.
o	Os preços dos produtos variam de 0.85 a 6 735 reais.
o	Os preços dos fretes variam de 0 a 409.68 reais.

**Métricas de Performance**

Para a estimativa de predizer o valor de venda diário foi implementado um modelo utilizando o Facebook Prophet que atingiu uma performance RMSE de aproximadamente 9 612.24 reais (superando um pouco um modelo de base que é de 11 848.30 reais), isto é, em média o valor previsto pode diferir do valor real em +/- 9 mil reais.


# Conclusão

Através deste projeto foi possivel praticar e implementar conceiros importantes de Ciência e Engenharia de Dados e propor uma solução para um problema latente em qualquer empresa de e-commerce que é a análise da situação actual do negócio e a previsão de vendas dos meses subsequentes.

A resoluçao dos problemas acima mencionados, permitirá obter insights para desenhar e/ou alterar a estratégia do negócio da empresa, visto que, o e-commerce é um ambiente muito dinâmico e os clientes podem ter comportamentos diferentes de compras ao longo do tempo. Com a implementação desta solução teremos como beneficio, um recurso organizacional que permitirá identificar o comportamento de compra dos clientes e contribuirá para ajustar a estratégia de venda e retençao de clientes num horizonte temopral.

Por fim, como um processo de melhoria continua podemos reduzir o erro de previsão, desenvolver uma automação para executar o pipeline de coleta e transformaçao dos dados e automatizar a etapa de Machine Learning e Deploy.
