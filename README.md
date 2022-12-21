## softarex_test_task
###### Zyblyuk Roman


# Запуск Проекта

В проекте реализованно две версии kafka и flask, для того, чтобы выбрать нужную,
необходимо указать в .env файле поле VERSION.
Для kafka VERSION=kafka_version, для flask VERSION=flask_version

Нужно скачать данный [по ссылке](https://drive.google.com/file/d/156z3O_wkgRU4REbalXBmG9Vup5jJ4cA-/view) 
и забросить их в папку EnsembleTreeModel,
чтобы было $(VERSION)/EnsembleTreeModel/income-prediction/train.csv,
где $(VERSION) выбранная вами версия, либо "flask_version", либо "kafka_version"


Проект запускается командой в терминале:
```
docker-compose up 
```
После чего он установит все зависимости и запустит контейнер

![alt text](https://github.com/Zyblyuk/softarex_test_task/blob/master/images/dc_scr.png)

После этого появиться возможность зайти в приложение [по ссылке](http://localhost:8000/): 

![alt text](https://github.com/Zyblyuk/softarex_test_task/blob/master/images/home_page.png)

Дальше можно зарегистрироваться и пользоваться приложением:

![alt text](https://github.com/Zyblyuk/softarex_test_task/blob/master/images/register.png)

![alt text](https://github.com/Zyblyuk/softarex_test_task/blob/master/images/predict.png)

Есть возможность сохранять результат в .json формате, так же можно смотреть и сохранять историю:

![alt text](https://github.com/Zyblyuk/softarex_test_task/blob/master/images/history.png)

Добавлена возможность редактировать профиль:

![alt text](https://github.com/Zyblyuk/softarex_test_task/blob/master/images/profile1.png)
![alt text](https://github.com/Zyblyuk/softarex_test_task/blob/master/images/profile2.png)

