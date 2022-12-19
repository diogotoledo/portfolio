import streamlit as st

def idiomas():    
        st.title('Idiomas :earth_americas:')

        with st.expander("Portugês"):            
            st.markdown('##### :speaking_head_in_silhouette: Comunicação')
            st.caption('Nativo')
            st.markdown('##### :writing_hand: Escrita')
            st.caption('Excelente')
            st.markdown('##### :book: Leitura')
            st.caption('Excelente')

        with st.expander("Inglês"):            
            st.markdown('##### :speaking_head_in_silhouette: Comunicação')
            st.caption('Fluente')
            st.markdown('##### :writing_hand: Escrita')
            st.caption('Avançado')
            st.markdown('##### :book: Leitura')
            st.caption('Avançado')

        with st.expander("Espanhol"):            
            st.markdown('##### :speaking_head_in_silhouette: Comunicação')
            st.caption('Fluente')
            st.markdown('##### :writing_hand: Escrita')
            st.caption('Avançado')
            st.markdown('##### :book: Leitura')
            st.caption('Avançado')
