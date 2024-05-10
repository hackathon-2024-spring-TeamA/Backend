type_defs = """
    type Query {
        paginatedBookRequests(page: Int!, perPage: Int!): PaginationData!
        authenticateUser(request: Request!): Response
    }
"""