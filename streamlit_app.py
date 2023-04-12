import streamlit as st
from PIL import Image
import cv2

def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose the app mode", ["Image", "Video"])
    
    if app_mode == "Image":
        st.title("Image App")
        st.write("Select an image to display:")
        option = st.selectbox("Select an option", ("Local File", "Capture with Camera"))

        if option == "Local File":
            uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image", use_column_width=True)
                caption = st.text_input("Enter a caption for the image:")
                st.write("Caption:", caption)

        elif option == "Capture with Camera":
            cap = cv2.VideoCapture(0)
            if st.button("Capture"):
                ret, frame = cap.read()
                if ret:
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    st.image(image, caption="Captured Image", use_column_width=True)
                    caption = st.text_input("Enter a caption for the image:")
                    st.write("Caption:", caption)
            cap.release()
        
    elif app_mode == "Video":
        st.title("Video App")
        st.write("Select a video to display:")
        option = st.selectbox("Select an option", ("Local File", "Capture with Camera"))

        if option == "Local File":
            uploaded_file = st.file_uploader("Choose a video", type=["mp4"])
            if uploaded_file is not None:
                st.video(uploaded_file)

        elif option == "Capture with Camera":
            cap = cv2.VideoCapture(0)
            if st.button("Start Recording"):
                st.write("Recording started...")
                frames = []
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frames.append(frame)
                st.write("Recording stopped.")
                cap.release()
                st.video(frames)

if __name__ == "__main__":
    main()
