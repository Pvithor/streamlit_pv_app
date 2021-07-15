import streamlit as st
import numpy as np
import pandas as pd
st.set_page_config(
    page_title="Dados",
    layout='wide',
)

@st.cache
def pandas(nome,sepa=';'):
    """ Abrir data frame e retorana com o nome dos cabeçario """
    try:
        data= pd.read_excel(nome)
        cabeca = list(data)
    
    except:
        try:
            data = pd.read_hdf(nome)
            cabeca = list(data)
        except:
            data = pd.read_csv(nome,sep=sepa )
            cabeca = list(data)
    
    return data ,cabeca

class config_pandas():
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
def dowload(df):
    """ Baixar apos mudanca """
    frame.to_excel('teste_exportacao.xlsx',index=False)
    href = f'<a href="data:file/csv;{frame}">Download csv file</a>'

def opc(str):
    try:
        if str[0]:
            return True
    except:
        return False

st.title("Dados tratamento")

#enviar arquivo
puro = st.file_uploader('Arquivo excel',type=['xlsx','dbf','csv'])
resest = False
if puro is not None:
    if puro.name.split('.')[-1] == 'csv':
        conf_cvs,conf_cvs2 = st.beta_columns(2)
        with conf_cvs:  
            cvs_1 = st.text_input('separador do cvs:[padrao ** ; **] ')
        if cvs_1 == '': cvs_1=';'

    #print(puro.name.split('.')[-1])
    if puro.name.split('.')[-1] == 'xlsx':
        conf_1,conf_2 = st.beta_columns(2)
        with conf_1:
            header = st.text_input('inicio do hearder: ')
        with conf_2:
            folha = st.text_input('Olha a ser extraida: ')

reset= False
#Liberar apos  ter arquivo
if puro is not None:
    frame,cabeca= pandas(puro,sepa= cvs_1)
    if st.checkbox('mostrar tabela',key='bruto'):
        st.write(frame[:5])

    opcoes = st.multiselect('Opcoes',cabeca)
    
    #columa com `pesquisa`e `colua`
    col1,col2= st.beta_columns(2)
    with col1:
        pesquisa = st.text_input('Valor para ser pesquisado')
        remove_linha= st.text_input('linha pare remove').split(',')
    with col2:
        columa = st.text_input('Nome da columa')

    

    opc = opc(opcoes)
    #filtar columa
    df2=config_pandas.filtrar(frame,opcoes)
    
    #GEral
    if pesquisa:
        df2=config_pandas.pesquisa(frame,columa,opcoes,pesquisa)

    if remove_linha != ['']:
        df2= config_pandas.remove_line(df2,remove_linha) 
        reset = True


    #preview
    previw,teset = st.beta_columns(2)
    with previw:
        st.checkbox('mostrar preview',key='preview')
    with teset:
        tudo=st.checkbox('mostrar tudo',key='full')
    

    if previw:
        if tudo:
            st.write(df2)
        else:   
            st.write(df2.loc[:5])
    
        # st.info('ola')
        # st.success('Sucesso')
        # st.warning('warnig')
        # st.error('erro')
       

    if st.button('Exportar'):
        st.markdown(dowload(frame), unsafe_allow_html=True)
        st.write('Exportado')
    
    else:
        st.write('Click para exportar')
