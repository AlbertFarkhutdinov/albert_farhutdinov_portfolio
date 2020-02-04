function generateRandom(minValue, maxValue) {
    'use strict';
    return Math.round(Math.random() * (maxValue - minValue) + minValue);
}

function generateNumber() {
    'use strict';
    var number = [], min = 1, max = 9;
    for (var i = 0; i < numberOfDigits; i++) {
        var part = generateRandom(min, max);
        if (i == 0) {
            number[0] = part;
        }
        else {
            while (number.indexOf(part) != -1) {
                part = generateRandom(min, max);
            }
            number[i] = part;
        }
    }
    return number;
}

function checkNumber(myresult) {
    'use strict';
    attempts++;
    var answer = [false, 0, 0]; //0 - result, 1 - bulls, 2 - cows.
    var ranks = String(myresult).split("");
    for (var i = 0; i < ranks.length; i++) {
        if (parseInt(ranks[i]) == number[i]) {
            answer[1]++;
        }
        else if (number.indexOf(parseInt(ranks[i])) != -1) {
            answer[2]++;
        }
    }
    if (answer[1] == numberOfDigits) {
        answer[0] = true;
    }
    return answer;
}

function guessNumber() {
    'use strict';
    var result = +prompt("Input your number (-1 to quit)", 0);
    var gameIsRunning = true;
    while (gameIsRunning == true) {
        if (result == -1) {
            gameIsRunning = false;
        }
        else if (result == 0 || isNaN(result)) {
            alert("You did not input a number");
            result = +prompt("Input your number (-1 to quit)", 0);
        }
        else {
            var answer = checkNumber(result);
            if (answer[0]) {
                alert("Congratulations! You guessed the number. Number of attempts: " + attempts);
                gameIsRunning = false;
            }
            else {
                result = +prompt("Bulls: " + answer[1] + ". Cows: " + answer[2] + ". Input your number (-1 to quit)", 0);
            }
        }
    }
}
var numberOfDigits = 4;
var attempts = 0;
number = generateNumber();
alert(number);
guessNumber();