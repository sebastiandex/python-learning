print ('Поиграем в загадки? Тебе будет задано 10 вопросов, \nПиши ответ как можно точнее.\n')
score = 0

answer = input('Каков цвет настроения у Филлипа Киркорова? \n\nОтвет:   ')#1
if answer == 'Синий' or 'синий'or 'СИНИЙ':
	score = score + 1

answer = input('Какого цвета луна у Бори Моисеева? \n\nОтвет:   ')#2
if answer == 'Голубая' or 'голубая'or 'ГОЛУБАЯ':
	score = score + 1
answer = input('Назови самую "кодерскую" змею \n\nОтвет:   ')#3
if answer == 'Python' or 'python'or 'Питон' or 'питон':
	score = score + 1

answer = input('Как обозначается строковая переменная в Python? \n\nОтвет:   ')#4
if answer == 'Str' or 'str' or 'string':
	score = score + 1
answer = input('Сколько пробелов больше всего нравится Питону? \n\nОтвет:   ')#5
if answer == '4' or 'четыре':
		score = score + 1

answer = input('Устал придумывать вопросы. Сколько будет 3+3? \n\nОтвет:   ')#6
if answer == '6' or 'шесть' or 'Шесть':
		score = score + 1

answer = input('А если к шести 1 прибавить? \n\nОтвет:   ')#7
if answer == '7' or 'семь' or 'Семь':
			score = score + 1

answer = input('Сколько будет 2х4? \n\nОтвет:   ')#8
if answer == '8' or 'восемь' or 'Восемь':
			score = score + 1
answer = input('Сколько будет 5+4? \n\nОтвет:   ')#9
if answer == '9' or 'девять' or 'Девять':
				score = score + 1

answer = input('Сколько будет 5+5? \n\nОтвет:   ')#10
if answer == '10' or 'Десять' or 'десять':
				score = score + 1


if score <= 3:
	print('Стоит попробовать ещё раз! \nТы правильно ответил только на',score,'вопросов из 10-ти. :(')
if score >3 and score <= 7:
	print('Очень хорошо! \nТы правильно ответил на',score,'вопросов из 10-ти!')
if score >7 and score <10:
	print('Почти идеально! \nТы ответил аж на',score,'вопросов из 10-ти!!')
if score == 10:
	print('Ты просто гений! \nОтветить на',score,'вопросов из 10-ти мог только самый лучший!')