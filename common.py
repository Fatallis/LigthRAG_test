# common.py
import os
from dotenv import load_dotenv
from lightrag import LightRAG
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed

load_dotenv()

def get_rag(working_dir: str = None) -> LightRAG:
    work_dir = working_dir or os.getenv("WORKING_DIR", "./lightrag_data")
    return LightRAG(
        working_dir=work_dir,
        llm_model_func=gpt_4o_mini_complete,
        embedding_func=openai_embed
    )
