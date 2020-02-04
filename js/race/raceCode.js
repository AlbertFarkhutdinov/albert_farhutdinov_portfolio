var min = 2;
var max = 9;
var numberOfCars = 5;
var startPosition = 680;
var timeInterval = 25;
var timer = null;
var cars = [];
var carPosition = [];

function checkPrompt(string) {
    'use strict';
    var number;
    do {
        number = +prompt(string);
    } while (isNaN(number));
    return number;
}
var mySum = checkPrompt("Введите Вашу сумму (в рублях).");
do {
    var carNumber = checkPrompt("На какую машину (от 1 до " + numberOfCars + ") вы делаете ставку?");
} while (carNumber > numberOfCars || carNumber < 1);
var myBet = checkPrompt("Сколько Вы ставите на выигрыш?");
var background = document.getElementById('background');

function go() {
    'use strict';
    for (var i = 0; i < numberOfCars; i++) {
        cars[i] = document.getElementById("car_" + (i + 1));
        cars[i].style.border = "none";
        carPosition[i] = startPosition;
    }
    timer = window.setInterval(timerGo, timeInterval);
}

function addCars() {
    'use strict';
    var button = document.createElement('input');
    button.type = 'button';
    button.value = 'Start';
    button.id = 'start_button';
    button.addEventListener('click', go);
    background.append(button);
    for (var i = 0; i < numberOfCars; i++) {
        var carImage = document.createElement('img');
        carImage.className = 'car';
        carImage.id = carImage.className + '_' + (i + 1);
        carImage.src = carImage.id + '.png';
        background.append(carImage);
        carImage.style.top = ((i + 1) * 100) + 'px';
    }
}

function timerGo() {
    'use strict';
    for (var i = 0; i < numberOfCars; i++) {
        carPosition[i] -= Math.floor((Math.random() * (max - min) + min));
        if (carPosition[i] <= 0) {
            window.clearInterval(timer);
            if (i == carNumber - 1) {
                mySum += myBet;
                alert("Вы победили!" + "\nВаша сумма = " + mySum + " рублей.");
            }
            else {
                mySum -= myBet;
                alert("Вы проиграли. До финиша доехала машина с номером " + (i + 1) + "\nВаша сумма = " + mySum + " рублей.");
            }
            cars[i].style.border = "5px ridge yellow";
            return;
        }
        cars[i].style.left = carPosition[i] + "px";
    }
}
window.addEventListener('load', addCars);