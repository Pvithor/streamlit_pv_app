from pandas.io import excel
import streamlit as st
import numpy as np
import pandas as pd
from depedencias.defs import *

st.set_page_config(
    page_title="Dados",
    layout='wide',
)

st.title("Dados tratamento")

#enviar arquivo
puro = st.file_uploader('Arquivo excel',type=['xlsx','dbf','csv'])
resest = False
if puro is not None:
    if puro.name.split('.')[-1] == 'csv':
        conf_cvs,conf_cvs2 = st.beta_columns(2)
        with conf_cvs:  
            st.markdown('separador do cvs:[padrao ** ; **] ')
            cvs_1 = st.text_input('')
        if cvs_1 == '': cvs_1=';'

    #arquivo xlsx
    if puro.name.split('.')[-1] == 'xlsx':
        if st.checkbox('configuracoes adicionais'):
            conf_1,conf_2 = st.beta_columns(2)
            with conf_1:
                header = st.text_input('inicio do hearder: ')
            with conf_2:
                folha = st.text_input('Olha a ser extraida: ')

reset= False
#Liberar apos  ter arquivo
if puro is not None:
    #csv
    if puro.name.split('.')[-1] == 'csv':
       frame,cabeca= data_frame.csv(puro,sepa=cvs_1)
    
    elif puro.name.split('.')[-1] == 'dbf':
        frame,cabeca= data_frame.hdf(puro)
    
    elif puro.name.split('.')[-1] == 'xlsx':
        frame,cabeca= data_frame.exel(puro)

    if st.checkbox('mostrar tabela',key='bruto'):
        st.write(frame[:5]) 


    opcoes = st.multiselect('Cabecarios para retirar',cabeca)
    
    #columa com `pesquisa`e `colua`
    col1,col2= st.beta_columns(2)
    with col1:
        pesquisa = st.text_input('Valor para ser pesquisado')
        remove_linha= st.text_input('linha pare remove').split(',')
    
    with col2:
        columa = st.text_input('Nome da columa')
   

    opc = opc(opcoes)
    #filtar columa
    df2=filtros.filtrar(frame,opcoes)
    
    #GEral
    if pesquisa:
        df2=filtros.pesquisa(frame,columa,opcoes,pesquisa)

    if remove_linha != ['']:
        df2= filtros.remove_line(df2,remove_linha) 
        reset = True


    #preview
    previw,teset = st.beta_columns(2)
    with previw:
        st.checkbox('mostrar preview',key='preview')
    with teset:
        tudo=st.checkbox('mostrar tudo',key='full')
    

    if previw:
        if tudo:
            st.pd(df2,index=False)
        else:   
            st.write(df2.loc[:5])
    
        # st.info('ola')
        # st.success('Sucesso')
        # st.warning('warnig')
        # st.error('erro')

    st.markdown(baixar(df2,'Baixar cvs'),unsafe_allow_html=True)