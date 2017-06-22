from Tkinter import * 

## TODO:
## -> Redefinir dimmension fenetre => DONE
## -> Tableau avec jours de la semaine => DONE (V1)
## -> Button & trigger a command


fenetre = Tk()
fenetre.title("COOK BOT V1")
fenetre['bg']='white'
fenetre.minsize(width=800, height=100)

Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=BOTTOM, padx=30, pady=30)


label = Label(fenetre, text="COOK BOT V1")
label.pack()


## Grid
## -> Never use pack() in a frame where you use grid()

x_margin = 15
y_margin = 15

monday_1 = Label(Frame1, text="Monday 1")
monday_1.grid(row=0, column=1, padx=x_margin, pady=y_margin)
monday_2 = Label(Frame1, text="Monday 2")
monday_2.grid(row=1, column=1, padx=x_margin, pady=y_margin)

tuesday_1 = Label(Frame1, text="Tuesday 1")
tuesday_1.grid(row=0, column=2, padx=x_margin, pady=y_margin)
tuesday_2 = Label(Frame1, text="Tuesday 2")
tuesday_2.grid(row=1, column=2, padx=x_margin, pady=y_margin)

wednesday_1 = Label(Frame1, text="Wednesday 1")
wednesday_1.grid(row=0, column=3, padx=x_margin, pady=y_margin)
wednesday_2 = Label(Frame1, text="Wednesday 2")
wednesday_2.grid(row=1, column=3, padx=x_margin, pady=y_margin)

thursday_1 = Label(Frame1, text="Thursday 1")
thursday_1.grid(row=0, column=4, padx=x_margin, pady=y_margin)
thursday_2 = Label(Frame1, text="Thursday 2")
thursday_2.grid(row=1, column=4, padx=x_margin, pady=y_margin)

friday_1 = Label(Frame1, text="Friday 1")
friday_1.grid(row=0, column=5, padx=x_margin, pady=y_margin)
friday_2 = Label(Frame1, text="Friday 2")
friday_2.grid(row=1, column=5, padx=x_margin, pady=y_margin)

saturday_1 = Label(Frame1, text="Saturday 1")
saturday_1.grid(row=0, column=6, padx=x_margin, pady=y_margin)
saturday_2 = Label(Frame1, text="Saturday 2")
saturday_2.grid(row=1, column=6, padx=x_margin, pady=y_margin)

sunday_1 = Label(Frame1, text="Sunday 1")
sunday_1.grid(row=0, column=7, padx=x_margin, pady=y_margin)
sunday_2 = Label(Frame1, text="Sunday 2")
sunday_2.grid(row=1, column=7, padx=x_margin, pady=y_margin)



# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()


fenetre.mainloop()