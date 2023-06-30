from pymongo import MongoClient


class DataBaseManager:
    
    @staticmethod
    def CreateDB(CDBName, CDBHost, CDBPort):
        client = MongoClient(f'mongodb://{CDBHost}:{CDBPort}/')
        
        if CDBHost is None and CDBPort is None:
            client = MongoClient('mongodb://localhost:27017/')       
        db = client[CDBName]
        DataBaseManager.VerifyDB(CDBName, db)
        return db
    
    @staticmethod
    def VerifyDB(name, client: MongoClient):
        if f'{name}' in client.list_database_names():
            print("Created with success")
    
    @staticmethod
    def Connect(ConName, ConHost, ConPort):
        client = MongoClient(f'mongodb://{ConHost}:{ConPort}/')
        db = client[ConName]
        DataBaseManager.VerifyDB(ConName, db)
        return db