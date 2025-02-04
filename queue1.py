#Die Python Liste
from collections import deque       # Importiert deque aus der collections-Bibliothek
q = deque()                         # Erstellt eine leere deque-Warteschlange

def enqueue(x):                     
    q.append(x)                      # Fügt ein Element x ans Ende der Warteschlange hinzu

def dequeue():
    q.pop(0)                        # Entfernt das erste Element aus der Warteschlange

def front():
    return[0]                       # Fehler: Sollte q[0] zurückgeben, um das erste Element anzuzeigen

def rear():
    i = len(q) -1                   # Berechnet den Index des letzten Elements
    return q[i]                     # Gibt das letzte Element der Warteschlange zurück


q = []
enqueue(1)                          # Fügt 1 in die Warteschlange ein
enqueue(2)
enqueue(3)
front()                             # Zeigt das vordere Element
rear()                              # Zeigt das hintere Element
dequeue()                           # Entfernt das erste Element
dequeue()
