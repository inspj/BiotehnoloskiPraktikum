#Konstanta ravnoteze za Bredforda [ml/mg]
_k_b_ = 0.702
#Konstana ravnoteze za DNS [dm^3/mmol]
_k_dns_ = 0.24

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


_c_pet_dns_ = list()
#koncentracija inverznog secera
for a in _A_dns_:
    _c_pet_dns_.append(float(a/_k_dns_))
print("Koncentracija inverznog secera: ", _c_pet_dns_)

_n_pet_ = list()
#broj molova inverznog secera
for a in _c_pet_dns_:
    _n_pet_.append(float(a*V))

print("Broj molova invertnog secera: ", _n_pet_)

_aktivnost_ = list()
for a in _n_pet_:
    _aktivnost_.append(float(a/t*razblazenje))

print("Aktivnost: ", _aktivnost_)

#zapreminska aktivnost
_v_aktivnost_ = list()
for a in _aktivnost_:
    _v_aktivnost_.append(float(a*_v_enzima_))

print("Zapreminska aktivnost: ", _v_aktivnost_)

_c_pet_b_ = list()

for a in _A_b_:
    _c_pet_b_.append(float(a*10/_k_b_))

print("Koncentracija proteina: ", _c_pet_b_)

_sa_ = list()
#specificna aktivnost
for i in range(2):
        _sa_.append(_v_aktivnost_[i]/_c_pet_b_[i])
        
print("Specificna aktivnost za sirovi: ", _sa_[0])
print("Specificna aktivnost za uzorak: ", _sa_[1])
