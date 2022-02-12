# imports
import streamlit as st
import numpy as np
import os
import time
#import cv2
timestr = time.strftime('%Y-%m-%d-%H:%M:%S')


# Para gerar o QR_code
import qrcode
from PIL import Image


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=10, border=14)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


# Function to load Image
def load_image(img):
    im = Image.open(img)
    return im

#Aplicação
def main():
    menu = ['Home', 'Decoder','Sobre']

    choice = st.sidebar.selectbox('Menu',menu)


    st.title('Gerador de QR_Code')
    if choice == 'Home':
        #st.subheader('Home')

        # entrada de dados
        with st.form(key='myqr_form'):
            raw_text = st.text_input('Escreva ou cole o endereço do conteúdo.... ')
            name_image = st.text_input('Escreva o nome  para salvar sua imagem...')
            submit_button = st.form_submit_button('Gerar QR_Code')
        if submit_button:
            col1,col2 = st.columns(2)
            with col1:
                # add data
                qr.add_data(raw_text)
                # generate
                qr.make(fit=True)
                img = qr.make_image(fill_color='black', back_color='white')

                # Filename
                img_filename = name_image+'_{}.png'.format(timestr)
                path_for_images = os.path.join('images', img_filename)
                img.save(path_for_images)

                final_img = load_image(path_for_images)
                st.image(final_img)
            with col2:
                st.info('Texto Original')
                st.write(raw_text)
    elif choice == 'Decoder':
        st.subheader('Decoder')
        st.write('Em construção')
        
    #
    #     image_file = st.file_uploader('Upload Image', type=['jpg','png','jpeg'])
    #     if image_file is not None:
    #         # Method 1: Display Image
    #         img = load_image(image_file)
    #         #st.image(img)
    #
    #         # Method 2: Using opencv
    #         # file_bytes = np.asanyarray(bytearray(image_file.read()),dtype=np.uint8)
    #         # opencv_image = cv2.imdecode(file_bytes,1)
    #
    #         c1,c2 = st.columns(2)
    #         with c1:
    #              st.image(img)
    #         #
    #         with c2:
    #              st.info('QR Code Decodificado')
    #         #     det = cv2.QRCodeDetector()
    #         #     retval,points,straight_qrcode = det.detectAndDecode(opencv_image)
    #         #
    #         #     # Retval is for the text
    #              st.write(raw_text)
    #
    #         #st.image(opencv_image)
    else:
        st.subheader('Sobre')
        st.write('Em construção')


if __name__ == '__main__':
    main()