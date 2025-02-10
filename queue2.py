#collections.deque – Eine besondere Liste in Python

from collections import deque       # Importiert deque aus der collections-Bibliothek, um eine doppelseitige Warteschlange zu verwenden
def enqueue(x):                     # Funktion zum Hinzufügen eines Elements zur deque
 q.append(x)                        # Fügt ein Element x ans Ende der Warteschlange hinzu

def dequeue():                      # Funktion zum Entfernen eines Elements aus der deque
 q.popleft()                        # Entfernt das erste Element aus der Warteschlange

q = deque()                         # Erstellung einer deque
enqueue(1)                          # Fügt 1 in die Warteschlange ein
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
dequeue()                           # Entfernt das erste Element
dequeue()