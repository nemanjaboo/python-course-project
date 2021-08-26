class Zaposleni:
    def __init__(self, ime_prezime, JMBG, br_telefona, diploma, username, password, sef=False):
        Zaposleni.Validacija(ime_prezime, JMBG, br_telefona, diploma, username, password, sef)
        self.ime_prezime = ime_prezime
        self.JMBG = JMBG
        self.br_telefona = br_telefona
        self.diploma = diploma
        self.username = username
        self.password = password
        self.sef = sef


    def __str__(self):
        return 'Zaposleni: {}\nJMBG: {}\nBroj telefona: {}\n'.format(self.ime_prezime, self.JMBG, self.br_telefona)

    @staticmethod
    def Validacija(ime_prezime, JMBG, br_telefona, diploma, username, password, sef):
        assert type(ime_prezime) == str, 'Ime i prezime moraju biti string'
        assert type(JMBG) == str, 'Jedinstveni Maticni Broj mora biti string'
        assert type(br_telefona) == str, 'Broj telefona mora biti string'
        assert type(diploma) == str, 'Diploma mora biti string'
        assert type(username) == str, 'Korisnicko ime mora biti string'
        assert type(password) == str, 'Lozinka mora biti string'
        assert type(sef) == bool, 'Sef mora biti boolean vrednost'


class Knjiga:
    def __init__(self, naslov, autor, godina_izdavanja, zemlja_porekla, jezik, stanje='Na stanju'):
        Knjiga.Validacija(naslov, autor, godina_izdavanja, zemlja_porekla, jezik, stanje)
        self.naslov = naslov
        self.autor = autor
        self.godina_izdavanja = godina_izdavanja
        self.zemlja_porekla = zemlja_porekla
        self.jezik = jezik
        self.stanje = stanje

    def __str__(self):
        return 'Naslov: {}\nAutor: {}\nZemlja porekla: {}\nJezik originalne verzije: {}\nStanje: {}\n'.format(
            self.naslov, self.autor, self.zemlja_porekla,
            self.jezik, self.stanje)

    @staticmethod
    def Validacija(naslov, autor, godina_izdavanja, zemlja_porekla, jezik, stanje):
        assert type(naslov) == str, 'Naslov mora biti string'
        assert type(autor) == str, 'Autor mora biti string'
        assert type(godina_izdavanja) == str, 'Godina izdavanja mora biti string'
        assert type(zemlja_porekla) == str, 'Zemlja porekla mora biti string'
        assert type(jezik) == str, 'Jezik mora biti string string'
        assert type(stanje) == str, 'Stanje mora biti string'


class Biblioteka:
    def __init__(self, zaposleni, knjige, jePrijavljen):
        self.zaposleni = zaposleni
        self.knjige = knjige
        self.jePrijavljen = False
        self.aktivni = ''

    @staticmethod
    def Validacija(zaposleni, knjige, jePrijavljen):
        assert type(zaposleni) == list, 'Mora biti lista zaposlenih'

        for radnik in zaposleni:
            assert type(radnik) == Zaposleni, 'Mora biti objekat klase Zaposleni'

        assert type(knjige) == list, 'Mora biti lista knjiga'

        for book in knjige:
            assert type(book) == Knjiga, 'Mora biti objekat klase Knjiga'

        assert type(jePrijavljen) == bool, 'Mora biti boolean vrednost'

    def registracija_zaposlenog(self, ime_prezime, JMBG, br_telefona, diploma, username, password, sef):
        for radnik in self.zaposleni:
            if radnik.ime_prezime == ime_prezime or radnik.JMBG == JMBG:
                raise Exception
        self.zaposleni.append(Zaposleni(ime_prezime, JMBG, br_telefona, diploma, username, password, sef))
        reg = open('zaposleni.txt', 'a')
        reg.write(
            '\n' + ime_prezime + ',' + JMBG + ',' + br_telefona + ',' + diploma + ',' + username + ',' + password + ',' + str(
                sef))
        reg.close()


    def login(self, username, password):
        for radnik in self.zaposleni:
            if username == radnik.username and password == radnik.password:
                self.jePrijavljen = True
                self.aktivni += username
                break
        if not self.jePrijavljen:
            raise Exception



    def dodaj_knjigu(self, ime):
        assert type(ime) == Knjiga, 'Mora biti objekat klase Knjiga'
        self.knjige.append(ime)
        b = open('knjige.txt', 'a')
        b.write(ime.naslov + ',' + ime.autor + ',' + ime.godina_izdavanja + ',' + ime.zemlja_porekla +
                ',' + ime.jezik + ',' + ime.stanje + '\n')
        b.close()

    def izbaci_knjigu(self, naslov):
        for book in self.knjige:
            if book.naslov == naslov:
                knjige_fajl = open('knjige.txt', 'r')
                lines = knjige_fajl.readlines()
                knjige_fajl.close()

                for i in range(len(lines)):
                    if naslov in lines[i]:
                        del lines[i]
                        break

                novi = open('knjige.txt', 'w')
                for line in lines:
                    novi.write(line)
                novi.close()
                return
        raise Exception


    def nadji_knjigu(self, naslov):
        for book in self.knjige:
            if book.naslov == naslov:
                return 'Knjiga:{:^10}\nAutor:{:^10}\nGodina izdavanja:{:^10}\n' \
                       'Zemlja porekla:{:^10}\nJezik originalne verzije:{:^10}\n' \
                       'Stanje:{:^10}\n{:^10}'.format(book.naslov, book.autor, book.godina_izdavanja,
                                                           book.zemlja_porekla, book.jezik, book.stanje, '=' * 100)

        raise Exception

    def izdaj_knjigu(self, naslov):
        for book in self.knjige:
            if book.naslov == naslov:
                book.stanje = 'Izdato'
                knjige_fajl = open('knjige.txt', 'r')
                lines = knjige_fajl.readlines()
                knjige_fajl.close()
                izmena = ''
                for i in range(len(lines)):
                    if naslov in lines[i]:
                        izmena += lines[i].replace('Na stanju', 'Izdato')
                        del lines[i]
                        break

                for i in lines:
                    izmena += i
                novi_unos = open('knjige.txt', 'w')
                novi_unos.write(izmena)
                novi_unos.close()

    def vrati_knjigu(self, naslov):
        for book in self.knjige:
            if book.naslov == naslov:
                book.stanje = 'Na Stanju'
                knjige_fajl = open('knjige.txt', 'r')
                lines = knjige_fajl.readlines()
                knjige_fajl.close()
                izmena = ''
                for i in range(len(lines)):
                    if naslov in lines[i]:
                        izmena += lines[i].replace('Izdato', 'Na stanju')
                        del lines[i]
                        break

                for i in lines:
                    izmena += i
                novi_unos = open('knjige.txt', 'w')
                novi_unos.write(izmena)
                novi_unos.close()




    def zaposli(self, zaposlen):
        assert type(zaposlen) == Zaposleni, 'Mora biti objekat klase Zaposleni'
        for radnik in self.zaposleni:
            if radnik.JMBG == zaposlen.JMBG or radnik.username == zaposlen.username:
                raise Exception

        self.zaposleni.append(zaposlen)
        r = open('zaposleni.txt', 'a')
        r.write(zaposlen.ime_prezime + ',' + zaposlen.JMBG + ',' + zaposlen.br_telefona
                + ',' + zaposlen.diploma + ',' + zaposlen.username + ','
                + zaposlen.password + ',' + str(zaposlen.sef)+'\n')


    def otpusti(self, ime_prezime):
        for radnik in self.zaposleni:
            if radnik.ime_prezime == ime_prezime:
                radnici_fajl = open('zaposleni.txt', 'r')
                lines = radnici_fajl.readlines()
                radnici_fajl.close()

                for i in range(len(lines)):
                    if ime_prezime in lines[i]:
                        del lines[i]
                        break

                novi = open('zaposleni.txt', 'w')
                for line in lines:
                    novi.write(line)
                novi.close()


zaposleni = []
knjige = []

z = [i.split(',') for i in open('zaposleni.txt')]
for i in z:
    if i[6].strip('\n') == 'True':
        zaposleni.append(Zaposleni(i[0], i[1], i[2], i[3], i[4], i[5], True))
    if i[6].strip('\n') == 'False':
        zaposleni.append(Zaposleni(i[0], i[1], i[2], i[3], i[4], i[5]))





k = [i.split(',') for i in open('knjige.txt')]
for i in k:
    knjige.append(Knjiga(i[0], i[1], i[2], i[3], i[4], i[5]))

biblioteka = Biblioteka(zaposleni, knjige, False)

