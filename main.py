import streamlit as st
from utils.image_processing import create_composite_image
from utils.video_processing import extract_frames
from utils.animation import animate_avatar, prepare_images_for_animation
from utils.tts import text_to_speech
import os

st.title("AI Avatar Creator")

# Step 1: Image Upload
st.header("Step 1: Upload Images")
uploaded_images = st.file_uploader("Choose images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_images:
    image_paths = []
    for uploaded_image in uploaded_images:
        image_path = f"temp/{uploaded_image.name}"
        with open(image_path, "wb") as f:
            f.write(uploaded_image.getbuffer())
        image_paths.append(image_path)

    composite_image = create_composite_image(image_paths)
    if composite_image:
        st.image(composite_image, caption="Composite Avatar")
        composite_image.save('composite_avatar.jpg')

# Step 2: Video Upload
st.header("Step 2: Upload Video")
uploaded_video = st.file_uploader("Choose a video", type=["mp4", "avi"])

if uploaded_video:
    video_path = f"temp/{uploaded_video.name}"
    with open(video_path, "wb") as f:
        f.write(uploaded_video.getbuffer())
    
    frame_dir = "frames"
    extract_frames(video_path, frame_dir)
    st.success(f"Frames extracted to {frame_dir}")

# Step 3: Animate Avatar
st.header("Step 3: Animate Avatar")
if st.button("Animate"):
    face_images = [Image.open(f'temp/{img.name}') for img in uploaded_images]
    opencv_images = prepare_images_for_animation(face_images)
    animate_avatar(opencv_images)

# Step 4: Add Voiceover
st.header("Step 4: Add Voiceover")
text_input = st.text_area("Enter text for the avatar to speak", value="Hello! I am your AI avatar.")
if st.button("Generate Voiceover"):
    text_to_speech(text_input, 'avatar_voiceover.mp3')
    st.audio('avatar_voiceover.mp3')
