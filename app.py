import streamlit as st

st.set_page_config(
    page_title="Rape cases in India"
)

home = st.Page('Home.py', title= 'Introduction', icon=":material/home:")

obj1 = st.Page('Objective1.py' , title = "Distribution of Rape Cases Across States ",default=True,)
obj2 = st.Page('Objective2.py' , title = "Trends and Annual Changes ",default=True)
obj3 = st.Page('Objective3.py' , title = "Correlation Between Rape Cases and Related Crimes ",default=True)

pg = st.navigation(
        {
            "Menu":[home,obj1,obj2,obj3]
        }
    )

pg.run()
