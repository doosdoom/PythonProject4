import smtplib
import os

text = '''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!
%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 
Как будет проходить ваше обучение на %website%? 
→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 
Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

password = os.getenv("PASSWORD")
email = os.getenv("EMAIL")
link_site = '%website%'
friend_name = '%friend_name%'
my_name = '%my_name%'
text = text.replace(link_site, 'https://dvmn.org/referrals/5rCfixBuoEL6cwwis6v2d1exmdOdmY8et7OW3XBT/').replace(friend_name, 'Друг').replace(my_name, 'Егор')
letter = '''From: mail
To: mail
Subject: приглашение
Content-Type: text/plain; charset="UTF-8";'''.replace('mail', email) + '\n' + '\n' + text

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(email, password)
server.sendmail(email, email, letter.encode('utf-8'))
server.quit()