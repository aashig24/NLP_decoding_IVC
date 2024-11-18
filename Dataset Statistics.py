import zipfile

zip_file_path = '/content/Indus-Seal-Dataset-master.zip'

text_count = 0
symbol_count = 0
regular_count = 0

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    for file in zip_ref.namelist():

        if file.endswith('/'):
            continue

        if 'text' in file.lower():
            text_count += 1
        elif 'symbolic' in file.lower():
            symbol_count += 1
        elif file.endswith(('.jpg', '.jpeg', '.png')):
            regular_count += 1


total_images = text_count + symbol_count + regular_count
text_percentage = (text_count / total_images) * 100 if total_images > 0 else 0
symbol_percentage = (symbol_count / total_images) * 100 if total_images > 0 else 0
regular_percentage = (regular_count / total_images) * 100 if total_images > 0 else 0


print("Dataset Analysis:")
print(f"Text Images: {text_count} ({text_percentage:.2f}%)")
print(f"Symbolic Images: {symbol_count} ({symbol_percentage:.2f}%)")
print(f"Regular Images: {regular_count} ({regular_percentage:.2f}%)")
print(f"Total Images: {total_images}")
