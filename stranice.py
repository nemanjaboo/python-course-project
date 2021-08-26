from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from klase import biblioteka
from klase import Zaposleni
from klase import Knjiga

title_font = 'Cambria 20 bold'
pozadina = '#D6D6D6'
label_font = 'Cambria 15 '


class PocetnaStranica(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg=pozadina)
        Label(self, text='Dobrodosli u Biblioteku', font='Cambria 30 bold', bg=pozadina, fg='black').pack(pady=230)


class Registracija(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg=pozadina)
        Label(self, text='Registracija', bg=pozadina, font=title_font, fg='black').pack(pady=3)
        w = Canvas(self, width=1200, height=1)
        w.pack(pady=20)
        w.create_line(0, 0, 300, 300)

        lime_prezime = Label(self, text='Ime i Prezime', bg=pozadina, font=label_font, fg='black').pack()
        entryime = Entry(self)
        entryime.pack(pady=3)

        ljmbg = Label(self, text='JMBG', bg=pozadina, font=label_font, fg='black').pack()
        entryjmbg = Entry(self)
        entryjmbg.pack()

        ltel = Label(self, text='Broj telefona: ', bg=pozadina, font=label_font, fg='black').pack()
        etel = Entry(self)
        etel.pack()

        ldip = Label(self, text='Diploma: ', bg=pozadina, font=label_font, fg='black').pack()
        edip = Entry(self)
        edip.pack()

        lusername = Label(self, text='username', bg=pozadina, font=label_font, fg='black').pack()
        entryusername = Entry(self)
        entryusername.pack()

        lpassword = Label(self, text='password', bg=pozadina, font=label_font, fg='black').pack()
        entrypassword = Entry(self)
        entrypassword.pack()

        regbutton = ttk.Button(self, text='Registruj se', command=lambda: registracija(entryime.get(), entryjmbg.get(),
                                                                                       etel.get(), edip.get(),
                                                                                       entryusername.get(),
                                                                                       entrypassword.get(), False))
        regbutton.pack(pady=10)

        def registracija(imeprezime, matbroj, tel, degree, korime, lozinka, boss):
            polja_registracije = [entryime.get(), entryjmbg.get(), etel.get(), edip.get(), entryusername.get(),
                                  entrypassword.get()]
            for i in polja_registracije:
                if i == '' or i == ' ':
                    messagebox.showerror(title='Greska', message='Sva polja moraju biti popunjena!')
                    entryime.delete(0, END)
                    entryjmbg.delete(0, END)
                    etel.delete(0, END)
                    edip.delete(0, END)
                    entryusername.delete(0, END)
                    entrypassword.delete(0, END)
                    return
            try:
                biblioteka.registracija_zaposlenog(imeprezime, matbroj, tel, degree, korime, lozinka, boss)
                messagebox.showinfo(title='Info', message='Uspesna registracija!')
                entryime.delete(0, END)
                entryjmbg.delete(0, END)
                etel.delete(0, END)
                edip.delete(0, END)
                entryusername.delete(0, END)
                entrypassword.delete(0, END)
            except:
                messagebox.showerror(title='Greska', message='Korisnik vec postoji')


class Login(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg=pozadina)
        Label(self, text='Login', bg=pozadina, font=title_font, fg='black').pack(pady=3)
        w = Canvas(self, width=1200, height=1)
        w.pack(pady=20)
        w.create_line(0, 0, 300, 300)

        lkor_ime = Label(self, text='username', bg=pozadina, font=label_font, fg='black').pack()
        ekor_ime = Entry(self)
        ekor_ime.pack(pady=10)

        lpass = Label(self, text='password', bg=pozadina, font=label_font, fg='black').pack()
        epass = Entry(self, show='*')
        epass.pack(pady=10)

        prijavabutton = ttk.Button(self, text='Prijavi se', command=lambda: prijava(ekor_ime.get(), epass.get()))
        prijavabutton.pack()

        def prijava(korime, sifra):
            login_polja = [ekor_ime.get(), epass.get()]
            for polje in login_polja:
                if polje == '' or polje == ' ':
                    messagebox.showerror(title='Greska', message='Sva polja moraju biti popunjena!')
                    ekor_ime.delete(0, END)
                    epass.delete(0, END)
                    return
            try:
                biblioteka.login(korime, sifra)
                if biblioteka.jePrijavljen:
                    messagebox.showinfo(title='Info', message='Dobrodosli u sistem')
                    ekor_ime.delete(0, END)
                    epass.delete(0, END)
            except:
                messagebox.showerror(title='Greska', message='Neispravno korisnicko ime ili lozinka')


class IzdajKnjigu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg=pozadina)
        Label(self, text='Izdaj Knjigu', bg=pozadina, font=title_font, fg='black').pack(pady=3)
        w = Canvas(self, width=1200, height=1)
        w.pack(pady=20)
        w.create_line(0, 0, 300, 300)

        lnaslov = Label(self, text='Naslov', bg=pozadina, font=label_font, fg='black').pack()
        enaslov = Entry(self)
        enaslov.pack(pady=10)

        podacilabel = Label(self, text='', bg=pozadina, fg='black', font='Cambria 20 bold')
        podacilabel.pack()

        nadjibutton = ttk.Button(self, text='Nadji knjigu', command=lambda: trazenje_knjige(enaslov.get()))
        nadjibutton.pack(pady=15)

        izdajbutton = ttk.Button(self, text='Izdaj knjigu', command=lambda: izdavanje(enaslov.get()))
        izdajbutton.pack(pady=15)



        def trazenje_knjige(ime_knjige):
            if enaslov.get() == '' or enaslov.get() == ' ':
                messagebox.showerror(title='Greska', message='Nije uneto ime knjige')
                enaslov.delete(0, END)
                return
            try:
                podaci = biblioteka.nadji_knjigu(ime_knjige)
                podacilabel.configure(text=podaci)
            except:
                messagebox.showerror(title='Greska', message='Knjiga nije pronadjena')

        def izdavanje(naslov_knjige):
            if enaslov.get() == '' or enaslov.get() == ' ':
                messagebox.showerror(title='Greska', message='Nije uneto ime knjige')
                enaslov.delete(0, END)
                return
            try:
                biblioteka.izdaj_knjigu(naslov_knjige)
                messagebox.showinfo(title='Uspeh', message='Knjiga izdata!')
                enaslov.delete(0, END)
            except:
                messagebox.showerror(title='Greska', message='Doslo je do greske')


class VratiKnjigu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg=pozadina)
        Label(self, text='Izdaj Knjigu', bg=pozadina, font=title_font, fg='black').pack(pady=3)
        w = Canvas(self, width=1200, height=1)
        w.pack(pady=20)
        w.create_line(0, 0, 300, 300)

        lvrati = Label(self, text='Naslov', bg=pozadina, font=label_font, fg='black').pack()
        evrati = Entry(self)
        evrati.pack(pady=10)

        vratibutton = ttk.Button(self, text='Vrati knjigu', command=lambda: vracanje(evrati.get()))
        vratibutton.pack(pady=15)

        def vracanje(naslov_knjige):
            if evrati.get() == '' or evrati.get() == ' ':
                messagebox.showerror(title='Greska', message='Nije uneto ime knjige')
                evrati.delete(0, END)
                return
            try:
                biblioteka.vrati_knjigu(naslov_knjige)
                messagebox.showinfo(title='Uspeh', message='Knjiga je vracena!')
                evrati.delete(0, END)
            except:
                messagebox.showerror(title='Greska', message='Unesena knjiga nije u sistemu')


class DodajKnjigu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg=pozadina)
        Label(self, text='Dodaj Knjigu', bg=pozadina, font=title_font, fg='black').pack(pady=3)
        w = Canvas(self, width=1200, height=1)
        w.pack(pady=20)
        w.create_line(0, 0, 300, 300)

        ldodajnaslov = Label(self, text='Naslov:', bg=pozadina, font=label_font, fg='black').pack()
        edodajnaslov = Entry(self)
        edodajnaslov.pack(pady=3)

        lautor = Label(self, text='Autor:', bg=pozadina, font=label_font, fg='black').pack()
        eautor = Entry(self)
        eautor.pack()

        lgod_izd = Label(self, text='Godina izdavanja:', bg=pozadina, font=label_font, fg='black').pack()
        egod_izd = Entry(self)
        egod_izd.pack()

        lporeklo = Label(self, text='Zemlja porekla:', bg=pozadina, font=label_font, fg='black').pack()
        eporeklo = Entry(self)
        eporeklo.pack()

        ljezik = Label(self, text='Jezik:', bg=pozadina, font=label_font, fg='black').pack()
        ejezik = Entry(self)
        ejezik.pack()

        regbutton = ttk.Button(self, text='Dodaj knjigu',
                               command=lambda: unesi_knjigu(Knjiga(edodajnaslov.get(), eautor.get(),
                                                                   egod_izd.get(), eporeklo.get(),
                                                                   ejezik.get(), 'Na Stanju')))
        regbutton.pack(pady=10)

        def unesi_knjigu(naslov):
            knjige_polja = [edodajnaslov.get(), eautor.get(), egod_izd.get(), eporeklo.get(), ejezik.get()]
            for polje in knjige_polja:
                if polje == '' or polje == ' ':
                    messagebox.showerror(title='Greska', message='Sva polja moraju biti ispunjena!')
                    edodajnaslov.delete(0, END)
                    eautor.delete(0, END)
                    egod_izd.delete(0, END)
                    eporeklo.delete(0, END)
                    ejezik.delete(0, END)
                    return
            try:
                biblioteka.dodaj_knjigu(naslov)
                messagebox.showinfo(title='Uspeh', message='Knjiga je uneta u sistem!')
                edodajnaslov.delete(0, END)
                eautor.delete(0, END)
                egod_izd.delete(0, END)
                eporeklo.delete(0, END)
                ejezik.delete(0, END)
            except:
                messagebox.showerror(title='Greska', message='Doslo je do greske!')


class IzbaciKnjigu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg=pozadina)
        Label(self, text='Izbaci Knjigu', bg=pozadina, font=title_font, fg='black').pack(pady=3)
        w = Canvas(self, width=1200, height=1)
        w.pack(pady=20)
        w.create_line(0, 0, 300, 300)

        lizbaci = Label(self, text='Naslov: ', bg=pozadina, font=label_font, fg='black').pack()

        eizbaci = Entry(self)
        eizbaci.pack()

        izbbutton = ttk.Button(self, text='Izbaci knjigu', command=lambda: brisi_knjigu(eizbaci.get()))
        izbbutton.pack(pady=10)

        def brisi_knjigu(za_brisanje):
            if eizbaci.get() == '' or eizbaci.get() == ' ':
                messagebox.showerror(title='Greska', message='Sva polja moraju biti ispunjena!')
                eizbaci.delete(0, END)
                return
            try:
                biblioteka.izbaci_knjigu(za_brisanje)
                messagebox.showinfo(title='Uspeh', message='Knjiga je obrisana')
                eizbaci.delete(0, END)
            except:
                messagebox.showerror(title='Greska', message='Knjiga ne postoji u sistemu')


class Zaposli(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg=pozadina)
        Label(self, text='Zaposli', bg=pozadina, font=title_font, fg='black').pack(pady=3)
        w = Canvas(self, width=1200, height=1)
        w.pack(pady=20)
        w.create_line(0, 0, 300, 300)

        lime = Label(self, text='Ime i Prezime:', bg=pozadina, font=label_font, fg='black').pack()
        eime = Entry(self)
        eime.pack()

        lmaticni = Label(self, text='JMBG:', bg=pozadina, font=label_font, fg='black').pack()
        ematicni = Entry(self)
        ematicni.pack()

        lbroj = Label(self, text='Broj telefona:', bg=pozadina, font=label_font, fg='black').pack()
        ebroj = Entry(self)
        ebroj.pack()

        ldiploma = Label(self, text='Diploma:', bg=pozadina, font=label_font, fg='black').pack()
        ediploma = Entry(self)
        ediploma.pack()

        lpickuser = Label(self, text='username:', bg=pozadina, font=label_font, fg='black').pack()
        epickuser = Entry(self)
        epickuser.pack()

        lpicpass = Label(self, text='password:', bg=pozadina, font=label_font, fg='black').pack()
        epickpass = Entry(self)
        epickpass.pack()

        zaposlibutton = ttk.Button(self, text='Zaposli', command=lambda: zaposli_radnika())
        zaposlibutton.pack(pady=15)

        def zaposli_radnika():
            zaposli_polja = [eime.get(), ematicni.get(), ebroj.get(), ediploma.get(), epickuser.get(), epickpass.get()]
            for polje in zaposli_polja:
                if polje == '' or polje == ' ':
                    messagebox.showerror(title='Greska', message='Sva polja moraju biti ispunjena!')
                    eime.delete(0, END)
                    ematicni.delete(0, END)
                    ebroj.delete(0, END)
                    ediploma.delete(0, END)
                    epickpass.delete(0, END)
                    return
            try:
                biblioteka.zaposli(Zaposleni(eime.get(), ematicni.get(), ebroj.get(), ediploma.get(), epickuser.get(),
                                             epickpass.get(), False))
                messagebox.showinfo(title='Info', message='Uspesno izvrseno!')
                eime.delete(0, END)
                ematicni.delete(0, END)
                ebroj.delete(0, END)
                ediploma.delete(0, END)
                epickuser.delete(0, END)
                epickpass.delete(0, END)
            except:
                messagebox.showerror(title='Greska', message='Nije uspelo!')


class Otpusti(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg=pozadina)
        Label(self, text='Otpusti', bg=pozadina, font=title_font, fg='black').pack(pady=3)
        w = Canvas(self, width=1200, height=1)
        w.pack(pady=20)
        w.create_line(0, 0, 300, 300)

        lotpust = Label(self, text='Ime i prezime:', bg=pozadina, font=label_font, fg='black').pack()
        eotpust = Entry(self)
        eotpust.pack(pady=10)

        otpustibutton = ttk.Button(self, text='Otpusti', command=lambda: izbrisi_radnika(eotpust.get()))
        otpustibutton.pack(pady=15)

        def izbrisi_radnika(radnik):
            if eotpust.get() == '' or eotpust.get() == ' ':
                messagebox.showerror(title='Greska', message='Uneto je prazno polje!')
                eotpust.delete(0, END)
                return
            try:
                biblioteka.otpusti(radnik)
                messagebox.showinfo(title='Info', message='Radnik otpusten')
                eotpust.delete(0, END)
            except:
                messagebox.showerror(title='Greska', message='Radnik nije pronadjen')


frames = (PocetnaStranica, Registracija, Login, IzdajKnjigu, VratiKnjigu, DodajKnjigu, IzbaciKnjigu, Zaposli, Otpusti)
