# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    spider.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abelrodr <abelrodr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 18:23:18 by abelrodr          #+#    #+#              #
#    Updated: 2023/04/21 14:32:19 by abelrodr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

__author__ = "abelrodr"
__copyright__ = "Copyright 2023, Cybersec Bootcamp Malaga"
__credits__ = ["abelrodr"]
__email__ = "abelrodr42malaga@gmail.com"

print('''
███████╗██████╗ ██╗██████╗ ███████╗██████╗ 
██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
███████╗██████╔╝██║██║  ██║█████╗  ██████╔╝
╚════██║██╔═══╝ ██║██║  ██║██╔══╝  ██╔══██╗
███████║██║     ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

                                                  
              .% &&.@&                            
            #& % @@& @&&&@@&@&@    & &&&          
        %&&@&  &,@&&&%%%%%%%&&&&@@. &@@*% %       
       &,  &%  &&&&%%%%%%%%%&&&%@&@%&&&  &  %     
      %   .@ @@@@@@@@&&&&&&&&&&&%&&&% &@  &  @    
     &(   & @//%*&&@&@,/*@@&&@&&@%@@@ #&   &  */  
     &   @ @@,&*.@&&,,/@&@@&&@@@@&@@@  &.  @   ,  
    @      %@&@@&&&&&@&&@@@&&@@@@*&    @@         
    &           *@@@@             &.    &         
    @                              &    &&        
  &@                                &             
                                     %@%       
''')

import os
import requests
from bs4 import BeautifulSoup
import argparse
from urllib.parse import urlparse

# ========================= DOWNLOAD_IMAGE ================================ #

# Esta función descarga una imagen dada una URL y un directorio de destino. 
# Comienza comprobando si la carpeta de destino ya existe y, si es así, muestra un mensaje de error y sale de la función. 
# Si la carpeta no existe, intenta descargar la imagen utilizando la biblioteca requests. Si la solicitud es exitosa (status code 200), 
# escribe el contenido de la imagen en un archivo y muestra un mensaje de éxito. Si la solicitud no es exitosa, muestra un mensaje de error.


def download_image(url, directory):
    """Función para descargar una imagen dada una URL y un directorio de destino"""
    if os.path.exists(directory):
        print(f"El archivo {directory} ya existe")
        return
    try:
        response = requests.get(url)
        response.raise_for_status()  # Agregar esta línea para detectar errores de solicitud
        with open(directory, 'wb') as f:
            f.write(response.content)
        print(f"Archivo {url} descargado correctamente en {directory}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar {url}: {e}")
    except Exception as e:
        print(f"Ocurrió un error al descargar {url}: {e}")

# ========================= DOWNLOAD_IMAGE ================================ #

# ====================== DOWNLOAD_RECURSIVE =============================== #

# Esta funcion descarga recursivamente todas las imágenes de un sitio web dado. 
# Comienza comprobando si la URL ha sido visitada anteriormente. Si es así o si se ha alcanzado la profundidad máxima de recursión, sale de la función. 
# Si no, agrega la URL a la lista de URLs visitadas y descarga todas las imágenes que encuentra en la página utilizando la función `download_image()`.
# Además, la función busca todos los enlaces (`<a>`) en la página y descarga recursivamente todas las imágenes en los enlaces que apuntan a otras páginas si se cumplen ciertas condiciones. 
# En particular, la función solo seguirá los enlaces que comienzan con `http` y que no han sido visitados anteriormente.


def download_recursive(url, max_depth, directory, visited_urls=None):
    """Función para descargar de forma recursiva todas las imágenes de un sitio web dado"""
    if visited_urls is None:
        visited_urls = set()
    if max_depth == 0 or url in visited_urls:
        return
    visited_urls.add(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            for img in soup.find_all('img'):
                img_url = img.get('src')
                if img_url and (img_url.endswith('.jpg') or img_url.endswith('.jpeg') or img_url.endswith('.png') or img_url.endswith('.gif') or img_url.endswith('.bmp')):
                    img_name = os.path.basename(img_url)
                    img_dir = os.path.join(directory, img_name)
                    download_image(img_url, img_dir)
            for link in soup.find_all('a'):
                link_url = link.get('href')
                if link_url is None:
                    continue
                if link_url.startswith('http') and link_url not in visited_urls:
                    download_recursive(link_url, max_depth-1, directory, visited_urls)
    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a {url}: {e}")
    except Exception as e:
        print(f"Ocurrió un error al acceder a {url}: {e}")

# ====================== DOWNLOAD_RECURSIVE =============================== #

# ============================== MAIN ===================================== #

# main(), es la función principal. 
# Utiliza la biblioteca argparse para analizar los argumentos de la línea de comandos y descargar imágenes de un sitio web dado utilizando la función download_recursive(). 
# La función principal recibe como argumentos la URL del sitio web, el nivel máximo de profundidad de descarga recursiva, el directorio de destino de las imágenes descargadas y una bandera para indicar si se desea descargar de forma recursiva todas las imágenes.

def main():
    try:
        parser = argparse.ArgumentParser(description='Descarga imágenes de un sitio web recursivamente.')
        parser.add_argument('url', metavar='URL', type=str, help='URL del sitio web')
        parser.add_argument('-r', action='store_true', help='Descarga de forma recursiva todas las imágenes')
        parser.add_argument('-l', type=int, default=5, help='Nivel máximo de profundidad de descarga recursiva')
        parser.add_argument('-p', type=str, default='./data/', help='Directorio de destino de las imágenes descargadas')
        args = parser.parse_args()

        url = args.url
        recursive = args.r
        max_depth = args.l
        directory = args.p

        if os.path.exists(url):
            # Es una ruta local
            if not os.path.isdir(url):
                print("La ruta debe ser un directorio")
                return
            if recursive:
                for root, dir, files in os.walk(url):
                    for file in files:
                        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                            img_url = os.path.join(root, file)
                            img_name = os.path.basename(img_url)
                            img_dir = os.path.join(directory, img_name)
                            download_image(img_url, img_dir)
            else:
                for file in os.listdir(url):
                    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                        img_url = os.path.join(url, file)
                        img_name = os.path.basename(img_url)
                        img_dir = os.path.join(directory, img_name)
                        download_image(img_url, img_dir)
        else:
            # Es una dirección web
            if not url.startswith('http'):
                print("La URL debe comenzar con http o https")
                return

            if not os.path.exists(directory):
                os.makedirs(directory)

            if recursive:
                download_recursive(url, max_depth, directory)
            else:
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    for img in soup.find_all('img'):
                        img_url = img.get('src')
                        if img_url and (img_url.endswith('.jpg') or img_url.endswith('.jpeg') or img_url.endswith('.png') or img_url.endswith('.gif') or img_url.endswith('.bmp')):
                            img_name = os.path.basename(img_url)
                            img_dir = os.path.join(directory, img_name)
                            download_image(img_url, img_dir)
                else:
                    print(f"Error al acceder a {url}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == '__main__':
    main()

# ============================== MAIN ===================================== #