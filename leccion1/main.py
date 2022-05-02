# ¿Qué mes se ha gastado más?
# ¿Qué mes se ha ahorrado más?
# ¿Cuál es la media de gastos al año?
# ¿Cuál ha sido el gasto total a lo largo del año?
# ¿Cuáles han sido los ingresos totales a lo largo del año?
# Opcional: Realice una gráfica de la evolución de ingresos a lo largo del año .
'''----------------------------------------------------------------------'''
# Compruebe que el fichero existe y que tiene 12 columnas, una para
# cada mes del año.
# Para cada mes compruebe que hay contenido.
# Compruebe que todos los datos son correctos. De no haber un dato
# correcto, el programa debe saber actuar en consecuencia y continuar
# con su ejecución.


import pandas as pd

class ColumnException(Exception):
    def __init__(self, param) :
        self.param = param
        if self.param != 12:
            print("El fichero no tiene 12 Columnas")
def Sum(list): 
    neg_sum = 0
    pos_sum = 0
    ahorro = 0
    for num in list:
        num = int(num) 
        if(num < 0): 
            neg_sum += num 
        
        else:      
            pos_sum += num 
    ahorro = neg_sum + pos_sum

    return neg_sum, pos_sum, ahorro


try:
    df = pd.read_csv("./leccion1/finanzas2020.csv", sep="\t")
    df2 = pd.DataFrame() #Para tratar datos
    columns = ['Gastos','Ingresos','Ahorro']
    dfTotales = pd.DataFrame(columns=columns,index=df.columns.values)
    df['Enero'] = df['Enero'].str.replace('\'','') #Corrige error de valor en Enero
    df['Julio'] = df['Julio'].str.replace('\'','') #Corrige error de valor en Julio
    df['Noviembre'] = df['Noviembre'].str.replace('\'','') #Corrige error de valor en Noviembre
    df['Septiembre'] = df['Septiembre'].str.replace(r'[a-zA-Z]{2,4}', '0')
    df['Octubre'] = df['Octubre'].str.replace(r'[a-zA-Z]{2,4}', '0') #corrige si tiene letras y las pase valor 0
    
    gastosE,ingresosE,ahorroE = Sum(df['Enero'])
    gastosF,ingresosF,ahorroF = Sum(df['Febrero'])
    gastosM,ingresosM,ahorroM = Sum(df['Marzo'])
    gastosA,ingresosA,ahorroA= Sum(df['Abril'])
    gastosMa,ingresosMa,ahorroMa = Sum(df['Mayo'])
    gastosJu,ingresosJu,ahorroJu = Sum(df['Junio'])
    gastosJul,ingresosJul,ahorroJul = Sum(df['Julio'])
    gastosAgo,ingresosAgo,ahorroAgo = Sum(df['Agosto'])
    gastosSe,ingresosSe,ahorroSe = Sum(df['Septiembre'])
    gastosOC,ingresosOC,ahorroOC = Sum(df['Octubre'])
    gastosNov,ingresosNov,ahorroNov = Sum(df['Noviembre'])
    gastosDic,ingresosDic,ahorroDic = Sum(df['Diciembre'])

    dfTotales = dfTotales.assign(Gastos = [gastosE,gastosF,gastosM,gastosA,gastosMa,gastosJu,gastosJul,gastosAgo,gastosSe,gastosOC,gastosNov,gastosDic,])
    dfTotales = dfTotales.assign(Ingresos = [ingresosE,ingresosF,ingresosM,ingresosA,ingresosMa,ingresosJu,ingresosJul,ingresosAgo,ingresosSe,ingresosOC,ingresosNov,ingresosDic])
    dfTotales = dfTotales.assign(Ahorro = [ahorroE,ahorroF,ahorroM,ahorroA,ahorroMa,ahorroJu,ahorroJul,ahorroAgo,ahorroSe,ahorroOC,ahorroNov,ahorroDic])
    
    '''Mes Con más Gastos'''
    print("\n")
    print(f"Mes Con más Gastos: {dfTotales['Gastos'].idxmin()} -> {dfTotales['Gastos'].min()}" )
    '''------------------'''
    '''Mes Con más Ahorro'''
    print(f"Mes Con más Ahorro: {dfTotales['Ahorro'].idxmax()} -> {dfTotales['Ahorro'].max()}" )
    '''------------------'''
    '''Media de gastos'''
    print(f"Media de Gastos del año: {round(dfTotales['Gastos'].mean(),2)} " )
    '''------------------'''
    '''Total en Gastos'''
    print(f"Total Gastos en el año: {dfTotales['Gastos'].sum()} " )
    '''------------------'''
    '''Total en Ingresos'''
    print(f"Total Gastos en el año: {dfTotales['Ingresos'].sum()} " )
    print("\n")
    '''------------------'''
    
except IOError as e:
    print(e)
except ColumnException as error:
    print(error)
except ValueError as e:
    print(e)


    




