import streamlit as st
from module import page2
from PIL import Image
import os
from streamlit_option_menu import option_menu

def main():
    st.set_page_config(page_title="Try IT On", page_icon=Image.open("assets/logo.jpeg"), layout="wide")   
    if st.session_state.page == "About":
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])  # Create columns to adjust centering
        with col3:
            st.image('assets/image 1.jpeg', width=300, use_column_width=False)  # Adjust the width as needed        
        selected = option_menu(menu_title=None, options=["Home"], orientation="horizontal")      
        if selected == "Home":
            st.markdown("<h1 style='text-align: center;'>Welcome To Try IT On</h1>", unsafe_allow_html=True)
            col1, col2 = st.columns([1, 1])
            with col1:
                st.header("What is Try IT On?")
                st.markdown("""
                Try IT On is a cutting-edge application designed to revolutionize the way people shop for clothing. It enables users to virtually try on garments without physically wearing them, providing an immersive and convenient shopping experience right from the comfort of their homes. By leveraging advanced augmented reality technology, Try IT On empowers users to visualize how different clothing items look on them in real-time, facilitating informed purchasing decisions and reducing the hassle of traditional in-store fittings.
                """)
                st.header("How Does Try IT On Work?")
                st.markdown("""
                Try IT On utilizes sophisticated augmented reality (AR) algorithms to superimpose virtual clothing onto a user's live video feed. The process begins by detecting and mapping the user's body contours and dimensions. Next, the application identifies the specific clothing item selected by the user from its extensive catalog. Using this information, Try IT On dynamically adjusts the appearance and fit of the garment to match the user's body proportions in real-time. This seamless integration of AR technology enables users to see how different outfits look on them from various angles, helping them choose the perfect style and size without ever needing to physically try on the clothes.
                """)
                st.header("Importance of Try IT On")
                st.markdown("""
                Try IT On represents a significant advancement in the realm of online shopping, addressing common challenges associated with purchasing clothing remotely. By offering a virtual try-on experience, the application enhances user confidence and satisfaction by providing a more accurate representation of how garments will look and fit. This reduces the likelihood of returns due to sizing or style discrepancies, thereby improving overall efficiency for both consumers and retailers. Additionally, Try IT On promotes inclusivity by enabling users of all body types to visualize themselves in different clothing options, fostering a more inclusive and diverse shopping environment. Overall, Try IT On streamlines the shopping process, enhances customer engagement, and drives innovation in the fashion industry.
                """)
                if st.button("Test TryITOn"):
                    st.session_state.page = "Page 2"
            with col2:
                st.image('assets/image1.jpeg', width=900, use_column_width=False)
    elif st.session_state.page == "Page 2":
        page2()

if __name__ == "__main__":
    if "page" not in st.session_state:
        st.session_state.page = "About"
    main()
