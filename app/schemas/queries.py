type_defs = """
    type Query {
        ### [Mock] ###
        authenticateUser(request: Request!): Response

        ### [リクエスト機能] ###
        paginatedBookRequests(page: Int!, perPage: Int!): PaginationData!
    }
"""