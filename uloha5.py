# ============================================================================
# PRÍKLAD 5: Práca s medzerami
# ============================================================================
"""
Máte string: "   Python   "
Odstráňte medzery na začiatku, na konci a na oboch stranách.
Vypíšte všetky tri varianty (každú v apostrofoch aby boli vidieť medzery).
"""

# Vaše riešenie:
text = "   Python   "
lava = text.lstrip()
prava = text.strip()
oba = text.strip()
print("Lava:", "'" + lava + "'")
print("Prava:", "' " + prava + "'")
print("Oba:", "'" + oba + "'")