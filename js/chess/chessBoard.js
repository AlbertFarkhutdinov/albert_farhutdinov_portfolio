var mainSize = 400,
    fieldSize = mainSize,
    cellSize = mainSize / 8,
    borderSize = mainSize / 20,
    boardSize = mainSize + borderSize + borderSize;
fieldSize += "px";
cellSize += "px";
borderSize += "px";
boardSize += "px";
var color1 = "white", color2 = "black";

function newBlock(parrent, blockName, blockWidth, blockHeight, isFloating) {
    'use strict';
    var div = document.createElement("div");
    div.className = blockName;
    div.style.width = blockWidth;
    div.style.height = blockHeight;
    if (isFloating) {
        div.style.float = "left";
    }
    parrent.append(div);
    return div;
}

function newOutline(element, width, style, color) {
    'use strict';
    element.style.outlineWidth = width;
    element.style.outlineStyle = style;
    element.style.outlineColor = color;
}

function alignBlock(element) {
    'use strict';
    element.style.marginTop = 0;
    element.style.marginBottom = 0;
    element.style.marginLeft = "auto";
    element.style.marginRight = "auto";
}

function alignLetter(element, height) {
    'use strict';
    element.style.textAlign = "center";
    element.style.lineHeight = height;
}

function putSymbol(parrent, blockName, blockWidth, blockHeight, height, isRotated) {
    'use strict';
    var symbol = newBlock(parrent, blockName, blockWidth, blockHeight, true);
    alignLetter(symbol, height);
    if (isRotated) {
        symbol.style.transform = "rotate(180deg)";
    }
    return symbol;
}

function chessBoard() {
    'use strict';
    var board = newBlock(document.body, "board", boardSize, boardSize, false),
        upLetters = newBlock(board, "up-letters", fieldSize, borderSize, false),
        leftDigits = newBlock(board, "left-digits", borderSize, fieldSize, true),
        field = newBlock(board, "field", fieldSize, fieldSize, true),
        rightDigits = newBlock(board, "right-digits", borderSize, fieldSize, true),
        downLetters = newBlock(board, "down-letters", fieldSize, borderSize, false);
    alignBlock(board);
    alignBlock(upLetters);
    alignBlock(downLetters);
    newOutline(board, "1px", "solid", color2);
    newOutline(field, "1px", "solid", color2);
    downLetters.style.clear = "both";
    for (var i = 0; i < 8; i++) {
        var upLetter = putSymbol(upLetters, "letter", cellSize, borderSize, borderSize, true),
            downLetter = putSymbol(downLetters, "letter", cellSize, borderSize, borderSize, false),
            leftDigit = putSymbol(leftDigits, "digit", borderSize, cellSize, cellSize, false),
            rightDigit = putSymbol(rightDigits, "digit", borderSize, cellSize, cellSize, true);
        upLetter.innerHTML = String.fromCharCode(65 + i);
        downLetter.innerHTML = String.fromCharCode(65 + i);
        leftDigit.innerHTML = 8 - i;
        rightDigit.innerHTML = 8 - i;
        var row = newBlock(field, "row", fieldSize, cellSize, false);
        for (var j = 0; j < 8; j++) {
            var cell = newBlock(row, "cell", cellSize, cellSize, true);
            alignLetter(cell, cellSize);
            cell.style.backgroundColor = ((i + j) % 2 == 0) ? color1 : color2;
        }
    }
}
chessBoard();