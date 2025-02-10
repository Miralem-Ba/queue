#queue.Queue – Eine Warteschlange in Python

from queue import Queue

q = Queue(maxsize = 5)              # Eine Queue mit einer maximalen Größe von 5 wird erstellt    

def enqueue(x):                     # Funktion zum Hinzufügen eines Elements zur Queue
    q.put(x)                        # Fügt das Element x in die Warteschlange ein

def dequeue():                      # Funktion zum Entfernen eines Elements aus der Queue
    q.get()                         # Entfernt das vorderste Element aus der Warteschlange

q = Queue(maxsize = 5)              # Erneute Erstellung einer Queue mit max. 5 Elementen
enqueue(1)                          # Einfügen von fünf Elementen in die Queue
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
q.qsize()                           # Ausgabe der aktuellen Größe der Queue
dequeue()                           # Entfernen von zwei Elementen aus der Queue
dequeue()
q.qsize()