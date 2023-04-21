# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abelrodr <abelrodr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/14 16:55:31 by abelrodr          #+#    #+#              #
#    Updated: 2023/04/21 14:35:20 by abelrodr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

__author__ = "abelrodr"
__copyright__ = "Copyright 2023, Cybersec Bootcamp Malaga"
__credits__ = ["abelrodr"]
__email__ = "abelrodr42malaga@gmail.com"

print('''
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌
▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌▐░▌    ▐░▌
▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌
▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌
 ▀▀▀▀▀▀▀▀▀█░▌▐░▌          ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     ▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌
          ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌    ▐░▌▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░▌           ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀ 

                  @((%%%%%%%%%/                    
              @/%%%#       #@/%%@                 
             @@%%            %%%%@                
            /%%%@             @%%%                
           @%@@(@(             //%@               
           @////%%@  @@       &%%%@               
            *%&%%@@#%/        %%%#                
                          #@@@@@&&@               
                    @&&&@#&@%&&@@&&%&&@           
                 @&&&&@@#&@@@@&&%%&&&@@&&@        
               @& @@&&@#&&&&&&&&%%@&&@&&&&@       
             @&&@@&(&#/(((%&&&&%@&&&&&@@  &%(     
          ,&&  @&&&#%##(#(###@@&&&&@@@  #&%#%     
          (@@@@@ ,@@%#####%@@&&&&@@@&@&&&@&@ ,    
            @%&@.#,*@&&&@,*/*@(&&&&@&&@ @&&&&@    
         *%&@   *****@@*(@///*&&&@   &&&@@@@      
       #%#&    @&&&@@&&&@&&&@...@   @/%%#@        
    @##%%#&@     @@@& @# @  @  &   @&%%%&&&@      
    &&@@&%@@.     .@@@@@@&&&&&@ #@#%%%%%@&&@      
    @%%%%#@@@%%%@           @&%&%%%%%%@@@@@       
    @@%%%#@@@@@@&@#@      @%@@@@&@&@@@@@&@@       
     @@@@@@@@  @@@&%&    &&@@,    @@@@@@&%        
        @@@@@%@     @#  #%&    @#&&@@             
             @@&@%@      @@&@@@@                                                                               
''')

import argparse
import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS
import docx
import PyPDF2

def parser_analyzer():
    parser = argparse.ArgumentParser(
        description="Tool for display the metadata.",
        epilog="Project 'arachnida' of Bootcamp CyberSecurity of Fundación 42 (Málaga)."
    )

    parser.add_argument("IMAGE", help="Image for analyze", type=str)
    parser.add_argument("IMAGES", help="Images for analyze.", nargs="*")

    return parser.parse_args()

def scorpion(image_paths):
    for path in image_paths:
        if path.endswith('.pdf') or path.endswith('.docx'):
            file_metadata(path)
        else:
            try:
                imagen = Image.open(path)

            except:
                print(f"We couldnt open {path}.")

            else:
                print(f"{'Name':32}: {imagen.filename.split('/')[-1]}")
                print(f"{'Dimension':32}: {imagen.size[0]}, {imagen.size[1]}")
                print(f"{'Format':32}: {imagen.format}")
                print(f"{'Mode':32}: {imagen.mode}")
                print(f"{'Palette':32}: {imagen.palette}")

                if not imagen.getexif():
                    print(f"{'Exif':32}: {imagen.getexif()}")

                print()
                            
                data = imagen.getexif()
                for id in data:
                    try:
                        name = TAGS.get(id)
                        value = data.get(id)

                        print(f"{name:32}: {value}")

                    except Exception:
                        print(f"Tag {id} not found.")

        print("-" * 80)

def file_metadata(path):
    if path.endswith('.pdf'):
        pdf_metadata(path)
    elif path.endswith('docx'):
        docx_metadata(path)
    else:
        print(f"Unsupported file format for {path}")

def pdf_metadata(file_path):
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        info = reader.metadata
        print(f"{'Title':32}: {info.title}")
        print(f"{'Author':32}: {info.author}")
        print(f"{'Subject':32}: {info.subject}")
        if '/Keywords' in info:
            keywords = info['/Keywords']
            print(f"{'Keywords':32}: {keywords}")
        else:
            print(f"{'Keywords':32}: None")
        print(f"{'Producer':32}: {info.producer}")
        return info

def docx_metadata(file_path):
    doc = docx.Document(file_path)
    core_properties = doc.core_properties
    print(f"{'Title':32}: {core_properties.title}")
    print(f"{'Author':32}: {core_properties.author}")
    print(f"{'Subject':32}: {core_properties.subject}")
    print(f"{'Category':32}: {core_properties.category}")
    print(f"{'Comments':32}: {core_properties.comments}")    
        

if __name__ == "__main__":
    args = parser_analyzer()

    ubications = list()
    ubications.append(args.IMAGE)
    ubications += args.IMAGES

    scorpion(ubications)