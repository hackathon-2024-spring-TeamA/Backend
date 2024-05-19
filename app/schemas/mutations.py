type_defs = """
    type Mutation {
        ### [Mock] ###
        createUser(request: Request!): String!

        ### [リクエスト機能] ###
        updateBookRequestStatus(requestId: String!, status: String!): BookRequest!
    }
"""