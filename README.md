# arachnida
# Cyber42-arachnida

*** PARA VER LA OPCION CON LOS CODIGOS COMENTADOS Y EN ESPAÑOL PUEDES ENTRAR EN EL SIGUIENTE LINK ***
*** **https://bird-cricket-e45.notion.site/Arachnida-6ea1126355d245f59655da1500ee9a62** **

## Spider.py ##

This Python script allows you to download images from a website, either directly or recursively to a specified depth. The script uses the argparse library to parse the command-line arguments and the requests and BeautifulSoup libraries to download and parse the website content.

# Usage

  	python3 download_images.py <url> [-r] [-l <depth>] [-p <path>]

	<url>: Required argument to specify the URL of the website from which to download the images.

	-r, --recursive: Optional flag to specify if the images should be downloaded recursively from all linked pages.

	-l <depth>, --level <depth>: Optional argument to specify the maximum depth of recursive downloads. Default is 5.

	-p <path>, --path <path>: Optional argument to specify the directory path where the downloaded images will be stored. Default is ./data/.
		
# Functions

	get_extension(url): Extracts the file extension from a URL.

	download_file(url, file_path): Downloads a file from a URL and saves it to the specified file path.

	get_links(url): Returns a set of all links to images on a given webpage.

	download_recursive(url, level, path): Recursively downloads all images from a website and any linked pages up to the specified depth.
		
# Examples
	
	To download all images from the website http://example.com to the ./data/ directory, run:
		
		python3 download_images.py http://example.com -p ./data/
		
	To download all images from the website http://example.com and any linked pages up to a depth of 3, run:

		python3 download_images.py http://example.com -r -l 3 -p ./data/
