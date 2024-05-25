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

    ################### [検索機能] ##################

    type SearchPaginationData {
      totalCount: Int!
      currentPage: Int!
      perPage: Int!
      books: [SearchBook!]!
    }

    type SearchBook {
      id: Int!
      user_id: String!
      book_information: BookInformation!
      donation_date: String!
      latest_book_loan: BookLoan
      latest_book_request: BookRequest
    }

    type BookLoan {
      id: String!
      user_id: String!
      book: Book!
      book_id: Int!
      rent_date: String!
      due_date: String!
      return_date: String
      is_held: Boolean!
    }

    ################### [借りる機能] ##################

    type CreateBookRequestResponse {
      isSuccess: Boolean!
      errorMessage: String
    }

    input CreateBookRequestInput {
      bookId: Int!
      holderId: String!
      requesterId: String!
    }

    ################### [寄付機能] ##################

    type Books {
        id: Int!
        user_id: String!
        book_information_id: Int!
        donation_date: String!
        book_information: BookInformation!
    }

    type SaveBookResponse {
        book: Books
        error: String
    }

    ################### [{}機能] ##################


"""
