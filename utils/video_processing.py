import os
from moviepy.editor import VideoFileClip
from PIL import Image

def extract_frames(video_path, output_dir, num_frames=10):
    clip = VideoFileClip(video_path)
    duration = clip.duration
    interval = duration / num_frames
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(num_frames):
        frame_time = i * interval
        frame = clip.get_frame(frame_time)
        frame_image = Image.fromarray(frame)
        frame_image.save(f"{output_dir}/frame_{i}.jpg")
