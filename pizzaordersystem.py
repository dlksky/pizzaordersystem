import csv
import datetime

class Pizza():
  def get_description(self):
    return self.__class__.__name__

  def get_cost(self):
    return self.__class__.cost

class Klasik(Pizza):
  cost= 100.0
  def __init__(self):
      self.description="klasik pizza içerisinde olan malzemeler: Zeytin,Sosis"
      print(self.description  + "\n")

class Margarita(Pizza):
  cost=120.0
  def __init__(self):
    self.description="Margarita pizza içerisinde olan malzemeler: Domates,Mozeralla"
    print(self.description + "\n")

class TUrkPizza(Pizza):
  cost=130.0
  def __init__(self):
    self.description="TürkPizza pizza içerisinde olan malzemeler: Sucuk,Pastırma"
    print(self.description + "\n")

class SadePizza(Pizza):
  cost=90
  def __init__(self):
    self.description="Sade Pizza pizza içerisinde olan malzemeler: Domates,Zeytin"
    print(self.description +"\n")
  
class Decorator(Pizza):
    def __init__(self, topping):
        self.component = topping

    def get_cost(self):
        return self.component.get_cost() + \
          Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
          ' ;' + Pizza.get_description(self)
    
#Decorator alt sınıf oluşturulacak 
class Zeytin(Decorator):
    cost = 2.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Mantar(Decorator):
    cost = 3.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Peynir(Decorator):
    cost = 4.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Et(Decorator):
    cost = 10.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Sogan(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Misir(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)

def main():
    with open("pizzaorder.txt" , encoding="utf-8") as cust_menu:
        for l in cust_menu:
            print(l, end="")

    class_dict = {1: Klasik, 
                  2: Margarita, 
                  3: TUrkPizza, 
                  4: SadePizza, 
                  11: Zeytin, 
                 12: Mantar, 
                  13: Peynir, 
                  14: Et, 
                  15: Sogan, 
                  16: Misir}
    code = input("Lütfen Pizzanızı Seçiniz: ")
    while code not in ["1", "2", "3", "4"]:
        code = input("Hatalı Seçim Yaptınız: ")

    order = class_dict[int(code)]()


    while code != "*":
        code = input("Ek Malzeme Almak İçin Menüye göre  Tuşlama Yapınız (Direkt Siparişinizi Onaylamak İçin '*' Tuşuna Basınız): ")
        if code in ["11","12","13","14","15","16"]:
            order = class_dict[int(code)](order)

    print("\n"+order.get_description().strip() +
          "; $" + str(order.get_cost()))
    print("\n")


#Sipariş Bilgi Kartı oluşturuyoruz.
    print("----------Sipariş Bilgileri----------\n")
    NAME = input("İsminiz: ")
    SURNAME= input(" Soy İsminiz: ")
    TC = input("TC Kimlik Numaranız: ")
    KREDI_NO = input("Kredi Kartı Numaranızı Giriniz: ")
    KREDI_PSW = input("Kredi Kartı Şifrenizi Giriniz: ")
    SIPARIS_ZAMANI = datetime.datetime.now()

    with open('Orderss_Database.csv', encoding="utf-8" , 'a') as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow([NAME,SURNAME,TC, KREDI_NO, KREDI_PSW, order.get_description(), SIPARIS_ZAMANI])
    print("Siparişiniz Onaylandı.")







main()
