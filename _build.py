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
	self.canvas_list['option'] = Canvas( self.windows, 
		width = 50, 		height = 50, 
		border=0,
		highlightthickness=0
	)
	for i in range(3):
		self.canvas_list['option'].create_line( 
			10, 15+i*12, 40, 15+i*12,
			width  = 6,
			smooth = True,
			fill   = 'gray'
		)	
	self.canvas_list['option'].place( x=0, y=0, anchor='nw' )

	## creating main canvas
	self.canvas_list['main_area'] = Canvas( self.windows,

		)

