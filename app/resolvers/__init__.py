# from app.resolvers.user.queries import query as user_query
# from app.resolvers.user.mutations import mutation as user_mutation

# query = [user_query]
# mutation = [user_mutation]

# 他の機能を追加する場合は以下のようにまとめる

from app.resolvers.user.queries import query as user_query
from app.resolvers.user.mutations import mutation as user_mutation
from app.resolvers.request.queries import query as request_query
from app.resolvers.request.mutations import mutation as request_mutation
from app.resolvers.search.queries import query as search_query
from app.resolvers.loan.mutations import mutation as loan_mutation

query = [user_query, request_query, search_query]
mutation = [user_mutation, request_mutation, loan_mutation]