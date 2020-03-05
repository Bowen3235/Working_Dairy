from tkinter import *
import webbrowser
import PIL
import os
import time

def build( self ):
	self.canvas_list['bg'] = Canvas( self.windows,
		width=300,
		height=700,
		border=0,
		highlightthickness=0
	)
	self.canvas_list['bg'].pack(  )

	## creating option button
	self.canvas_list['option'] = Canvas( self.canvas_list['bg'], 
		width = 50,
		height = 50, 
		bd=0,
		highlightthickness=0,
		offset='0,0',
		#bg='gray'
	)
	for i in range(3):
		self.canvas_list['option'].create_line( 
			0, 15+i*12, 30, 15+i*12,
			width  = 6,
			smooth = True,
			fill   = 'gray'
		)	
	self.canvas_list['option'].grid( column=0,ipadx=0,padx=0,sticky=E+W )

	## creating main canvas
	self.canvas_list['main_area'] = Canvas( self.canvas_list['bg'],
		width=260,
		height=610,
		border=1,
		highlightthickness=1,
		highlightbackground="gray",
		relief=SUNKEN
	)
	self.canvas_list['main_area'].grid( row=1 )
	#for i in self.canvas_list['option'].config():
	#	print( i ,'\t : ' , self.canvas_list['option'].config()[i] )
	#print( self.canvas_list['main_area'].canvasy( 10 ) )


