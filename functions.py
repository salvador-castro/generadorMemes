from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, text, output_path):
    try:
        # Abrir la imagen
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        
        # Cargar una fuente predeterminada
        try:
            font = ImageFont.truetype("arial.ttf", 36)
        except IOError:
            font = ImageFont.load_default()
        
        # Obtener dimensiones de la imagen
        width, height = image.size
        
        # Determinar la posición del texto
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        x = (width - text_width) / 2
        y = height - text_height - 20
        
        # Agregar el texto
        draw.text((x, y), text, font=font, fill="white")
        
        # Guardar la imagen editada
        image.save(output_path)
        print("Meme generado correctamente.")
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")