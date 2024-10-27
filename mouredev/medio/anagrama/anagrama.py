def anagrama(palabra_1: str, palabra_2: str)-> bool:
	contador = 0
	palabra_2_lista = []
	for y in palabra_2:
		palabra_2_lista.append(y)
	if palabra_1 == palabra_2:
		return False
	for x in palabra_1:
		if x in palabra_2_lista:
			contador += 1
			palabra_2_lista.remove(x)
		elif x not in palabra_2_lista:
			contador -= 1
	if contador == len(palabra_2):
		return True
	else:
		return False

# La posibilidad simple:

def anagrama(palabra_1: str, palabra_2: str) -> bool:
    
    if palabra_1 == palabra_2:
        return False
    return sorted(palabra_1) == sorted(palabra_2)