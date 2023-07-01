from pymongo import MongoClient
from bson.objectid import ObjectId

class DataBaseManager:
    
    def CreateDB(self, CDBName, CDBHost, CDBPort):
        if CDBHost == '' and CDBPort == '':
            CDBHost = 'localhost'
            CDBPort = 27017
        
        client = MongoClient(f'mongodb://{CDBHost}:{CDBPort}/')
        db = client[CDBName]
        
        # Verificar a conexão com o banco de dados
        try:
            client.server_info()
            print('Conexão com o banco de dados estabelecida com sucesso.')
        except Exception as e:
            print(f'Erro ao conectar ao banco de dados: {e}')
        
        return db
    
    def Connect(self, ConName, ConHost, ConPort):
        client = MongoClient(f'mongodb://{ConHost}:{ConPort}/')
        db = client[ConName]
        
        # Verificar a conexão com o banco de dados
        try:
            client.server_info()
            print('Conexão com o banco de dados estabelecida com sucesso.')
        except Exception as e:
            print(f'Erro ao conectar ao banco de dados: {e}')
        
        return db
# CRUD para a coleção 'marca'
class MarcaDAO:
    def __init__(self, db):
        self.collection = db['marca']

    def add(self, marca):
        return self.collection.insert_one(marca).inserted_id

    def delete(self, id):
        filter = {'_id': ObjectId(id)}
        result = self.collection.delete_one(filter)
        if result.deleted_count > 0:
            return True
        else:
            return False

    def update(self, id, nome):
        filter = {'_id': ObjectId(id)}
        update = {'$set': {'nome': nome}}
        result = self.collection.update_one(filter, update)
        if result.modified_count > 0:
            return True
        else:
            return False

    def getById(self, id):
        objI = ObjectId(id)
        return self.collection.find_one({'_id': objI})

    def getAll(self):
        return list(self.collection.find())


# CRUD para a coleção 'modelo'
class ModeloDAO:
    def __init__(self, db):
        self.collection = db['modelo']

    def add(self, modelo):
        return self.collection.insert_one(modelo).inserted_id

    def edit(self, id, modelo):
        return self.collection.update_one({'_id': id}, {'$set': modelo}).modified_count

    def delete(self, id):
        return self.collection.delete_one({'_id': id}).deleted_count

    def getById(self, id):
        return self.collection.find_one({'_id': id})

    def getAll(self):
        return list(self.collection.find())


# CRUD para a coleção 'carro'
class CarroDAO:
    def __init__(self, db):
        self.collection = db['carro']

    def add(self, carro):
        return self.collection.insert_one(carro).inserted_id

    def edit(self, id, carro):
        return self.collection.update_one({'_id': id}, {'$set': carro}).modified_count

    def delete(self, id):
        return self.collection.delete_one({'_id': id}).deleted_count

    def getById(self, id):
        return self.collection.find_one({'_id': id})

    def getAll(self):
        return list(self.collection.find())