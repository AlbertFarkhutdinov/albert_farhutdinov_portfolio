var choices = [];
var currentQuestion = 0;

function isAnswer(number, event) {
    'use strict';
    if (isNaN(event) || !isFinite(event)) {
        alert('You inputted unacceptable symbol');
        return false;
    }
    else if (event < 1 || event > number) {
        alert('Your number is out of range');
        return false;
    }
    return true;
}

function checkAnything(string, maxValue) {
    'use strict';
    do {
        var ok = false;
        var event = +prompt(string);
        if (event == -1) {
            break;
        }
        else {
            ok = isAnswer(maxValue, event);
        }
    } while (!ok);
    return event;
}

function checkChoice(option) {
    'use strict';
    var allAnswers = '';
    for (var answer of option.answers) {
        allAnswers += answer;
    }
    var questionText = option.text + allAnswers + '-1 to take the money.';
    var choice = checkAnything(questionText, option.answers.length);
    return choice;
}

function checkStage() {
    'use strict';
    var text = 'Your answers are saved.\n' + 'Input number of the question (from 1 to ' + currentQuestion + ') , that you want to see.\n' + '-1 to quit.';
    var stage = checkAnything(text, currentQuestion);
    if (stage != -1) {
        if (choices[stage - 1] == undefined) {
            alert('You took the money on that question.')
        }
        else {
            alert(choices[stage - 1]);
        }
    }
}

function finishGame(rubles) {
    'use strict';
    alert('You prize is ' + rubles + ' rubles.');
    checkStage();
    alert('Thanks for the game!')
}

function playGame(option) {
    'use strict';
    if (option === null) {
        alert('Congratulations! You won!');
        finishGame(money[15])
        return;
    }
    currentQuestion++;
    var event = checkChoice(option);
    if (event == -1) {
        finishGame(money[currentQuestion - 1]);
    } 
    else if (event >= 1 && event <= option.answers.length) {
        var right = 'The right answer: ' + option.answers[option.rightAnswer - 1];
        choices.push(option.text + 'Your answer: ' + option.answers[event - 1] + right);
        if (event == option.rightAnswer) {
            playGame(option.next);
        }
        else {
            alert(right);
            if (currentQuestion <= 5) {
                finishGame(money[0]);
            }
            else if (currentQuestion > 5 && currentQuestion <= 10) {
                finishGame(money[5]);
            }
            else if (currentQuestion > 10 && currentQuestion <= 15) {
                finishGame(money[10]);
            }
        }
    }
    else {
        alert('Error!')
    }
}

playGame(questions[0]);