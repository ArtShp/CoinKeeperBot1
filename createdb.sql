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
    created date,
    category_codename integer,
    text text,
    FOREIGN KEY(category_codename) REFERENCES category(codename)
);

INSERT INTO category (codename, name, is_base_expense, aliases)
VALUES
    ("products", "продукты", true, "еда"),

    ("coffee", "кофе", true, "кофе"),

    ("dinner", "обед", true, "столовая, ланч, бизнес-ланч, бизнес ланч"),

    ("cafe", "кафе", true, "ресторан, рест, мак, макдональдс, макдак, kfc, ilpatio, il patio"),

    ("transport", "общ. транспорт", false, "метро, автобус, metro"),

    ("taxi", "такси", false, "яндекс такси, yandex taxi"),

    ("phone", "телефон", false, "теле2, связь"),

    ("books", "книги", false, "литература, литра, лит-ра"),

    ("internet", "интернет", false, "инет, inet"),

    ("subscriptions", "подписки", false, "подписка"),

    ("other", "прочее", true, "");
