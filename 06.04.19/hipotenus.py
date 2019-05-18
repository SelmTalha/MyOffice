"""
Hipotenus : Dik ucgende dik acinin karsisindaki kenara denir.
Formulu : a^2+b^2=c^2
old. gore kullanicidan alinan A ve B kenarina gore hipotenusu hesaplayan kodu yazalim.
"""

a_kenari=int(input("A:"))
b_kenari=int(input("B:"))

c=(a_kenari ** 2 + b_kenari ** 2) ** 0.5

print("Hipotenus:",c)
