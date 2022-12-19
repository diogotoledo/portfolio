import streamlit as st

def habilidades():    
        st.title('Habilidades :male-student:')

        with st.expander(":one: Interpessoais"):            
            st.caption(':diamond_shape_with_a_dot_inside: Relacionamento Interpessoal')
            st.caption(':diamond_shape_with_a_dot_inside: Trabalho em Equipe')
            st.caption(':diamond_shape_with_a_dot_inside: Comunicação clara e efetiva')

        with st.expander(":two: Técnicas"):            
            st.caption(':diamond_shape_with_a_dot_inside: Raciocínio Lógico')
            st.caption(':diamond_shape_with_a_dot_inside: Criatividade')
            st.caption(':diamond_shape_with_a_dot_inside: Olhar Analítico')
        
        with st.expander(":three: Comportamentais"):            
            st.caption(':diamond_shape_with_a_dot_inside: Descontraído')
            st.caption(':diamond_shape_with_a_dot_inside: Fácil de lidar')
            st.caption(':diamond_shape_with_a_dot_inside: Focado')
            st.caption(':diamond_shape_with_a_dot_inside: Justo')
