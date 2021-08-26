from stranice import *
global frames


class GUI(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title('Biblitoka')
        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        meni = Menu(container)
        bm = Menu(meni, tearoff=0)
        bm.add_command(label='Registracija', command=lambda: self.digni_stranicu(Registracija))
        bm.add_command(label='Login', command=lambda: self.digni_stranicu(Login))
        bm.add_separator()
        bm.add_command(label='Zaposli', command=lambda: self.provera_sef(Zaposli))
        bm.add_command(label='Otpusti', command=lambda: self.provera_sef(Otpusti))
        bm.add_separator()
        bm.add_command(label='Izlaz', command=lambda: self.destroy())
        meni.add_cascade(menu=bm, label='Zaposleni')

        km = Menu(meni, tearoff=0)

        km.add_command(label='Izdaj knjigu', command=lambda: self.provera_radnik(IzdajKnjigu))
        km.add_command(label='Vrati knjigu', command=lambda: self.provera_radnik(VratiKnjigu))
        km.add_separator()
        km.add_command(label='Dodaj knjigu', command=lambda: self.provera_radnik(DodajKnjigu))
        km.add_command(label='Izbaci knjigu', command=lambda: self.provera_radnik(IzbaciKnjigu))

        meni.add_cascade(menu=km, label='Knjige')

        Tk.config(self, menu=meni)

        self.display_stranice = {}

        for s in frames:
            stranica = s(container, self)
            self.display_stranice[s] = stranica
            stranica.grid(row=0, column=0, sticky='nwes')

        self.digni_stranicu(Login)

    def digni_stranicu(self, controller):
        stranica = self.display_stranice[controller]
        stranica.tkraise()

    def provera_sef(self, controller):
        if biblioteka.jePrijavljen:
            for radnik in biblioteka.zaposleni:
                if radnik.username == biblioteka.aktivni:
                    if radnik.sef:
                        self.digni_stranicu(controller)

    def provera_radnik(self, controller):
        if biblioteka.jePrijavljen:
            self.digni_stranicu(controller)


BBL = GUI()
BBL.geometry('1200x600')
BBL.mainloop()
