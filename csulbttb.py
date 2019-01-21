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
import oneday as od

def start_this_program(true_if_signin, true_if_register, parent):
	pass
	if true_if_signin:
		si.run_gui(parent)
	elif true_if_register:
		re.run_gui(parent)
	else:
		od.run_gui(parent)


if __name__ == "__main__":
	# Show button for inventory -> graphic_interface.py
	# Show button for cert check -> cert_chec1_interface.py
	# Show a picture of cerebro
	root = tk.Tk()
	root.iconbitmap(resource_path('icon.ico'))
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.geometry("{}x{}+0+0".format(1000, 1000))
	root.wm_title("CSULB Table Tennis & Badminton Software")
	mainframe = tk.Frame(master=root, background = "#9BE7FF")
	mainframe.pack(side="top", fill="both", expand=True)
 
	helv36 = tkFont.Font(family='century gothic', size=36, weight='normal')

	title = tk.Label(mainframe, text = "CSULB Table Tennis & Badminton Software", font = helv36)
	title.place(relx = 0.5, rely = 0.1, anchor = 'center')
	
	signIn = tk.Button(mainframe, text="Sign In", padx='20', pady='20', font = helv36, borderwidth='5' , background = "#ff5c33")
	signIn["command"] = lambda: start_this_program(True, False, root)
	signIn.place(relx = 0.5, rely = 0.3, anchor = 'center')

	register = tk.Button(mainframe, text="Register", padx='20', pady='20', font = helv36, borderwidth='5', background = "#80b3ff")
	register["command"] = lambda: start_this_program(False, True, root)
	register.place(relx = 0.5, rely = 0.5, anchor = 'center')

	oneday = tk.Button(mainframe, text="$2 One Day Pass", padx='20', pady='20', font = helv36, borderwidth='5', background = "#80ff80")
	oneday["command"] = lambda: start_this_program(False, False, root)
	oneday.place(relx = 0.5, rely = 0.7, anchor = 'center')
	#the_image = tk.PhotoImage(file=resource_path('img/cerebot.gif'))
	#banner = tk.Label(image=the_image)
	#banner.pack(side="top")

	mainframe.mainloop()
