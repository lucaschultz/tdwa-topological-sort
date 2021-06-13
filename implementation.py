from random import shuffle
from typing import List, Tuple

# Für verbose Ausführung
import sys
verbose: bool = True if ("-v" in sys.argv or "--verbose" in sys.argv) else False
verboseprint = print if verbose else lambda *a, **k: None

# Grundtypen
Knoten = str
Kante = Tuple[str, str]

# Containertypen
KnotenListe = List[Knoten]
KantenListe = List[Kante]


def kanten_auf(knoten: Knoten, kanten: KantenListe) -> KantenListe:
    '''Gib KantenListe aus mit allen Kanten die auf `knoten` führen'''
    return [kante for kante in kanten if kante[1] == knoten]


def ohne_kanten_von(knoten: Knoten, kanten: KantenListe) -> KantenListe:
    '''Gib KantenListe aus mit allen Kanten die nicht von `knoten` ausgehen'''
    return [kante for kante in kanten if not kante[0] == knoten]


def topologisch_sortieren(unsortierte_knoten: KnotenListe, kanten: KantenListe) -> KnotenListe:
    '''Gib topologisch sortierte KnotenListe aus'''
    sortierte_knoten: KnotenListe = []
    runde: int = 0
    verboseprint('') # Für verbose Ausführung
    while unsortierte_knoten:
        runde += 1 # Für verbose Ausführung
        verboseprint("=" * 70) # Für verbose Ausführung
        verboseprint(f'Beginne Runde: {runde}\n'.upper()) # Für verbose Ausführung
        zyklisch: bool = True
        for knoten in unsortierte_knoten.copy():
            verboseprint("-" * 40) # Für verbose Ausführung
            verboseprint(f'Betrachte Knoten: "{knoten}"') # Für verbose Ausführung
            if not kanten_auf(knoten, kanten):
                verboseprint('Eingehenden Kanten: 0') # Für verbose Ausführung
                unsortierte_knoten.remove(knoten)
                verboseprint('Entfernt aus unsortierten Knoten') # Für verbose Ausführung
                sortierte_knoten.append(knoten)
                verboseprint('Eingefügt in sortierte Knoten') # Für verbose Ausführung
                kanten = ohne_kanten_von(knoten, kanten)
                verboseprint('Alle Kanten gelöscht die vom Knoten ausgehen') # Für verbose Ausführung
                zyklisch = False
            else:
                verboseprint(f'Eingehenden Kanten: {len(kanten_auf(knoten, kanten))}') # Für verbose Ausführung
                verboseprint('Keine weitere Aktion möglich') # Für verbose Ausführung
        if zyklisch:
            raise ValueError("Knotenliste enthält zyklische Abhängigkeiten")
        verboseprint(f'\nBeende Runde: {runde}'.upper()) # Für verbose Ausführung
    return sortierte_knoten


# Alle Aufgaben aus der Primärquelle
unsortierte_aufgaben: KnotenListe = [
    "Cola kaufen",
    "Müll raus bringen",
    "Schuhe putzen",
    "Computer aufbauen",
    "Mathehausaufgabe",
    "In die Stadt fahren",
    "Computer ins Netz bringen",
    "Spülmittel kaufen",
    "Aufgabenblatt drucken",
    "Buch aus Bibo holen",
    "Abwaschen",
    "Internet-Recherche",
    "Deutschaufsatz",
    "Placebo-Song online kaufen",
    "Party-Sampler brennen",
]

# Alle Abhängigkeiten der Aufgaben aus der Primärquelle
abhängigkeiten: KantenListe = [
    ("In die Stadt fahren", "Spülmittel kaufen"),
    ("Spülmittel kaufen", "Abwaschen"),
    ("In die Stadt fahren", "Cola kaufen"),
    ("In die Stadt fahren", "Buch aus Bibo holen"),
    ("Buch aus Bibo holen", "Deutschaufsatz"),
    ("Computer aufbauen", "Computer ins Netz bringen"),
    ("Computer ins Netz bringen", "Internet-Recherche"),
    ("Internet-Recherche", "Deutschaufsatz"),
    ("Computer ins Netz bringen", "Aufgabenblatt drucken"),
    ("Aufgabenblatt drucken", "Mathehausaufgabe"),
    ("Computer ins Netz bringen", "Placebo-Song online kaufen"),
    ("Placebo-Song online kaufen", "Party-Sampler brennen"),
]

# Mische aufgaben
shuffle(unsortierte_aufgaben)

# Gib unsortierte Aufgaben aus
print("Gemischte Aufgaben:\n" + "=" * 30)
for n, node in enumerate(unsortierte_aufgaben):
    print('{:02d}: {}'.format(n+1, node))

# Sortiere Aufgaben
sorted_tasks: KnotenListe = topologisch_sortieren(unsortierte_aufgaben, abhängigkeiten)

# Gib sortierte Aufgaben aus
print("\nSortierte Aufgaben:\n" + "=" * 30)
for n, node in enumerate(sorted_tasks):
    print('{:02d}: {}'.format(n+1, node))
