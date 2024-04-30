from fastapi import FastAPI
from ariadne import make_executable_schema
from ariadne.asgi import GraphQL
from app.resolvers.queries import query
from app.resolvers.mutations import mutation
# from app.resolvers.mutations import mutation
from app.schemas import schema_type_defs
from app.db import create_context

app = FastAPI()

schema = make_executable_schema(schema_type_defs, [query, mutation])
graphql_app = GraphQL(schema, debug=True, context_value=create_context)

app.mount("/graphql", graphql_app)