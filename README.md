# poweroff
Simple web interface to local server on ubuntu (flask-mongo)

Простейшая реализация. 
это первый подход к данной теме 
т.к. развить и сделать более безопасным 
можно - добавить (для выполнения команд shutdown и reboot) 
1. или на веб сокетах с серваком на с\с++
2. либо запуск скрипта по крону- опрос базы и запуски выключения ребуута
3. либо в сторону - клиент-серверное приложение с возможностью управления и другими машинами 
(но это уже будет совершенно другая история )




Сейчас - все выполняетсЯ очень топорно 
(апи - запуск басш скрипта выключение - ребут- отмена )
но цель => выключать сервер со смартфона достигнута и даже больше того. 
и совершенствовать можно бесконечно  и зазовершенствоваться - 
но совершенство ради совершенство это .. был бы это студ проект или заказ - можно было бы.
а так 3 дня и функциоонал есть.

По факту работает на bootstrap 4 (т.к. смарту уже 5+ лет)
хотя есть верска под 5 бутстрап 

Начальная страница - кнопки - пересыл на адреса
/api/off/5  - выключение через 5 минут

Из фишек - это счетчик до выключния 
реализовано через записи в базу Монго 
т.е. это не просто js счетчик и при обновлении стнаницы он слетает
а полноценное табло - при загрузке с друого устройства - 
показывает корректное отображение оставшегося времени до выключения сервера
+ логирование времени выключения
+ возможность отменить выключение через веб интерфейс

для плноценной работы 
необходимо отключить запрос на ввод пароля по sudo 
для shutdown + reboot
(через visudo)

У меня уствновка с ngnix-gunicorn 
руководство 
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04-ru


Удачи в использовании) 







