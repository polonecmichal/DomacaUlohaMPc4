# ============================================================================
# PRÍKLAD 4: Rozdeľovanie stringov
# ============================================================================
"""
Máte email: "jan.novak@example.com"
Rozdeľte ho na používateľské meno a doménu pomocou split().
Vypíšte vo formáte: "Používateľ: XXX, Doména: YYY"
"""

# Vaše riešenie:
email = "jan.novak@example.com"
pouzivatel = email.split("@") [0];
domena  = email.split("@") [1];
print("pouzivatel:", pouzivatel, "domena:", domena)