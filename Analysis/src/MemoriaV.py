# coding=utf-8

#Vectores de direcciones de memoria

#Globales

VecIntGlobal = []
VecFloatGlobal = []
VecBoolGlobal = []
VecStringGlobal = []
#Locales

VecIntLocal = []
VecFloatLocal = []
VecBoolLocal = []
VecStringLocal = []

#Temporales

VecIntTemp = []
VecFloatTemp = []
VecBoolTemp = []
VecStringTemp = []

# rango de direcciones para variables globales
memGlobalInt = 1000
memGlobalIntInicio = 1000
memGlobalFloat = 2000
memGlobalFloatInicio = 2000
memGlobalBool = 3000
memGlobalBoolInicio = 3000
memGlobalString = 4000
memGlobalStringInicio = 4000

# rango de direcciones para variables locales
memLocalInt = 5000
memLocalIntInicio = 5000
memLocalFloat = 6000
memLocalFloatInicio = 6000
memLocalBool = 7000
memLocalBoolInicio = 7000
memLocalString = 8000
memLocalStringInicio = 8000

# rango de irecciones para variables temporales
memIntTemp = 9000
memIntTempInicio = 9000
memFloatTemp = 10000
memFloatTempInicio = 10000
memBoolTemp = 11000
memBoolTempInicio = 11000
memStringTemp = 12000
memStringTempInicio = 12000

def actMemoria(r, tipo, scope):
  
    global memGlobalInt 
    global memGlobalFloat 
    global memGlobalBool 
    global memGlobalString 
    global memLocalInt 
    global memLocalFloat 
    global memLocalBool 
    global memLocalString 

    if scope == 'local':
        if tipo == 'int':
            memLocalInt += (int(r) - 1)
        if tipo == 'float':
            memLocalFloat += (int(r) - 1)
        if tipo == 'bool':
            memLocalBool += (int(r) - 1)
        if tipo == 'string':
            memLocalString += (int(r) - 1)
    else:
        if tipo == 'int':
            memGlobalInt += (int(r) - 1)
        if tipo == 'float':
            memGlobalFloat += (int(r) - 1)
        if tipo == 'bool':
            memGlobalBool += (int(r) - 1)
        if tipo == 'string':
            memGlobalString += (int(r) - 1)

def getScope(dir):
    if dir >= 1000 and dir <= 4999:
        return 'global'
    elif dir >= 5000 and dir <= 8999:
        return 'local'
    else:
        return 'temp'
def setValueLocal(dir,value):
	if dir < 6000:
		if len(VecIntLocal) > dir - 5000:
			VecIntLocal[dir-5000] = value
		else:
			VecIntLocal.append(value)
	elif dir < 7000:
		if len(VecFloatLocal) > dir - 6000:
			VecFloatLocal[dir-6000] = value
		else:
			VecFloatLocal.append(value)
	elif dir < 8000:
		if len(VecBoolLocal) > dir - 7000:
			VecBoolLocal[dir -7000] = value
		else:
			VecBoolLocal.append(value)
	else:
		if len(VecStringLocal) > dir - 8000:
			VecStringLocal[dir-8000] = value
		else:
			VecStringLocal.append(value)

def getValueGlobal(dir):
	if dir < 2000:
		return VecIntGlobal[dir-1000]
	elif dir < 3000:
		return VecFloatGlobal[dir-2000]
	elif dir < 4000:
		return VecBoolGlobal[dir-3000]
	else:
		return VecStringGlobal[dir-4000]

def getValueTemp(dir):
	if dir < 10000:
		return VecIntTemp[dir-9000]
	elif dir < 11000:
		return VecFloatTemp[dir-10000]
	elif dir < 12000:
		return VecBoolTemp[dir-11000]
	else:
		return VecStringTemp[dir-12000]

def getValueLocal(dir):
	if dir < 6000:
		return VecIntLocal[dir-5000]
	elif dir < 7000:
		return VecFloatLocal[dir-6000]
	elif dir < 8000:
		return VecBoolLocal[dir-7000]
	else:
		return VecStringLocal[dir-8000]

def setValueGlobal(dir,value):

	if dir < 2000:
		if len(VecIntGlobal) > dir - 1000:
			VecIntGlobal[dir-1000] = value
		else:
			VecIntGlobal.append(value)
	elif dir < 3000:
		if len(VecFloatGlobal) > dir - 2000:
			VecFloatGlobal[dir-2000] = value
		else:
			VecFloatGlobal.append(value)
	elif dir < 4000:
		if len(VecBoolGlobal) > dir - 3000:
			VecBoolGlobal[dir -3000] = value
		else:
			VecBoolGlobal.append(value)
	else:
		if len(VecStringGlobal) > dir - 4000:
			VecStringGlobal[dir-4000] = value
		else:
			VecStringGlobal.append(value)

def setValueTemporal(dir,value):
	if dir < 10000:
		if len(VecIntTemp) > dir - 9000:	
			VecIntTemp[dir-9000] = value
		else:
			VecIntTemp.append(value)
	elif dir < 11000:
		if len(VecFloatTemp) > dir -10000:
			VecFloatTemp[dir - 10000] = value
		else:
			VecFloatTemp.append(value)
	elif dir < 12000:
		if len(VecBoolTemp) > dir - 11000:
			VecBoolTemp[dir - 11000] = value
		else:
			VecBoolTemp.append(value)
	else:
		if len(VecStringTemp) > dir - 12000:
			VecStringTempp[dir-12000] = value
		else:
			VecStringTemp.append(value)

def getTypeGlobal(dir):
    if dir < memGlobalFloatInicio:
        return 'int'
    elif dir < memGlobalBoolInicio:
        return 'float'
    elif dir < memGlobalStringInicio:
        return 'bool'
    else:
        return 'string'

def getTypeLocal(dir):
    if dir < memLocalFloatInicio:
        return 'int'
    elif dir < memLocalBoolInicio:
        return 'float'
    elif dir < memLocalStringInicio:
        return 'bool'
    else:
        return 'string'


def getTypeTemp(dir):
    if dir < memFloatTempInicio:
        return 'int'
    elif dir < memBoolTempInicio:
        return 'float'
    elif dir < memStringTempInicio:
        return 'bool'
    else:
        return 'string'

def fixType(dir,value):
    if dir >= 1000 and dir <= 1999 or dir >= 5000 and dir <= 5999 or dir >= 9000 and dir <= 9999:
        return int(value)
    elif dir >= 2000 and dir <= 2999 or dir >= 6000 and dir <= 6999 or dir >= 10000 and dir <= 10999:
        return float(value)
    elif dir >= 3000 and dir <= 3999 or dir >= 7000 and dir <= 7999 or dir >= 11000 and dir <= 11999:
        return value
    else:
        return str(value)



# Funcion para asignar una dirección de memoria a una variable global en base a su tipo

def set_dir_global(tipo, cant):
    global memGlobalInt
    global memGlobalFloat
    global memGlobalBool
    global memGlobalString

    assignedDir = None
    if tipo == 'int':
        assignedDir = memGlobalInt
        memGlobalInt += cant
    elif tipo == 'float':
        assignedDir = memGlobalFloat
        memGlobalFloat += cant
    elif tipo == 'bool':
        assignedDir = memGlobalBool
        memGlobalBool += cant
    elif tipo == 'string':
        assignedDir = memGlobalString
        memGlobalString += cant
    return assignedDir

# Función para asignar una dirección de mmeoria a una variable local en base a su tipo

def set_dir_local(tipo, cant):
    global memLocalInt
    global memLocalFloat
    global memLocalBool
    global memLocalString

    assignedDir = None
    if tipo == 'int':
        assignedDir = memLocalInt
        memLocalInt += cant
    elif tipo == 'float':
        assignedDir = memLocalFloat
        memLocalFloat += cant
    elif tipo == 'bool':
        assignedDir = memLocalBool
        memLocalBool += cant
    elif tipo == 'string':
        assignedDir = memLocalString
        memLocalString += cant
    return assignedDir

# Función para generar una dirección de memoria para un temporal de operaciones en los cuadruplos,
# en base a su tipo

def set_dir_temp(tipoTemp):
    global memIntTemp
    global memFloatTemp
    global memBoolTemp
    global memStringTemp

    if tipoTemp == "int":
        assignedTemp = memIntTemp
        memIntTemp += 1
    elif tipoTemp == "float":
        assignedTemp = memFloatTemp
        memFloatTemp += 1
    elif tipoTemp == "bool":
       assignedTemp = memBoolTemp
       memBoolTemp += 1
    elif tipoTemp == "string":
        assignedTemp = memStringTemp
        memStringTemp += 1
    assignedTemp = "(" + str(assignedTemp)    
    return assignedTemp

def get_Total_Temp_Int():
    return memIntTemp - memIntTempInicio


def get_Total_Temp_Float():
    return memFloatTemp - memFloatTempInicio


def get_Total_Temp_Bool():
    return memBoolTemp - memBoolTempInicio


def get_Total_Temp_String():
    return memStringTemp - memStringTempInicio

# Funcion que regresa la variable correspondiente a función y dirección de memoria
def get_var(proc, dire):
    for var, varelems in dirProc[proc]['Vars'].iteritems():
        if varelems['Dir'] == dire:
            return var
