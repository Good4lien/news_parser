#News_parser SQLite
### parsing economy news from RBC ("https://www.rbc.ru/economics)

![888](https://user-images.githubusercontent.com/54048747/224272427-a403b68f-f2b1-42af-9e32-ae5e18c705f8.JPG)

SQL:
CREATE TABLE IF NOT EXISTS news(
    id INT PRIMARY KEY autoincrement,
    time_ TEXT,
    name_ TEXT);

