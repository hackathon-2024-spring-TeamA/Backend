from app.schemas.types import type_defs as types_type_defs
from app.schemas.queries import type_defs as queries_type_defs
from app.schemas.mutations import type_defs as mutations_type_defs

schema_type_defs = [types_type_defs, queries_type_defs, mutations_type_defs]

# 今後機能が増えたら以下のようにまとめることで対応できる

# from app.schemas.user.types import type_defs as user_types_type_defs
# from app.schemas.user.queries import type_defs as user_queries_type_defs
# from app.schemas.user.mutations import type_defs as user_mutations_type_defs

# # 他の機能のtype_defsをインポート
# from app.schemas.book.types import type_defs as book_types_type_defs
# from app.schemas.book.queries import type_defs as book_queries_type_defs
# from app.schemas.book.mutations import type_defs as book_mutations_type_defs

# schema_type_defs = [
#     user_types_type_defs,
#     user_queries_type_defs,
#     user_mutations_type_defs,
#     book_types_type_defs,
#     book_queries_type_defs,
#     book_mutations_type_defs,
#     # 他の機能のtype_defsを追加
# ]