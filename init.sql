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


-----------------------
-----------------------
-- 追加
-----------------------
-----------------------

-- book_informationsテーブルにデータを追加
INSERT INTO book_informations (book_information_id, isbn_number, title, author, published_date, description, image_path)
VALUES
(4, '9784873115658', 'EffectiveJava第2版', 'JoshuaBloch', '2015-03-19', 'JavaSE7/8に対応した、Javaプログラミングのベストプラクティス', 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974&q=80'),
(5, '9784873117584', 'Kotlinスタートブック', '長澤太郎', '2020-08-07', 'Kotlinの基本文法やオブジェクト指向プログラミングの概念を学ぶ', 'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80'),
(6, '9784774193977', 'Pythonによるデータ分析入門', 'WesMcKinney', '2018-06-29', 'Pythonを使ったデータ分析の基礎から応用までを解説', 'https://images.unsplash.com/photo-1532012197267-da84d127e765?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80'),
(7, '9784873118888', 'Rustプログラミング入門', 'SteveKlabnik, CarolNichols', '2021-11-25', 'Rustプログラミング言語の基本的な使い方を学ぶ', 'https://images.unsplash.com/photo-1618477388954-7852f32655ec?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80'),
(8, '9784295013754', 'テスト駆動開発', 'KentBeck', '2017-10-14', 'テスト駆動開発の基本的な考え方とテクニックを学ぶ', 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80'),
(9, '9784798160191', 'リーンスタートアップ', 'EricRies', '2012-04-07', 'スタートアップのための製品開発とビジネスモデルの構築方法を学ぶ', 'https://images.unsplash.com/photo-1586281380117-5a60ae2050cc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80');

-- booksテーブルにデータを追加
INSERT INTO books (id, user_id, book_information_id, donation_date)
VALUES
(4, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 4, '2023-10-01'),
(5, 'fedcba09-8765-4321-0987-654321fedcba', 5, '2023-11-01'),
(6, 'fedcba09-8765-4321-0987-654321fe8888', 6, '2023-12-01'),
(7, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 7, '2024-01-01'),
(8, 'fedcba09-8765-4321-0987-654321fedcba', 8, '2024-02-01'),
(9, 'fedcba09-8765-4321-0987-654321fe8888', 9, '2024-03-01');

-- book_requestsテーブルにデータを追加
INSERT INTO book_requests (id, book_id, requester_id, holder_id, request_date, status)
VALUES
('c1b2c3d4-e5f6-7890-1234-567890abcdef', 4, 'fedcba09-8765-4321-0987-654321fe8888', 'a1b2c3d4-e5f6-7890-1234-567890abcdef', '2024-02-15', 'requested'),
('d1b2c3d4-e5f6-7890-1234-567890abcdef', 5, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 'fedcba09-8765-4321-0987-654321fedcba', '2024-03-15', 'requested'),
('e1b2c3d4-e5f6-7890-1234-567890abcdef', 6, 'fedcba09-8765-4321-0987-654321fedcba', 'fedcba09-8765-4321-0987-654321fe8888', '2024-04-15', 'requested'),
('f1b2c3d4-e5f6-7890-1234-567890abcdef', 7, 'fedcba09-8765-4321-0987-654321fe8888', 'a1b2c3d4-e5f6-7890-1234-567890abcdef', '2024-05-15', 'requested'),
('g1b2c3d4-e5f6-7890-1234-567890abcdef', 8, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 'fedcba09-8765-4321-0987-654321fedcba', '2024-06-15', 'requested'),
('h1b2c3d4-e5f6-7890-1234-567890abcdef', 9, 'fedcba09-8765-4321-0987-654321fedcba', 'fedcba09-8765-4321-0987-654321fe8888', '2024-07-15', 'requested');


-----------------------
-----------------------
-- さらに追加データ
-----------------------
-----------------------



-- book_informationsテーブルにデータを追加
INSERT INTO book_informations (book_information_id, isbn_number, title, author, published_date, description, image_path)
VALUES
(10, '9784798060408', 'スッキリわかるSQL入門', '中山清喬, 国本大悟', '2018-07-13', 'データベースの基礎からSQLの基本的な書き方までを解説', 'https://images.unsplash.com/photo-1589998059171-988d887df646?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1476&q=80'),
(11, '9784839955557', 'ゼロから作るDeep Learning', '斎藤康毅', '2016-09-24', 'Pythonで始める深層学習の理論と実装', 'https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80'),
(12, '9784297127800', '独学プログラマー', 'コーリー・アルソフ', '2022-02-19', 'プログラミングを独学で学ぶためのロードマップ', 'https://images.unsplash.com/photo-1537884944318-390069bb8665?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80'),
(13, '9784774196176', 'エリック・エヴァンスのドメイン駆動設計', 'エリック・エヴァンス', '2018-02-09', '実践者から学ぶソフトウェア設計の原則', 'https://images.unsplash.com/photo-1605379399642-870262d3d051?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1506&q=80'),
(14, '9784798167022', '現場で役立つシステム設計の原則', '増田亨', '2020-06-26', 'システム設計の考え方と手法を学ぶ', 'https://images.unsplash.com/photo-1592424002053-21f369ad7fdb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1074&q=80');

-- booksテーブルにデータを追加
INSERT INTO books (id, user_id, book_information_id, donation_date)
VALUES
(10, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 10, '2024-04-01'),
(11, 'fedcba09-8765-4321-0987-654321fedcba', 11, '2024-05-01'),
(12, 'fedcba09-8765-4321-0987-654321fe8888', 12, '2024-06-01'),
(13, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 13, '2024-07-01'),
(14, 'fedcba09-8765-4321-0987-654321fedcba', 14, '2024-08-01'),
(15, 'fedcba09-8765-4321-0987-654321fe8888', 4, '2024-09-01'),
(16, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 5, '2024-10-01'),
(17, 'fedcba09-8765-4321-0987-654321fedcba', 6, '2024-11-01'),
(18, 'fedcba09-8765-4321-0987-654321fe8888', 7, '2024-12-01'),
(19, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 8, '2025-01-01'),
(20, 'fedcba09-8765-4321-0987-654321fedcba', 9, '2025-02-01'),
(21, 'fedcba09-8765-4321-0987-654321fe8888', 10, '2025-03-01'),
(22, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 11, '2025-04-01'),
(23, 'fedcba09-8765-4321-0987-654321fedcba', 12, '2025-05-01'),
(24, 'fedcba09-8765-4321-0987-654321fe8888', 13, '2025-06-01');

-- book_requestsテーブルにデータを追加
INSERT INTO book_requests (id, book_id, requester_id, holder_id, request_date, status)
VALUES
('j1b2c3d4-e5f6-7890-1234-567890abcdef', 10, 'fedcba09-8765-4321-0987-654321fe8888', 'a1b2c3d4-e5f6-7890-1234-567890abcdef', '2024-09-15', 'requested'),
('k1b2c3d4-e5f6-7890-1234-567890abcdef', 11, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 'fedcba09-8765-4321-0987-654321fedcba', '2024-10-15', 'requested'),
('l1b2c3d4-e5f6-7890-1234-567890abcdef', 12, 'fedcba09-8765-4321-0987-654321fedcba', 'fedcba09-8765-4321-0987-654321fe8888', '2024-11-15', 'requested'),
('m1b2c3d4-e5f6-7890-1234-567890abcdef', 13, 'fedcba09-8765-4321-0987-654321fe8888', 'a1b2c3d4-e5f6-7890-1234-567890abcdef', '2024-12-15', 'requested'),
('n1b2c3d4-e5f6-7890-1234-567890abcdef', 14, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 'fedcba09-8765-4321-0987-654321fedcba', '2025-01-15', 'requested'),
('o1b2c3d4-e5f6-7890-1234-567890abcdef', 15, 'fedcba09-8765-4321-0987-654321fedcba', 'fedcba09-8765-4321-0987-654321fe8888', '2025-02-15', 'requested'),
('p1b2c3d4-e5f6-7890-1234-567890abcdef', 16, 'fedcba09-8765-4321-0987-654321fe8888', 'a1b2c3d4-e5f6-7890-1234-567890abcdef', '2025-03-15', 'requested'),
('q1b2c3d4-e5f6-7890-1234-567890abcdef', 17, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 'fedcba09-8765-4321-0987-654321fedcba', '2025-04-15', 'requested'),
('r1b2c3d4-e5f6-7890-1234-567890abcdef', 18, 'fedcba09-8765-4321-0987-654321fedcba', 'fedcba09-8765-4321-0987-654321fe8888', '2025-05-15', 'requested'),
('s1b2c3d4-e5f6-7890-1234-567890abcdef', 19, 'fedcba09-8765-4321-0987-654321fe8888', 'a1b2c3d4-e5f6-7890-1234-567890abcdef', '2025-06-15', 'requested'),
('t1b2c3d4-e5f6-7890-1234-567890abcdef', 20, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 'fedcba09-8765-4321-0987-654321fedcba', '2025-07-15', 'requested'),
('u1b2c3d4-e5f6-7890-1234-567890abcdef', 21, 'fedcba09-8765-4321-0987-654321fedcba', 'fedcba09-8765-4321-0987-654321fe8888', '2025-08-15', 'requested'),
('v1b2c3d4-e5f6-7890-1234-567890abcdef', 22, 'fedcba09-8765-4321-0987-654321fe8888', 'a1b2c3d4-e5f6-7890-1234-567890abcdef', '2025-09-15', 'requested'),
('w1b2c3d4-e5f6-7890-1234-567890abcdef', 23, 'a1b2c3d4-e5f6-7890-1234-567890abcdef', 'fedcba09-8765-4321-0987-654321fedcba', '2025-10-15', 'requested'),
('x1b2c3d4-e5f6-7890-1234-567890abcdef', 24, 'fedcba09-8765-4321-0987-654321fedcba', 'fedcba09-8765-4321-0987-654321fe8888', '2025-11-15', 'requested');