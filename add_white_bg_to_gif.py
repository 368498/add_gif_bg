#!/usr/bin/env python3

import sys
import os
from PIL import Image, ImageSequence

def add_white_bg_to_gif(input_gif_path, output_gif_path):
    try:
        with Image.open(input_gif_path) as gif_image:
            output_frames = []
            frame_duration = gif_image.info.get('duration', 100)
            loop_count = gif_image.info.get('loop', 0)
            disposal_method = gif_image.info.get('disposal', 2)

            for gif_frame in ImageSequence.Iterator(gif_image):
                rgba_frame = gif_frame.convert('RGBA')
                white_bg = Image.new('RGBA', rgba_frame.size, (255, 255, 255, 255))
                composited_frame = Image.alpha_composite(white_bg, rgba_frame)
                paletted_frame = composited_frame.convert('P', palette=Image.ADAPTIVE)
                output_frames.append(paletted_frame)

            output_frames[0].save(
                output_gif_path,
                save_all=True,
                append_images=output_frames[1:],
                duration=frame_duration,
                loop=loop_count,
                disposal=disposal_method
            )
        print(f"Success: Saved GIF with white background to '{output_gif_path}'")
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python add_white_bg_to_gif.py input.gif output.gif")
        sys.exit(1)
    input_gif_path, output_gif_path = sys.argv[1], sys.argv[2]
    if not os.path.isfile(input_gif_path):
        print(f"Error: File '{input_gif_path}' does not exist.")
        sys.exit(1)
    add_white_bg_to_gif(input_gif_path, output_gif_path)

if __name__ == "__main__":
    main() 
