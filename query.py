# query.py
import asyncio
from common import get_rag
from lightrag import QueryParam
from lightrag.kg.shared_storage import initialize_pipeline_status

async def main():
    rag = get_rag()
    await rag.initialize_storages()
    await initialize_pipeline_status()
    pregunta = input("🧠 ¿Qué quieres preguntar? ")
    respuesta = await rag.aquery(pregunta, param=QueryParam(mode="naive"))
    print("\n🔍 Respuesta:")
    print(respuesta)

if __name__ == "__main__":
    asyncio.run(main())
