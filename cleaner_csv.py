import pandas as pd
import os

# Paths
csv_file = "HAM10000_metadata_filtered.csv"   # your current CSV
images_folder = "HAM10000_images_final"             # folder with remaining images
output_csv = "HAM10000_metadata_synced.csv"   # new synced CSV

# Load the CSV
df = pd.read_csv(csv_file)

# Get available image IDs (without .jpg extension)
available_images = {os.path.splitext(f)[0] for f in os.listdir(images_folder)}

# Keep only rows with image_id that exists in the folder
df_synced = df[df['image_id'].isin(available_images)]

# Save new CSV
df_synced.to_csv(output_csv, index=False)

print(f"✅ CSV synced successfully!")
print(f"Original rows: {len(df)} | Remaining rows: {len(df_synced)}")
print(f"Saved to: {output_csv}")
