USER_1 = (277352270, 'Leddavlet')
USER_2 = (354668710, 'lidrudakova', 1, 'Lydia', 'Rudakova')

PLANT_1 = "<Plants plant_id=1, name='Фиалка', description='Домашняя фиалка представляет собой низкорослый травянистый многолетник, который является вечнозеленым. Побеги у него укорочены, а в состав прикорневой розетки входят ворсистые листовые пластины округлой формы и кожистые на ощупь. Листва кустиков-мальчиков (boys) имеет равномерный зеленый окрас, а у кустиков-девочек (girls) у основания располагается светлое пятнышко. Основание у листвы сердцевидное неравнобокое, при этом верхняя часть имеет округлую форму либо заострение.', light='Нуждается в ярком свете, причем он должен быть рассеянным. Для фиалки подойдет окно северо-восточной, северной и северо-западной ориентации. Продолжительность светового дня ― от 13 до 14 ч.', temperature='Во время интенсивного роста ― от 18 до 24 градусов, в зимние месяцы ― не холоднее 15 градусов.', watering='Проводят его систематически пару раз в неделю. При этом раз в десять дней кустик рекомендуется поливать методом нижнего полива.', moisture='Для нормального развития сенполии необходима повышенная влажность воздуха. Причем повышать ее можно различными способами, кроме опрыскивания самого кустика. Дело в том, что на поверхность его листвы и цветков, которые находятся на свету,  ни в коем случае не должны попадать капельки влаги, так как из-за этого могут появиться солнечные ожоги.', fertilizer='Подкармливают растение лишь во время его интенсивного роста. Для этого регулярно трижды в месяц в почвосмесь вносят комплексное минеральное удобрение для комнатных цветущих культур. Удобрение рекомендуется смешивать с водой, используемой для нижнего полива. Обратите внимание, что фиалке хватит ½ части дозы от той, что рекомендована производителем (смотрите на упаковке).', transfer='Заменять почвосмесь в емкости следует каждый год. Однако менять емкость на более крупную надо лишь тогда, когда это необходимо.', more_info='Более подробно можно прочитать здесь:\nhttps://rastenievod.com/fialki.html', photo='https://rastenievod.com/wp-content/uploads/2017/05/1-24.jpg'>"

USERS_PLANTS = ["<UsersPlants user_plant_id=1, user_id=1, name='Фиалка раз'>",
                "<UsersPlants user_plant_id=2, user_id=1, name='Фиалка два'>"]

NOTIFICATION_1 = ["<UsersNotifications notific_id=1, user_plant_id=1, notif_category=1, notif_frequency=3, time='11:00', first_date='12.05.2020', next_date='19.05.2020'>"]

CATEGORIES = ["<NotificationCategory id=1, category='Полив', actions='поливать'>",
            "<NotificationCategory id=2, category='Опрыскивание', actions='опрыскивать'>",
            "<NotificationCategory id=3, category='Удобрение', actions='удобрять'>",
            "<NotificationCategory id=4, category='Пересадка', actions='пересаживать'>"]

FREQUENCIES = ["<NotificationFrequency id=1, category='Каждый день', day_plus=1, month_plus=0>",
            "<NotificationFrequency id=2, category='Через день', day_plus=2, month_plus=0>",
            "<NotificationFrequency id=3, category='Раз в три дня', day_plus=3, month_plus=0>",
            "<NotificationFrequency id=4, category='Раз в неделю', day_plus=7, month_plus=0>",
            "<NotificationFrequency id=5, category='Раз в две недели', day_plus=14, month_plus=0>",
            "<NotificationFrequency id=6, category='Раз в месяц', day_plus=0, month_plus=1>",
            "<NotificationFrequency id=7, category='Раз в полгода', day_plus=0, month_plus=6>",
            "<NotificationFrequency id=8, category='Раз в год', day_plus=0, month_plus=12>"]