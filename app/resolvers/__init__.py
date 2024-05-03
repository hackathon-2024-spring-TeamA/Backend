from app.resolvers.user.queries import query as user_query
from app.resolvers.user.mutations import mutation as user_mutation

query = [user_query]
mutation = [user_mutation]

# 他の機能を追加する場合は以下のようにまとめる

# from app.resolvers.user.queries import query as user_query
# from app.resolvers.user.mutations import mutation as user_mutation
# from app.resolvers.book.queries import query as book_query
# from app.resolvers.book.mutations import mutation as book_mutation

# query = [user_query, book_query]
# mutation = [user_mutation, book_mutation]