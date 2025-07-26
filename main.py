import streamlit 
from langhelper import generate_restaurant_recommendations
streamlit.title("Restaurant Recommender System")

cusine = streamlit.sidebar.selectbox('cusine',('Indian', 'Chinese', 'Italian'))



if cusine:
    res = generate_restaurant_recommendations(cusine)
    streamlit.markdown(f"### Restaurant Name: **{res['name'].strip()}**")
    menu = res['item'].strip().split(',')
    streamlit.subheader("Menu Items")
    for item in menu:
        streamlit.write("-", item)
    