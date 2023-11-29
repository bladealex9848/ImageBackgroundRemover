import streamlit as st
from PIL import Image
from rembg import remove
import io

# Configuración de la página de Streamlit para tu aplicación
st.set_page_config(
    page_title="Removedor de Fondo de Imágenes", 
    page_icon="🖼️",  # Puedes cambiar esto por un ícono que prefieras
    initial_sidebar_state='collapsed',
    # layout="wide",
    menu_items={
        'Get Help': 'https://isabellaea.com',  # Coloca aquí el enlace de tu preferencia
        'Report a bug': None,  # Puedes dejarlo como None o poner un enlace para reportar errores
        'About': "Removedor de Fondo de Imágenes te permite eliminar el fondo de tus imágenes de manera fácil y rápida."
    }
)

# Título y presentación de la aplicación
st.title('Removedor de Fondo de Imágenes')
st.write("""
Esta aplicación utiliza la tecnología de `rembg` para eliminar el fondo de tus imágenes.
Simplemente carga una imagen y deja que la magia suceda. Después de procesarla, podrás descargar la imagen sin fondo.
""")

# Subida de archivos
uploaded_file = st.file_uploader("Elige una imagen para eliminar el fondo", type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    # Mostrar información del archivo cargado
    st.write("Archivo cargado: ", uploaded_file.name)
    
    image = Image.open(uploaded_file)
    # Mostrar la imagen original
    st.image(image, caption='Imagen Original', use_column_width=True)
    
    # Proceso de eliminación del fondo
    output_image = remove(image)
    
    # Mostrar la imagen resultante
    st.image(output_image, caption='Imagen sin Fondo', use_column_width=True)
    
    # Preparar la imagen para descargar
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte = buf.getvalue()

    # Crear el nombre del archivo de salida
    output_filename = uploaded_file.name.rsplit('.', 1)[0] + '_rbg.png'

    # Botón de descarga
    st.download_button(
        label="Descargar imagen sin fondo",
        data=byte,
        file_name=output_filename,
        mime="image/png",
    )
    
# Footer
st.sidebar.markdown('---')
st.sidebar.subheader('Creado por:')
st.sidebar.markdown('Alexander Oviedo Fadul')
st.sidebar.markdown("[GitHub](https://github.com/bladealex9848) | [Website](https://alexander.oviedo.isabellaea.com/) | [Instagram](https://www.instagram.com/alexander.oviedo.fadul) | [Twitter](https://twitter.com/alexanderofadul) | [Facebook](https://www.facebook.com/alexanderof/) | [WhatsApp](https://api.whatsapp.com/send?phone=573015930519&text=Hola%20!Quiero%20conversar%20contigo!%20)")