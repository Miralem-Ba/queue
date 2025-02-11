#funktion
def add_elemte_to_queue(queue, element):
    queue.append(element)
    return queue  

def first_element(queue):
    q.pop(0)
    return queue


def add_element_to_elemente_in_queue(queue, element):
    queue.append(element)
    return queue

def setelement(queue, element):
    queue.add(element)
    return queue


thiselement = {
    "name": "miralem",
    "age": 28,
    "value": 1
    
}

def add_list_to_queue(queue, element):
    q.append(element)
    return queue




#Main
if __name__ == "__main__":
    print("main is executed!")
    q = []
    q = add_elemte_to_queue(q, 1)
    q = add_elemte_to_queue(q, 2)
    q = add_elemte_to_queue(q, 3)
    print("start")
    print(q)

    q = first_element(q)
    print("erstes element löschen")
    print(q)

    q = add_element_to_elemente_in_queue(q, 4)
    q = add_element_to_elemente_in_queue(q, 5)
    q = add_element_to_elemente_in_queue(q, 6)
    q = add_element_to_elemente_in_queue(q, 7)
    print("elemente in elemente zu queue hinzufügen")
    print(q)

    
    q = add_list_to_queue(q, 1)
    q = add_list_to_queue(q, 2)
    q = add_list_to_queue(q, [9, 8, 7])
    print("verschachtelte Liste")
    print(q)

    q = set()
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

    thiselement
    print("dictionarties{}")
    print(q)

    thiselement.pop("value")
    print("value löschen")
    print(thiselement)

    thiselement["color"] = "green"
    print("farbe hinzufügen")
    print(thiselement)

    thiselement.update({"color": "blue", "name": "MiraLem"})
    print("farbe und name ändern")
    print(thiselement)