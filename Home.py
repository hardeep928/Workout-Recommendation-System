import streamlit as st
from PIL import Image

def app():
    st.title("Welcome to :violet[Healthify]")
    st.caption("A way to make you fit")
    st.markdown("---")

    st.write("Welcome to the Healthify!. This is your one-stop destination for Workout and motivation to build your body and mind strong.")

    st.header("Why Do We Need to Workout?")
    st.write("Participating in physical activities improves overall physical fitness, strength, and stamina. Beyond the physical benefits, exercise provides a valuable outlet for stress relief and relaxation, fosters social connections within fitness communities, and helps individuals achieve personal fitness goals, ultimately leading to improved quality of life and self-confidence.")
    st.image("Pose1.jpg", caption="Image by Mabel Amber from Pixabay", use_column_width=True)

    st.header("Explore Workouts")
    st.write("Browse our collection of workout tailored to various fitness goals and experience levels. There's something for everyone")

    st.header("Get Motivated")
    st.write("Motivation is the driving force behind every successful workout. It fuels our determination and propels us toward our fitness goals, reminding us that with perseverance, anything is achievable.")
    st.write("Need some motivation to kickstart your workout routine? Check out our inspiring Posters, and videos for staying motivated.")
    st.image("Pose2.jpg", caption="Image by Arek Socha from Pixabay", use_column_width=True)

    st.markdown("---")
    st.write(":red[Ready to get started?] Choose an option from the sidebar to explore our content.")