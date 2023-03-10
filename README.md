# News_parser SQLite
### parsing economy news from RBC ("https://www.rbc.ru/economics)


![331](https://user-images.githubusercontent.com/54048747/224293143-24b3d2b4-8124-43a1-98b9-de3e2a62d9ac.JPG)


## SQL:
```SQL
CREATE TABLE IF NOT EXISTS news(
    id INT PRIMARY KEY autoincrement,
    time_ TEXT,
    name_ TEXT);
```
