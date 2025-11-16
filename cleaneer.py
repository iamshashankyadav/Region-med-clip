import pandas as pd
import os

# Paths
csv_file = "HAM10000_metadata_synced.csv"   # your final CSV file
images_folder = "HAM10000_images_final"           # your image folder

# Load CSV
df = pd.read_csv(csv_file)

# Extract expected image IDs
csv_image_ids = set(df['image_id'].astype(str))

# Get actual image IDs from folder (without .jpg extension)
folder_image_ids = {os.path.splitext(f)[0] for f in os.listdir(images_folder)}

# Compare sets
missing_in_folder = csv_image_ids - folder_image_ ids
extra_in_folder = folder_image_ids - csv_image_ids

# Print summary
print("✅ Dataset Integrity Check Complete:")
print(f" - Total CSV rows: {len(csv_image_ids)}")
print(f" - Total images in folder: {len(folder_image_ids)}")
print(f" - Missing images: {len(missing_in_folder)}")
print(f" - Extra images (not in CSV): {len(extra_in_folder)}")

# Optional: show some missing ones if any
if missing_in_folder:
    print("\n⚠️ Missing image files:")
    print(list(missing_in_folder)[:20])  # show first 20

if extra_in_folder:
    print("\n⚠️ Extra images not listed in CSV:")
    print(list(extra_in_folder)[:20])  # show first 20

if not missing_in_folder and not extra_in_folder:
    print("\n🎯 Everything is perfectly matched!")
