"""
Projekt č.4 Task manager do kurzu Tester s Pythonem od Engeta

author: Jan Páč
email: czjanpac@gmail.com
"""

ukoly = []

def pridat_ukol():
    print("")
    
    while True:
        nazev = input("Zadejte název úkolu: ")
        popis = input("Zadejte popis úkolu: ")

        if not nazev or not popis:
            print("Název i popis úkolu musí být vyplněny, zkuste to znovu.")
            continue

        ukol = f"{nazev} - {popis}"
        ukoly.append(ukol)
        print(f"Úkol ´{nazev}´ byl přidán.")
        break

def zobrazit_ukoly():
    print("""
Seznam úkolů:""")
    
    for index, ukol in enumerate(ukoly, start=1):
        print(f"{index}. {ukol}")

def odstranit_ukol():
    zobrazit_ukoly()
    
    while True:        
        vyber_k_odstraneni = input("Zadejte číslo úkolu, který chcete odstranit: ")
        
        if vyber_k_odstraneni.isdigit():
            vyber_k_odstraneni = int(vyber_k_odstraneni)
            if not 1 <= vyber_k_odstraneni <= len(ukoly):
                print("Neplatná volba.")
                continue
        else:
            print("Neplatná volba.")
            continue
        
        odstraneny_ukol = ukoly.pop(vyber_k_odstraneni - 1)
        nazev_odstraneneho_ukolu = odstraneny_ukol.split(" - ")[0]
        print(f"Úkol ´{nazev_odstraneneho_ukolu}´ byl odstraněn.")
        break

def hlavni_menu():
    while True:
        print("""
Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu""")
        
        vyber_z_menu = input("Vyberte možnost 1-4: ")
        
        if vyber_z_menu.isdigit():
            vyber_z_menu = int(vyber_z_menu)
            if not 1 <= vyber_z_menu <= 4:
                print("Neplatná volba.")
                continue
        else:
            print("Neplatná volba.")
            continue

        # provedení volby
        if vyber_z_menu == 1:
            pridat_ukol()
        elif vyber_z_menu == 2:
            zobrazit_ukoly()
        elif vyber_z_menu == 3:
            odstranit_ukol()
        elif vyber_z_menu == 4:
            print("Konec programu")
            break

hlavni_menu()