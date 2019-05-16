string = input("String: ")
szam = 0
kis = 0
nagy = 0
egyeb = 0
kis_ls = ["á", "é", "í","ó", "ö", "ő", "ú", "ü", "ű"] #vizgálathoz hogy magyar szöveggel is sikerüljön
nagy_ls = ["Á", "É", "Í", "Ó", "Ö", "Ő", "Ú", "Ü", "Ű"]
for i in string.replace(" ", ""): #kiveszem a szóközöket
    if "a" <= i <= "z" or i in kis_ls:
        kis += 1
    elif "A" <= i <= "Z" or i in nagy_ls:
        nagy += 1
    elif "0" <= i <= "9":
        szam += 1
    else:
        egyeb += 1
print("szám = {} kisbetűk = {} nagybetűk = {} egyéb = {}".format(szam, kis, nagy, egyeb))