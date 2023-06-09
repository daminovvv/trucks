# trucks
---
## Описание
trucks - это сервис поиска ближайших машин для перевозки грузов.

Сервис поддерживает следующие функции:
- Создание нового груза (характеристики локаций pick-up, delivery определяются по введенному zip-коду);
- Получение списка грузов (локации pick-up, delivery, количество ближайших машин до груза ( =< 450 миль));
- Получение информации о конкретном грузе по ID (локации pick-up, delivery, вес, описание, список номеров ВСЕХ машин с расстоянием до выбранного груза);
- Редактирование машины по ID (локация (определяется по введенному zip-коду));
- Редактирование груза по ID (вес, описание);
- Удаление груза по ID.

При запуске приложения осуществляется выгрузка списка локаций из файла "uszips.csv"
Также БД заполняется 20 машинами с рандомной локацией.

- Расчет и отображение расстояния осуществляется в милях;
- Маршруты не прокладываются, используется расстояние от точки до точки
- Расчет расстояния должен осуществляться с помощью библиотеки geopy.



---
## Установка

---
### Шаги ДОКЕР
#### Кратко
- [ ] установить docker
- [ ] клонировать репозиторий
- [ ] запустить контейнер


#### 1. Установка Docker
https://docs.docker.com/desktop/install/windows-install/


#### 2. Клонирование репозитория
Создаем папку, заходим в неё, клонируем репозиторий.
```
md trucks
cd trucks
git clone https://github.com/daminovvv/trucks.git
```


#### 3. Запуск контейнера
В папке проекта выполнить:
```
docker compose up
```


#### 4. Запрос к API
Документация OpenAPI можно найти на

http://127.0.0.1:8000/swagger/

С помощью браузера или Postman отправить `GET` запрос на адрес

http://127.0.0.1:8000/cargo/
