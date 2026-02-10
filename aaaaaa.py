# def qaytim_hisobla(narx, tolangan):
#     if tolangan < narx:
#         return f"Pul yetarli emas"
#     else:
#         return f"{tolangan - narx}"
#
# print(qaytim_hisobla(15000, 10000))
# print(qaytim_hisobla(1000, 5000))
#
# # 2 - masala
#
# class Transport:
#     def __init__(self, model, yil):
#         self.model = model
#         self.yil = yil
#
#     def malumot(self):
#         return f"Model: {self.model}, Yil: {self.yil}"
#
# class Avtomobil(Transport):
#     def __init__(self, model, yil, yonilgi_turi):
#         # Ota klassning __init__ metodini chaqirish
#         super().__init__(model, yil)
#         self.yonilgi_turi = yonilgi_turi
#
#     def malumot(self):
#         # Ota klassdagi malumot() metodiga yangi qism qo'shish
#         return super().malumot() + f", Yonilg'i: {self.yonilgi_turi}"
#
# class Avtobus(Transport):
#     def __init__(self, model, yil, o_rinlar_soni):
#         # Ota klassning __init__ metodini chaqirish
#         super().__init__(model, yil)
#         self.o_rinlar_soni = o_rinlar_soni
#
#     def malumot(self):
#         # Ota klassdagi malumot() metodiga yangi qism qo'shish
#         return super().malumot() + f", O'rinlar: {self.o_rinlar_soni}"
#
#
# a = Avtomobil("Cobalt", 2022, "benzin")
# print(a.malumot())
#
# b = Avtobus("Isuzu", 2018, 40)
# print(b.malumot())
#
# # 3 - masala
#
# class Xodim:
#     def __init__(self, ism, asosiy_maosh):
#         self.ism = ism
#         self.asosiy_maosh = asosiy_maosh
#
#     def oylik(self):
#         return self.asosiy_maosh
#
#     def malumot(self):
#         return f"Ism: {self.ism}, Oylik: {self.oylik()}"
#
# class Oqsoch(Xodim):
#     def __init__(self, ism, asosiy_maosh, bonus_foiz):
#         super().__init__(ism, asosiy_maosh)
#         self.bonus_foiz = bonus_foiz
#
#     def oylik(self):
#         # Asosiy maoshga foizni qo'shib hisoblash
#         bonus = self.asosiy_maosh * (self.bonus_foiz / 100)
#         return self.asosiy_maosh + bonus
#
# class SoatbayXodim(Xodim):
#     def __init__(self, ism, soat, soatlik_stavka):
#         # Hisoblangan maoshni ota klassga (asosiy_maosh sifatida) jo'natamiz
#         jami_maosh = soat * soatlik_stavka
#         super().__init__(ism, jami_maosh)
#
# o = Oqsoch("Dilshod", 5_000_000, 20)
# s = SoatbayXodim("Aziza", soat=160, soatlik_stavka=50_000)
#
# print(o.malumot())
# print(s.malumot())
#
# # 4 - masala
#
# class Mahsulot:
#     def __init__(self, nom, narx):
#         self.nom = nom
#         self.narx = narx
#
#     def chegirmali_narx(self, foiz):
#         yangi_narx = self.narx * (1 - foiz / 100)
#         return yangi_narx
#
# class Elektronika(Mahsulot):
#     def __init__(self, nom, narx, kafolat_oy):
#         super().__init__(nom, narx)
#         self.kafolat_oy = kafolat_oy
#
#     def malumot(self):
#         return f"Nom: {self.nom}, Narx: {self.narx}, Kafolat: {self.kafolat_oy} oy"
#
# class OziqOvqat(Mahsulot):
#     def __init__(self, nom, narx, yaroqlilik_kuni):
#         super().__init__(nom, narx)
#         self.yaroqlilik_kuni = yaroqlilik_kuni
#
#     def malumot(self):
#         return f"Nom: {self.nom}, Narx: {self.narx}, Yaroqlilik: {self.yaroqlilik_kuni}"
#
# e = Elektronika("Laptop", 12_000_000, 12)
# o = OziqOvqat("Sut", 12_000, "2025-01-10")
#
# print(e.malumot())
# print(f"Chegirmali narx: {e.chegirmali_narx(10)}")
#
# print(o.malumot())
#
# # 5 - masala
#
# class Shaxs:
#     def __init__(self, ism):
#         self.ism = ism
#
#
# class Talaba(Shaxs):
#     def __init__(self, ism, id_raqam):
#         # Shaxs klassining konstruktorini chaqiramiz
#         super().__init__(ism)
#         self.id_raqam = id_raqam
#
#
# class ImtihonNatijasi(Talaba):
#     def __init__(self, ism, id_raqam, baholar):
#         super().__init__(ism, id_raqam)
#         self.baholar = baholar
#
#     def ortalama(self):
#         if not self.baholar:
#             return 0
#         return sum(self.baholar) / len(self.baholar)
#
#     def status(self):
#         o_rtacha = self.ortalama()
#
#         if o_rtacha >= 86:
#             return "A'lo"
#         elif 71 <= o_rtacha <= 85:
#             return "Yaxshi"
#         elif 56 <= o_rtacha <= 70:
#             return "Qoniqarli"
#         else:
#             return "Qoniqarsiz"
#
#
# natija = ImtihonNatijasi("Ali", "T001", [90, 80, 100])
#
# print(f"Ism: {natija.ism}")  # Ali
# print(f"ID: {natija.id_raqam}")  # T001
# print(f"O'rtacha: {natija.ortalama()}")  # 90.0
# print(f"Status: {natija.status()}")  # A'lo
#
# # 6 - masala
#
# class Hisob:
#     def __init__(self, raqam, egasi, balans):
#         self.raqam = raqam
#         self.egasi = egasi
#         self.balans = balans
#
#     def kirim(self, summa):
#         self.balans += summa
#         return self.balans
#
#     def chiqim(self, summa):
#         if self.balans >= summa:
#             self.balans -= summa
#             return self.balans
#         else:
#             print("Xatolik: Mablag' yetarli emas!")
#             return None
#
# class JamgArmaMixin:
#     def foiz_qosh(self):
#         bonus = self.balans * (self.foiz_stavka / 100)
#         self.balans += bonus
#         return self.balans
#
# class KreditMixin:
#     def chiqim(self, summa):
#         if (self.balans + self.limit) >= summa:
#             self.balans -= summa
#             return self.balans
#         else:
#             print("Xatolik: Kredit limiti yetarli emas!")
#             return None
#
# class VIPHisob(Hisob, JamgArmaMixin, KreditMixin):
#     def __init__(self, raqam, egasi, balans, foiz_stavka, limit):
#         super().__init__(raqam, egasi, balans)
#         # Mixin atributlarini o'rnatamiz
#         self.foiz_stavka = foiz_stavka
#         self.limit = limit
#
# vip = VIPHisob("001", "Karim", 2_000_000, foiz_stavka=12, limit=500_000)
#
#
# vip.foiz_qosh()
# print(f"Foizdan keyingi balans: {vip.balans}")
#
#
# vip.chiqim(2_400_000)
# print(f"Chiqimdan keyingi balans: {vip.balans}")
#
# 