import random
bilgisayar=["*","+","-"]
print("TAŞ KAĞIT MAKAS OYUNUNUNA HOŞGELDİN!!!!!!!!!!!!")
sayac1=0
sayac2=0
while (int(sayac1)<3) and (int(sayac2)<3) :
  kullanici=input("TAŞ:*\nKAĞIT:+\nMAKAS:-\nSeçimini yap!")
  secim_bir=random.choice(bilgisayar)
  if (kullanici == "*" and secim_bir =="-") or (kullanici =="-" and secim_bir =="+"):
    print("Tebrikler turu kazandınız")
    sayac1=sayac1+1
  elif (kullanici == "*" and secim_bir =="+") or (kullanici == "+" and secim_bir =="*"):
    print("Üzgünüz kaybettiniz")
    sayac2=sayac2+1
  else:
    print("Durum berabere")
print("Son Durum:",sayac1,"-",sayac2)


