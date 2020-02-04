var question = {
    text: '',
    answers: [],
    rightAnswer: 1,
    next: {}
};

function cloneObject(oldObject) {
    'use strict';
    var newObject = {};
    for (var key in oldObject) {
      newObject[key] = oldObject[key];
    }
    return newObject;
}

questions = [];
money = [0, 500, 1000, 2000, 3000, 5000, 10000, 15000, 25000, 50000, 100000, 200000, 400000, 800000, 1500000, 3000000];
for (i = 0; i < 15; i++) {
    var newQuestion = cloneObject(question);
    questions.push(newQuestion);
    questions[i].text = 'Вопрос ' + (i+1) + '.\n' + 'Разыгрывается: ' + money[i+1] + ' рублей.\n';
}

for (i = 0; i < 14; i++) {
    questions[i].next = questions[i+1];
}
questions[14].next = null;

questions[0].text += 'Где дети ищут подарки утром 1 января?\n';
questions[0].answers = ['1 - под ёлкой\n', '2 - под палкой\n', '3 - под скалкой\n', '4 - под мухой\n'];
questions[0].rightAnswer = 1;

questions[1].text += 'Что из перечисленного - пирог?\n';
questions[1].answers = ['1 - кусака\n', '2 - закаляка\n', '3 - забияка\n', '4 - кулебяка\n'];
questions[1].rightAnswer = 4;

questions[2].text += 'Провожают, как известно, по уму, а как встречают?\n';
questions[2].answers = ['1 - по одёжке\n', '2 - по сберкнижке\n', '3 - по прописке\n', '4 - по рекомендации\n'];
questions[2].rightAnswer = 1;

questions[3].text += 'Как называют мелководный бассейн, предназначенный для детей?\n';
questions[3].answers = ['1 - утятник\n', '2 - лягушатник\n', '3 - селёдочник\n', '4 - тюленник\n'];
questions[3].rightAnswer = 2;

questions[4].text += 'Что, по словам кота Бегемота, он делал, когда его пришли арестовывать?\n';
questions[4].answers = ['1 - починял примус\n', '2 - чистил обувь\n', '3 - варил кашу\n', '4 - играл в шахматы\n'];
questions[4].rightAnswer = 1;

questions[5].text += 'Бочонок с каким числом в русском лото принято называть «топориками»?\n';
questions[5].answers = ['1 - 11\n', '2 - 69\n', '3 - 77\n', '4 - 88\n'];
questions[5].rightAnswer = 3;

questions[6].text += 'Что из перечисленного название концертного зала, а не стадиона?\n';
questions[6].answers = ['1 - «Камп Ноу»\n', '2 - «Альберт-холл»\n', '3 - «Сан-Сиро»\n', '4 - «Энфилд»\n'];
questions[6].rightAnswer = 2;

questions[7].text += 'В каком фильме Бен Аффлек был не только исполнителем главной роли, но и режиссёром?\n';
questions[7].answers = ['1 - «Операция «Арго»\n', '2 - «Операция «Трест»»\n', '3 - «Операция «Святой Януарий»»\n', '4 - «Операция «Ы» …»\n'];
questions[7].rightAnswer = 1;

questions[8].text += 'Как не называется ни одна из глав романа Лермонтова «Герой нашего времени»?\n';
questions[8].answers = ['1 - «Княжна Мэри»\n', '2 - «Бэла»\n', '3 - «Княгиня Лиговская»\n', '4 - «Максим Максимыч»\n'];
questions[8].rightAnswer = 3;

questions[9].text += 'Чего мы не знаем о статуе Венеры Милосской?\n';
questions[9].answers = ['1 - имя заказчика\n', '2 - точное место находки\n', '3 - год находки\n', '4 - были ли у неё руки\n'];
questions[9].rightAnswer = 1;

questions[10].text += 'Что норвежцы дарят на Новый год в качестве символа тепла и счастья?\n';
questions[10].answers = ['1 - дрова\n', '2 - свечи\n', '3 - спички\n', '4 - пледы\n'];
questions[10].rightAnswer = 3;

questions[11].text += 'Где впервые была произнесена фраза «Не в силе Бог, а в правде», ставшей впоследствии крылатой?\n';
questions[11].answers = ['1 - в Новгороде\n', '2 - в фильме «Брат 2»\n', '3 - в Белом Море\n', '4 - в соборе Парижской Богоматери\n'];
questions[11].rightAnswer = 1;

questions[12].text += 'Как называется психологический эффект, который несколько лет назад открыли американские ученые?\n';
questions[12].answers = ['1 - оконной рамы\n', '2 - закрытой фрамуги\n', '3 - дверного проёма\n', '4 - туалетного крючка\n'];
questions[12].rightAnswer = 3;

questions[13].text += 'Какой предмет стал причиной смерти французского композитора Жан-Батиста Люлли?\n';
questions[13].answers = ['1 - дирижёрская трость\n', '2 - струна рояля\n', '3 - гусиное перо\n', '4 - смычок скрипки\n'];
questions[13].rightAnswer = 1;

questions[14].text += 'Что не умеют делать ящерицы гекконы?\n';
questions[14].answers = ['1 - ловить рыбу\n', '2 - ходить по потолку\n', '3 - менять цвет\n', '4 - петь\n'];
questions[14].rightAnswer = 1;