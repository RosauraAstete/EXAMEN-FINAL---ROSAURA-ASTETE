#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importar pandas
get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd


# In[3]:


# Crea una Serie de los numeros 10, 20 and 10.

serie1 = pd.Series( [ 10 , 20 , 10 ] );
print(serie1)


# In[4]:


# Crea una Serie con tres objetos: 'rojo', 'verde', 'azul'

serie2 = pd.Series( [ 'rojo' , 'verde' , 'azul' ] );
print(serie2)


# In[5]:


# Crea un dataframe vacío llamado 'df'

df = pd.DataFrame()


# In[6]:


# Crea una nueva columna en el dataframe, y asignale la primera serie que has creado

df['Serie 1'] = serie1
df.head()


# In[7]:


# Crea otra columna en el dataframe y asignale la segunda Serie que has creado

df['Serie 2'] = serie2
df.head()


# In[8]:


# Lee el archivo llamado 'avengers.csv" localizado en la carpeta "data" y crea un DataFrame, llamado 'avengers'. 
# El archivo está localizado en "data/avengers.csv"

df = pd.read_csv ( 'avengers.csv' , sep = ',')


# In[9]:


# Muestra las primeras 5 filas del DataFrame

df.head()


# In[10]:


# Muestra las primeras 10 filas del DataFrame

df.head(10)


# In[11]:


# Muestra las últimas 5 filas del DataFrame

df.tail()


# In[12]:


# Muestra el tamaño del DataFrame

df.shape


# In[13]:


df.describe()


# In[14]:


# Muestra los data types del dataframe

df.dtypes


# In[15]:


# Cambia el indice a la columna "fecha_inicio"

df.set_index("fecha_inicio")


# In[16]:


# Ordena el índice de forma descendiente

df = df.set_index("fecha_inicio")
df.sort_index( ascending = False)


# In[17]:


# Resetea el índice

df.reset_index( drop = True , inplace = True )


# In[18]:


df.head()


# In[19]:


# Ejercicio - Busqueda de Alojamiento en Airbnb

df_airbnb = pd.read_csv("airbnb.csv")


# In[20]:


df_airbnb.head()


# In[21]:


# Caso 1

condicion1 = df_airbnb ['reviews'] > 10
condicion2 = df_airbnb ['overall_satisfaction'] > 4

filtro = df_airbnb [ condicion1 & condicion2 ]
filtro


# In[22]:


filtro_sorted = filtro.sort_values (["overall_satisfaction" , "reviews"] , ascending = [False , False])
filtro_sorted


# In[23]:


filtro_sorted.head(3)


# In[24]:


# Caso 2

filtrado = df_airbnb[ (df_airbnb.room_id == 97503) | (df_airbnb.room_id == 90387) ]
roberto = pd.DataFrame(filtrado)
filtrado


# In[25]:


roberto.to_excel('roberto.xlsx')


# In[26]:


# Caso 3

cond1 = df_airbnb ['price'] <= 50
cond2 = df_airbnb ['room_type'] == 'Shared room'

filtro2 = df_airbnb [ cond1 & cond2 ]
filtro2


# In[27]:


filtro2_sorted = filtro2.sort_values (["overall_satisfaction" , "price"] , ascending = [False , True])
filtro2_sorted


# In[28]:


filtro2_sorted.head(10)


# In[29]:


# Caso Matplot

import matplotlib.pyplot as plt


# In[30]:


df_airbnb.room_type.value_counts().plot.pie(
    colors = ["#AAF683","#FFD97D","#FF9B85"],
    autopct="%0.1f %%"
)


# In[ ]:




