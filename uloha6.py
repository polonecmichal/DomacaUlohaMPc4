
# ============================================================================
# PRÍKLAD 6: Overovanie obsahu stringu
# ============================================================================
"""
Napíšte program, ktorý overí, či string obsahuje iba číslice.
Otestujte na týchto stringoch: "12345", "123abc", "3.14"
Pre každý vypíšte, či je číselný alebo nie.
"""

# Vaše riešenie:
test1 = "12345"
test2 = "123abc"
test3 = "3.14"
string = [test1, test2, test3]
for s in string:
    if s.isdigit():
        print(f"'{s}' je ciselny.")
    else:
        print(f"'{s}' nie je ciselny.")