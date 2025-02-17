# Funktionen für Listen-Queue

# Element in die Queue (Liste) hinzufügen
def add_elemte_to_queue(queue, element):
    queue.append(element)
    return queue  

# Erstes Element in der Queue löschen
def first_element(queue):
    q.pop(0)
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
    queue.pop()
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
    print("elementhinzufügen")
    print(q)

    print("Dictionates")
    # Initialisierung eines Dictionary (dict_q)
    dict_q = {}

    #Elemente hinzufügen in Dictionarie
    dict_q = add_element_to_dict_queue(dict_q, "1", {"name": "miralem", "age": 28, "value":1})
    dict_q = add_element_to_dict_queue(dict_q, "2",{"name": "edin", "age": 26, "values":2})
    dict_q = add_element_to_dict_queue(dict_q, "3",{"name": "Lea", "age":24, "values":3})
    print("Dictionary nach dem Hinzufügen von Elementen")
    print(dict_q)

    # Element entfernen
    dict_q = remove_element_dict_queue(dict_q, "3")
    print("Dictionary nach dem Entfernen von '3' Element")
    print(dict_q)

    # Verschachteltes Element in Dictionarie hinzufügen
    dict_q = add_nested_element_to_dict_queue(dict_q, "Verschateltes-element",{"test1":[1, 2, 3], "test2":{"a":10, "b":100}})
    print("Dictionary nach Hinzufügen eines verschachtelten Elements")
    print(dict_q)

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


    # type: ignore