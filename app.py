import streamlit as st
from sobre import sobre
from formacao import formacao
from habilidades import habilidades
from idiomas import idiomas

st.set_page_config(page_title="Diogo de Toledo - Analista de Dados", layout="wide")

menu = ['Home', 'Sobre', 'Habilidades', 'Formação', 'Idiomas', 'Stack', 'Projetos', 'Contato']

st.sidebar.title('Diogo de Toledo')
st.sidebar.caption('Dados :game_die: SQL :globe_with_meridians: Python :snake: Power BI :signal_strength:')
page = st.sidebar.selectbox("Escolha uma opção:", menu)

if page == 'Home':
    st.title('Bem vindo! :wave:')
    st.caption('Bem vindo ao meu portfólio pessoal, por favor utilize o menu à esquerda para acessar a seção desejada.')
    st.caption('Qualquer dúvida, sugestão ou comentário, entre em contato na sessão "Contato" ao lado e deixe sua mensagem.')
    st.caption('Agradeço a sua visita! :smile:')

elif page == 'Sobre':
    sobre()

elif page == 'Habilidades':
    habilidades()

elif page == 'Formação':
    formacao()

elif page == 'Idiomas':
    idiomas()