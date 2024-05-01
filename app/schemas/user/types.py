type_defs = """
    type User {
        id: ID!
        name: String!
        email: String!
    }

    type Response {
        isSuccess: Boolean!
        errorMessage: String
        data: User
    }

    input Request {
        email: String!
        password: String!
    }
"""