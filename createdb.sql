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
    raw_text text,
    FOREIGN KEY(category_codename) REFERENCES category(codename)
);

insert into category (codename, name, is_base_expense, aliases)
values
    ("products", "продукты", 1, "еда"),
("walk", "гулять", 1, "перекус", "гулять", "погулять", "пепси", "pepsi", "фастфуд",
                         "fast food", "mcdonalds", "kfc", "burger king", "чипсы", "кино",
                         "shawarma", "шаурма", "шавуха", "шаверма", "doner", "doner king"),
("technics", "техника", 1, "pc", "пк", "компьютер", "монитор", "cable", "провода",
                              "клавиатура", "keyboard", "мышь", "mouse", "headphones",
                              "наушники", "smartphone", "телефон", "консоль"),
("games", "игры", 1, "ps4", "ps5", "playstation", "ps game", "pc game", "new game"),
("gift", "подарки", 1, "8 марта", "др", "нг"),
("other", "прочее", 1, "");

insert into budget(codename, daily_limit) values ('base', 50);
