# ============================================================================
# PRÍKLAD 9: Kontrola začiatku a konca stringu
# ============================================================================
"""
Máte názov súboru: "dokument.pdf"
Skontrolujte, či sa končí príponou .pdf.
Skontrolujte, či sa začína slovom "dokument".
Vypíšte výsledky oboch kontrol.
"""

# Vaše riešenie:
nazov = "dokument.pdf"
print("Konci na .pdf:", nazov.endswith(".pdf"))
print("Zacina na dokument:", nazov.startswith("dokument"))