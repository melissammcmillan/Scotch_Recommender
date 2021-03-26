import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

#Welcome and Introduction
st.header('Welcome to My Scotch Recommender.')
st.subheader('Please use this App to pick your next scotch.')

#Load dataset
scotches = pd.read_csv('data/labeled_distilleries.csv', index_col=0)

#User chooses recommendation by distillery or by category
st.write('Would you like a recommendation using a distillery or a category?')
recomm_type = st.selectbox('Select', ["None", "By Distillery", "By Category"])
#pick_distillery = st.checkbox('Do you want to see the thing?')

#function for finding label of picked Distillery
def label_grabber(distillery):
    """ This function will use the distillery picked by the user, look into the dataframe
    to grab that label, and then list all the scotches with that label.

    Arguments: the response from the pick_distill dropdown menu; a string of the distillery

    Returns: The list of distilleries with that same label.
    """
    #grab the info for the distillery chosen
    interim_df = scotches[scotches['Distillery'] == distillery]

    #then grab the label for that distillery
    target_label = list(interim_df['labels'])

    #filter the scotches databse using that label
    filter_df = scotches[scotches['labels'] == target_label[0]]

    #make a list of the distilleries using that label
    recommended_list = list(filter_df['Distillery'])

    #return the list of distilleries in that filtered dataframe
    return recommended_list

#function for recommending a distillery based on the category
def cat_grabber(category):
    """ This function will use the category chosen by the user, associate the label,
    grab the scotches/distilleries from that label/category, and list them out for
    recommendation.

    Arguments: the response from the pick_cat selector;
    -  the category Smoky/Medicinal corresponds to label 1
    -  the category Honey/Spicy/Winey corresponds to label 0
    -  the category Sweet/Fruity/Floral corresponds to label 2

    Returns a list of recommendations using the label that corresponds to the chosen category.
    """
    #take in the category, and associate with a label
    if category == 'Smoky/Medicinal':
        label_selected = 1
    elif category == 'Honey/Spicy/Winey':
        label_selected = 0
    else:
        label_selected = 2

    #use the label_selected variable to limit the scotches dataframe to the same category
    df_label = scotches[scotches['labels'] == label_selected]

    #return the list of distilleries for those in df_label
    list_of_recommendations = list(df_label['Distillery'])
    return list_of_recommendations


#if picking by distillery, choose from dropdown menu and get recommendation
if recomm_type == "By Distillery":
    pick_distill = st.selectbox('Select a Distillery', scotches['Distillery'])
    #'You selected: ', pick_distill
    #Here is the recommendation:
    st.write(f'Based on the distillery you chose, we recommend trying scotches from these other distilleries: {label_grabber(pick_distill)}')
    st.balloons()

#if picking by category, choose from the 3 categories and get recommendation
if recomm_type == "By Category":
    pick_cat = st.selectbox('Select a Category', ['Smoky/Medicinal', 'Honey/Spicy/Winey', 'Sweet/Fruity/Floral'])
    #recommendations from that category
    st.write(f'Based on the category you chose, we recommend trying scotches from these distilleries: {cat_grabber(pick_cat)}')
    st.balloons()

#aesthetics
background = \
'''
    <style>
    body \
    {
        background-image: 'assets/drink-3108435_1920.jpg');
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: 100% 100%;
    }
    </style>
'''

st.markdown(background, unsafe_allow_html=True)
