import streamlit as st


def footer_home():

    st.markdown("""
        <div style="
            margin-top:1rem;
            padding-bottom:1rem;
            text-align:center;
            color:white;
            font-size:15px;
            font-weight:400;
            line-height:1.8;
        ">
            SnapClass • AI Attendance System <br>
            Built with Streamlit & Python
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():

    st.markdown("""
        <div style="
            margin-top:1rem;
            padding-bottom:1rem;
            text-align:center;
            color:black;
            font-size:15px;
            font-weight:400;
            line-height:1.8;
        ">
            SnapClass • AI Attendance System <br>
            Built with Streamlit & Python
        </div>
    """, unsafe_allow_html=True)