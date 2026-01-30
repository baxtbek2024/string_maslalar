#1 masala

matn = "salom dostim qalaysiz".title()
print(matn)

#2-masala
def qavs_ischidagi_matn(matn):
    natija = []
    temp = ""
    ichida = False

    for i in matn:
        if i == "(":
            ichida = True
            temp = ""
        elif i == ")":
            ichida = False
            natija.append(temp)
        elif ichida:
            temp += i

    return natija

print(qavs_ischidagi_matn("mening ismim(Baxtbek), do'stimniki (Bunyod)"))

#3-masala
def email(email):
    return "@" in email and "." in email
print(email("jigijigipapa@gmail.com"))

#3-masala
def noyob_harf(matn):
    yangi = ""
    for i in matn:
        if i not in matn:
            yangi += i
    return yangi

print(noyob_harf("salom ortoq"))

#4-masala
matn = "aziza"
matn = matn.lower().replace(" ", " ")

if matn == matn[::-1]:
    print("palindrom")
else:
    print("palindrom emas")

#5-masala
matn = "bugun sizlar bilan bugun olib borilgan ishlarni koramiz"
sozlar = matn.split()

eng_kop = ""
soni = 0

for i in sozlar:
    if sozlar.count(i) > soni:
        eng_kop = i
        soni = sozlar.count(i)

print(eng_kop, soni)


#6-masala
matn = "1234567890"
natija = ""

for i in range(len(matn)):
    if i != 0 and i % 3 == 0:
        natija += "-"
    natija += matn[i]

print(natija)
