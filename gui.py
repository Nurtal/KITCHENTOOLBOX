from Tkinter import *
from Tkinter import StringVar
## TODO:
## [DONE]-> Redefinir dimmension fenetre => DONE
## [DONE]-> Tableau avec jours de la semaine => DONE (V1)
## [DONE]-> Button & trigger a command for the suggestion generation => DONE
## [DONE]-> Display suggestion in grid => DONE
##		- update labels from file => DONE
##		- run the suggestion generation in the command => DONE
## [DONE]-> Lock part of the solution with a checkbox
## -> Smart suggestion (i.e do not authorized same receipe the same day)
## -> Define xml template for receipe
## -> update index of receipe with receipes files
## -> web crawler to create new receipes
## -> receipe manager
## -> Add image for suggestions
## -> Fixe thz size of the window
## -> Replace the button


## Importation
import planner




## function
def update_suggestion_grid():
	"""
	-> Generate the suggestions
	-> Write the suggestion in the grid
	"""
	## Generate Suggestion
	suggestions = planner.generate_suggestion()

	## Update the grid
	if(not check_status_monday_1.get()):
		label_monday_1.set(str(suggestions["Lundi_midi"]))
	if(not check_status_monday_2.get()):
		label_monday_2.set(str(suggestions["Lundi_soir"]))
	if(not check_status_tuesday_1.get()):
		label_tuesday_1.set(str(suggestions["Mardi_midi"]))
	if(not check_status_tuesday_2.get()):
		label_tuesday_2.set(str(suggestions["Mardi_soir"]))
	if(not check_status_wednesday_1.get()):
		label_wednesday_1.set(str(suggestions["Mercredi_midi"]))
	if(not check_status_wednesday_2.get()):
		label_wednesday_2.set(str(suggestions["Mercredi_soir"]))
	if(not check_status_thursday_1.get()):
		label_thursday_1.set(str(suggestions["Jeudi_midi"]))
	if(not check_status_thursday_2.get()):
		label_thursday_2.set(str(suggestions["Jeudi_soir"]))
	if(not check_status_friday_1.get()):
		label_friday_1.set(str(suggestions["Vendredi_midi"]))
	if(not check_status_friday_2.get()):
		label_friday_2.set(str(suggestions["Vendredi_soir"]))
	if(not check_status_saturday_1.get()):
		label_saturday_1.set(str(suggestions["Samedi_midi"]))
	if(not check_status_saturday_2.get()):
		label_saturday_2.set(str(suggestions["Samedi_soir"]))
	if(not check_status_sunday_1.get()):
		label_sunday_1.set(str(suggestions["Dimanche_midi"]))
	if(not check_status_sunday_2.get()):
		label_sunday_2.set(str(suggestions["Dimanche_soir"]))


def test_check_box():
	"""
	just for test
	"""

	print check_state.get()


fenetre = Tk()
fenetre.title("COOK BOT V1")
fenetre['bg']='white'
fenetre.minsize(width=800, height=100)

Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=BOTTOM, padx=30, pady=30)

labelText = StringVar()
labelText.set("Falcon")
label = Label(fenetre, textvariable=labelText)
label.pack()

check_state = IntVar()
bouton = Checkbutton(fenetre, text="Keep", variable=check_state)
bouton.pack()


## Grid
## -> Never use pack() in a frame where you use grid()

label_monday_1 = StringVar()
label_monday_2 = StringVar()
label_tuesday_1 = StringVar()
label_tuesday_2 = StringVar()
label_wednesday_1 = StringVar()
label_wednesday_2 = StringVar()
label_thursday_1 = StringVar()
label_thursday_2 = StringVar()
label_friday_1 = StringVar()
label_friday_2 = StringVar()
label_saturday_1 = StringVar()
label_saturday_2 = StringVar()
label_sunday_1 = StringVar()
label_sunday_2 = StringVar()

check_status_monday_1 = IntVar()
check_status_monday_2 = IntVar()
check_status_tuesday_1 = IntVar()
check_status_tuesday_2 = IntVar()
check_status_wednesday_1 = IntVar()
check_status_wednesday_2 = IntVar()
check_status_thursday_1 = IntVar()
check_status_thursday_2 = IntVar()
check_status_friday_1 = IntVar()
check_status_friday_2 = IntVar()
check_status_saturday_1 = IntVar()
check_status_saturday_2 = IntVar()
check_status_sunday_1 = IntVar()
check_status_sunday_2 = IntVar()



x_margin = 15
y_margin = 15

monday_1 = Label(Frame1, textvariable=label_monday_1)
monday_1.grid(row=0, column=1, padx=x_margin, pady=y_margin)
checkbox_monday_1 = Checkbutton(Frame1, text="Garder", variable=check_status_monday_1)
checkbox_monday_1.grid(row=1, column=1, padx=x_margin, pady=y_margin)
monday_2 = Label(Frame1, textvariable=label_monday_2)
monday_2.grid(row=2, column=1, padx=x_margin, pady=y_margin)
checkbox_monday_2 = Checkbutton(Frame1, text="Garder", variable=check_status_monday_2)
checkbox_monday_2.grid(row=3, column=1, padx=x_margin, pady=y_margin)

tuesday_1 = Label(Frame1, textvariable=label_tuesday_1)
tuesday_1.grid(row=0, column=2, padx=x_margin, pady=y_margin)
checkbox_tuesday_1 = Checkbutton(Frame1, text="Garder", variable=check_status_tuesday_1)
checkbox_tuesday_1.grid(row=1, column=2, padx=x_margin, pady=y_margin)
tuesday_2 = Label(Frame1, textvariable=label_tuesday_2)
tuesday_2.grid(row=2, column=2, padx=x_margin, pady=y_margin)
checkbox_tuesday_2 = Checkbutton(Frame1, text="Garder", variable=check_status_tuesday_2)
checkbox_tuesday_2.grid(row=3, column=2, padx=x_margin, pady=y_margin)

wednesday_1 = Label(Frame1, textvariable=label_wednesday_1)
wednesday_1.grid(row=0, column=3, padx=x_margin, pady=y_margin)
checkbox_wednesday_1 = Checkbutton(Frame1, text="Garder", variable=check_status_wednesday_1)
checkbox_wednesday_1.grid(row=1, column=3, padx=x_margin, pady=y_margin)
wednesday_2 = Label(Frame1, textvariable=label_wednesday_2)
wednesday_2.grid(row=2, column=3, padx=x_margin, pady=y_margin)
checkbox_wednesday_2 = Checkbutton(Frame1, text="Garder", variable=check_status_wednesday_2)
checkbox_wednesday_2.grid(row=3, column=3, padx=x_margin, pady=y_margin)

thursday_1 = Label(Frame1, textvariable=label_thursday_1)
thursday_1.grid(row=0, column=4, padx=x_margin, pady=y_margin)
checkbox_thursday_1 = Checkbutton(Frame1, text="Garder", variable=check_status_thursday_1)
checkbox_thursday_1.grid(row=1, column=4, padx=x_margin, pady=y_margin)
thursday_2 = Label(Frame1, textvariable=label_thursday_2)
thursday_2.grid(row=2, column=4, padx=x_margin, pady=y_margin)
checkbox_thursday_2 = Checkbutton(Frame1, text="Garder", variable=check_status_thursday_2)
checkbox_thursday_2.grid(row=3, column=4, padx=x_margin, pady=y_margin)

friday_1 = Label(Frame1, textvariable=label_friday_1)
friday_1.grid(row=0, column=5, padx=x_margin, pady=y_margin)
checkbox_friday_1 = Checkbutton(Frame1, text="Garder", variable=check_status_friday_1)
checkbox_friday_1.grid(row=1, column=5, padx=x_margin, pady=y_margin)
friday_2 = Label(Frame1, textvariable=label_friday_2)
friday_2.grid(row=2, column=5, padx=x_margin, pady=y_margin)
checkbox_friday_2 = Checkbutton(Frame1, text="Garder", variable=check_status_friday_2)
checkbox_friday_2.grid(row=3, column=5, padx=x_margin, pady=y_margin)

saturday_1 = Label(Frame1, textvariable=label_saturday_1)
saturday_1.grid(row=0, column=6, padx=x_margin, pady=y_margin)
checkbox_saturday_1 = Checkbutton(Frame1, text="Garder", variable=check_status_saturday_1)
checkbox_saturday_1.grid(row=1, column=6, padx=x_margin, pady=y_margin)
saturday_2 = Label(Frame1, textvariable=label_saturday_2)
saturday_2.grid(row=2, column=6, padx=x_margin, pady=y_margin)
checkbox_saturday_2 = Checkbutton(Frame1, text="Garder", variable=check_status_saturday_2)
checkbox_saturday_2.grid(row=3, column=6, padx=x_margin, pady=y_margin)

sunday_1 = Label(Frame1, textvariable=label_sunday_1)
sunday_1.grid(row=0, column=7, padx=x_margin, pady=y_margin)
checkbox_sunday_1 = Checkbutton(Frame1, text="Garder", variable=check_status_sunday_1)
checkbox_sunday_1.grid(row=1, column=7, padx=x_margin, pady=y_margin)
sunday_2 = Label(Frame1, textvariable=label_sunday_2)
sunday_2.grid(row=2, column=7, padx=x_margin, pady=y_margin)
checkbox_sunday_2 = Checkbutton(Frame1, text="Garder", variable=check_status_sunday_2)
checkbox_sunday_2.grid(row=3, column=7, padx=x_margin, pady=y_margin)

# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

## Bouton generate suggestion
bouton=Button(fenetre, text="Run", command=update_suggestion_grid)
bouton.pack()

## Bouton test
bouton=Button(fenetre, text="Test", command=test_check_box)
bouton.pack()


fenetre.mainloop()