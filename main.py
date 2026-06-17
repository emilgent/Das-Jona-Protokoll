import time
import sys
import os

# --- PERSISTENZ-MODUL ---
def speicherstand_laden():
    if os.path.exists("save.txt"):
        try: return int(open("save.txt", "r").read())
        except: return 0
    return 0

def speicherstand_speichern(anzahl):
    with open("save.txt", "w") as f:
        f.write(str(anzahl))

# --- HILFSFUNKTIONEN ---
def erzähler_text(text, verzögerung=0.015):
    for zeichen in text:
        sys.stdout.write(zeichen)
        sys.stdout.flush()
        time.sleep(verzögerung)
    print("\n")

def check_geheimnis(eingabe, state):
    """Das Easter Egg bleibt komplett unsichtbar im Hintergrund."""
    if eingabe.lower() == "admin":
        erzähler_text("\n>>> [WARNUNG]: UNBEFUGTER OVERRIDE ERKANNT.")
        erzähler_text(">>> REALITÄTS-MATRIX WIRD GEÖFFNET...\n")
        terminal_konsole(state)
        return True
    return False

def terminal_konsole(state):
    erzähler_text("--- CODENAME: REALE_WELT_KONSOLE ---")
    print("[1] Quanten-Tunneling aktivieren (Noclip)")
    print("[2] Dimensions-Sprung ausführen (Jump)")
    print("[3] Konsole schließen")
    befehl = input("Befehl wählen: ")
    
    if befehl == "1":
        state["noclip"] = True
        erzähler_text(">>> Status geändert: Wände sind ab jetzt optional.")
    elif befehl == "2":
        erzähler_text("Ziel-Koordinate eingeben:")
        print("[1] Hauptbüro\n[2] Der sterile Flur\n[3] Chefbüro\n[4] Der tiefe Keller")
        ziel = input("> ")
        if ziel == "1": state["raum"] = "hauptbüro"
        elif ziel == "2": state["raum"] = "flur"
        elif ziel == "3": state["raum"] = "chef"
        elif ziel == "4": state["raum"] = "keller"
        erzähler_text(">>> Teleportation abgeschlossen.")
        state["cheat_sprung"] = True
    else:
        erzähler_text("Exitiere Konsole...")

# --- SPIELRÄUME ---
def spiel_starten():
    spiel_anzahl = speicherstand_laden() + 1
    speicherstand_speichern(spiel_anzahl)
    
    state = {
        "noclip": False, 
        "raum": "hauptbüro",
        "inventar": [],
        "chef_wütend": False,
        "cheat_sprung": False
    }
    
    erzähler_text(f"--- PROTOKOLL RUNDE {spiel_anzahl} ---")
    erzähler_text("Die Geschichte beginnt wie so oft. Jona sitzt an Schreibtisch 427. Die Monitore starren Jona mit gähnender Leere an.")
    erzähler_text("Alle Kollegen sind weg. Einfach weg. Der Erzähler räuspert sich ungeduldig in Jonas Kopf.")
    
    while True:
        if state["raum"] == "hauptbüro":
            raum_hauptbüro(state)
        elif state["raum"] == "flur":
            raum_linker_flur(state)
        elif state["raum"] == "chef":
            raum_chefbüro(state)
        elif state["raum"] == "keller":
            raum_rechter_flur(state)

def raum_hauptbüro(state):
    erzähler_text("\nDu stehst inmitten des riesigen Großraumbüros. Die Stille wird nur vom Summen der Klimaanlage unterbrochen.")
    print("[1] Geh durch die linke Tür (Der Erzähler fleht dich fast schon an).")
    print("[2] Geh durch die rechte Tür in Richtung der düsteren Treppen.")
    print("[3] Durchwühle die Schreibtische der Kollegen.")
    print("[4] Triff eine radikale Entscheidung: Setz dich wieder hin und mach Feierabend.")
    
    wahl = input("> ")
    if check_geheimnis(wahl, state): return
    
    if wahl == "1": 
        state["raum"] = "flur"
    elif wahl == "2": 
        state["raum"] = "keller"
    elif wahl == "3":
        erzähler_text("Du wühlst in den Schubladen von Klaus aus der Buchhaltung. Zwischen alten Kaugummis findest du eine schwere, goldene Büroklammer.")
        state["inventar"].append("Büroklammer")
    elif wahl == "4":
        ende_feierabend()

def raum_linker_flur(state):
    erzähler_text("\nDer Flur verläuft absolut geradlinig. Die Wände sind in einem deprimierenden Behörden-Grau gestrichen.")
    print("[1] Geh weiter geradeaus auf die große, doppelflügelige Tür des Chefs zu.")
    print("[2] Drehe um und gehe zurück ins Hauptbüro.")
    print("[3] Untersuche den verdächtig summenden Getränkeautomaten am Rand.")
    print("[4] Versuche, eines der verschlossenen Fenster aufzuhebeln.")
    
    wahl = input("> ")
    if check_geheimnis(wahl, state): return
    
    if wahl == "1": 
        state["raum"] = "chef"
    elif wahl == "2": 
        state["raum"] = "hauptbüro"
    elif wahl == "3":
        if "Büroklammer" in state["inventar"]:
            erzähler_text("Du benutzt die goldene Büroklammer, um den Münzschlitz zu manipulieren. Der Automat rattert und spuckt eine alte Schlüsselkarte aus!")
            state["inventar"].append("Schlüsselkarte")
        else:
            erzähler_text("Der Automat verlangt Geld. Du hast kein Geld. Der Erzähler seufzt tief über diesen Zeitverlust.")
    elif wahl == "4":
        erzähler_text("Die Fenster sind aus Panzerglas. Du schlägst dir nur die Hand an der Scheibe an. Autsch.")

def raum_chefbüro(state):
    if state["cheat_sprung"]:
        erzähler_text("\nDer Erzähler klingt plötzlich verzerrt: 'Warten Sie... wie sind Sie hierhergekommen? Sie haben die Türen übersprungen!'")
        state["cheat_sprung"] = False
        state["chef_wütend"] = True
    else:
        erzähler_text("\nDas Chefbüro verströmt puren Luxus. Ein gigantischer Schreibtisch steht im Zentrum. Auf ihm leuchtet ein fetter, roter Knopf.")
    
    print("[1] Drücke den einladenden roten Knopf.")
    print("[2] Untersuche den Safe in der Wand hinter dem Gemälde.")
    print("[3] Tritt an das riesige Panorama-Fenster und genieße die Aussicht.")
    print("[4] Geh zurück auf den Flur.")
    
    wahl = input("> ")
    if check_geheimnis(wahl, state): return
    
    if wahl == "1":
        if state["chef_wütend"]:
            ende_paradoxon()
        else:
            ende_explosion()
    elif wahl == "2":
        if "Schlüsselkarte" in state["inventar"]:
            ende_geheimnis()
        else:
            erzähler_text("Der Safe benötigt eine elektronische Schlüsselkarte. Hier blickt dich nur ein roter Scanner an.")
    elif wahl == "3":
        ende_freiheit()
    elif wahl == "4":
        state["raum"] = "flur"

def raum_rechter_flur(state):
    erzähler_text("\nHier unten im Keller riecht es nach feuchtem Beton und alter Wäsche. Die Treppe endet vor einer massiven, fensterlosen Stahltür.")
    print("[1] Versuche, die Stahltür mit roher Gewalt aufzudrücken.")
    print("[2] Folge den dicken Kabeln am Boden, die in eine dunkle Kriechecke führen.")
    print("[3] Geh die Treppe wieder rauf ins sichere Hauptbüro.")
    
    wahl = input("> ")
    if check_geheimnis(wahl, state): return
    
    if wahl == "1":
        if state["noclip"]:
            ende_matrix()
        else:
            erzähler_text("Du wirfst dich gegen die Tür. Sie bewegt sich keinen Millimeter. Dein Ego ist verletzt.")
    elif wahl == "2":
        ende_gefangen()
    elif wahl == "3":
        state["raum"] = "hauptbüro"

# --- DIE EXKLUSIVEN ENDEN ---
def ende_feierabend():
    erzähler_text("\n--- ENDE 1: DER STINKNORMALE FEIERABEND ---")
    erzähler_text("Jona beschloss, dass ungeklärte Mysterien nicht im Arbeitsvertrag standen. Jona packte die Tasche und ging nach Hause.")
    erzähler_text("Ein herrlich ereignisloses Leben wartete auf Jona. Manchmal ist Nichtstun der größte Sieg.")
    sys.exit()

def ende_explosion():
    erzähler_text("\n--- ENDE 2: DER GROSSE RESET ---")
    erzähler_text("Du hast den Knopf gedrückt. Natürlich hast du das. Ein lautes Sirenengeheul ertönt.")
    erzähler_text("Das gesamte Gebäude leitet die Selbstzerstörung ein. Der Erzähler flüstert: 'Warum konntest du nicht einmal hören?'")
    sys.exit()

def ende_freiheit():
    erzähler_text("\n--- ENDE 3: BLICK IN DIE REALE WELT ---")
    erzähler_text("Du schaust aus dem Fenster. Die Stadt unten bewegt sich nicht. Die Autos sind flache Texturen. Die Passanten haben keine Gesichter.")
    erzähler_text("Du erkennst die Wahrheit: Dieses Büro ist deine ganze Welt. Es gibt kein Draußen. Du lächelst, denn nun bist du frei von Illusionen.")
    sys.exit()

def ende_gefangen():
    erzähler_text("\n--- ENDE 4: DIE EWIGE DUNKELHEIT ---")
    erzähler_text("Du kriechst tiefer in die Kabelgänge. Das Licht über dir erlischt. Du verlierst die Orientierung.")
    erzähler_text("Der Erzähler verlässt deinen Kopf: 'Viel Spaß beim Suchen des Ausgangs. Ich suche mir einen neuen Spieler.'")
    sys.exit()

def ende_geheimnis():
    erzähler_text("\n--- ENDE 5: DER UNTERNEHMENS-COUP ---")
    erzähler_text("Der Safe gleitet auf. Darin liegen die Besitzurkunden der Firma – ausgestellt auf deinen Namen!")
    erzähler_text("Du bist jetzt der Chef. Der Erzähler räuspert sich ehrfürchtig: 'Guten Tag, Boss. Was sind Ihre Anweisungen für heute?'")
    sys.exit()

def ende_matrix():
    erzähler_text("\n--- ENDE 6: DER GLITCH IN DER MATRIX ---")
    erzähler_text("Da du die physikalischen Gesetze (Noclip) ausgehebelt hast, drückst du dich mühelos durch die Stahltür.")
    erzähler_text("Hinter der Tür ist... nichts. Ein leerer, weißer Raum. Der unfertige Code des Spiels.")
    erzähler_text("Du hast das Spiel geschlagen, indem du seine Illusion komplett enttarnt hast.")
    sys.exit()

def ende_paradoxon():
    erzähler_text("\n--- ENDE 7: DAS ENTSCHEIDUNGS-PARADOXON ---")
    erzähler_text("Weil du dich ins Chefbüro teleportiert hast, kollidiert das Spielskript mit deiner Position.")
    erzähler_text("Der Erzähler schreit vor Verwirrung. Die Kausalität bricht zusammen. Das Spiel stürzt ab.")
    sys.exit()

if __name__ == "__main__":
    spiel_starten()
