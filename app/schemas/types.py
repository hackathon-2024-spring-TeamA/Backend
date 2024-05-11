type_defs = """

    ################## [Mock] ##################

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

    ################### [リクエスト機能] ##################

    type BookInformation {
        book_information_id: ID!
        isbn_number: String!
        title: String!
        author: String!
        published_date: String
        description: String
        image_path: String
    }

    type Book {
        id: ID!
        user_id: String!
        book_information: BookInformation!
        donation_date: String!
    }

    type BookRequest {
        id: ID!
        book: Book!
        requester_id: String!
        holder_id: String!
        request_date: String!
        status: String!
    }

    type PaginationData {
        totalCount: Int!
        currentPage: Int!
        perPage: Int!
        bookRequests: [BookRequest!]!
    }

    ################### [{}機能] ##################


"""