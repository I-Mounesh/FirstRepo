import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.pyplot import style

st.title("Compare Your Internal And External Academic Performance")

# create a Matplotlib figure
fig, ax=plt.subplots()
style.use('ggplot')
x=["SEMP","CN","TOC","USP","REIPR","EVS","mini-PROJ","NSS","OODP"]
y=[]
st.write("Internals")
for i in range(len(x)):
    s = st.number_input(f"Enter the Marks for {x[i]}:", key=f"mark_{i}",min_value=0.00,max_value=50.00)
    y.append(s)

x1=["SEMP","CN","TOC","USP","REIPR","EVS","mini-PROJ","NSS","OODP"]
y1=[]

st.write("Externals")
for i in range(len(x1)):
    r = st.number_input(f"Enter the Marks for {x1[i]}:", key=f"marks_{i}",min_value=0.00,max_value=50.00)
    y1.append(r)

if st.button("Plot"):
    st.balloons()
    ax.plot(x,y,label='Internals')
    ax.plot(x1,y1,label='Externals')
    ax.legend()
    st.pyplot(fig)
    
st.write("Thank You")
