from tkinter import *
import webbrowser
import PIL
import os
import time

def build( self ):
	self.canvas_list['option'] = Canvas( self.windows, 
		width = 50, 
		height = 50, 
		bg='red',
		 )
	self.canvas_list['option'].create_rectangle( 0, 0, 50, 50, fill='red' )
	self.canvas_list['option'].pack( anchor='nw' )
