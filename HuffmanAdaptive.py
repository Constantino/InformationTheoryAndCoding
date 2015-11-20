#!/usr/bin/python
import string
import time
import random
import operator
from random import choice

#DEBUG = True
DEBUG = False

class Nodo:
    """nodo hoja
    """
    def __init__(self, simbolo, peso):
        self.simbolo = simbolo
        self.peso = peso
        self.der = None
        self.izq = None
        self.padre = None

def actualiza_arbol(frec):
    """hace el arbol de acuerdo a las frecuencias
    regresa la raiz del arbol
    """
    nodos = []
    ordenados = sorted(frec, key=frec.get)
    for i in ordenados:
        nodos.append(Nodo(i, frec[i]))
    while True:
        if len(nodos)>1:
            izq = nodos[0]
            nodos = nodos[1:]
            der = nodos[0]
            nodos = nodos[1:]
            x = Nodo(str(izq.simbolo)+str(der.simbolo), izq.peso + der.peso)
            x.izq = izq
            x.der = der
            nodos.append(x)
            der.padre = x
            izq.padre = x
            nodos = sorted(nodos, key=lambda x: x.peso)
            if DEBUG:
                print "*papa %s %s, *izq %s %s *der %s %s" %(x.peso, x.simbolo, 
                                                            x.izq.peso,x.izq.simbolo, 
                                                            x.der.peso,x.der.simbolo)
        elif len(nodos)==1:
            padre = Nodo(str(izq.simbolo)+str(der.simbolo), izq.peso + der.peso)
            padre.izq = izq
            padre.der = der
            nodos = []
            if DEBUG:
                print "*papa %s %s, *izq %s %s *der %s %s" %(padre.peso, padre.simbolo, padre.izq.peso,padre.izq.simbolo, padre.der.peso, padre.der.simbolo)
        else:
            break
    return padre

def decodificar(raiz):
    """decodifica
    """
    f = open("frase_codificada.txt")
    frase_codificada = f.read()
    #print frase_codificada
    frase_encontrada = ""
    padre = raiz
    while len(frase_codificada)>0:
        s = str(frase_codificada[0])
        frase_codificada = frase_codificada[1:]
        if s == "0":
            raiz = raiz.der
        else:
            raiz = raiz.izq
        if raiz.der == None and raiz.izq == None:
            frase_encontrada = frase_encontrada+raiz.simbolo
            raiz = padre
    return frase_encontrada


def codigos(hojas):
    """obtiene los codigos haciendo un recorrido desde la
    hoja a la raiz
    """
    lista = []
    dic = {}
    for i in hojas:
        byte = ""
        padre = i.padre
        actual = i
        while True:
            if padre:
                pass
            else:
                break
            if actual == padre.izq:
                byte = byte + "1"
            else:
                byte = byte + "0"
            actual = padre
            padre = padre.padre
        lista.append((i.simbolo, i.peso, byte[::-1]))
        dic[i.simbolo]=byte[::-1]
    if DEBUG:
        print lista, dic
    return lista, dic

def obtiene_hojas(nodos):
    """obtiene las hojas del arbol, recibe como entrada
    toda la lista de nodos
    """
    hojas = []
    for nodo in nodos:
        if nodo.der == None and nodo.izq == None:
            hojas.append(nodo)
    if DEBUG:
        print "Numero de hojas %s" %(len(hojas))
    return hojas

def recorrer(padre, lista_nodos, lista_pesos):
    """recorrido en preorden solo para obtener la lista de
    todos los nodos
    """
    if padre != None:
        lista_nodos.append(padre)
        lista_pesos.append(padre.peso)
        recorrer(padre.izq, lista_nodos, lista_pesos)
        recorrer(padre.der, lista_nodos, lista_pesos)
    return lista_nodos, lista_pesos


def escribe_codigos(frase, codigos):
    """escribe la frase codificada
    """
    f = open("frase_codificada.txt", "w")
    for i in frase:
        try:
            f.write("%s" %codigos[i])
        except:
            pass
    f = open("frase_codificada.txt")
    texto = f.read()
    f.close()
    return len(texto)

def escribe_tabla(codigos):
    """escribe el diccionario en un archivo
    """
    f = open("tabla_frecuencias.txt", "w")
    for i in codigos:
        f.write("%s %s\n" %(i[0], i[2]))


def frecuencia(frase, frec):
    """obtiene la frecuencia de los simbolos
    en la frase
    """
    frec_temp = {}
    for l in frase:
        if not(l in frec_temp):
            frec_temp[l] = frase.count(l)
    frec = dict([(n, frec.get(n, 0)+frec_temp.get(n, 0)) for n in set(frec)|set(frec_temp)])
    return frec

def leer_texto():
    """
    """
    f = open("texto.txt")
    texto = f.read()
    texto = texto.replace("\n","")
    return texto

def genera_dist_unif(n):
    """
    """
    texto = ''
    caracteres = list(string.printable[:80])
    for i in range(n):
        texto += choice(list(string.printable[:80]))
    return texto

def pasos(texto, paso):
    frec = {}
    for i in range(0,len(texto), paso):
        fragmento = texto[i:i+paso]
        frec = frecuencia(fragmento, frec)
        raiz = actualiza_arbol(frec)
        #recorrido en preorden
        lista_pesos = []
        lista_nodos = []
        lista_nodos, lista_pesos = recorrer(raiz, lista_nodos, lista_pesos)
        print "Recorrido en preorden %s" %lista_pesos
        #obtengo hojas del arbol
        hojas = obtiene_hojas(lista_nodos)
        #se obtienen los codigos para cada simbolo
        lista_codigos, dic_codigos = codigos(hojas)
        #se escribe una tabla con sus frecuencias
        escribe_tabla(lista_codigos)
        #se pasa el texto normal a los codigos encontrados
        len_codificado = escribe_codigos(texto, dic_codigos)
        #se decodifica
        frase_decodificada = decodificar(raiz)
        print "La frase encontrada: %s" %frase_decodificada
        

def huffman_adaptativo(texto):
    """experimento
    """
    inicio = time.time()
    x = []
    y = []
    for i in range(3, 10000, 100):
        paso = i
        inicio = time.time()
        pasos(texto, paso)
        total = time.time()-inicio
        print i, total
        x.append(i)
        y.append(total)
    return x, y

def main():
    texto = leer_texto()
    x1,y1 = huffman_adaptativo(texto)
    #texto = genera_dist_unif(len(texto))
    #x2,y2 = huffman_adaptativo(texto)

main()