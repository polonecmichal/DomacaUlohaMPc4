# ============================================================================
# PRÍKLAD 8: Hľadanie pozície podreťazca
# ============================================================================
"""
V stringu "Programovanie v Pythone je zábavné"
Nájdite pozíciu slova "Python" pomocou find() a index().
Vypíšte obe pozície.
Bonus: Skúste nájsť slovo "Java" pomocou find() - čo sa stane?
"""

# Vaše riešenie:
text = "Programovanie v Pythone je zábavné"
poyicia_f = text.find("Python")
pozicia_i = text.index("Python")
print("Pozicia find():", poyicia_f)
print("Pozicia index():", pozicia_i)
pozicia_java = text.find("Java")
print("Pozicia Java find():", pozicia_java)