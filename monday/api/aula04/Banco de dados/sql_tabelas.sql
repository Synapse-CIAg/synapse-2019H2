CREATE TABLE IF NOT EXISTS `authors` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(45) NULL,
    `birth_date` DATETIME NULL,
    `thumbnail_url` VARCHAR(255) NULL
);

CREATE TABLE IF NOT EXISTS `books` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    `title` VARCHAR(45) NOT NULL, 
    `sinopsis` VARCHAR(255) NOT NULL, 
    `release_date` DATETIME NULL, 
    `thumbnail_url` VARCHAR(255) NULL, 
    `author_id` INT, 
    CONSTRAINT fk_author FOREIGN KEY (author_id) 
    REFERENCES authors(id)
);

CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    `user_name` VARCHAR(50) NOT NULL UNIQUE,
    `fullname` VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS `genres` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(45) NULL
);

CREATE TABLE IF NOT EXISTS `books_genres` (
    book_id INT,
    genre_id INT,
    CONSTRAINT fk_book FOREIGN KEY (book_id) 
    REFERENCES books(id),
    CONSTRAINT fk_genre FOREIGN KEY (genre_id) 
    REFERENCES genres(id)
);

CREATE TABLE IF NOT EXISTS `comments` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `message` VARCHAR(255) NULL,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `book_id` INT,
    `user_id` INT,
    CONSTRAINT fk_book_comment FOREIGN KEY (book_id) 
    REFERENCES books(id),
    CONSTRAINT fk_user FOREIGN KEY (user_id) 
    REFERENCES users(id)
);
