#Warteschlange mit Priorität – Bestimmte Aufgaben zuerst abarbeiten

from queue import PriorityQueue

def enqueue(p, x):                  # Funktion zum Hinzufügen eines Elements mit Priorität zur PriorityQueue
    q.put(p, x)                     # Fügt das Element x mit Priorität p in die Warteschlange ein

def dequeue():                      # Funktion zum Entfernen des Elements mit der höchsten Priorität
    print(q.get())                  # Entfernt und gibt das Element mit der höchsten Priorität aus

q = PriorityQueue()                 # Erstellung einer PriorityQueue

enqueue(3, 'a')                     # Einfügen von Elementen mit verschiedenen Prioritäten
enqueue(5, 'b')
enqueue(1, 'c')
enqueue(2, 'd')
enqueue(4, 'e')
q.size()                            # Ausgabe der aktuellen Größe der Queue
dequeue()                           # Entfernen der Elemente mit der höchsten Priorität
dequeue()
