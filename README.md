# Documentación FastAPI
Asegúrese de ejecutar primero el siguiente comando para iniciar su servidor local:
```py
uvicorn main:app --reload
```

- [Swagger Documentation](http://127.0.0.1:8000/docs)
- [ReDoc Documentation](http://127.0.0.1:8000/redoc)
- [OpenAPI Schema](http://127.0.0.1:8000/openapi.json)

# MongoDB

- [Descarga versión community](https://www.mongodb.com/try/download)
- [Instalación](https://www.mongodb.com/docs/manual/tutorial)

### Módulo conexión MongoDB
```cmd
 pip install pymongo
```

### Iniciar servidor local (conexión: mongodb://localhost)
```cmd
cd "C:\Program Files\MongoDB\Server\7.0\bin>"
mongod
```

# Despliegue API en la nube:

- [Deta](https://www.deta.sh/)
- [Intrucciones](https://fastapi.tiangolo.com/deployment/deta/)
