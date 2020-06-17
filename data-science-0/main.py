#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[4]:


black_friday.head(10)


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[24]:


def q1():
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[33]:


def q2():
    womans_medium_age = black_friday[(black_friday['Gender'] == 'F') & (black_friday['Age'] == '26-35')].shape
        
    return int(womans_medium_age[0])


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[34]:


def q3():
    return black_friday['User_ID'].nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[35]:


def q4():
    return black_friday.dtypes.nunique()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[6]:


def q5():
    black_friday_missing_rows = black_friday[black_friday.isna().any(axis=1) == True]
    
    return float(black_friday_missing_rows.shape[0] / black_friday.shape[0])


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[40]:


def q6():
    black_friday_missing_max = black_friday.isna().sum().max()
    
    return int(black_friday_missing_max)


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[39]:


def q7():
    black_friday_most_frequent = black_friday['Product_Category_3'].dropna().mode()
    
    return int(black_friday_most_frequent)

q7()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[44]:


def q8():
    bf_purchase = black_friday['Purchase']
    
    norm_bf_purchase = (bf_purchase - bf_purchase.min()) / (bf_purchase.max() - bf_purchase.min())
    
    return float(norm_bf_purchase.mean())

q8()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[52]:


def q9():
    bf_purchase = black_friday['Purchase']
    
    stand_bf_purchase = (bf_purchase - bf_purchase.mean()) / bf_purchase.std()
    
    return(stand_bf_purchase[(stand_bf_purchase >= -1) & (stand_bf_purchase <= 1)].shape[0])

q9()


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[60]:


def q10():
    black_friday_product = black_friday[['Product_Category_2', 'Product_Category_3']]

    black_friday_product = black_friday_product[black_friday_product['Product_Category_2'].isna()]

    return black_friday_product['Product_Category_2'].equals(black_friday_product['Product_Category_3'])

q10()

