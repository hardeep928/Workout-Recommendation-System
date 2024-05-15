'''#gO5NTwsGxdach6UXpyiOFJ6zSDMSJOHsLiHZ1lIfbjGNbaH1rYSAgkYq'''

def app():
    import streamlit as st
    import pickle
    import random

    # Load the exercise data
    exercises = pickle.load(open("exercises_list.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))

    # Create the main content of the page
    st.header("Workout Recommendation System")
    levels = ['Beginner', 'Intermediate', 'Expert']
    areas = exercises['Area'].unique()

    select_level = st.selectbox("Select Level from Dropdown", levels)
    select_area = st.selectbox("Select Area from Dropdown", areas)

    def recommend(exercise, area):
        filtered_exercises = exercises[(exercises['Level'] == exercise) & (exercises['Area'] == area)]
        if filtered_exercises.empty:
            st.write("No exercises found for the selected level and area.")
            return []

        recommend_exercises = []
        for _ in range(min(5, len(filtered_exercises))):
            # Get a random exercise from the filtered list
            exercise_index = random.randint(0, len(filtered_exercises) - 1)
            recommend_exercises.append(filtered_exercises.iloc[exercise_index].Title)

        return recommend_exercises

    if st.button("Show Recommendation"):
        exercise_names = recommend(select_level, select_area)
        for i, name in enumerate(exercise_names):
            st.markdown(f'[{name}]({exercises.loc[exercises["Title"] == name, "URL"].values[0]})', unsafe_allow_html=True)

    # Create the "Get Motivation" button
    if st.button("Get Motivation"):
        st.write("## Let's Motivate You")

     # Create a columns layout to display images side by side
        col1, col2= st.columns(2)
        with col1:
            st.image("Motivation-Image-1.jpg", caption="", use_column_width=True, width=10)
        with col2:
            st.image("Motivation-Image-2.jpg", caption="",use_column_width=False, width=322)
    
        col3, col4=st.columns(2)
        with col3:
            st.image("Motivation-Image-3.jpg", caption="",use_column_width=False, width=322)
        with col4:
            st.image("Motivation-Image-4.png",caption="",use_column_width=False, width=322)

    
        st.markdown("""
        ## Here are some motivational quotes:
        - "Success is not final, failure is not fatal: It is the courage to continue that counts." - Winston Churchill
        - "The only way to do great work is to love what you do." - Steve Jobs
        - "Believe you can and you're halfway there." - Theodore Roosevelt
        """)
    



        st.markdown("""
        ## Here are some motivational YouTube links:
        Tap any image to play the video:
        [![Video 1](https://img.youtube.com/vi/wnHW6o8WMas/sddefault.jpg)](https://www.youtube.com/watch?v=wnHW6o8WMas&pp=ygUebW90aXZhdGlvbmFsIHZpZGVvIGZvciB3b3Jrb3V0)
        [![Video 2](https://img.youtube.com/vi/WE50ZSVQeDs/sddefault.jpg)](https://www.youtube.com/watch?v=WE50ZSVQeDs)
        [![Video 3](https://img.youtube.com/vi/V2EfL1j4KYE/sddefault.jpg)](https://www.youtube.com/watch?v=V2EfL1j4KYE)
        [![Video 4](https://img.youtube.com/vi/KmEv2sa7lNU/sddefault.jpg)](https://www.youtube.com/watch?v=KmEv2sa7lNU)
        """)