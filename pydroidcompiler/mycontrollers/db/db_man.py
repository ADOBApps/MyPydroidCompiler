# _*_ coding: utf-8 _*_
"""
Created on 21/06/2022
	Class to manage Data base sqlite3
@author: ADOB
"""

import sqlite3 as sql

class DBMan:

	def __init__ (self):
		print("Calling constructor")

	def __del__ (self):
		class_name = self.__class__.__name__
		print(class_name, "destroyed")

	def createDB(self, db):
		conn = sql.connect(db)
		#Save (commit) the changes
		conn.commit()

		#Close DB connection
		conn.close()

	def createPTable(self, db,table, item1, type1, item2, type2):
		conn = sql.connect(db)
		cursor = conn.cursor()

		#Use f-string to insert var values in sql sentence
		inst = f"CREATE TABLE '{table}'('{item1}' '{type1}', '{item2}' '{type2}')"

		try:
			cursor.execute(inst)
		except:
			print(f"No se pudo crear la tabla '{table}'")

		conn.commit()
		conn.close()

	def createTable(self, db,table):
		conn = sql.connect(db)
		cursor = conn.cursor()

		#Use f-string to insert var values in sql sentence
		inst = f"CREATE TABLE '{table}'(name text,price integer)"

		try:
			cursor.execute(inst)
		except:
			print(f"No se pudo crear la tabla '{table}'")

		conn.commit()
		conn.close()

	def insertRow(self, db, table, name, price):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"INSERT INTO '{table}' VALUES ('{name}', {price})"

		try:
			cursor.execute(inst)
		except:
			print(f"No se pudo insertar el dato en la tabla '{table}'")

		conn.commit()
		conn.close()

	def insertRows(self, db, table, myList):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"INSERT INTO '{table}' VALUES (?, ?)"
		try:
			cursor.executemany(inst, myList)
		except:
			print(f"No se pudo insertar el dato en la tabla '{table}'")
		conn.commit()
		conn.close()

	def readRows(self, db, table):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"SELECT * FROM '{table}'"

		try:
			cursor.execute(inst)
			data = cursor.fetchall()
		except:
			print(f"No se pudo leer los datos de la tabla '{table}'")
		
		conn.commit()
		conn.close()

		#Retorna una lista, los elementos de esta son tuplas
		return data

	#Read data ordered ascendent
	def readOrdered(self, db, table, field):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"SELECT * FROM '{table}' ORDER BY {field}"

		try:
			cursor.execute(inst)
			data = cursor.fetchall()
		except:
			print(f"No se pudo leer los datos de la tabla '{table}'")
		
		conn.commit()
		conn.close()
		#print(data)
		#Retorna una lista, los elementos de esta son tuplas
		return data

	def searchByName(self, db, table, item):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"SELECT * FROM '{table}' WHERE name like '{item}'"

		try:
			cursor.execute(inst)
			data = cursor.fetchall()
		except:
			print(f"No se pudo leer los datos de la tabla '{table}'")
		
		conn.commit()
		conn.close()
		#print(data)
		#Retorna una lista, los elementos de esta son tuplas
		return data

	def searchByLess(self, db, table, item):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"SELECT * FROM '{table}' WHERE price < {item}"

		try:
			cursor.execute(inst)
			data = cursor.fetchall()
		except:
			print(f"No se pudo leer los datos de la tabla '{table}'")
		
		conn.commit()
		conn.close()
		#print(data)
		#Retorna una lista, los elementos de esta son tuplas
		return data

	#Update datum
	def updateDatum(self, db, table, item, price):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"UPDATE '{table}' SET price={price} WHERE name='{item}'"

		try:
			cursor.execute(inst)
		except:
			print(f"No se pudo modificar el valor de {item} de la tabla '{table}'")
		
		conn.commit()
		conn.close()

	#Delete datum
	def deleteRow(self, db, table, item):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst= f"DELETE FROM '{table}' WHERE name='{item}'"

		try:
			cursor.execute(inst)
			conn.commit()
			conn.close()
			return True
		except:
			print(f"No se pudo borrar {item} de la tabla '{table}'")
			conn.commit()
			conn.close()
			return False

	#Create categories
	def createCategory(self, db, table):
		conn = sql.connect(db)
		cursor = conn.cursor()

		#Use f-string
		inst = f"CREATE TABLE '{table}'(name text, price integer, mytype text)"
		try:
			cursor.execute(inst)
		except:
			print(f"No se pudo crear la tabla: {table}")
		conn.commit()
		conn.close()
		
	#Insert vagetables
	def insertVegetable(self, db, table, name, price, mytype):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"INSERT INTO '{table}' VALUES ('{name}', {price}, '{mytype}')"
		try:
			cursor.execute(inst)
		except:
			print(f"No se pudo insertar el dato en la tabla '{table}'")
		conn.commit()
		conn.close()

	#Insert into carrito
	def insertProduct(self, db, table, name, price, mytype):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"INSERT INTO '{table}' VALUES ('{name}', {price}, '{mytype}')"
		try:
			cursor.execute(inst)
			conn.commit()
			conn.close()
			return True
		except:
			print(f"No se pudo insertar el dato en la tabla '{table}'")
			conn.commit()
			conn.close()
			return False

	#Get data info
	def getVegetables(self, db, table):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"SELECT * FROM '{table}'"
		try:
			cursor.execute(inst)
			data = cursor.fetchall()
			for r in data:
				print(r)
		except:
			print(f"No se pudo leer los datos de la tabla '{table}'")
		conn.commit()
		conn.close()
		#Retorna una lista, los elementos de esta son tuplas
		return data

	#get by type
	def getByType(self, db, table, mytype):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"SELECT * FROM '{table}' WHERE mytype='{mytype}'"
		try:
			cursor.execute(inst)
			data = cursor.fetchall()
			for r in data:
				print(r)
		except:
			print(f"No se pudo leer los datos de la tabla '{table}'")
		conn.commit()
		conn.close()

		#Return list of tuples
		return data

	#Get by name
	def getByName(self, db, table, name):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"SELECT * FROM '{table}' WHERE name='{name}'"
		try:
			cursor.execute(inst)
			data = cursor.fetchall()
			for r in data:
				print(r)
		except:
			print(f"No se pudo leer los datos de la tabla '{table}'")
		conn.commit()
		conn.close()

		#Return list of tuples
		return data

	#Update vegetables price
	def updatePrice(self, db, table, item, price):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"UPDATE '{table}' SET price={price} WHERE name='{item}'"

		try:
			cursor.execute(inst)
		except:
			print(f"No se pudo leer los datos de la tabla '{table}'")
		
		conn.commit()
		conn.close()


	#Verify existence of tables
	def verifyDB(self, db, table):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'"
		try:
			listOfTables = cursor.execute(inst).fetchall()
			if listOfTables == []:
				print("No found")
				return False
			else:
				print("Exists")
				return True
		except:
			print("Fatal error")
		conn.commit()
		conn.close()

	#Verify existence of element
	def verifyDatum(self, db, table, element):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"SELECT * FROM '{table}' WHERE name='{element}'"
		try:
			listOfElements = cursor.execute(inst).fetchall()
			if listOfElements:
				print("Exists")
				return True
			else:
				print("No found")
				return False
		except:
			print("Fatal error")
		conn.commit()
		conn.close()


#######################################

# _*_ coding: utf-8 _*_
"""
Created on 18/08/2022
	Class to manage Data base mongodb
@author: ADOB
"""

import pymongo

class MongoMan:

	# Starter class
	def __init__(self, url):
		class_name = self.__class__.__name__
		print(class_name, "Weak up")

		if (url != ""):
			self.client = pymongo.MongoClient(url)
		else:
			self.client = pymongo.MongoClient("mongodb://localhost:27017/")

	# Kill function
	def __del__(self):
		class_name = self.__class__.__name__
		print(class_name, "Finished")

	def createDB(self, db):
		database = self.client[db]

	#Create tables-->collections
	def createTable(self, db, ntable):
		try:
			database = self.client[db]
			if( self.verifyColletion(db, ntable) ):
				print("collection already exists")
			else:
				collection = database[ntable]
		except:
			print(f"No se pudo crear la tabla '{ntable}'")
	def createCollection(self, db, ntable):
		try:
			database = self.client[db]
			if( self.verifyColletion(db, ntable) ):
				print("collection already exists")
			else:
				collection = database[ntable]
		except:
			print(f"No se pudo crear la tabla '{ntable}'")


	# insertDatum(self, databasename, tablename, {})
	def insertDatum(self, db, ntable, jsdata):
		try:
			database = self.client[db]
			collection = database[ntable]
			if( self.verifyDatum(db, ntable, jsdata['name']) ):
				print("Datum already exists")
			else:
				collection.insert_one(jsdata)
		except:
			print(f"No se pudo insetar {jsdata} en la tabla '{ntable}'")

	# insertData(self, databasename, tablename, [{}])
	def insertData(self, db, ntable, jsdata):
		try:
			i = 0
			while( len(jsdata) ):
				self.insertDatum(db, ntable, jsdata[i])
				i=i+1
		except:
			print(f"No se pudo insetar {jsdata} en la tabla '{ntable}'")

	def insertFData(self, db, ntable, jsdata):
		try:
			database = self.client[db]
			collection = database[ntable]
			collection.insert_many(jsdata)
		except:
			print(f"No se pudo insetar {jsdata} en la tabla '{ntable}'")

	# Get datum
	def readDatum(self, db, ntable, query):
		try:
			database = self.client[db]
			collection = database[ntable]
			datum = collection.find(query)

			return datum
		except:
			print(f"No se pudo obtener {query}")
		return datum

	# Get data
	def readData(self, db, ntable):
		try:
			database = self.client[db]
			collection = database[ntable]
			datum = collection.find()
			return datum
		except:
			print(f"No se pudo obtener")
		return datum

	#Read data ordered
	def readOrdered(self, db, ntable, field):
		try:
			database = self.client[db]
			collection = database[ntable]
			datum = collection.find().sort(field)
			return datum
		except:
			print(f"No se pudo leer los datos de la tabla '{ntable}'")
		return datum

	#Get collections, return array with colletion names
	def getColletions(self, db):
		dbcolletions = self.client[db].list_collection_names()
		return dbcolletions

	# Search items
	def searchByName(self, db, ntable, item):
		query = {"name": item}
		try:
			database = self.client[db]
			collection = database[ntable]
			datum = collection.find(query)
			return datum
		except:
			print(f"No se pudo leer los datos de la tabla '{ntable}'")
		return datum

	#Update datum
	def updateDatum(self, db, ntable, criteria, oldval, newval):
		query = {criteria: oldval}
		newvalue = {"$set": {criteria: newval}}
		try:
			database = self.client[db]
			collection = database[ntable]
			collection.update_one(query, newvalue)
			datum = collection.find()
			return datum
		except:
			print(f"No se pudo leer los datos de la tabla '{ntable}'")
		return datum

	#Delete datum
	def deleteDatum(self, db, ntable, query):
		try:
			database = self.client[db]
			collection = database[ntable]
			collection.delete_one(query)
			return True
		except:
			print(f"No se pudo borrar {item} de la tabla '{ntable}'")
			return False

	#Delete data
	def deleteData(self, db, ntable):
		try:
			database = self.client[db]
			collection = database[ntable]
			collection.drop()
			return True
		except:
			print(f"No se pudo borrar {item} de la tabla '{ntable}'")
			return False

	#Delete collections
	def deleteAll(self, db):
		mycols = self.getColletions(db)
		for n in mycols:
			self.deleteData(db, n)

	#Verify database
	def verifyDatabase(self, db):
		databases = self.client.list_database_names()
		if db in databases:
			print("DB exists")
			return True
		else:
			print("DB not found")
			return False

	#Verify collection
	def verifyColletion(self, db, ntable):
		databases = self.client[db].list_collection_names()
		if ntable in databases:
			print("collection exists")
			return True
		else:
			print("collection not found")
			return False

	#Verify datum
	def verifyDatum(self, db, ntable, item):
		registros = self.searchByName(db, ntable, item)
		for x in registros:
			if x != "":
				print(x)
				return True
			else:
				return False