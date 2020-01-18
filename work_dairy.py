import tkinter as Tk
import webbrowser
import PIL
import os
import time

Height	= 700
Width	= 300

class Controller(object):
	"""Controller for handling all event"""
	def __init__( self ):
		self.windows = Tk.Tk( )
		self.windows.title( 'WorkingDairy' )
		self.windows.geometry( ('%dx%d+0+0' % (Width, Height)) )
		self.windows.resizable( 0, 0 )
		self.windows.wm_attributes( "-transparent", True )

		self.canvas_list = {}
		self.resource = {}

		from _build import build
		from _bind  import bind

		build(self)
		bind(self)

	def run( self ):
		self.windows.mainloop()
		












def main():
	Con = Controller()
	Con.run()
if __name__ == '__main__':
	main()