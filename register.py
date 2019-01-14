import tkinter as tk
import tkinter.ttk as ttk
import datetime
import time
import sys
import google_sheet_log as gslog
import tkinter.font as tkFont
# from asana_automate import main

import os
import sign_in as si
from tkinter import *

def resource_path(relative_path):
  try:
    base_path = sys._MEIPASS
  except Exception:
   base_path = os.path.abspath(".")
  return os.path.join(base_path, relative_path)

# The main window (sans popups) is an extension of a TK frame
# This class houses all of the GUI widgets
class Application(tk.Frame):

	# Initilizes scroll bar, auto resizing
	# Calls populate function to create vendor entry widgets
	def __init__(self, master=None):

		self.master = master

		super().__init__(master)
		self.canvas = tk.Canvas(master, borderwidth=0, background="#9BE7FF")
		self.mainframe = tk.Frame(self.canvas, background="#ffffff")
		self.vsb = tk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.vsb.set)

		self.vsb.pack(side="right", fill="y")
		self.canvas.pack(side="left", fill="both", expand=True)
		self.canvas.create_window((4,4), window=self.mainframe, anchor="ne", 
									tags="self.mainframe")

		self.mainframe.bind("<Configure>", self.onFrameConfigure)

		self.populate(self.mainframe)
	
	def onMouseWheel(self, event):
		if (self.mainframe.winfo_height() <= self.master.winfo_height()):
			self.mainframe.unbind_all("<MouseWheel>")
		self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

	def onFrameConfigure(self, event):
		'''Reset the scroll region to encompass the inner frame'''
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))

	# Vendor Info Frame, with entry to input number of HDDS
	def populate(self, mainframe):

		# self.embed_logo(mainframe)
		# rows 0-2, cols 10-14 size 1x3
		self.autofill_today_in_date(mainframe)
		self.member_input(mainframe)
		self.back_button(mainframe)
		self.register_button(mainframe)
		# self.make_separator_at_row(4)
		self.start_time = time.time()

	# # Adding a personal touch
	# def embed_logo(self, f):
	# 	self.logo = tk.PhotoImage(file=resource_path("img/hitlogo.gif"))
	# 	self.logo_label = tk.Label(f, image=self.logo)
	# 	self.logo_label.grid(row=0, column=7, rowspan=3, columnspan=3)


	# GUI has ENTRY for technician which calls the ec.validate_technician function
	def member_input(self, f):
		
		self.member_input = tk.Label(f, text="Enter your full name: ")
		self.member_entry = tk.Entry(f, width=30)

		self.member_input.grid(row=1, column=2, columnspan=3, padx=(150, 5), pady=5)
		self.member_entry.grid(row=2, column=2, columnspan=6, padx=(150, 5), pady=5)
		# self.func(self.variable)
		# self.technician_input_entry.grid(row=0, column=11, columnspan=3, padx=5, pady=5)	

	def func(self, value):
		self.member_input_entry = self.variable.get()
		self.member = self.member_input_entry
		print("tech entry", self.member_input_entry)

	# GUI autofills today's date
	def autofill_today_in_date(self, f):
		self.autofill_today_label = tk.Label(f, text="Today's Date: ")
		self.autofill_today_date = tk.Label(f, text=datetime.datetime.now().strftime("%m/%d/%y"))
		self.autofill_today_label.grid(row=3, column=2, columnspan=3, padx=(150, 5), pady=5)
		self.autofill_today_date.grid(row=3, column=5, columnspan=3, padx=5, pady=5)

	# def make_separator_at_row(self, r):
	# 	ttk.Separator(self.mainframe ,orient=tk.HORIZONTAL).grid(row=r, column=0, columnspan=14, sticky='ew', pady=20)

	#creates back button interface
	def back_button(self,f):
		self.back_button = tk.Radiobutton(f, text="Back", indicatoron=0, value="Back", padx = 50, command = lambda : self.main_menu(f))
		self.back_button.grid(row=0, column=0)

	def register_button(self, f):
		self.register_button = tk.Button(f, text="Register")
		self.register_button["command"] = lambda: self.run_logic()
		self.register_button.grid(row=8, column=2, columnspan=5, pady=(20, 20), sticky='ew')

	#Caleed from ONLY the back button
	def main_menu(self, master):
		self.master.destroy()
		root = tk.Tk()
		# root.iconbitmap(resource_path('img/icon.ico'))
		w, h = root.winfo_screenwidth(), root.winfo_screenheight()
		root.geometry("{}x{}+0+0".format(1000, 1000))
		root.wm_title("CSULB Table Tennis & Badminton")
		mainframe = tk.Frame(master=root, background = "#9BE7FF")
		mainframe.pack(side="top", fill="both", expand=True)

		helv36 = tkFont.Font(family='century gothic', size=36, weight='normal')

		title = tk.Label(mainframe, text = "CSULB Table Tennis & Badminton Software", font = helv36)
		title.place(relx = 0.5, rely = 0.1, anchor = 'center')
		
		signIn = tk.Button(mainframe, text="Sign In", padx='20', pady='20', font = helv36, borderwidth='5' , background = "#ff5c33")
		signIn["command"] = lambda: self.start_this_program(True, root)
		signIn.place(relx = 0.5, rely = 0.3, anchor = 'center')

		register = tk.Button(mainframe, text="Register", padx='20', pady='20', font = helv36, borderwidth='5', background = "#80b3ff")
		register["command"] = lambda: self.start_this_program(False, root)
		register.place(relx = 0.5, rely = 0.5, anchor = 'center')

	#USED FOR BACK BUTTON in main_menu
	def start_this_program(self, true_if_signin, parent):
		if true_if_signin:
			si.run_gui(parent)
		else:
			run_gui(parent)
	
	# Called by the run button
	# Makes various calls to functions in error_check.py
	def run_logic(self):
		self.p = lambda: self.make_log(self.p)
			
	
	def api_hooks(self, top):
		top.destroy()

	def dummy(self, top):
		print("Dummy function")
		top.destroy()

	def kill_program(self, p):
		self.quit()
		p.destroy()


	def make_log(self, top):
		# self.automatic_program_log = [[
		# 	"SUCCESS", 
		# 	str(datetime.datetime.now()), 
		# 	str(self.NUM_HDDS), 
		# 	self.technician, 
		# 	str(round(time.time() - self.start_time, 2)), 
		# 	str(ec.num_errors)
		# ]]
		print("Time is ",str(round(time.time() - self.start_time, 2)))
		#Now I'm going to call this
		gslog.main()


## Below three custom popup classes to call

class WarningPopup(tk.Toplevel):
	def __init__(self, message):
		super().__init__()
		self.attributes("-topmost", True)
		self.focus_force()
		self.grab_set()
		self.title="WARNING"
		self.msg = tk.Message(self, text=message)
		self.msg.pack()
		self.button = tk.Button(self, text="Dismiss", command=self.destroy)
		self.button.pack()

# Constructor that creates the main window object
def run_gui(parent):
	# print(resource_path('img/icon.ico'))
	parent.destroy()
	root = tk.Tk()
	# root.iconbitmap(resource_path('img/icon.ico'))
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	#root.geometry("{}x{}+0+0".format(w, h))
	root.geometry("{}x{}+0+0".format(850, h-500))
	root.wm_title("Register")
	app = Application(master=root)
	app.pack(side="top", fill="both", expand=True)
	app.mainloop()