import streamlit as st
import streamlit.components.v1 as components


# ---- HIDE STREAMLIT STYLE ----

def streamlit_style():

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.set_page_config(
    page_title="Site Energy Usage Intensity Prediction",
    page_icon="⚡",
    layout="centered",
    menu_items={
        'About': "# This is an site energy intensity prediction application made by Avi Kumar Talaviya"
    }
)

    st.markdown(
            f'''
            <style>
                .reportview-container .sidebar-content {{
                    padding-top: {0}rem;
                }}
                .reportview-container .main .block-container {{
                    padding-top: {0}rem;
                }}
            </style>
            ''',unsafe_allow_html=True)

    st.markdown("""
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """, unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            width: 250px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            width: 250px;
            margin-left: -500px;
            }
        </style>
        
        """,
        unsafe_allow_html=True)

    hvar = """
    
            <script>
            
                var elements = window.parents.document.querySelectorAll('.streamlit-expanderHeader')
                elements[0].style.color = 'rgba(83, 36, 118, 1)';
                elements[0].style.fontFamily = 'Didot';
                elements[0].style.fontStyle = 'x-large';
                elements[0].style.fontWeight = 'bold';
            </script>
    
    """