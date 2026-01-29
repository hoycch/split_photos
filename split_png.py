from PIL import Image
import os

input_folder = "pngs"          # ← change this
output_folder = "split_results" # ← change this or keep same folder

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if not filename.lower().endswith(('.png', '.PNG')):
        continue

    path = os.path.join(input_folder, filename)
    try:
        img = Image.open(path)
        width, height = img.size

        mid = width // 2

        left  = img.crop((0,       0, mid, height))
        right = img.crop((mid,     0, width, height))

        name, ext = os.path.splitext(filename)

        left.save(os.path.join(output_folder, f"{name}_left{ext}"))
        right.save(os.path.join(output_folder, f"{name}_right{ext}"))

        print(f"Split {filename}  →  {name}_left.png + {name}_right.png")

    except Exception as e:
        print(f"Error processing {filename}: {e}")
