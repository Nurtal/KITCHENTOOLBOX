from Tkinter import * 

fenetre = Tk()
fenetre.title("COOK BOT V1")
fenetre['bg']='white'



label = Label(fenetre, text="COOK BOT V1")
label.pack()

# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()


fenetre.mainloop()