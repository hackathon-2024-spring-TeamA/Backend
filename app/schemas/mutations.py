type_defs = """
    type Mutation {
        ### [Mock] ###
        createUser(request: Request!): String!

        ### [リクエスト機能] ###
        updateBookRequestStatus(requestId: String!, status: String!, userId: String, bookId: Int): BookRequest!

        ### [借りる機能] ###
        createBookRequest(request: CreateBookRequestInput!): CreateBookRequestResponse!
    }
"""