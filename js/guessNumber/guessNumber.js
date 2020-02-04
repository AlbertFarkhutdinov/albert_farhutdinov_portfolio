var attempts = 0;
var min = 1;
var max = 100;
var number = Math.round(Math.random() * (max - min) + min);

function guessNumber() {
    'use strict';
    if (attempts === 3) {
        alert("The number of attempts is zero. You lose! The right number: " + number);
        return;
    }
    attempts++;
    var result = +prompt("Input your number (-1 to quit)", 0);
    if (result == number) {
        alert("Congratulations! You guessed the number. Number of attempts: " + attempts);
        location.reload();
    }
    else if (parseInt(result) == 0 || isNaN(result)) {
        alert("You did not input a number");
        guessNumber();
    }
    else if (parseInt(result) == -1) {
        alert("Thanks foк the game!");
    }
    else {
        if (result > number) {
            alert("You number is more than the right one");
        }
        else {
            alert("You number is less than the right one");
        }
        guessNumber();
    }
}
guessNumber();