INSERT INTO users (user_id, email, password, nickname, created_at, updated_at, updated_by, is_delete)
VALUES
    ('a1b2c3d4-e5f6-7890-1234-567890abcdef', 'user1@example.com', 'password123', 'User One', NOW(), NOW(), NULL, 0),
    ('fedcba09-8765-4321-0987-654321fedcba', 'user2@example.com', 'password456', 'User Two', NOW(), NOW(), NULL, 0),
    ('fedcba09-8765-4321-0987-654321fe8888', 'user3@example.com', 'password789', 'User Three', NOW(), NOW(), NULL, 0);

INSERT INTO book_informations (book_information_id, isbn_number, title, author, published_date, description, image_path)
VALUES
    (1, '9784798141746', 'リーダブルコード', 'Dustin Boswell, Trevor Foucher', '2012-04-26', '読みやすくて保守しやすいコードの書き方を学ぶ', 'http://books.google.com/books/content?id=Wx1dLwEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api'),
    (2, '9784774180343', '達人プログラマー', 'Andrew Hunt, David Thomas', '2005-02-25', 'ソフトウェア開発の職人技を学ぶ', 'http://books.google.com/books/content?id=i0ozAwAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api'),
    (3, '8888888888888', 'Golang', 'Me', '2005-02-25', 'Golangを学ぶ', 'http://books.google.com/books/content?id=ba4IEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api');

INSERT INTO books (id, user_id, book_information_id, donation_date)
VALUES
    (1, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 1, '2023-05-01'),
    (2, 'fedcba09-8765-4321-0987-654321fedcba', 2, '2023-06-01'),
    (3, 'fedcba09-8765-4321-0987-654321fe8888', 3, '2023-07-01');

INSERT INTO book_requests (id, book_id, requester_id, holder_id, request_date, status)
VALUES
    ("a1b2c3d4-e5f6-7890-1234-567890a88888", 1, 'fedcba09-8765-4321-0987-654321fedcba', 'a1b2c3d4-e5f6-7890-1234-567890abcdef', '2023-07-01', 'requested'),
    ("a1b2c3d4-e5f6-7890-1234-567888888888", 2, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 'fedcba09-8765-4321-0987-654321fedcba', '2023-08-01', 'sending'),
    ("a1b2c3d4-e5f6-7890-1234-568888888888", 3, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 'fedcba09-8765-4321-0987-654321fedcba', '2023-09-17', 'arrived');

INSERT INTO book_loans (id, user_id, book_id, rent_date, due_date, return_date, is_held)
VALUES
    ("8888c3d4-e5f6-7890-1234-567890abcdef", 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 1, '2023-07-15', '2023-08-15', NULL, 1),
    ("888888d4-e5f6-7890-1234-567890abcdef", 'fedcba09-8765-4321-0987-654321fedcba', 2, '2023-08-15', '2023-09-15', NULL, 1),
    ("888888d4-e5f6-8888-1234-567890abcdef", 'fedcba09-8765-4321-0987-654321fedcba', 3, '2023-08-16', '2023-09-16', '2023-09-18', 0);

