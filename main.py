import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageOps,Image
from textContent import *

st.set_page_config(layout="wide")
st.markdown("""<style>footer{visibility:visible;}</style>""",unsafe_allow_html=True)



cols=st.columns([0.3,0.7])
with cols[1]:
    #st.subheader(":red[Mohamed Ifreen]")
    st.markdown(
        """
        <style>
        .custom-subheader {
            margin-bottom: -20px; /* Adjust this value to reduce space */
            color:#FFA500;
            font-size:30px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<div class='custom-subheader'>Welcome to the world of Ifreen &#x1F60E</div>",unsafe_allow_html=True)

    with st.columns([0.03,0.97])[1]:


        st.write("MS Artificial Intelligence | Boston University")
st.text(" ")
listTabs=["About Me","Resume","Projects","Experiments","Achievements","Certifications"]
whitespace = 45
## Fills and centers each tab label with em-spaces
tabs=st.tabs([s.center(whitespace,"\u2001") for s in listTabs])
print(tabs)
with tabs[0]:
    cols=st.columns([0.4,0.1,0.5])
    with cols[-1]:
        st.text("")
        st.text("")
        st.text("")
        st.markdown("""<style>
.big-font {
    font-size:50px !important;
    color:grey !important;
}
</style><p class="big-font">Hi! This is Ifreen....</p>""",unsafe_allow_html=True)
        st.text(" ")
        st.text(f"{var1}")


    with cols[0]:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.image("Me.png")


with tabs[1]:
    st.text("")
    st.text("")

    cols=st.columns([0.5, 0.5, 0.2])

    with cols[1]:
        st.subheader(":grey[Work Experience] :fire:")
    st.text("")
    st.text("")

    with cols[-1]:
        with open("ifreenResume.pdf","rb") as f:
            st.download_button("Download Resume! :nerd_face:",data=f,file_name="ifreenResume.pdf",mime="application/pdf")

    cols = st.columns(3)
    with cols[0]:
        with st.expander(":red[Rapid Acceleration Partners (Sep 2023 - Aug 2024)]",expanded=True):
            with st.container(border=True):
                st.markdown(css_1+"""<p class="big-font">Senior Machine Learning Engineer </p>""", unsafe_allow_html=True)
                st.text("")
                st.markdown(css_2+"<p class=small-font>• Spearheaded deep learning projects, creating fast-tracked POCs, resulting in multi-million dollar contracts.<br><br>• Led AI system development for Hussmann (Panasonic) to analyze product complaints, providing insights based on serial numbers; resulting in a $3 million project.<br><br>• Engineered AI voice analysis for Denave to evaluate sales call sentiment, saving 100+ hours monthly.<br><br>• Designed AI system for VirtueServe to map ICD codes and generate medical summaries, reducing scribing time by 70% and making the ICD mapping much efficient. </p>", unsafe_allow_html=True)

    with cols[1]:
        with st.expander(":red[LTIMindtree (June 2021 - Aug 2023)]",expanded=True):
            with st.container(border=True):
                st.markdown(css_1+"<p class=big-font>Senior Data Engineer </p>""", unsafe_allow_html=True)
                st.text("")
                st.markdown(css_2+"""<p class="small-font">• Led end-to-end ML model development, from requirement gathering to deployment with code optimizations.<br><br>• Implemented NLP-based models for ticket mining and attribute extraction, reducing manual efforts by 60%.<br><br>• Created Auto-Tagging Tool for Support Tickets, improving resolution and categorization time by 40%.</p>""",unsafe_allow_html=True)
    with cols[2]:
        with st.expander(":red[LTIMindtree (Oct 2020 - June 2021)]",expanded=True):
            with st.container(border=True):
                st.markdown(css_1+"<p class=big-font>Graduate Engineer Trainee</p>", unsafe_allow_html=True)
                st.text("")
                st.markdown(css_2+"""<p class="small-font">• Received intensive hands-on training — Statistics, Data analysis using Python & code optimisations<br><br>• Worked on basic projects and assignments applying the skills learnt and validated through assessments.""",unsafe_allow_html=True)


    st.text("")
    st.text("")

    with st.columns([0.42,0.58])[1]:
        st.subheader(":grey[Education] :fire:")
    st.text("")
    st.text("")
    cols = st.columns(2)
    with cols[0]:
        with st.expander(":red[Boston University (Sep 2024 - Dec 2025)]",expanded=True):
            with st.container(border=True):
                st.markdown(css_1 + """<p class="big-font">Masters in AI </p>""",unsafe_allow_html=True)
                st.text(" ")
                st.markdown(css_2+"<p class=small-font> I am currently pursuing my Masters in AI with an expected graduation of December 2025. The program is geared towards gaining both theoretical as well as practical understanding of AI. </p>", unsafe_allow_html=True)

    with cols[1]:
        with st.expander(":red[Anna University (June 2016 - May 2020)]",expanded=True):
            with st.container(border=True):
                st.markdown(css_1 + """<p class="big-font">Bachelors in Information Technology </p>""",unsafe_allow_html=True)
                st.text(" ")
                st.markdown(css_2+"""<p class="small-font">During my undergraduate studies, I gained a strong foundation in computer science and mathematics. I also participated in several hackathons and coding competitions, which helped me develop my problem-solving and critical thinking skills.</p>""",unsafe_allow_html=True)




























