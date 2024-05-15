import streamlit as st

def app():
   # st.image()
    st.subheader('Healthify is a place where users come to change their lifestyle and their health also share their valuable thoughts with the world.')

    st.header(':green[Feedback Section]')
    feedback = st.text_area("Share your feedback", "")
    if st.button("Submit Feedback"):
        if feedback:
            st.success("Thank you for your feedback! We appreciate your input.")
        else:
            st.warning("Please provide your feedback before submitting.")

    st.markdown('Created by: [Hardeep Singh Sahib](https://www.linkedin.com/in/hardeep-singh-sahib%F0%9F%87%AE%F0%9F%87%B3-61bb811b9/)')
    st.markdown('Contact via mail: 23391006@geu.ac.in')
    