from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ariadne import make_executable_schema
from ariadne.asgi import GraphQL
from app.resolvers import query, mutation# from app.resolvers.mutations import mutation
from app.schemas import schema_type_defs
from app.db import create_context
import logging
import sys

# ログフォーマットの設定
logging.basicConfig(
    level=logging.INFO,  # ログレベルの設定 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

# ロガーの取得
logger = logging.getLogger(__name__)


app = FastAPI()

# CORSの設定を追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

schema = make_executable_schema(schema_type_defs, query + mutation)
graphql_app = GraphQL(schema, debug=True, context_value=create_context)

app.mount("/graphql", graphql_app)
