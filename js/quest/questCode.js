var choices = [];
var lastStage = 0;

function isAnswer(number, event) {
    'use strict';
    if (isNaN(event) || !isFinite(event)) {
        alert('Вы ввели недопустимый символ');
        return false;
    } else if (event < 1 || event > number) {
        alert('Ваше число выходит из допустимого диапозона');
        return false;
    }
    return true;
}

function checkAnything(string, maxValue) {
    'use strict';
    var ok, event;
    do {
        ok = false;
        event = +prompt(string);
        if (event === -1) {
            break;
        } else {
            ok = isAnswer(maxValue, event);
        }
    } while (!ok);
    return event;
}

function checkStage() {
    'use strict';
    var text = 'Ваши ответы сохранены.\n' +
        'Введите номер шага (от 1 до ' + lastStage + ') , который Вы хотите посмотреть.\n' +
        '-1 - Выход из игры.',
        stage = checkAnything(text, lastStage);
    if (stage !== -1) {
        if (choices[stage - 1] === undefined) {
            alert('На данном шаге Вы покинули игру, не дав ответа.');
        } else {
            alert(choices[stage - 1]);
        }
    }
}

function checkChoice(option) {
    'use strict';
    var answers = '', text, choice;
    for (var item of option.answer) {
        answers += item;
    }
    text = option.question + answers + '-1 - Выход из игры.';
    choice = checkAnything(text, option.number);
    return choice;
}

function switchEvent(option) {
    'use strict';
    if (option === null) {
        checkStage();
        alert('Игра завершена! Спасибо за игру!');
        return;
    }
    var event = checkChoice(option);
    lastStage++;
    if (event === -1) {
        checkStage();
        alert('Спасибо за игру!');
    } else if (event >= 1 && event <= option.number) {
        for (var i=1; i <= option.number; i++) {
            if (event == i){
                choices.push(option.question + option.answer[i-1]);
                switchEvent(option.next[i-1]);
            }
        }
    }
    else {
        alert('Ошибка');
    }
}

switchEvent(a);