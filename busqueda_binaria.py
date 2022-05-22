def binaria(lista,x):
    if len(lista)<=0:
        return "Numero no encontrado"
    m = lista[len(lista)//2]
    if m == x:
        return "Numero encontrado"
    else:
        if x < m:
            return binaria(lista[:len(lista)//2],x)
        else:
            return binaria(lista[(len(lista)//2)+1:],x)
lista = [1,2,3]
print (binaria(lista,4))