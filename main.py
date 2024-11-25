import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageOps,Image
from textContent import *
from style import *
import base64
import ollama
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
from ragContext import *
st.set_page_config(layout="wide")



#print("_")

@st.cache_resource
def get_client():
    return create_collection()



a,b,c="","",""
template="Your primary functionality is to provide answers when asked about the person Ifreen. You are Ifreen. You are the AI who should simulate the role of Ifreen. Ifreen who is a 26 year old male, who is a student pursuing Artificial Intelligence at Boston University currently. Your answer should be directed towards the end user. I will be providing you with recent dialogue exchanegs along with the latest user query so that you can understand the history and context of the chat. Previous Chat Exchange : {} <End of Chat Exchange>, ------- Current User Query : {} <End of User Query> YOU SHOULD ANSWER TO THE USEE QUERY ALONE----  Here is some Information About ifreen : {}. <End of Context about Ifreen> Now based on the the context and history of dialogue exchanges, Answer his query! Answer the user quer and only answer about Ifreen when he specifically asks. Your response should address the user by considering you as Ifreen. You the AI are Ifreen and responding to the end-user. And make it natural like a convo. To repeat : Answer the User query and make it natural and not stupid. "




def appendMessage():
    st.session_state["history"].append({"User": st.session_state["userInput"]})



if "history" not in st.session_state:
    st.session_state["history"]=[{"AI":"Hi, Please ask me anything about Ifreen!"}]

cols=st.columns([0.3,0.55,0.19])

with cols[0]:

    col_=st.columns([0.15,0.95])
    with col_[0]:
        st.text(" ")
        st.markdown(
            """<a href="https://www.linkedin.com/in/mohamed-ifreen-a60634177/">
                <img src="data:image/png;base64,{}" width="40">
                </a>""".format(
                base64.b64encode(open("images/Social/Linkedin.png", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )
    with col_[1]:
        st.text(" ")
        st.markdown(
            """<a href="https://www.kaggle.com/ifreenibrahim">
                <img src="data:image/png;base64,{}" width="75">
                </a>""".format(
                base64.b64encode(open("images/Social/Kaggle.jpg", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )

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



with cols[-1]:
    st.text(" ")
    st.text(" ")
    chatMode=st.popover("Experimental Chat",icon="👻",use_container_width=False)
    with chatMode:
        chatBox=st.container(height=400)
        with chatBox:
            if "history" in st.session_state:
                for item in st.session_state["history"]:
                    with st.chat_message(list(item.keys())[0]):
                        st.write(str(list(item.values())[0]))
        message=st.chat_input("Please enter your message",on_submit=appendMessage,key="userInput")
        if message:
            #client=get_client()
            client=create_collection()
            documents=get_data(message,client)["documents"][:3]
            #print(documents)
            #print(("_____"))
            template_=template.format(st.session_state["history"][-5:],message,str(documents))
            print(template_)
            response = ollama.generate(model='llama3.2', prompt=template_)
            with chatBox.chat_message("AI"):
                st.write(response["response"])
                st.session_state["history"].append({"AI": response["response"]})

st.text(" ")
listTabs=["About Me","Resume","Experiments","Achievements","Certifications"]
whitespace = 43
## Fills and centers each tab label with em-spaces
tabs=st.tabs([s.center(whitespace,"\u2001") for s in listTabs])
#print(tabs)
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
        st.text(f"{introduction}")


    with cols[0]:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.image("images/Ifreen/Me.png")


with tabs[1]:
    st.text("")
    st.text("")

    cols=st.columns([0.5, 0.5, 0.2])

    with cols[1]:
        st.subheader(":grey[Work Experience] :fire:")
    st.text("")
    st.text("")

    with cols[-1]:
        with open("images/Ifreen/ifreenResume.pdf", "rb") as f:
            st.download_button("Download Resume! :nerd_face:", data=f, file_name="images/Ifreen/ifreenResume.pdf", mime="application/pdf")

    cols = st.columns(3)
    with cols[0]:
        with st.expander(f":red[{company3}]",expanded=True):
            with st.container(border=True):
                st.markdown(css_1+"""<p class="big-font">Senior Machine Learning Engineer </p>""", unsafe_allow_html=True)
                st.text("")
                st.markdown(css_2+f"<p class=small-font>{company3_content} </p>", unsafe_allow_html=True)

    with cols[1]:
        with st.expander(f":red[{company2}]",expanded=True):
            with st.container(border=True):
                st.markdown(css_1+"<p class=big-font>Senior Data Engineer </p>""", unsafe_allow_html=True)
                st.text("")
                st.markdown(css_2+f"""<p class="small-font">{company2_content}</p>""",unsafe_allow_html=True)
    with cols[2]:
        with st.expander(f":red[{company1}]",expanded=True):
            with st.container(border=True):
                st.markdown(css_1+"<p class=big-font>Graduate Engineer Trainee</p>", unsafe_allow_html=True)
                st.text("")
                st.markdown(css_2+f"""<p class="small-font">{company1_content}""",unsafe_allow_html=True)


    st.text("")
    st.text("")

    with st.columns([0.42,0.58])[1]:
        st.subheader(":grey[Education] :fire:")
    st.text("")
    st.text("")
    cols = st.columns(2)
    with cols[0]:
        with st.expander(f":red[{school2}]",expanded=True):
            with st.container(border=True):
                st.markdown(css_1 + f"""<p class="big-font">{school2_degree}</p>""",unsafe_allow_html=True)
                st.text(" ")
                st.markdown(css_2+f"<p class=small-font>{school2_content}</p>", unsafe_allow_html=True)

    with cols[1]:
        with st.expander(f":red[{school1}]",expanded=True):
            with st.container(border=True):
                st.markdown(css_1 + f"""<p class="big-font">{school1_degree}</p>""",unsafe_allow_html=True)
                st.text(" ")
                st.markdown(css_2+f"""<p class="small-font">{school1_content}</p>""",unsafe_allow_html=True)



with tabs[2]:
    st.text("")
    st.text("")
    cols=st.columns([0.4,0.1,0.5])
    with cols[0]:
        st.subheader("Experiments :sunglasses:")
        st.text("")
        st.markdown(css_2 + f"""<p class="small-font">{experiments_title}</p>""", unsafe_allow_html=True)

    with cols[-1]:
        st.markdown(css_1 + f"""<p class="big-font">{experiment_name_1}</p>""",unsafe_allow_html=True)
        st.markdown(css_2 + f"""<p class="small-font">{experiment_content_1}</p>""", unsafe_allow_html=True)
        st.text("")
        st.image("images/Experiments/cool_1.png")
        st.text("")
        st.markdown(css_1 + f"""<p class="big-font">{experiment_name_2}</p>""",unsafe_allow_html=True)
        st.markdown(css_2 + f"""<p class="small-font">{experiment_content_2}</p>""", unsafe_allow_html=True)
        st.text("")
        st.image("images/Experiments/coolImage_2.png")
        st.text("")
        st.markdown(css_1 + f"""<p class="big-font">{experiment_name_3}</p>""",unsafe_allow_html=True)
        st.markdown(css_2 + f"""<p class="small-font">{experiment_content_3}</p>""", unsafe_allow_html=True)
        st.text("")
        st.image("images/Experiments/coolImage_3.png")



with tabs[3]:
    st.text("")
    with st.columns([0.42, 0.58])[1]:
        st.subheader("Awards :first_place_medal: ")
    st.text("")
    cols=st.columns(4)
    with cols[0]:
        st.image("images/Achievements/ach1.png")
        st.text("")
        st.subheader(f"{award_name_1}")
        st.text("")
        st.text("")
        st.text(f"{award_content_1}")
    with cols[1]:
        st.image("images/Achievements/ach2.png")
        st.text("")
        st.subheader(f"{award_name_2}")
        st.text(f"{award_content_2}")
    with cols[2]:
        st.image("images/Achievements/ach3.png")
        st.text("")
        st.subheader(f"{award_name_3}")
        st.text("")
        st.text("")
        st.text(f"{award_content_3}")
    with cols[3]:
        st.image("images/Achievements/ach4.png",width=280)
        st.text("")
        st.subheader(f"{award_name_4}")
        st.text(f"{award_content_4}")


    st.text("")


    with st.columns([0.35, 0.65])[1]:
        st.subheader("Competitive Programming :computer: ")
    st.text("")
    st.text("")
    cols=st.columns(3)
    with cols[0]:
        st.image("images/Achievements/logo1.png",width=180)
        st.text("")
        st.write("Specialist - Competitions")
    with cols[1]:
        st.image("images/Achievements/logo2.png",width=300)
        st.text("")
        st.write("6 Star - Problem Solving")
    with cols[2]:
        st.image("images/Achievements/logo3.png",width=300)
        st.text("")
        st.text("")
        st.write("4 Star - Comptetions")

    st.text("")
    st.text("")
    with st.columns([0.35, 0.65])[1]:
        st.subheader("Presentations Given :walking: ")
    st.text("")
    st.text("")
    cols=st.columns(3)
    with cols[0]:
        st.image("images/Achievements/talk1.png",width=415)
    with cols[1]:
        st.image("images/Achievements/talk1_.png")
    with cols[2]:
        with st.columns([0.2,0.8])[1]:
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.write(f"{presentation_1}")


    cols=st.columns([0.67,0.33])
    with cols[0]:
        st.image("images/Achievements/Boston.jpeg")
    with cols[1]:
        with st.columns([0.2,0.8])[1]:
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.write(f"{presentation_2}")



    st.text("")
    st.text("")
    st.text("")
    with st.columns([0.35, 0.65])[1]:
        st.subheader("Memberships :walking: ")
    st.text("")
    st.text("")
    with st.columns([0.32, 0.68])[1]:
        st.text("IEEE Computational Intelligence Member")




with tabs[-1]:
    st.text("")
    with st.columns([0.42, 0.58])[1]:
        st.subheader("Ceritfications :100: ")
    st.text("")
    cols=st.columns(2)
    with cols[0]:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.subheader(f"{certification_1_title}")
        st.text("")
        st.text("")
        st.write(f"{certification_1_content}")
    with cols[1]:
        st.image("images/Certifications/tensorflow.png")

    st.text("")
    cols=st.columns(2)
    with cols[0]:
        st.image("images/Certifications/aws.png")
    with cols[1]:
        st.text("")
        st.text("")
        st.text("")
        st.text("")

        st.subheader(f"{certification_2_title}")
        st.text("")
        st.text("")
        st.write(f"{certification_2_content}")

    st.text("")
    st.text("")


    with st.columns([0.42, 0.58])[1]:
        st.subheader("Courses :100: ")


    col=st.columns(4)
    with col[0]:
        st.image("images/Certifications/course1.png")
        st.write(f"{course1_content}")
    with col[1]:
        st.image("images/Certifications/course2.png")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.write(f"{course2_content}")
    with col[2]:
        st.image("images/Certifications/course3.png")
        st.text("")
        st.write(f"{course3_content}")
    with col[3]:
        st.image("images/Certifications/course4.png",width=300)
        st.text("")
        st.write(f"{course4_content}")


