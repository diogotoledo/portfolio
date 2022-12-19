import streamlit as st

def formacao():    
        st.title('Formação :male-student:')

        with st.expander("Segundo Grau Técnico :white_check_mark:"):
            st.markdown('##### Colégio Cotemig')
            st.caption('2000/2003 Informática Gerencial :computer:')
            st.caption('Unidade Floresta - Belo Horizonte - MG')

        with st.expander("Graduação 1 :white_check_mark:"):
            st.markdown('##### Centro Universitário UNA')
            st.caption('2010/2016 Administração de Empresas com ênfase em Comércio Exterior :globe_with_meridians:')
            st.caption('Campus Aimorés - Belo Horizonte - MG')
        
        with st.expander("Graduação 2 :hourglass:"):
            st.markdown('##### Faculdade Pitágoras')
            st.caption('2021/2023 Técnologo em Ciência de Dados :game_die:')
            st.caption(':arrow_right: Conclusão prevista para 07/2023')
            st.caption('Campus Centro - Betim - MG')