#! python3
#-*- coding: utf-8 -*-

#multiplyQuiz.py - программа, которая даёт 10 заданий на умножение и проверяет правильность

import pyinputplus as pyip, time, random

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    #выбираем 2 случайных числа
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        # Правильные ответы задаются аргументом allowRegexes;
        # неправильные ответы задаются аргументом blockRegexes
        # (в случае неправильного ответа отображается
        # пользовательское сообщение)
        pyip.inputStr(prompt,allowRegexes=['^%s$' % (num1 * num2)], \
                      blockRegexes=[('.*', 'Неправильно!')],\
                      timeout= 8, limit= 3)
    except pyip.TimeoutException:
        print('Время истекло!')
    except pyip.RetryLimitException:
        print('Закончилось количество попыток!')
    else:
        # Этот блок выполняется, если в блоке try
        # не возникло исключений
        print('правильно!')
        correctAnswers += 1
    time.sleep(1) # короткая пауза, позволяющая пользователю
                    # увидеть результат
    print('Счёт %s/%s' % (correctAnswers,numberOfQuestions))