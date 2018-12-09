import xlsxwriter

workbook = xlsxwriter.Workbook('ViktorijaVezba7.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

#Konstanta ravnoteze za Bredforda [ml/mg]
_k_b_ = 0.702
#Konstana ravnoteze za DNS [dm^3/mmol]
_k_dns_ = 0.24

#Potrebno nam je vreme u kome se odigravala reakcija
t = int(input("Koliko dugo se odigravala reakcija: "))
#Kolika je zapremina reakcione smese. Uzima u obzir zapreminu pufera, saharoze i enzima
V = int(input("Kolika je zapremina reakcione smese: "))
#Koliko razblazenje se pravilo
razblazenje = int(input("Koliko je razblazenje: "))
#Zapremina enzima koja se koristi
_v_enzima_ = int(input("Kolika je zapremina enzima: "))

if _v_enzima_ == 0 or _v_enzima_ == None:
    _v_enzima_ = 1

#Apsorbance za Bradforda
_A_b_ = list()
while True:
    apsorbanca = input("Upisi vrednost za apsorbancu u slucaju metode po Bredfordu: ")
    if len(apsorbanca) < 1:
        break
    _A_b_.append(float(apsorbanca))

print("Apsorbanca za bredforda: ", _A_b_)

#Apsorbanca za DNS
_A_dns_ = list()
while True:
    apsorbanca = input("Upisi vrednost za apsorbancu u slucaju metode po DNS-u: ")
    if len(apsorbanca) < 1:
        break
    _A_dns_.append(float(apsorbanca))

print("Apsorbanca za DNS: ", _A_dns_)

_c_pet_dns_ = list()
#koncentracija inverznog secera
for a in _A_dns_:
    _c_pet_dns_.append(round(float(a/_k_dns_),3))
print("Koncentracija inverznog secera: ", _c_pet_dns_)

_n_pet_ = list()
#broj molova inverznog secera
for a in _c_pet_dns_:
    _n_pet_.append(round(float(a*V),3))

print("Broj molova invertnog secera: ", _n_pet_)

_aktivnost_ = list()
for a in _n_pet_:
    _aktivnost_.append(round(float(a/t*razblazenje),3))

print("Aktivnost: ", _aktivnost_)

#zapreminska aktivnost
_v_aktivnost_ = list()
for a in _aktivnost_:
    _v_aktivnost_.append(round(float(a*_v_enzima_),3))

print("Zapreminska aktivnost: ", _v_aktivnost_)

_c_pet_b_ = list()

for a in _A_b_:
    _c_pet_b_.append(round(float(a*10/_k_b_),3))

print("Koncentracija proteina: ", _c_pet_b_)

_sa_ = list()
#specificna aktivnost
for i in range(2):
        _sa_.append(round(_v_aktivnost_[i]/_c_pet_b_[i],3))

#Upisivanje podataka u excel fajl
worksheet.write('A1', 'Kb = 0.702 ml/mg')
worksheet.write('A2', 'Kdns = 0.24 dm3/mmol')
podaci = (
    ['t [s] = ', t],
    ['V [ml] = ', V],
    ['R = ', razblazenje],
    ['Ve [ml] = ', _v_enzima_]
)
row = 3
col = 0
for item, value in (podaci):
    worksheet.write(row, col, item, bold)
    worksheet.write(row, col+1, value)
    row += 1
row += 1
col = 0
worksheet.write(row, col, 'DNS', bold)
worksheet.write(row, col+1, 'Apsorbanca')
worksheet.write(row, col+2, 'C = A/Kdns [mmol/dm3]')
worksheet.write(row, col+3, 'broj molova*10^5')
row += 1
worksheet.write(row,col, 'sirovi')
worksheet.write(row, col+1, str(_A_dns_[0]))
worksheet.write(row, col+2, str(_c_pet_dns_[0]))
worksheet.write(row, col+3, str(_n_pet_[0]))
row += 1
worksheet.write(row, col, 'uzorak' )
worksheet.write(row, col+1, str(_A_dns_[1]))
worksheet.write(row, col+2, str(_c_pet_dns_[1]))
worksheet.write(row, col+3, str(_n_pet_[1]))
row += 2
col = 1
worksheet.write(row, col, 'Aktivnost [µmol/min]')
worksheet.write(row, col+1, 'Zapreminska aktivnost [IU/ml]')
col = 0
row += 1
worksheet.write(row,col, 'sirovi')
worksheet.write(row, col+1, str(_aktivnost_[0]))
worksheet.write(row, col+2, str(_v_aktivnost_[0]))
row += 1
worksheet.write(row, col, 'uzorak' )
worksheet.write(row, col+1, str(_aktivnost_[1]))
worksheet.write(row, col+2, str(_v_aktivnost_[1]))
row += 2
worksheet.write(row, col, 'SA = A/Sp = Zapreminska aktivnost/Cp [IU/mg]')
row +=1
worksheet.write(row, col, 'Cp = A*10/Kb [mg/ml]')
row += 2
worksheet.write(row, col, 'Bradford', bold)
worksheet.write(row, col+1, 'A')
worksheet.write(row, col+2, 'Cp[mg/ml]')
worksheet.write(row, col+3, 'SA[IU/mg]')
row += 1
worksheet.write(row,col, 'sirovi')
worksheet.write(row, col+1, str(_A_b_[0]))
worksheet.write(row, col+2, str(_c_pet_b_[0]))
worksheet.write(row, col+3, str(_sa_[0]))
row += 1
worksheet.write(row,col, 'uzorak')
worksheet.write(row, col+1, str(_A_b_[1]))
worksheet.write(row, col+2, str(_c_pet_b_[1]))
worksheet.write(row, col+3, str(_sa_[1]))
workbook.close()

print("Specificna aktivnost za sirovi: ", _sa_[0])
print("Specificna aktivnost za uzorak: ", _sa_[1])
