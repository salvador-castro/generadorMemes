import os
from functions import add_text_to_image

def main():
    # Crear carpetas si no existen
    os.makedirs("images", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    
    image_path = input("Ingrese el nombre de la imagen en la carpeta 'images': ")
    text = input("Ingrese el texto del meme: ")
    output_name = input("Ingrese el nombre del archivo de salida: ")
    
    image_path = os.path.join("images", image_path)
    output_path = os.path.join("output", output_name)
    
    if not os.path.exists(image_path):
        print("Error: La imagen no existe en la carpeta 'images'.")
        return
    
    add_text_to_image(image_path, text, output_path)
    print(f"Meme guardado en {output_path}")