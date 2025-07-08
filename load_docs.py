# load_docs.py
import asyncio
from common import get_rag
from lightrag.kg.shared_storage import initialize_pipeline_status
from utils.file_loader import load_documents_from_folder

async def cargar():
    rag = get_rag()
    await rag.initialize_storages()
    await initialize_pipeline_status()

    documentos = load_documents_from_folder("./docs")
    if not documentos:
        print("⚠️ No se encontraron documentos válidos en ./docs")
        return

    await rag.ainsert(documentos)
    print(f"✅ {len(documentos)} fragmentos cargados.")

if __name__ == "__main__":
    asyncio.run(cargar())
