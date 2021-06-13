theme: Simple Merriweather
footer: Topologisches Sortieren  ·  Luca Schultz
slidenumbers: true
build-lists: false

<!-- Folien Generiert mit Deckset: https://www.deckset.com -->

<br/>

# Topologisches Sortieren

#### Präsentationsaufgabe für TdWA

**Luca Schultz**
Rheinische Friedrich-Wilhelms-Universität Bonn
13.07.2021

---

#### Inhalt

---

#### Sortieren von gerichteten Graphen

![right 70%](simple_graphs.pdf)

- Ordnung von Knoten eines **gerichteten**, **asyklischen** Graph
- Für jede gerichtete Kante von Knoten $$a$$ zu Knoten $$b$$ ist Knoten $$a$$ vor Knoten $$b$$ in der Ordnung.
- Zum Beispiel anwendbar:
    + Belegung von Lehrveranstaltungen
    + Softwareentwicklung
    + Task Scheduling

<a name="erster-graph"/>

---

#### Mathematik: Starke Ordnung

- Eine Ordungn $$\prec_R$$ einer Menge $$M$$ ist eine **binäre Relation** $$\prec_R \subseteq M \times M$$
- Eine binäre Relation ist eine **starke Ordnung** genau dann wenn sie folgende Bedingungen erfüllt: 
    1. Irreflexivität: $$\forall a \in M: \neg(a \prec_R a)$$
    2. Transitivität: $$\forall a, b, c \in M: a \prec_R b \land b \prec_R c \implies a \prec_R c$$
    3. Asymetrisch: $$\forall a, b \in M: a \prec_R b \implies \neg(b \prec_R a)$$

---

#### Mathematik: Beispiel für eine starke Ordnung

Beim Graph $$G = (M, \prec_R)$$ auf der [vorherigen Folie](#erster-graph) ist die Menge der Kanten $$\prec_R \subseteq M \times M$$ eine **starke Ordung** auf die Menge der Knoten $$M$$:

- Menge der Knoten: $$M = \{a, b, c, d, e, f \}$$
- Menge der Kanten (Relation): $$\prec_R = \{(a, b), (a, f), (b, c), (c, e), (c, d), (d, f), (d, e) \}$$

---

#### Mathematik: Starke Totalordnung

- Eine starke Ordnung $$\prec_T$$ heißt **starke Totalordnung** genau dann wenn gilt:
    + $$\prec_T$$ ist **linear**: $$\forall a, b \in M: a = b \underline{\lor} a \prec_T b \underline{\lor} b \prec_T a$$
- **Sortieralgorithmus:** Finde zu einer starken Ordnung $$\prec_R \subseteq M \times M$$ auf $$M$$ eine starke Totalordnung $$\prec_T$$ so dass gilt $$\prec_R \subseteq \prec_T$$

---

#### Kahns Sortieralgorithmus: Intuition

Jeder gerichtete, azyklische Graph hat *mindestens* einen Knoten ohne eingehende Kanten (Eingangsgrad $$i = 0$$)

1. Entferne alle Knoten mit $$i = 0$$ und alle Kanten die von ihnen ausgehen
2. Füge die entfernten Knoten in die geordneten Knoten ein
3. Es entstehen neue ungeordnete Knoten mit $$i=0$$
4. Wiederhole bis es keine ungeordneten Knoten mehr gibt

---

#### Datensatz aus der Primärquelle

![inline](tree_structure.pdf)

---

#### Sortierter Datensatz aus der Primärquelle

![inline](tree_sorted.pdf)

---

#### Python: Kahns Sortierlgorithmus

```python
def topologisch_sortieren(unsortierte_knoten: KnotenListe, kanten: KantenListe) -> KnotenListe:
    '''Gib topologisch sortierte KnotenListe aus'''
    sortierte_knoten: KnotenListe = []
    while unsortierte_knoten:
        zyklisch: bool = True
        for knoten in unsortierte_knoten.copy():
            if not kanten_auf(knoten, kanten):
                unsortierte_knoten.remove(knoten)
                sortierte_knoten.append(knoten)
                kanten = ohne_kanten_von(knoten, kanten)
                zyklisch = False
        if zyklisch:
            raise ValueError("Knotenliste enthält zyklische Abhängigkeiten")
    return sortierte_knoten
```

---

#### Python: Vorbereitung für den Algorithmus

![right 130%](data_structure.pdf)

[.code-highlight: all]
[.code-highlight: 1-3]
[.code-highlight: 4-6]
[.code-highlight: 7-10]
[.code-highlight: all]

```python
from random import shuffle
from typing import List, Tuple

# Grundtypen
Knoten = str
Kante = Tuple[str, str]

# Containertypen
KnotenListe = List[Knoten]
KantenListe = List[Kante]
```


---

#### Python: Knoten in `KnotenListe`

```python
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
```

---

#### Python: Kanten in `KantenListe`

```python
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
```

---

#### Python: Hilfsfunktionen

[.code-highlight: all]
[.code-highlight: 1]
[.code-highlight: 3-4]
[.code-highlight: 6]
[.code-highlight: 8-9]
[.code-highlight: all]

```python
def kanten_auf(knoten: Knoten, kanten: KantenListe) -> KantenListe:
    '''Gib KantenListe aus mit allen Kanten die auf `knoten` führen'''
    return [kante for kante in kanten if kante[1] == knoten]


def ohne_kanten_von(knoten: Knoten, kanten: KantenListe) -> KantenListe:
    '''Gib KantenListe aus mit allen Kanten die nicht von `knoten` ausgehen'''
    return [kante for kante in kanten if not kante[0] == knoten]
```

---

#### Python: Die Sortierfunktion

[.code-highlight: all]
[.code-highlight: 1]
[.code-highlight: 3]
[.code-highlight: 4-13]
[.code-highlight: 4]
[.code-highlight: 5]
[.code-highlight: 6-11]
[.code-highlight: 6]
[.code-highlight: 7-11]
[.code-highlight: 7]
[.code-highlight: 8]
[.code-highlight: 9]
[.code-highlight: 10]
[.code-highlight: 11]
[.code-highlight: 12-13]
[.code-highlight: 14]
[.code-highlight: all]

```python
def topologisch_sortieren(unsortierte_knoten: KnotenListe, kanten: KantenListe) -> KnotenListe:
    '''Gib topologisch sortierte KnotenListe aus'''
    sortierte_knoten: KnotenListe = []
    while unsortierte_knoten:
        zyklisch: bool = True
        for knoten in unsortierte_knoten.copy():
            if not kanten_auf(knoten, kanten):
                unsortierte_knoten.remove(knoten)
                sortierte_knoten.append(knoten)
                kanten = ohne_kanten_von(knoten, kanten)
                zyklisch = False
        if zyklisch:
            raise ValueError("Knotenliste enthält zyklische Abhängigkeiten")
    return sortierte_knoten
```

---

#### Python: Aufrufen der Sortierfunktion

[.code-highlight: all]
[.code-highlight: 1-2]
[.code-highlight: 4-7]
[.code-highlight: 9-10]
[.code-highlight: 12-15]
[.code-highlight: all]

```python
# Shuffle nodes
shuffle(unsorted_tasks)

# print shuffled nodes
print("Gemischte Aufgaben:\n" + "=" * 30)
for n, node in enumerate(unsorted_tasks):
    print('{:02d}: {}'.format(n+1, node))

# Sort nodes
sorted_tasks: KnotenListe = topologisch_sortieren(unsortierte_aufgaben, abhängigkeiten)

# Print sorted nodes
print("\nSortierte Aufgaben:\n" + "=" * 30)
for n, node in enumerate(sorted_tasks):
    print('{:02d}: {}'.format(n+1, node))
```

---

#### Python: Ergebnis

![inline](output1.png) ![inline](output2.png) ![inline](output3.png)

---

#### Python: Selber Probieren

---

### Zusammenfassung

---


#### Quellen

---