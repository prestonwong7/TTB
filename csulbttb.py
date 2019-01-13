# Run this program to run everything

import tkinter as tk # For GUI
import os
import tkinter.font as tkFont

def resource_path(relative_path):
  try:
    base_path = sys._MEIPASS
  except Exception:
   base_path = os.path.abspath(".")
  return os.path.join(base_path, relative_path)

import sign_in as si
import register as re

def start_this_program(true_if_signin, parent):
	pass
	if true_if_signin:
		si.run_gui(parent)
	else:
		re.run_gui(parent)


if __name__ == "__main__":
	# Show button for inventory -> graphic_interface.py
	# Show button for cert check -> cert_chec1_interface.py
	# Show a picture of cerebro
	root = tk.Tk()
	# root.iconbitmap(resource_path('img/icon.ico'))
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.geometry("{}x{}+0+0".format(1000, 1000))
	root.wm_title("CSULB Table Tennis & Badminton Software")
	mainframe = tk.Frame(master=root, background = "#9BE7FF")
	mainframe.pack(side="top", fill="both", expand=True)

	helv36 = tkFont.Font(family='century gothic', size=36, weight='normal')

	title = tk.Label(mainframe, text = "CSULB Table Tennis & Badminton Software")
	title.pack(side="top")
	
	signIn = tk.Button(mainframe, text="Sign In", padx='20', pady='20', font = helv36, borderwidth='5' , background = "#FF4435")
	signIn["command"] = lambda: start_this_program(True, root)
	signIn.pack(side="top")

	register = tk.Button(mainframe, text="Register", padx='20', pady='20', font = helv36, borderwidth='5', background = "#005EC4")
	register["command"] = lambda: start_this_program(False, root)
	register.pack(side='top')

	#the_image = tk.PhotoImage(file=resource_path('img/cerebot.gif'))
	#banner = tk.Label(image=the_image)
	#banner.pack(side="top")

	mainframe.mainloop()
