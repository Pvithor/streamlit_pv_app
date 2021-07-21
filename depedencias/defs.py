import streamlit as st
import numpy as np
import pandas as pd
import base64

@st.cache
class data_frame():
    """ Abrir data frame e retorana com o nome dos cabeçario """
    def exel(nome):
        data= pd.read_excel(nome)
        cabeca = list(data)
        return data ,cabeca
        
    def hdf(nome):
        data = pd.read_hdf(nome)
        cabeca = list(data)
        return data ,cabeca

    def csv(nome,sepa=';'):
        data = pd.read_csv(nome,sep=sepa )
        cabeca = list(data)

        return data ,cabeca

class filtros():
    """ Opcoes do pandas """
    def filtrar(df,filtrar):
        """Filtrar pelo nome """
        frame = df[filtrar]
        return frame
    
    def pesquisa(df,coluna,opcoes,filtrar):
        """ Filtar por columa e valor """
        if filter == '' or coluna == '':
            return
        frame = config_pandas.filtrar(df,opcoes)
        frame = frame.loc[(df[coluna]==filtrar)]
        return frame

    def remove_line(df,list):
        """ Remover linha do pandas """
        frame = df
        try:
            for line in list:
                frame = frame.drop(int(line))
            return frame
        except KeyError:
            st.error(f'Não válido {line}')
            return False

def opc(str):
    try:
        if str[0]:
            return True
    except:
        return False

def baixar(df,file_label='File.cvs',nome='dado'):
    csv = df.to_csv(index=False)
    #csv = df.to_csv(index=False)
    bin_str = base64.b64encode(csv.encode()).decode()
    #b64 =  base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{nome}.xlsx">{file_label}</a>'
    return href

class ajuste_prev():
    def cvs_limpa():
        pass