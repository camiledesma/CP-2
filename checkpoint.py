# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

# Recordar utilizar la ruta relativa, no la absoluta para ingestar los datos desde los CSV.
# EJ: 'datasets/xxxxxxxxxx.csv'

from xml.dom.minidom import Entity
import pandas as pd
import numpy as np

def Ret_Pregunta01():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros cuya entidad sean Colombia o México retornando ese valor en un dato de tipo tupla (catidad de registros Colombia, catidad de registros México).
    Pista: averiguar la funcion Shape
    '''
    #Tu código aca:
    df=pd.read_csv(r"C:\Users\lenovo\Desktop\CP05_04_01\datasets/Fuentes_Consumo_Energia.csv", encoding="UTF-8")
    Colom= df["Entity"].value_counts()["Colombia"]
    Mex= df["Entity"].value_counts()["Mexico"]
    tupla=(Colom, Mex)
    return tupla

def Ret_Pregunta02():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe eliminar las columnas 'Code' y 'Entity' y luego informar la cantidad de columnas
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
 
    df=pd.read_csv(r"C:\Users\lenovo\Desktop\CP05_04_01\datasets/Fuentes_Consumo_Energia.csv", encoding="UTF-8")
    col= ["Code", "Entity"]
    df1=df.drop(col, axis=1)
    h=int(df1.shape[1])
    return h

def Ret_Pregunta03():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros de la columna Year sin tener en cuenta aquellos con valores faltantes
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df=pd.read_csv(r"C:\Users\lenovo\Desktop\CP05_04_01\datasets/Fuentes_Consumo_Energia.csv", encoding="UTF-8")
    #df.info()
    #print(df.isna().sum())
#No hay valores faltantes en la columna Year
    Cant_Reg=df["Year"].count()
    Cant_Reg
    return Cant_Reg

def Ret_Pregunta04():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    El ExaJulio es una unidad diferentes al TWh, es decir, no tiene sentido sumarlos o
    buscar proporciones entre ellos, la fórmula de conversión es:
    277.778 Teravatios/Hora (TWh) = 1 Exajulio
    Los campos terminados en "_EJ" corresponden a mediciones en Exajulios,
    y los terminados en "_TWh" corresponden a Teravatios/Hora.
    La consigna es crear un nuevo campo, que se denomine "Consumo_Total"
    y que guarde la sumatoria de todos los consumos expresados en Teravatios/Hora
    (convirtiendo a esta medida los que están en Exajulios)
    Esta función debe informar el consumo total para la entidad 'World' y año '2019',
    redondeado a 2 decimales, retornando ese valor en un dato de tipo float.
    '''
    #Tu código aca:
    #return 'Funcion incompleta'

def Ret_Pregunta05():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar el año de mayor generación de energía hídrica (Hydro_Generation_TWh)
    para la entidad 'Europe' retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df=pd.read_csv(r"C:\Users\lenovo\Desktop\CP05_04_01\datasets/Fuentes_Consumo_Energia.csv", encoding="UTF-8")
    Europa=df[df["Entity"]=="Europe"]
    Energia_Europa=Europa["Year"][Europa["Hydro_Generation_TWh"].idxmax()]
    return Energia_Europa

def Ret_Pregunta06(m1, m2, m3):
    '''
    Esta función recibe tres array de Numpy de 2 dimensiones cada uno, y devuelve el valor booleano
    True si es posible realizar una multiplicación entre las tres matrices (n1 x n2 x n3),
    y el valor booleano False si no lo es
    Ej:
        n1 = np.array([[0,0,0],[1,1,1],[2,2,2]])
        n2 = np.array([[3,3],[4,4],[5,5]])
        n3 = np.array([1,1],[2,2])
        print(Ret_Pregunta06(n1,n2,n3))
            True            -> Valor devuelto por la función en este ejemplo
        print(Ret_Pregunta06(n2,n1,n3))
            False            -> Valor devuelto por la función en este ejemplo
    '''
    #Tu código aca:
    m1 = np.array([[0,0,0],[1,1,1],[2,2,2]])
    m2 = np.array([[3,3],[4,4],[5,5]])
    m3 = np.array([[1,1],[2,2]])
    if (m1.shape[1] == m2.shape[0] and m2.shape[1] == m3.shape[0]):
        return True
    else:
        return False
    

def Ret_Pregunta07():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "GGAL - Cotizaciones historicas.csv". Este csv contiene información de cotización de la 
    acción del Banco Galcia SA. Esta función debe tomar la columna máximo y 
    devolver la suma de los valores de esta, con 4 decimales después del punto, redondeado.
    '''
    #Tu código aca:
    df=pd.read_csv(r"C:\Users\lenovo\Desktop\CP05_04_01\datasets/GGAL - Cotizaciones historicas.csv", encoding="UTF-8")
    Suma=df["maximo"].sum()
    Suma_con_4_decimales= round(Suma,4)
    return Suma_con_4_decimales

def Ret_Pregunta08():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de entidades diferentes que están presentes en el dataset
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df=pd.read_csv(r"C:\Users\lenovo\Desktop\CP05_04_01\datasets/Fuentes_Consumo_Energia.csv", encoding="UTF-8")
    Entidades= df["Entity"].unique()
    Cantidad_De_Entidades= len(Entidades)
    return Cantidad_De_Entidades

def Ret_Pregunta09():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Tabla1_ejercicio.csv" y "datasets/Tabla2_ejercicio.csv".
    Esta función debe retornar: score_promedio_femenino y score_promedio_masculino en formato tupla, teniendo en cuenta que no debe haber valores repetidos.'''
    #Tu código aca:
    #return 'Funcion incompleta'

def Ret_Pregunta10(lista):
    '''
    Esta función recibe como parámetro un objeto de la clase Lista() definida en el archivo Lista.py.
    Debe recorrer la lista y retornan la cantidad de nodos que posee. Utilizar el método de la clase
    Lista llamado getCabecera()
    Ejemplo:
        lis = Lista()
        lista.agregarElemento(1)
        lista.agregarElemento(2)
        lista.agregarElemento(3)
        print(Ret_Pregunta10(lista))
            3    -> Debe ser el valor devuelto por la función Ret_Pregunta10() en este ejemplo
    '''
    #Tu código aca:
    #return 'Funcion incompleta
