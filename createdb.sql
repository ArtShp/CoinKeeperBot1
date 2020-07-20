create table budget(
    codename varchar(255) primary key,
    daily_limit integer
);

create table category(
    codename varchar(255) primary key,
    name varchar(255),
    is_base_expense boolean,
    aliases text
);

create table expense(
    id integer primary key,
    amount integer,
    created datetime,
    category_codename integer,
    text text,
    FOREIGN KEY(category_codename) REFERENCES category(codename)
);

INSERT INTO category (codename, name, is_base_expense, aliases)
VALUES
    ("products", "продукты", true, "еда"),
    ("walk", "гулять", true, "перекус", "гулять", "погулять", "пепси" "pepsi", "фастфуд",
                             "fast food", "mcdonalds", "kfc", "burger king", "чипсы", "кино",
                             "shawarma", "шаурма", "шавуха", "шаверма", "doner", "doner king"),
    ("technics", "техника", true, "pc", "пк", "компьютер", "монитор", "cable", "провода",
                                  "клавиатура", "keyboard", "мышь", "mouse", "headphones",
                                  "наушники", "smartphone", "телефон", "консоль"),
    ("games", "игры", true, "ps4", "ps5", "playstation", "ps game", "pc game", "new game"),
    ("gift", "подарки", true, "8 марта", "др", "нг"),
    ("other", "прочее", true, "");
