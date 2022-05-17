def scrapper(num_last=15,nom_candidat="NONE"):
    print(nom_candidat,i)



list = ["#Arthaud",
"#Roussel",
"#Macron",
"#Lassalle",
"#LePen",
"#Zemmour",
"#Melenchon",
"#Hidalgo",
"#Jadot",
"#Pecresse",
"#Poutou",
"Dupont-Aignan"]

for a in list:
    print(a)
    for i in range(1,30,1):
        scrapper(num_last=i,nom_candidat=a)