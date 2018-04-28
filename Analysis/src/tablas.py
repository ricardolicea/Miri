# coding=utf-8

#Diccionarios de memoria

DicMemoria = {'Global': {}, 'Local': {}, 'Temp': {}, 'Const': {} } 
DicMemoria['Global'] = {'Int':{}, 'Float': {}, 'Bool': {}, 'String': {}}
DicMemoria['Global']['Int'] = {'Pos': pos, 'Dir': self.dir, 'Value': val}


# rango de direcciones para variables globales

memGlobalInt = 1
memGlobalIntInicio = 1
memGlobalFloat = 1000
memGlobalFloatInicio = 1000
memGlobalBool = 2000
memGlobalBoolInicio = 2000
memGlobalString = 3000
memGlobalStringInicio = 3000

#rango de direcciones para variables locales
memLocalInt = 4000
memLocalIntInicio = 4000
memLocalFloat = 5000
memLocalFloatInicio = 5000
memLocalBool = 6000
memLocalBoolInicio = 6000
memLocalString = 7000
memLocalStringInicio = 7000

#rango de irecciones para variables temporales
memIntTemp = 8000
memIntTempInicio = 8000
memFloatTemp = 9000
memFloatTempInicio = 9000
memBoolTemp = 10000
memBoolTempInicio = 10000
memStringTemp = 11000
memStringTempInicio = 11000

#Rango de direcciones para constantes
memConstInt = 12000
memConstIntInicio = 12000
memConstFloat = 13000
memConstFloatInicio = 13000
memConstBool = 14000
memConstBoolInicio = 14000
memConstString = 15000
memConstStringInicio = 15000

def setValueGlobal(dir,value)
	if dir < memGlobalFloatInicio
	






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

def getTypeConst(dir):
	if dir < memConstFloatInicio:
		return 'int'
	elif dir < memConstBoolInicio:
		return 'float'
	elif dir < memConstStringInicio:
		return 'bool'
	else:
		return 'string'
	

#Funcion para asignar una dirección de memoria a una variable global en base a su tipo
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



#Función para asignar una dirección de mmeoria a una variable local en base a su tipo
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


#Función para generar una dirección de memoria para un temporal de operaciones en los cuadruplos, 
#en base a su tipo
def set_dir_temp(tipoTemp):
	global memIntTemp
	global memFloatTemp
	global memBoolTemp
	global memStringTemp

	if tipoTemp == "int":
		memIntTemp += 1
		dirTemp  = memIntTemp
	elif tipoTemp == "float":
		memFloatTemp +=1
		dirTemp = memFloatTemp
	elif tipoTemp == "bool":
		memBoolTemp +=1
		dirTemp = memBoolTemp
	elif tipoTemp == "String":
		memStringTemp +=1
		dirTemp = memStringTemp
	return dirTemp

#Funcion para generar una direccion de memoria para una constante 
def set_dir_const(tipo,cant):
	global memConstBool
	global memConstFloat
	global memConstInt
	global memConstString

	assignedDir = None
	
	if tipo == 'int':
		assignedDir = memConstInt
		memConstInt += cant
	elif tipo == 'bool':
		assignedDir = memConstBool
		memConstBool += cant 
	elif tipo == 'float':
		assignedDir = memConstFloat
		memConstFloat += cant 
	elif tipo == 'string':
		assignedDir = memConstString
		memConstString += cant 

def get_Total_Temp_Int():
	return memIntTemp - memIntTempInicio

def get_Total_Temp_Float():
	return memFloatTemp - memFloatTempInicio

def get_Total_Temp_Bool():
	return memBoolTemp - memBoolTempInicio

def get_Total_Temp_String():
	return memStringTemp - memStringTempInicio

#Funcion que regresa la variable correspondiente a función y dirección de memoria
def get_var(proc, dire):
	for var, varelems in dirProc[proc]['Vars'].iteritems():
		if varelems['Dir'] == dire:
			return var
