import os
from PIL import Image

def generate_animated_gif():
    print("🎬 Generating Animated GIF...")
    
    # Define the sequence of images for the animation
    # We want to cycle through the Mermaid Title Diagram and the 4 output charts
    image_paths = [
        "images/title-diagram.png",
        "output/enrollment_trend.png",
        "output/adverse_events.png",
        "output/demographics.png",
        "output/vitals_analysis.png"
    ]
    
    # Filter to only existing images
    valid_paths = [p for p in image_paths if os.path.exists(p)]
    
    if not valid_paths:
        print("❌ No images found for GIF generation.")
        return

    frames = []
    for path in valid_paths:
        img = Image.open(path)
        # Ensure consistent size (optional but recommended for GIFs)
        # Choosing a reasonable size for a title image
        img = img.convert("RGB")
        img.thumbnail((1200, 800))
        
        # Create a new white background image to handle varying sizes
        background = Image.new('RGB', (1200, 800), (255, 255, 255))
        bg_w, bg_h = background.size
        img_w, img_h = img.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
        background.paste(img, offset)
        
        frames.append(background)

    if frames:
        os.makedirs("images", exist_ok=True)
        gif_path = "images/title-animation.gif"
        frames[0].save(
            gif_path,
            save_all=True,
            append_images=frames[1:],
            duration=2000,  # 2 seconds per frame
            loop=0
        )
        print(f"✅ Saved animated GIF to {gif_path}")

if __name__ == "__main__":
    generate_animated_gif()
