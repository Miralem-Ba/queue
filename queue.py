# Funktionen für Listen-Queue

# Element in die Queue (Liste) hinzufügen
def add_elemte_to_queue(queue, element):
    queue.append(element)
    return queue  

# Erstes Element in der Queue löschen
def first_element(queue):
    queue.pop(0)
    return queue

# Element zur Queue hinzufügen (doppelte Funktion von add_elemte_to_queue)
def add_element_to_elemente_in_queue(queue, element):
    queue.append(element)
    return queue

# Erstes Element zur Queue hinzufügen
def add_first_element_to_queue(queue, element):
    queue.append(element)
    return queue

# Eine Liste von Elementen zur Queue hinzufügen
def add_list_to_queue(queue, z):
    for bliblablu in z:
        queue.append(bliblablu)
    return queue

# Funktionen für Dictionary-Queue

# Element mit einem Schlüssel in das Dictionary einfügen
def add_element_to_dict_queue(dict_queue, key, element):
    dict_queue[key] = element
    return dict_queue

# Ein verschachteltes Element in das Dictionary einfügen
def add_nested_element_to_dict_queue(dict_queue, key, element):
    dict_queue[key] = element
    return dict_queue

# Element aus dem Dictionary entfernen, falls der Schlüssel existiert
def remove_element_dict_queue(dict_queue, key):
    if key in dict_queue:
        del dict_queue[key]
    return dict_queue

# Ein einzelnes Dictionary-Element zur Speicherung von Daten
thiselement = {
    "name": "miralem",
    "age": 28,
    "value": 1
}

# Element zu einem Set hinzufügen (Set speichert nur einzigartige Werte)
def setelement(queue, element):
    queue.add(element)
    return queue

# Alle Elemente der Queue iterieren und mit "|" getrennt ausgeben
def liste_iterieren(queue):
    for x in queue:
        print(x, end="|")
    return queue

# Ein verschachteltes Element (z. B. eine Liste oder ein Dictionary) zur Queue hinzufügen
def verschachteltes_element(queue, element):
    queue.append(element)
    return queue

# Letztes Element aus der Queue löschen
def elemente_löschen(queue):
    queue.pop(-1)
    return queue

# Dictionaries in Liste aufzeigen 
def list_dict(queue,dict_q):
    queue.append(dict_q)
    return queue

# Set iterieren
def set_iterieren(element):
    for element in my_set:
        print(element, end="|")

# Vereinigung von zwei Sets und Ausgabe der Elemente mit "|" getrennt
def vereinigung_iterieren(set1, set2):
    union_set = set1.union(set2)
    return union_set

# Element entfernen
def remove_first_set_element(my_set):
    my_set.pop()
    return my_set

#Main
if __name__ == "__main__":
    print("main is executed!")

    ## Initialisierung der Queue (Liste)
    q = []
    q = add_elemte_to_queue(q, 1)
    q = add_elemte_to_queue(q, 2)
    q = add_elemte_to_queue(q, 3)
    print("start")
    print(q)

    ## Erstes Element entfernen
    q = first_element(q)
    print("erstes element löschen")
    print(q)

    # Mehrere Elemente hinzufügen
    q = add_element_to_elemente_in_queue(q, 4)
    q = add_element_to_elemente_in_queue(q, 5)
    q = add_element_to_elemente_in_queue(q, 6)
    q = add_element_to_elemente_in_queue(q, 7)
    print("elemente in elemente zu queue hinzufügen")
    print(q)

    # Eine Liste von Elementen zur Queue hinzufügen
    l = [9,8,7]
    q = add_list_to_queue(q,l)
    print("Iterierte Liste")
    print(q)

    # Queue iterieren und ausgeben
    q = liste_iterieren(q)
    print("Liste iterieren")
    print(q)

    # Verschachtelte Elemente hinzufügen
    q = verschachteltes_element(q, 1)
    q = verschachteltes_element(q, 2)
    q = verschachteltes_element(q, [9, 8, 7])
    print("verschachtelte Liste")
    print(q)

    # Letztes Element löschen
    q = elemente_löschen(q)
    print("element löschen")
    print(q)

    # Ein Tupel als Element hinzufügen
    l = (1, 2, 3, 4, 5, 6, 7, 8, 9,)
    q = add_first_element_to_queue(q,l)
    print("element hinzufügen")
    print(q)

    print("Dictionates")

    # Initialisierung eines Dictionary (dict_q)
    dict_q = {}

    #Elemente hinzufügen in Dictionarie
    dict_q = add_element_to_dict_queue(dict_q, 1, {"name": "miralem", "age": 28, "value":1})
    dict_q = add_element_to_dict_queue(dict_q, 2,{"name": "edin", "age": 26, "values":2})
    dict_q = add_element_to_dict_queue(dict_q, 3,{"name": "Lea", "age":24, "values":3})
    print("Dictionary nach dem Hinzufügen von Elementen")
    print(dict_q)

    # Element entfernen
    dict_q = remove_element_dict_queue(dict_q, 3)
    print("Dictionary nach dem Entfernen von '3' Element")
    print(dict_q)

    # Verschachteltes Element in Dictionarie hinzufügen
    dict_q = add_nested_element_to_dict_queue(dict_q, "Verschateltes-element",{"test1":[1, 2, 3], "test2":{"a":10, "b":100}})
    print("Dictionary nach Hinzufügen eines verschachtelten Elements")
    print(dict_q)

    # Ein Dictionary wir erstellt
    d = {"name": "miralem","age":28}
    q = list_dict(q,d)
    print("Dictionarie in Liste")
    print(q)

    # Dictionary bearbeiten (thiselement)
    thiselement
    print("dictionarties{}")
    print(q)

    # Einen Key aus dem Dictionary entfernen
    thiselement.pop("value")
    print("value löschen")
    print(thiselement)
    
    # Neues Key-Value-Paar zum Dictionary hinzufügen
    thiselement["color"] = "green"
    print("farbe hinzufügen")
    print(thiselement)

    # Mehrere Werte im Dictionary aktualisieren
    thiselement.update({"color": "blue", "name": "MiraLem"})
    print("farbe und name ändern")
    print(thiselement)

    # Element aus Set entfernen
    q = elemente_löschen(q)
    print("element löschen")
    print(q)

    # Initialisierung eines Sets
    q = set()

    # Mehrere Elemente zum Set hinzufügen
    q = setelement(q, 6)
    q = setelement(q, 1)
    q = setelement(q, 2)
    q = setelement(q, 3)
    q = setelement(q, 3)
    q = setelement(q, 2)
    q = setelement(q, 1)
    q = setelement(q, 2)
    q = setelement(q, 2)
    q = setelement(q, 5)
    q = setelement(q, 4)
    q = setelement(q, 5)
    q = setelement(q, 6)
    print("set hinzufügen")
    print(q)

    # Set initialisieren
    my_set = set()

    # Mehrere Elemente hinzufügen
    my_set.add(1)
    my_set.add(2)
    my_set.add(2)
    my_set.add(3)
    my_set.add(4)
    my_set.add(5)
    print("Mehrere Elemente hinzufügen")
    print(my_set)
    
    #Erstes Element entfernen in Set
    my_set = remove_first_set_element(my_set)
    print("Erstes Element Löschen")
    print(my_set)

    # Zwei Sets definieren
    set1 = {1, 2, 3, 4}
    set2 = {9, 8, 7, 6}

    # iterieren von set
    my_set = set_iterieren(my_set)
    print("set iterieren")

    # Zusammenfügen von 2 elemente
    my_set = vereinigung_iterieren(set1, set2)
    print("Zusammenfügen von set1 und set2")
    print(my_set)

    # type: ignore