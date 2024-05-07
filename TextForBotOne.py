from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton

menu_Project = ReplyKeyboardMarkup(resize_keyboard=True)

b_1 = KeyboardButton("Запуск")
b_2 = KeyboardButton("Автор")

menu_Project.add(b_1,b_2)


inline_Project = InlineKeyboardMarkup(row_width=2)

b_3 = InlineKeyboardButton(text="тут что нап. на кнопке", url="ghbioiu")
b_4 = InlineKeyboardButton(text="Ссылка на автора", url="hhjljknkj")

inline_Project.add(b_3, b_4)

menu_kb_3 = InlineKeyboardMarkup(row_width=1)

b_5 = InlineKeyboardButton(text="ТЫКНИ СЮДА!!!", callback_data="random_num")

menu_kb_3.add(b_5)





START_TEXT = """Добро пожаловать!
Это бот, который поможет узнать
значение неизвестных вам слов,
а также более распространенные синонимы к ним.
Если хотите получить инструкцию, 
выберите команду "About bot"."""

ABOUT_BOT_TEXT = """Если хотите: 
Узнать информацию об авторе, нажмите кнопку "Автор",
Узнать значение каких слов вы можете здесь найти 
с помощью этого бота, напишите "список",
Узнать значение какого либо слова, для этого просто
напишите интересующее вас слово, посде чего бот
выдаст вам информацию о нем."""

WORD_LIST = """Кринж 
Сленг
Свег
Треш
Вайб
Краш
Жиза
Лмао
Мем
Пруф
Рофл
Френдзона
Хайп
Шипперить
Скам
Гг
Имба
Нормис
Дед инсайд 
Скипнуть
Алтын
Аршин
Безобычный
Вёдро
Извадиться
Искренок
Кузло
Кулижка
Ловитва
Морок
Мыльня
Назола
Нужа
Оборы
Паленица
Онучи"""

CRINGE = """Кринж (от англ. cringe) — чувство крайней неловкости, которое сразу отражается на лице.
Если жуткое, отвратительное или возмутительное событие вызывает широкий спектр эмоций, 
вплоть до негативных, его называют кринжовым. Стыд, позор, неприязнь, отвращение.
"""
SLENG ="""Сленг — это набор слов или новых значений существующих слов,
 употребляемых в различных группах. Арго, жаргон."""
SWEG = """Свэг — это сленговое слово, означающее отвязность, раскованность
 (как в одежде, так и в поведении). Употребляют, чтобы сделать акцент 
 на «крутости», высоком статусе."""
TRESH = """Трэш (от английского trash — «мусор», «хлам») — это слово, которое в молодежном сленге
 означает что-то негативное, вызывающее отвращение или неприятное удивление.
 Зачастую это синоним плохого вкуса или какой-то ерунды. """
VIBE = """Вайб — это настроение или атмосфера, которую может создать человек, место или ситуация."""
CRASH = """Краш — предмет тайной или безответной влюблённости, а иногда просто про того, 
кто нравится. Возлюбленный, любимый."""
GIZA = """Жиза — это сокращение от слова «жизнь».
Оно означает «жизненно», «такова жизнь», «так бывает».Как правило, слово употребляется при 
описании курьёзных или поучительных историй. Рассказ может заканчиваться словами «вот такая жиза!»."""
LMAO = """Лмао - это сокращение фразы ‘смеюсь до упаду". Это означает что-то смешное. LMAO - это фраза, 
которая приходит на ум, когда человек очень сильно смеется."""
MEM = """Мем (англ. meme) — это идея, символ или образ, которые быстро распространяются от человека
 к человеку, а также в интернете. Обычно мемы бывают неформальными, юмористическими 
 или сатирическими, а также ассоциируются с конкретными событиями или людьми. Прикол, шутка, анекдот."""
PRUF = """Пруф — подтверждение, доказательство. В Сети часто просят предоставить пруфы, 
то есть подтвердить сказанные слова фактами, документами. Доказательство, подтверждение, аргумент."""
ROFL = """Рофл — это молодёжное слово, означающее шутку, прикол, розыгрыш."""
FRIENDZONE = """Френдзона — понятие, означающее дружеские отношения между мужчиной 
и женщиной, когда один из них пытается перевести их в романтические."""
HYPE = """Хайп (англ. hype) — это шумиха, ажиотаж, дешёвая и кратковременная популярность."""
SHIPPERING = """Шипперить — это представлять, что какие-то персонажи 
(книги, фильма, сериала, игры) или популярные(необязательно) люди состоят в романтических отношениях, 
хотя в действительности это не так."""
SCAM = """Скам (от англ. scam — «мошенничество», «афера») — это мошеннический 
инвестиционный проект, созданный для получения быстрой выгоды. Обман."""
GG = """ГГ - главный герой чего-либо, от компьютерной игры до книги."""
IMBA = """Слово «имба» упростилось до значения «круто». Можно заменить это слово на «превосходный» 
или «лучший» и не потерять смысл сказанного."""
NORMIS = """Нормис — это человек, который не выделяется из толпы и имеет типичные представления о жизни.
Этот термин получил особое распространение в последнее время — в разгар развития онлайн-общения."""
DED_INSIDE = """Дед инсайд (от англ. dead inside, «мертвый внутри») — это мем, популярный в геймерской 
среде и в итоге породивший субкультуру тех, кто ощущает себя внутренне опустошенными, «мертвыми изнутри."""
SKIP = """Скип (от англ. «skip», пропустить) – понимании современной молодёжи это 
слово может означать «игнорировать», то есть пройти мимо какой-либо проблемы."""
ALTIN = """Алтын – старинная русская счетно-денежная единица.
С XVII в. алтыном стали именовать монету, которая по стоимости приравнивалась к шести московским деньгам."""
ARSHIN = """Аршин – старорусская единица измерения длины.
1 аршин = 1/3 сажени = 4 четверти = 16 вершков = 28 дюймов = 0,7112 м."""
BEZOBICHNI = """Безобычный – безобыЧЛИВЫЙ человек, не знающий обычая, житейских приличий, грубый, 
необходительный, безобычность. Безобычному человеку с людьми не жить."""
VEDRO = """Вёдро – тёплая, ясная, солнечная, сухая погода, при том, что понятие не применимо к зимней поре."""
IZVADITSA = """Извадиться — приучиться к дурным привычкам."""
ISKRENOK = """Искренок – это выемка в печи, служившая для хранения сухой
 растопки и кресала для разжигания огня. """
KUZLO = """Кузло – кузнечная работа, ковка."""
KYLIGKA = """Кулижка – лесная поляна, расчищенная для земледелия."""
LOVITVA = """Ловитва - это охота. Это процесс ловли, поимки. Происходит напрямую от глагола "ловить". 
Кроме того, ловитва - это еще и результат охоты, то есть добыча. А в более широком значении - пища, 
добытая человеком. Включая, кстати, собранные грибы и ягоды."""
MOROK = """Морок – мрак, сумрак, мрачность, темнота и густота воздуха. 
Так же тучи, как правило густые."""
MILNIA = """Мыльня – баня."""
NAZOLA = """Назола – грусть, тоска,  досада, огорченье."""
NYZA = """Нужа – нужда, необходимость."""
OBORI = """Оборы – веревка, тесьма, которой обкручиваются онучи (часть обуви, обвертка на ногу, 
замена чулок под сапоги и лапти) и прикрепляются к ноге лапти."""
PALENICA = """Поленица – дева-воительница в русских былинах, женщина-богатырь. 
В былинах это женщины-воительницы, в своих боевых навыках не уступающие мужчинам-богатырям."""
ONYCHI = """Онучи – часть обуви, обвертка на ногу, замена чулок под сапоги и лапти."""
