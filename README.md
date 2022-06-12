# Techno Music Player
###### My website for lovers Techno music. ENJOY

`
DJANGO + DOCKER
`
 
###### Для работы нужно:

  В корне создать .env файл с такими параметрами:
  ```
    ALLOWED_HOSTS=
    DEBUG=
    SECRET_KEY=

    NAME=
    USER=
    PASSWORD=
    HOST=
    PORT=

    POSTGRES_PASSWORD=
    POSTGRES_USER=
    POSTGRES_DB=
  ```
  `docker-compose build`
  `docker-compose --env-file .env up`

###### Для создания суперюзера:

  `docker exec -it dm python ./manage.py createsuperuser`


###### ФОТОГРАФИИ:


<img width="1678" alt="Снимок экрана 2022-06-12 в 21 09 16" src="https://user-images.githubusercontent.com/15955132/173249939-50e4d738-474e-4a0c-a959-d27f450de348.png">
<img width="720" alt="" src="https://user-images.githubusercontent.com/15955132/173250008-e932d2ff-6e36-494a-9bae-f281918b336a.jpg">