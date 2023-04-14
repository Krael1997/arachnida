# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    spider.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abelrodr <abelrodr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 18:23:18 by abelrodr          #+#    #+#              #
#    Updated: 2023/04/14 16:06:49 by abelrodr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import requests
import os

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# ================================ FUNCTIONS ================================== #

def get_extension(url):
	"""
	We get the extension of a file from a URL
	"""
	parsed = urlparse(url)
	root, ext = os.path.splitext(parsed.path)
	return ext.lower()

def download_file(url, file_path):
	"""
	We download a file from a URL and we save in the correct folder.
	"""
	response = requests.get(url, stream=True)
	with open(file_path, 'wb') as f:
		for chunk in response.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)

def get_links(url):
	"""
	We get every links or images content in a website.
	"""
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	links = set()
	for img in soup.find_all('img'):
		src = img.get('src')
		if src:
			link = urljoin(url, src)
			if get_extension(link) in IMG_EXTENSIONS:
				links.add(link)
	return links

def download_recursive(url, level, path):
	"""
	Download recursive the images from a URL and the links what 
	are linked with others URLS with images.
	"""
	if level < 0:
		return
	print(f'Downloading images from {url}...')
	links = get_links(url)
	for link in links:
		filename = os.path.basename(link)
		file_path = os.path.join(path, filename)
		download_file(link, file_path)
		if get_extension(link) not in IMG_EXTENSIONS:
			continue
		sub_links = get_links(link)
		for sub_link in sub_links:
			download_recursive(sub_link, level - 1, path)

# ================================ MAIN ==================================== #

if __name__ == '__main__':
    # Extensiones de imágenes permitidas.
    IMG_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    # Argumentos del programa.
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL del sitio web')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='descarga de forma recursiva las imágenes')
    parser.add_argument('-l', '--level', type=int, default=5,
                        help='nivel profundidad máximo de la descarga recursiva')
    parser.add_argument('-p', '--path', default='./data/',
                        help='ruta donde se guardarán los archivos descargados')
    args = parser.parse_args()

    # Crea el directorio de destino si no existe.
    os.makedirs(args.path, exist_ok=True)

    # Descarga las imágenes.
    if args.recursive:
        download_recursive(args.url, args.level, args.path)
    else:
        print(f'Descargando imágenes de {args.url}...')
        links = get_links(args.url)
        for link in links:
            filename = os.path.basename(link)
            file_path = os.path.join(args.path, filename)
            download_file(link, file_path)