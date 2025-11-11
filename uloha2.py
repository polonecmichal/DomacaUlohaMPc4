# ============================================================================
# PRÍKLAD 2: Zisťovanie dĺžky a počítanie znakov
# ============================================================================
"""
Máte vetu: "Python je skvelý programovací jazyk"
Zistite dĺžku vety a koľkokrát sa v nej vyskytuje písmeno 'a'.
Výsledky vypíšte vo formáte: "Dĺžka: X, Počet 'a': Y"
"""

# Vaše riešenie:
veta = "Python je skvelý programovací jazyk"
counter = 0
ltr_count = 0
for letters in veta:
    if letters == "a":
        counter +=1
        ltr_count + 1
    else:
        counter + 0
        ltr_count += 1
print(counter, ltr_count)
