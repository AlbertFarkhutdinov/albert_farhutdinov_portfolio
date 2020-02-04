// Параметры игры
var isCross = true, // Показывает, чей ход (если true то крестики)
    gameTable = [[null, null, null], [null, null, null], [null, null, null]], // Матрица игры, заполняемая значениями true для крестиков и false для ноликов
    movesToTheEnd = 9, // Число ходов до конца игры
    winner = null; // Показывает, кто победил

// Функция, показывающая, чей сейчас ход
function setGamer() {
    'use strict';
    var player = document.getElementById('gamer'); // Строка хода
    player.innerText = 'Сейчас ходит ' + (isCross ? 'X' : 'O');
}

// Функция для рисования игрового поля
function generateField() {
    'use strict';
    setGamer();
    for (var i = 0; i < 9; i++) {
        var board = document.getElementById('board'); // Игровое поле
        var element = createAndAppend('div', board, 'cell', false);
        var innerElement = createAndAppend('div', element, 'inner_cell', false);
        innerElement.addEventListener('click', cellClick);
        innerElement.setAttribute('column', ((i % 3) + 1).toString());
        innerElement.setAttribute('row', (parseInt(i / 3) + 1).toString());
    }
    document.getElementById('button').addEventListener('click', reset);
}

// Функция для создания html-тега с заданным id и именем класса, добавляющая его в конец родительского элемента
function createAndAppend(tag, parent, className, id) {
    'use strict';
    var element = document.createElement(tag);
    if (className) {
        element.className = className; // присваиваем имя класса, если на месте name не указано false
    }
    if (id) {
        element.id = id; // присваиваем id, если на месте name не указано false
    }
    parent.append(element);
    return element;
}

// Функция, обрабатывающая событие нажатия на ячейку
function cellClick() {
    'use strict';
    if (this.innerText == '') { //Проверка содержимого ячейки
        this.innerText = (isCross ? 'X' : 'O');
        var row = this.getAttribute('row');
        var column = this.getAttribute('column');
        gameTable[row - 1][column - 1] = isCross;
        movesToTheEnd--;
        winner = (checkWinner(row, column) ? isCross : null);
        if (movesToTheEnd == 0 || winner !== null) {
            if (winner !== null) {
                if (confirm('Победили ' + (winner ? 'X' : 'O') + '.\nЖелаете сыграть ещё?')) {
                    reset();
                }
            }
            else if (confirm('Игра закончилась в ничью.\nЖелаете сыграть ещё?')) {
                reset();
            }
        }
        else {
            isCross = !isCross;
            setGamer();
        }
    }
    else {
        alert('Недопустимый ход');
    }
}

// Функция сброса параметров игры
function reset() {
    'use strict';
    isCross = true; // Показывает, какой игрок сейчас ходит
    gameTable = [[null, null, null], [null, null, null], [null, null, null]]; // Матрица игры
    movesToTheEnd = 9; // Кол-во оставшихся ходов
    winner = null;
    var table = document.getElementsByClassName('inner_cell');
    for (var i = 0; i < table.length; i++) {
        table[i].innerText = '';
    }
    setGamer();
}

// Проверка победителя
function checkWinner(row, column) {
    'use strict';
    return (checkCell(row, 1) && checkCell(row, 2) && checkCell(row, 3)) || (checkCell(1, column) && checkCell(2, column) && checkCell(3, column)) || (checkCell(1, 1) && checkCell(2, 2) && checkCell(3, 3)) || (checkCell(3, 1) && checkCell(2, 2) && checkCell(1, 3));
}

// Проверка содержимого ячейки
function checkCell(row, column) {
    'use strict';
    return gameTable[row - 1][column - 1] === isCross;
}

reset();
generateField();