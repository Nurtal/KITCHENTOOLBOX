from Tkinter import *
from Tkinter import StringVar
## TODO:
## -> Redefinir dimmension fenetre => DONE
## -> Tableau avec jours de la semaine => DONE (V1)
## -> Button & trigger a command for the suggestion generation => DONE
## -> Display suggestion in grid : first just try tu update a label (DONE)
##		- update labels from file
##		- run the suggestion generation in the command

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
	label_monday_1.set(str(suggestions["Lundi_midi"]))
	label_monday_2.set(str(suggestions["Lundi_soir"]))
	label_tuesday_1.set(str(suggestions["Mardi_midi"]))
	label_tuesday_2.set(str(suggestions["Mardi_soir"]))
	label_wednesday_1.set(str(suggestions["Mercredi_midi"]))
	label_wednesday_2.set(str(suggestions["Mercredi_soir"]))
	label_thursday_1.set(str(suggestions["Jeudi_midi"]))
	label_thursday_2.set(str(suggestions["Jeudi_soir"]))
	label_friday_1.set(str(suggestions["Vendredi_midi"]))
	label_friday_2.set(str(suggestions["Vendredi_soir"]))
	label_saturday_1.set(str(suggestions["Samedi_midi"]))
	label_saturday_2.set(str(suggestions["Samedi_soir"]))
	label_sunday_1.set(str(suggestions["Dimanche_midi"]))
	label_sunday_2.set(str(suggestions["Dimanche_soir"]))



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


x_margin = 15
y_margin = 15

monday_1 = Label(Frame1, textvariable=label_monday_1)
monday_1.grid(row=0, column=1, padx=x_margin, pady=y_margin)
monday_2 = Label(Frame1, textvariable=label_monday_2)
monday_2.grid(row=1, column=1, padx=x_margin, pady=y_margin)

tuesday_1 = Label(Frame1, textvariable=label_tuesday_1)
tuesday_1.grid(row=0, column=2, padx=x_margin, pady=y_margin)
tuesday_2 = Label(Frame1, textvariable=label_tuesday_2)
tuesday_2.grid(row=1, column=2, padx=x_margin, pady=y_margin)

wednesday_1 = Label(Frame1, textvariable=label_wednesday_1)
wednesday_1.grid(row=0, column=3, padx=x_margin, pady=y_margin)
wednesday_2 = Label(Frame1, textvariable=label_wednesday_2)
wednesday_2.grid(row=1, column=3, padx=x_margin, pady=y_margin)

thursday_1 = Label(Frame1, textvariable=label_thursday_1)
thursday_1.grid(row=0, column=4, padx=x_margin, pady=y_margin)
thursday_2 = Label(Frame1, textvariable=label_thursday_2)
thursday_2.grid(row=1, column=4, padx=x_margin, pady=y_margin)

friday_1 = Label(Frame1, textvariable=label_friday_1)
friday_1.grid(row=0, column=5, padx=x_margin, pady=y_margin)
friday_2 = Label(Frame1, textvariable=label_friday_2)
friday_2.grid(row=1, column=5, padx=x_margin, pady=y_margin)

saturday_1 = Label(Frame1, textvariable=label_saturday_1)
saturday_1.grid(row=0, column=6, padx=x_margin, pady=y_margin)
saturday_2 = Label(Frame1, textvariable=label_saturday_2)
saturday_2.grid(row=1, column=6, padx=x_margin, pady=y_margin)

sunday_1 = Label(Frame1, textvariable=label_sunday_1)
sunday_1.grid(row=0, column=7, padx=x_margin, pady=y_margin)
sunday_2 = Label(Frame1, textvariable=label_sunday_2)
sunday_2.grid(row=1, column=7, padx=x_margin, pady=y_margin)


# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

## Bouton generate suggestion
bouton=Button(fenetre, text="Run", command=update_suggestion_grid)
bouton.pack()


fenetre.mainloop()