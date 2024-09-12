import shutil
import os

files=[r'R:\01_renderkitchen\03_bibliotheken\007 Software\KRPano\Renderkitchen Add-ons\Override files\vtourskin.xml',r'R:\01_renderkitchen\03_bibliotheken\007 Software\KRPano\Renderkitchen Add-ons\Override files\vtourskin_design_ultra_light.xml',r'R:\01_renderkitchen\03_bibliotheken\007 Software\KRPano\Renderkitchen Add-ons\Override files\vtourskin_hotspot.png']


def copier(file):
	source= file
	distenation=os.getcwd()+r'\skin'
	shutil.copy(source,distenation)

for file in files:
	copier(file)


print('copy successful!')


newtxt=''
safetytxt=''

with open('tour.xml','r') as file:
	mytxt=file.read()
	safetytxt=mytxt

	original=['<!-- <include url="skin/vtourskin_design_ultra_light.xml" /> -->','design_bgcolor="0x2D3E50"','design_bgalpha="0.8"','design_bgroundedge="1"']
	target= ['<include url="skin/vtourskin_design_ultra_light.xml" />','design_bgcolor="0xFFFFFF"','design_bgalpha="0.2"','design_bgroundedge="50"']


	for i in range(len(original)):
		mytxt=mytxt.replace(original[i],target[i])
		

	newtxt=mytxt

with open('tour.xml','w') as file:
	file.write(newtxt)

with open('tour_safety.xml','w') as file:
	file.write(safetytxt)


print('new file created')