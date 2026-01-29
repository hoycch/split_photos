from PIL import Image
import os

# ────────────────────────────────────────────────────────────────
# CONFIGURATION
# ────────────────────────────────────────────────────────────────
input_folder  = "pngs"               # ← folder with your PNG images
output_folder = "split_jpg_results"  # ← where to save the JPG halves

# JPG quality (1–95, higher = better quality + larger file)
jpg_quality   = 92
optimize      = True                 # True = slightly smaller files

os.makedirs(output_folder, exist_ok=True)

# ────────────────────────────────────────────────────────────────
# MAIN LOOP
# ────────────────────────────────────────────────────────────────
for filename in os.listdir(input_folder):
    if not filename.lower().endswith(('.jpg', '.JPG')):
        continue

    input_path = os.path.join(input_folder, filename)
    
    try:
        img = Image.open(input_path).convert("RGB")   # ← Convert to RGB (removes alpha → JPG compatible)
        
        width, height = img.size
        mid = width // 2

        # Crop left and right halves
        left  = img.crop((0,       0, mid,   height))
        right = img.crop((mid,     0, width, height))

        # Prepare output filenames (replace .png with _left.jpg / _right.jpg)
        base_name, _ = os.path.splitext(filename)     # removes .png
        left_path  = os.path.join(output_folder, f"{base_name}_left.jpg")
        right_path = os.path.join(output_folder, f"{base_name}_right.jpg")

        # Save as high-quality JPG
        left.save(
            left_path,
            "JPEG",
            quality     = jpg_quality,
            optimize    = optimize,
            progressive = True   # optional: faster web loading
        )
        right.save(
            right_path,
            "JPEG",
            quality     = jpg_quality,
            optimize    = optimize,
            progressive = True
        )

        print(f"Split {filename:30} → {base_name}_left.jpg  +  {base_name}_right.jpg "
              f"({jpg_quality}% quality)")

    except Exception as e:
        print(f"Error processing {filename}: {e}")
