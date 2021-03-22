'''
Project : Divers helps
Authors: GHANMI Helmi 
Date :  21 March 2021
'''
import pyqrcode 
import png 
import sys, os
from pyqrcode import QRCode 
def generate_qr_code(site_uri, qr_output_file_name):
	'''Generate QR code and save in into png and svg files.

	Args:
		site_uri: the uri of a website
		qr_output_file_name: name without any extention sould be used as files name

	Returns:
		generate and save the QR code in files
	'''

	# Path to store the output_qr_code files
	path_output_files = f'results/{qr_output_file_name}/'
	if not os.path.exists(path_output_files):
		os.makedirs(path_output_files)
	# String which represents the QR code 
	site_uri = site_uri
	# Generate QR code 
	url = pyqrcode.create(site_uri) 
	# Create and save the svg file naming "myqr.svg" 
	url.svg(f"{path_output_files}myqr_{qr_output_file_name}.svg", scale = 8) 
	# Create and save the png file naming "myqr.png" 
	url.png(f"{path_output_files}myqr_{qr_output_file_name}.png", scale = 6) 