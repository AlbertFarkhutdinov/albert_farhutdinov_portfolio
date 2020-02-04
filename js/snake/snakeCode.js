// Глобальные переменные: 
var FIELD_SIZE_X = 20; // Число строк
var FIELD_SIZE_Y = 20; // Число столбцов
var SNAKE_SPEED = 200; // Интервал между перемещениями змейки
var BOMB_SPEED = 10000; // Интервал между созданиями бомб
var snake; // Сама змейка
var direction; // Направление движения змейки
var snake_timer; // Таймер змейки
var bomb_timer; // Таймер для бомб
var score; // Результат
// Функция для создания html-тега с заданным id и именем класса, добавляющая его в конец родительского элемента
function create_and_append(tag, parent, class_name, id_name) {
    'use strict';
    var element = document.createElement(tag);
    if (class_name) {
        element.className = class_name; // присваиваем имя класса, если на месте class_name не указано false
    }
    if (id_name) {
        element.id = id_name; // присваиваем id, если на месте id_name не указано false
    }
    parent.append(element);
    return element;
}
// Функция, возвращающая массив классов элемента element
function class_array(element) {
    'use strict';
    return element.getAttribute('class').split(' ');
}
// Функция для добавления нового класса new_class к уже существуюшим классам элемента element
function add_class(element, new_class) {
    'use strict';
    element.className = element.getAttribute('class') + ' ' + new_class;
}
// Функция генерации игрового поля
function prepare_game_field() {
    'use strict';
    // Предварительно очистим поле от предыдущей игры
    snake = [];
    clearInterval(snake_timer);
    clearInterval(bomb_timer);
    score = 0;
    direction = 'y+';
    var snake_field = document.getElementById('snake_field');
    snake_field.innerHTML = '';
    var game_table = create_and_append('table', snake_field, false, 'game_table');
    for (var row_number = 0; row_number < FIELD_SIZE_X; row_number++) {
        var row = create_and_append('tr', game_table, 'game_table_row', 'row_' + row_number);
        for (var column_number = 0; column_number < FIELD_SIZE_Y; column_number++) {
            var cell = create_and_append('td', row, 'game_table_cell', 'cell_' + row_number + '_' + column_number);
        }
    }
}
// Функция инициализации
function init() {
    'use strict';
    // Генерация поля
    prepare_game_field();
    // Запуск игры при нажатии на кнопку "Старт". При повторном нажатии перезапускает игру сразу
    document.getElementById('snake_start').addEventListener('click', start_game);
    // Перезапуск игры при нажатии на кнопку "Новая игра". Появляется пустое поле без автозапуска игры
    document.getElementById('snake_renew').addEventListener('click', refresh_game);
    // Смена направления змейки при нажатии на стрелочки
    addEventListener('keydown', change_direction);
}
// Старт игры
function start_game() {
    'use strict';
    prepare_game_field();
    create_snake(); // Создали змейку
    snake_timer = setInterval(move, SNAKE_SPEED); // Каждые SNAKE_SPEED миллисекунд змейка передвигается
    random_create('food_unit', ['snake_unit', 'bomb_unit'])
    bomb_timer = setInterval(create_bomb, BOMB_SPEED); // Каждые BOMB_SPEED миллисекунд создаётся бомба
}
// Функция создания змейки из двух клеток в центре игрового поля. Массив snake начинается с хвоста
function create_snake() {
    'use strict';
    var start_coord_x = Math.floor(FIELD_SIZE_X / 2);
    var start_coord_y = Math.floor(FIELD_SIZE_Y / 2);
    for (var i = 0; i < 2; i++) { // 0 - хвост, 1 - голова
        var snake_unit = document.getElementById('cell_' + (start_coord_y - i) + '_' + start_coord_x);
        add_class(snake_unit, 'snake_unit');
        snake.push(snake_unit);
    }
}
// Функция, определяющая клетку, на которую перемещается голова змеи
function create_new_unit(x, y) {
    'use strict';
    switch (direction) {
    case ('x-'):
        if (x - 1 < 0) {
            x = FIELD_SIZE_X;
        }
        return document.getElementById('cell_' + y + '_' + (x - 1));
    case ('x+'):
        if (x + 1 == FIELD_SIZE_X) {
            x = -1;
        }
        return document.getElementById('cell_' + y + '_' + (x + 1));
    case ('y+'):
        if (y - 1 < 0) {
            y = FIELD_SIZE_Y;
        }
        return document.getElementById('cell_' + (y - 1) + '_' + x);
    case ('y-'):
        if (y + 1 == FIELD_SIZE_Y) {
            y = -1;
        }
        return document.getElementById('cell_' + (y + 1) + '_' + x);
    }
}
// Движение змейки
function move() {
    'use strict';
    var snake_coords = snake[snake.length - 1].getAttribute('id').split('_'); // Преобразовали id головы в массив
    var coord_y = parseInt(snake_coords[1]);
    var coord_x = parseInt(snake_coords[2]);
    var new_unit = create_new_unit(coord_x, coord_y); // Клетка, куда перемещается голова 
    // Если new_unit не часть змейки и не бомба, добавляем её к змее
    if (!check_unit(new_unit, 'snake_unit') && !check_unit(new_unit, 'bomb_unit')) {
        add_class(new_unit, 'snake_unit');
        snake.push(new_unit);
        // Если новая клетка не была едой, нужно убрать хвост
        if (!check_unit(new_unit, 'food_unit')) {
            var removed = snake.shift(); // Находим хвост - удаляем первый элемент массива и возвращаем его 
            removed.className = class_array(removed)[0]; // Удаляем хвост - оставляем только первый класс из массива классов
        }
    }
    else {
        finish_the_game();
    }
}
// Проверка клетки на принадлежность змейке, еде или бомбе
function check_unit(unit, unit_name) {
    'use strict';
    var check = false;
    if (class_array(unit).includes(unit_name)) {
        check = true;
        if (unit_name == 'food_unit') {
            score++;
            document.getElementById('score').innerHTML = "Your score: " + score;
            random_create('food_unit', ['snake_unit', 'bomb_unit']); // Если змея съела еду, создаём новую
        }
    }
    return check;
}
// Создание еды или бомбы
function random_create(unit_name, unacceptable_units) {
    'use strict';
    var is_created = false;
    while (!is_created) { // Пока клетка не создана
        var new_x = Math.floor(Math.random() * FIELD_SIZE_X);
        var new_y = Math.floor(Math.random() * FIELD_SIZE_Y);
        var new_cell = document.getElementById('cell_' + new_y + '_' + new_x);
        var checked = 1;
        // проверяем клетку на соответствие другим классам. Например, если создаём еду, то клетка не должна быть змеей или едой
        for (var unit of unacceptable_units) {
            var condition = !class_array(new_cell).includes(unit);
            checked *= condition;
        }
        if (checked) {
            add_class(new_cell, unit_name);
            is_created = true;
        }
    }
}
// Создание бомбы. Дополнительная функция, объявлена без аргументов, чтобы передать её в setInterval как объект
function create_bomb() {
    'use strict';
    random_create('bomb_unit', ['snake_unit', 'food_unit']);
}
// Изменение направления движения змейки по нажатию на клавиши стрелок
function change_direction(e) {
    'use strict';
    // console.log(e.keyCode);
    switch (e.keyCode) {
    case 37: // Клавиша влево
        if (direction != 'x+') {
            direction = 'x-'
        }
        break;
    case 38: // Клавиша вверх
        if (direction != 'y-') {
            direction = 'y+'
        }
        break;
    case 39: // Клавиша вправо
        if (direction != 'x-') {
            direction = 'x+'
        }
        break;
    case 40: // Клавиша вниз
        if (direction != 'y+') {
            direction = 'y-'
        }
        break;
    }
}
// Функция завершения игры
function finish_the_game() {
    'use strict';
    clearInterval(snake_timer);
    alert('You lose! Your score: ' + score.toString());
    refresh_game();
}
// Новая игра
function refresh_game() {
    'use strict';
    location.reload();
}
// Инициализация
window.onload = init;