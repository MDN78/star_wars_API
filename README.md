## Test project. API test - Star Wars API
----  
> The Star Wars API is the world's first quantified and programmatically-formatted set of Star Wars data.
> After hours of watching films and trawling through content online, service present to you all the People, Films, Species, Starships, Vehicles and Planets from Star Wars.
> Service have formatted this data in JSON and exposed it to you in a RESTish implementation that allows you to programmatically collect and measure the data.  
> [site SWAPI](https://swapi.dev/)

#### Tests, positive and negative:

1) People

- [x] Get people's list
- [x] Search people
- [x] Get first people
- [x] Get first people
- [x] without user agent

---- 

### Проект реализован с использованием:  
<p  align="left">
<code><img width="5%" title="python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"></code>
<code><img width="5%" title="pytest" src="https://github.com/MDN78/MDN78/blob/main/assets/pytest.png"></code>
<code><img width="5%" title="jenkins" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg"></code>
<code><img width="5%" title="allure" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_report.png"></code>
<code><img width="5%" title="alluretestops" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_testops.png"></code>
<code><img width="5%" title="github" src="https://github.com/MDN78/MDN78/blob/main/assets/github.png"></code>  
<code><img width="5%" title="telegram" src="assets/tg.png"></code>   
<code><img width="5%" title="pycharm" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg"></code>  

---- 

### <img width="3%" title="pc" src="assets/pc.jpg"> Локальный запуск UI и API тестов  
1) Скачать проект и открыть в IDE
2) Для локального запуска необходимо выполнить команду в терминале:

```commandline
pytest 
```
3) Выполнить запрос на формирование отчета  
   note: команда для Windows

```commandline
allure serve
```  
Результат: откроется страница с отчетом Allure Report

---- 

#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/C10_MDN782007_SWAPI/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Указать комментарий для уведомления в Телеграмм "COMMENT"
4. Указать сборку `ENVIRONMENT` по умолчанию "PROD"
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure

![image](assets/jenkins.PNG)

----

### Allure отчет

![image](assets/jenkins_allure_report.PNG)

Отчет позволяет получить детальную информацию по все шагам тестов, включая скриншоты и log - файлы

![image](assets/jenkins_allure_logs.PNG)    

----  

### <img width="3%" title="Telegramm" src="assets/tg.png"> Получение уведомлений о прохождении тестов в Telegram

После завершения сборки специальный Telegram-бот отправляет сообщение с отчетом.  

[//]: # (<img width="50%" title="Mobile" src="assets/telegramm_report.PNG">  )