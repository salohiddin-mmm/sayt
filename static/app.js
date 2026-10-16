/* ---------- Tarjimalar ---------- */
const T={
uz:{nav_jobs:"E'lonlar",nav_saved:"Saqlanganlar",login:"Kirish",logout:"Chiqish",hello:"Salom, ",post:"E'lon joylash",
hero_h1:"Ish kerakmi?",hero_h2:"Ish bizda bor, keling!",hero_p:"O'zbekistonning barcha viloyatlaridagi vakansiyalar bir joyda. Qidiring, saralang va ariza yuboring.",
ph_q:"Lavozim yoki kalit so'z: sotuvchi, haydovchi, Python...",all_reg:"Barcha viloyatlar",all_dist:"Barcha tumanlar",search:"Ish qidirish",
stat_active:"ta faol e'lon",stat_new:"tasi bugun qo'shilgan",tg:"Telegram kanalga obuna bo'ling",
warn_b:"Ehtiyot bo'ling. ",warn_t:"Ishga qabul uchun oldindan pul so'rashsa, bu firibgarlik belgisi. Shubhali e'lonni “Shikoyat qilish” tugmasi bilan yuboring.",
filters:"Filtrlar",f_type:"Ish turi",t_full:"To'liq stavka",t_part:"Yarim stavka",t_intern:"Amaliyot",f_region:"Hudud",remote:"Faqat masofaviy",
f_salary:"Maosh (mln so'm)",from:"dan",to:"gacha",sal_only:"Maosh ko'rsatilganlar",reset:"Filtrlarni tozalash",
sort_new:"Eng yangilari",sort_sal:"Maosh bo'yicha",found:"ta e'lon topildi",saved_title:"Saqlangan e'lonlar",back_all:"Barcha e'lonlar",
empty_t:"Hech narsa topilmadi",empty_d:"Qidiruv so'zini qisqartiring yoki filtrlarni tozalang.",
es_t:"Hali hech narsa saqlanmagan",es_d:"E'londagi ♡ belgisini bosib, yoqqanlarini shu yerga yig'ing.",
more:"Ko'proq ko'rsatish",left:"ta qoldi",new:"Yangi",remote_tag:"Masofaviy",mln:"mln so'm",ago_h:"soat oldin",ago_d:"kun oldin",
x_bonus:"+ bonus",x_food:"+ ovqat",x_weekly:"(haftalik to'lov)",x_deal:"(kelishuv asosida)",
d_type:"Ish turi",d_reg:"Hudud",d_sal:"Maosh",d_none:"Ko'rsatilmagan",d_desc:"Tavsif",d_req:"Talablar",d_con:"Aloqa",
apply:"Ariza yuborish",report:"Shikoyat qilish",reported:"Shikoyat yuborildi",dw_b:"Eslatma. ",dw_t:"Oldindan to'lov so'ralsa, rozi bo'lmang.",
co_jobs:"Ochiq vakansiyalar",
p_title:"E'lon joylash",p_sub:"E'lon tekshiruvdan keyin saytda chiqadi.",p_job:"Lavozim",p_co:"Kompaniya",p_cat:"Soha",p_type:"Ish turi",p_reg:"Viloyat",p_dist:"Tuman",
p_sal:"Maosh (ixtiyoriy)",p_sal_ph:"Masalan: 4-6 mln so'm",p_desc:"Tavsif",p_contact:"Aloqa (Telegram yoki telefon)",p_send:"Tekshiruvga yuborish",
p_ok_b:"Rahmat, e'lon qabul qilindi.",p_ok_t:"Tekshiruvdan keyin saytda chiqadi.",close:"Yopish",
tab_in:"Kirish",tab_up:"Ro'yxatdan o'tish",l_name:"Ismingiz",l_id:"Telefon yoki email",l_pw:"Parol",l_in:"Kirish",l_up:"Hisob yaratish",
l_note:"Kod telefon raqamingizga SMS orqali yuboriladi.",
reg_role:"Siz kimsiz?",role_seeker:"Ish qidiryapman",role_seeker_d:"Vakansiya qidirib, ariza yuboraman",role_emp:"Ish beruvchiman",role_emp_d:"Xodim qidiryapman, e'lon joylayman",l_company:"Kompaniya nomi",role_label_seeker:"Ish qidiruvchi",role_label_emp:"Ish beruvchi",
menu_profile:"Profil sozlamalari",choose:"Tanlang",
pr_title:"Profil sozlamalari",pr_photo_btn:"Rasm tanlash",pr_photo_rm:"O'chirish",pr_photo_hint:"JPG yoki PNG. Rasm kvadrat shaklida kesiladi.",
pr_name:"Ism",pr_email:"Email",pr_phone:"Telefon",pr_field:"Qiziqish sohasi",pr_tg:"Telegram",pr_about:"O'zim haqimda",
pr_co:"Kompaniya nomi",pr_site:"Kompaniya sayti yoki Telegram",pr_co_about:"Kompaniya haqida",pr_notify:"Yangi vakansiyalar haqida xabar olish",
pr_save:"Saqlash",pr_saved:"Saqlandi",pr_private:"Ma'lumotlaringiz serverda saqlanadi.",
l_phone:"Telefon raqam",a_next:"Davom etish",a_forgot:"Parolni unutdingizmi?",a_sms:"SMS kod bilan kirish",a_show:"Ko'rsatish",a_hide:"Yashirish",a_pw_hint:"Kamida 8 ta belgi.",
a_sms_title:"SMS kod bilan kirish",a_sms_hint:"Telefon raqamingizga 6 xonali kod yuboramiz.",a_forgot_title:"Parolni tiklash",a_forgot_hint:"Ro'yxatdan o'tgan raqamingizni kiriting, SMS orqali kod yuboramiz.",
a_send:"Kod yuborish",a_code_title:"Kodni kiriting",a_code_sent:"Kod {p} raqamiga yuborildi.",a_code:"6 xonali kod",a_verify:"Tasdiqlash",a_resend:"Qayta yuborish",a_resend_in:"Qayta yuborish ({s} s)",
a_demo:"Demo: SMS o'rniga kod shu yerda ko'rsatiladi: ",a_new_title:"Yangi parol",a_new_pw:"Yangi parol",a_new_pw2:"Parolni takrorlang",a_save_pw:"Parolni saqlash",a_back:"Orqaga",pr_change_pw:"Parolni o'zgartirish (SMS orqali)",
e_phone:"Telefon raqamni to'liq kiriting (9 ta raqam).",e_cred:"Telefon raqam yoki parol noto'g'ri. Hisobingiz bo'lmasa, ro'yxatdan o'ting.",e_lock:"Juda ko'p urinish. {s} soniyadan keyin qayta urinib ko'ring.",
e_nopw:"Bu hisobga parol o'rnatilmagan. “Parolni unutdingizmi?” orqali yangi parol o'rnating.",e_exists:"Bu raqam allaqachon ro'yxatdan o'tgan. Kiring yoki parolni tiklang.",e_noacc:"Bu raqam ro'yxatdan o'tmagan. Avval ro'yxatdan o'ting.",
e_pw_short:"Parol kamida 8 ta belgidan iborat bo'lsin.",e_pw_match:"Parollar bir xil emas.",e_code:"Kod noto'g'ri yoki muddati tugagan. Kerak bo'lsa yangi kod so'rang.",e_code_exp:"Kod muddati tugadi. Yangi kod so'rang.",e_code_tries:"Urinishlar tugadi. Yangi kod so'rang.",
e_company:"Kompaniya nomini kiriting.",e_crypto:"Xavfsiz ulanish kerak: saytni localhost yoki HTTPS orqali oching.",
e_soon:"Biroz kuting: {s} soniyadan keyin qayta urinib ko'ring.",e_rate:"Juda ko'p so'rov. Keyinroq urinib ko'ring.",e_reset:"Ruxsat muddati tugadi. Parolni tiklashni qaytadan boshlang.",e_sms:"SMS yuborib bo'lmadi. Keyinroq urinib ko'ring.",
e_net:"Server bilan aloqa yo'q. Server ishlayotganini va saytni http://127.0.0.1:5000 orqali ochganingizni tekshiring.",e_server:"Xatolik yuz berdi. Qayta urinib ko'ring.",e_email:"Email noto'g'ri.",e_photo:"Rasm noto'g'ri yoki juda katta.",e_unauth:"Sessiya tugagan. Qaytadan kiring.",
a_dev:"Sinov rejimi: SMS yuborilmaydi. {p} uchun kodni server oynasida (terminalda) ko'ring.",
privacy_link:"Maxfiylik siyosati",terms_link:"Foydalanish shartlari",cons_pre:"Men roziman:",e_consent:"Davom etish uchun maxfiylik siyosati va foydalanish shartlariga rozilik bering.",
bot_title:"Telegram orqali tasdiqlash",bot_hint:"Kod Telegram orqali yuboriladi. Raqamingizni bir marta tasdiqlashingiz kerak:",bot_s1:"Pastdagi tugma orqali botni oching",bot_s2:"Botda “Start” tugmasini bosing",bot_s3:"“Raqamni ulashish” tugmasini bosing",bot_open:"Telegram botni ochish",bot_wait:"Tasdiqlashni kutyapmiz. Tasdiqlagach, bu oyna o'zi davom etadi.",a_code_tg:"Kod Telegramdagi IshTopar botiga yuborildi ({p}).",
menu_my:"Mening e'lonlarim",menu_admin:"Admin panel",my_title:"Mening e'lonlarim",my_empty:"Hali e'lon joylamagansiz.",my_confirm:"O'chirishni tasdiqlaysizmi?",st_pending:"Tekshiruvda",st_approved:"Chiqarilgan",st_rejected:"Rad etilgan",st_hidden:"Yashirilgan",delete:"O'chirish",
adm_title:"Moderatsiya",adm_pending:"Yangi",adm_hidden:"Shikoyat",adm_empty:"Hozircha hech narsa yo'q.",adm_approve:"Tasdiqlash",adm_reject:"Rad etish",adm_reports:"Shikoyatlar:",
p_sal_mln:"Maosh, mln so'm (ixtiyoriy)",p_extra:"Qo'shimcha",x_none:"Yo'q",p_remote:"Masofaviy ish",p_req:"Talablar",p_need_login:"E'lon joylash uchun ish beruvchi hisobi bilan kiring.",p_ok_admin:"E'lon saytda chiqdi.",
del_h:"Hisobni o'chirish",del_t:"Hisob va barcha e'lonlaringiz butunlay o'chiriladi. Buni qaytarib bo'lmaydi.",del_btn:"Hisobni o'chirish",del_confirm:"Hisobni butunlay o'chirishni tasdiqlaysizmi?",del_need_pw:"Parolni kiriting.",
e_net_t:"Ulanib bo'lmadi",empty_all_t:"Hozircha e'lonlar yo'q",empty_all_d:"Birinchi bo'lib e'lon joylang yoki keyinroq qaytib keling.",
e_job:"Maydonlarni to'g'ri to'ldiring (lavozim, tavsif, aloqa, hudud).",e_salary:"Maosh noto'g'ri kiritilgan.",e_employer:"E'lonni faqat ish beruvchi hisobi joylay oladi.",e_forbidden:"Ruxsat yo'q.",e_notfound:"Topilmadi.",
e_h:"Ish beruvchilar uchun",e_p:"Xodim qidiryapsizmi? E'lon joylang, tekshiruvdan keyin u saytda chiqadi.",
e1_h:"Oddiy e'lon",e1_t:"Forma orqali e'lon yuboring. Tekshiruvdan o'tgach saytda chiqadi.",
e2_h:"Ajratib ko'rsatish",e2_t:"Muhim vakansiyani ro'yxat tepasida ko'rsating.",
e3_h:"Telegram kanalda tarqatish",e3_t:"E'lon IshTopar kanaliga ham joylanadi.",
foot1:"Ochiq kanallardagi ish e'lonlarini tartiblab beradi.",foot3:"Namuna dizayn: e'lonlar tasodifiy va haqiqiy emas.",
c_all:"Barchasi",c_sales:"Savdo",c_transport:"Transport",c_edu:"Ta'lim",c_office:"Ofis",c_it:"IT",c_service:"Xizmat",c_build:"Qurilish"},
ru:{nav_jobs:"Вакансии",nav_saved:"Сохранённые",login:"Войти",logout:"Выйти",hello:"Привет, ",post:"Разместить вакансию",
hero_h1:"Нужна работа?",hero_h2:"Работа у нас есть, заходите!",hero_p:"Вакансии из всех областей Узбекистана в одном месте. Ищите, фильтруйте и откликайтесь.",
ph_q:"Должность или слово: продавец, водитель, Python...",all_reg:"Все области",all_dist:"Все районы",search:"Найти работу",
stat_active:"активных вакансий",stat_new:"добавлено сегодня",tg:"Подписаться на Telegram-канал",
warn_b:"Будьте осторожны. ",warn_t:"Если за трудоустройство просят деньги вперёд, это признак мошенничества. Отправьте жалобу кнопкой «Пожаловаться».",
filters:"Фильтры",f_type:"Тип работы",t_full:"Полная занятость",t_part:"Частичная занятость",t_intern:"Стажировка",f_region:"Регион",remote:"Только удалённо",
f_salary:"Зарплата (млн сум)",from:"от",to:"до",sal_only:"С указанной зарплатой",reset:"Сбросить фильтры",
sort_new:"Сначала новые",sort_sal:"По зарплате",found:"вакансий найдено",saved_title:"Сохранённые вакансии",back_all:"Все вакансии",
empty_t:"Ничего не найдено",empty_d:"Сократите запрос или сбросьте фильтры.",
es_t:"Пока ничего не сохранено",es_d:"Нажмите ♡ на вакансии, чтобы собрать понравившиеся здесь.",
more:"Показать ещё",left:"осталось",new:"Новая",remote_tag:"Удалённо",mln:"млн сум",ago_h:"ч. назад",ago_d:"дн. назад",
x_bonus:"+ бонус",x_food:"+ питание",x_weekly:"(выплата еженедельно)",x_deal:"(по договорённости)",
d_type:"Тип работы",d_reg:"Регион",d_sal:"Зарплата",d_none:"Не указана",d_desc:"Описание",d_req:"Требования",d_con:"Контакты",
apply:"Откликнуться",report:"Пожаловаться",reported:"Жалоба отправлена",dw_b:"Помните. ",dw_t:"Если просят оплату вперёд, не соглашайтесь.",
co_jobs:"Открытые вакансии",
p_title:"Разместить вакансию",p_sub:"После проверки вакансия появится на сайте.",p_job:"Должность",p_co:"Компания",p_cat:"Сфера",p_type:"Тип работы",p_reg:"Область",p_dist:"Район",
p_sal:"Зарплата (необязательно)",p_sal_ph:"Например: 4-6 млн сум",p_desc:"Описание",p_contact:"Контакт (Telegram или телефон)",p_send:"Отправить на проверку",
p_ok_b:"Спасибо, вакансия принята.",p_ok_t:"После проверки она появится на сайте.",close:"Закрыть",
tab_in:"Вход",tab_up:"Регистрация",l_name:"Ваше имя",l_id:"Телефон или email",l_pw:"Пароль",l_in:"Войти",l_up:"Создать аккаунт",
l_note:"Код отправляется SMS на ваш номер телефона.",
reg_role:"Кто вы?",role_seeker:"Ищу работу",role_seeker_d:"Ищу вакансии и откликаюсь",role_emp:"Я работодатель",role_emp_d:"Ищу сотрудников, размещаю вакансии",l_company:"Название компании",role_label_seeker:"Соискатель",role_label_emp:"Работодатель",
menu_profile:"Настройки профиля",choose:"Выберите",
pr_title:"Настройки профиля",pr_photo_btn:"Выбрать фото",pr_photo_rm:"Удалить",pr_photo_hint:"JPG или PNG. Фото обрезается до квадрата.",
pr_name:"Имя",pr_email:"Email",pr_phone:"Телефон",pr_field:"Сфера интересов",pr_tg:"Telegram",pr_about:"О себе",
pr_co:"Название компании",pr_site:"Сайт или Telegram компании",pr_co_about:"О компании",pr_notify:"Получать уведомления о новых вакансиях",
pr_save:"Сохранить",pr_saved:"Сохранено",pr_private:"Ваши данные хранятся на сервере.",
l_phone:"Номер телефона",a_next:"Продолжить",a_forgot:"Забыли пароль?",a_sms:"Войти по SMS-коду",a_show:"Показать",a_hide:"Скрыть",a_pw_hint:"Не менее 8 символов.",
a_sms_title:"Вход по SMS-коду",a_sms_hint:"Мы отправим 6-значный код на ваш номер телефона.",a_forgot_title:"Восстановление пароля",a_forgot_hint:"Введите номер, на который зарегистрирован аккаунт, мы отправим код по SMS.",
a_send:"Отправить код",a_code_title:"Введите код",a_code_sent:"Код отправлен на номер {p}.",a_code:"6-значный код",a_verify:"Подтвердить",a_resend:"Отправить ещё раз",a_resend_in:"Отправить ещё раз ({s} с)",
a_demo:"Демо: вместо SMS код показан здесь: ",a_new_title:"Новый пароль",a_new_pw:"Новый пароль",a_new_pw2:"Повторите пароль",a_save_pw:"Сохранить пароль",a_back:"Назад",pr_change_pw:"Сменить пароль (по SMS)",
e_phone:"Введите номер полностью (9 цифр).",e_cred:"Неверный номер телефона или пароль. Если аккаунта нет, зарегистрируйтесь.",e_lock:"Слишком много попыток. Повторите через {s} с.",
e_nopw:"Для этого аккаунта пароль не задан. Задайте новый через «Забыли пароль?».",e_exists:"Этот номер уже зарегистрирован. Войдите или восстановите пароль.",e_noacc:"Этот номер не зарегистрирован. Сначала зарегистрируйтесь.",
e_pw_short:"Пароль должен содержать не менее 8 символов.",e_pw_match:"Пароли не совпадают.",e_code:"Неверный код или срок его действия истёк. При необходимости запросите новый.",e_code_exp:"Срок действия кода истёк. Запросите новый.",e_code_tries:"Попытки закончились. Запросите новый код.",
e_company:"Введите название компании.",e_crypto:"Нужно безопасное соединение: откройте сайт через localhost или HTTPS.",
e_soon:"Подождите: повторите через {s} с.",e_rate:"Слишком много запросов. Повторите позже.",e_reset:"Срок разрешения истёк. Начните восстановление заново.",e_sms:"Не удалось отправить SMS. Повторите позже.",
e_net:"Нет связи с сервером. Убедитесь, что сервер запущен и сайт открыт через http://127.0.0.1:5000.",e_server:"Произошла ошибка. Повторите попытку.",e_email:"Неверный email.",e_photo:"Фото неверное или слишком большое.",e_unauth:"Сессия истекла. Войдите снова.",
a_dev:"Тестовый режим: SMS не отправляется. Код для {p} смотрите в окне сервера (терминале).",
privacy_link:"Политика конфиденциальности",terms_link:"Условия использования",cons_pre:"Я принимаю:",e_consent:"Чтобы продолжить, примите политику конфиденциальности и условия использования.",
bot_title:"Подтверждение через Telegram",bot_hint:"Код придёт в Telegram. Номер нужно подтвердить один раз:",bot_s1:"Откройте бота кнопкой ниже",bot_s2:"Нажмите «Start» в боте",bot_s3:"Нажмите «Поделиться номером»",bot_open:"Открыть Telegram-бота",bot_wait:"Ждём подтверждения. После него это окно продолжит само.",a_code_tg:"Код отправлен в Telegram-бот IshTopar ({p}).",
menu_my:"Мои вакансии",menu_admin:"Админ-панель",my_title:"Мои вакансии",my_empty:"Вы пока не размещали вакансий.",my_confirm:"Подтвердить удаление?",st_pending:"На проверке",st_approved:"Опубликована",st_rejected:"Отклонена",st_hidden:"Скрыта",delete:"Удалить",
adm_title:"Модерация",adm_pending:"Новые",adm_hidden:"Жалобы",adm_empty:"Пока ничего нет.",adm_approve:"Одобрить",adm_reject:"Отклонить",adm_reports:"Жалобы:",
p_sal_mln:"Зарплата, млн сум (необязательно)",p_extra:"Дополнительно",x_none:"Нет",p_remote:"Удалённая работа",p_req:"Требования",p_need_login:"Чтобы разместить вакансию, войдите как работодатель.",p_ok_admin:"Вакансия опубликована.",
del_h:"Удаление аккаунта",del_t:"Аккаунт и все ваши вакансии будут удалены навсегда. Это нельзя отменить.",del_btn:"Удалить аккаунт",del_confirm:"Удалить аккаунт навсегда?",del_need_pw:"Введите пароль.",
e_net_t:"Не удалось подключиться",empty_all_t:"Пока нет вакансий",empty_all_d:"Разместите первую вакансию или загляните позже.",
e_job:"Заполните поля правильно (должность, описание, контакт, регион).",e_salary:"Неверно указана зарплата.",e_employer:"Вакансии могут размещать только работодатели.",e_forbidden:"Нет доступа.",e_notfound:"Не найдено.",
e_h:"Для работодателей",e_p:"Ищете сотрудников? Разместите вакансию, после проверки она появится на сайте.",
e1_h:"Обычная вакансия",e1_t:"Отправьте вакансию через форму. После проверки она появится на сайте.",
e2_h:"Выделение",e2_t:"Покажите важную вакансию в начале списка.",
e3_h:"Рассылка в Telegram-канале",e3_t:"Вакансия также попадёт в канал IshTopar.",
foot1:"Собирает вакансии из открытых каналов в одном списке.",foot3:"Демо-дизайн: вакансии вымышленные.",
c_all:"Все",c_sales:"Торговля",c_transport:"Транспорт",c_edu:"Образование",c_office:"Офис",c_it:"IT",c_service:"Сервис",c_build:"Строительство"},
en:{nav_jobs:"Jobs",nav_saved:"Saved",login:"Log in",logout:"Log out",hello:"Hi, ",post:"Post a job",
hero_h1:"Need a job?",hero_h2:"We've got work, come on in!",hero_p:"Vacancies from every region of Uzbekistan in one place. Search, filter and apply.",
ph_q:"Job title or keyword: seller, driver, Python...",all_reg:"All regions",all_dist:"All districts",search:"Find jobs",
stat_active:"active jobs",stat_new:"added today",tg:"Join our Telegram channel",
warn_b:"Stay alert. ",warn_t:"If you are asked to pay money up front to get a job, it is a sign of fraud. Report suspicious listings with the “Report” button.",
filters:"Filters",f_type:"Job type",t_full:"Full-time",t_part:"Part-time",t_intern:"Internship",f_region:"Region",remote:"Remote only",
f_salary:"Salary (mln UZS)",from:"from",to:"to",sal_only:"Salary shown",reset:"Clear filters",
sort_new:"Newest first",sort_sal:"By salary",found:"jobs found",saved_title:"Saved jobs",back_all:"All jobs",
empty_t:"Nothing found",empty_d:"Try a shorter search or clear the filters.",
es_t:"Nothing saved yet",es_d:"Tap ♡ on a job to collect your favourites here.",
more:"Show more",left:"left",new:"New",remote_tag:"Remote",mln:"mln UZS",ago_h:"h ago",ago_d:"d ago",
x_bonus:"+ bonus",x_food:"+ meals",x_weekly:"(paid weekly)",x_deal:"(negotiable)",
d_type:"Job type",d_reg:"Region",d_sal:"Salary",d_none:"Not specified",d_desc:"Description",d_req:"Requirements",d_con:"Contact",
apply:"Apply",report:"Report",reported:"Report sent",dw_b:"Remember. ",dw_t:"Never agree to pay money up front.",
co_jobs:"Open positions",
p_title:"Post a job",p_sub:"Your listing will appear on the site after review.",p_job:"Job title",p_co:"Company",p_cat:"Field",p_type:"Job type",p_reg:"Region",p_dist:"District",
p_sal:"Salary (optional)",p_sal_ph:"For example: 4-6 mln UZS",p_desc:"Description",p_contact:"Contact (Telegram or phone)",p_send:"Send for review",
p_ok_b:"Thank you, your listing was received.",p_ok_t:"It will appear on the site after review.",close:"Close",
tab_in:"Log in",tab_up:"Sign up",l_name:"Your name",l_id:"Phone or email",l_pw:"Password",l_in:"Log in",l_up:"Create account",
l_note:"The code is sent to your phone number by SMS.",
reg_role:"Who are you?",role_seeker:"I'm looking for a job",role_seeker_d:"I search for jobs and apply",role_emp:"I'm an employer",role_emp_d:"I'm hiring and posting jobs",l_company:"Company name",role_label_seeker:"Job seeker",role_label_emp:"Employer",
menu_profile:"Profile settings",choose:"Choose",
pr_title:"Profile settings",pr_photo_btn:"Choose photo",pr_photo_rm:"Remove",pr_photo_hint:"JPG or PNG. The photo is cropped to a square.",
pr_name:"Name",pr_email:"Email",pr_phone:"Phone",pr_field:"Field of interest",pr_tg:"Telegram",pr_about:"About me",
pr_co:"Company name",pr_site:"Company website or Telegram",pr_co_about:"About the company",pr_notify:"Notify me about new vacancies",
pr_save:"Save",pr_saved:"Saved",pr_private:"Your data is stored on the server.",
l_phone:"Phone number",a_next:"Continue",a_forgot:"Forgot password?",a_sms:"Log in with SMS code",a_show:"Show",a_hide:"Hide",a_pw_hint:"At least 8 characters.",
a_sms_title:"Log in with SMS code",a_sms_hint:"We will send a 6-digit code to your phone number.",a_forgot_title:"Reset password",a_forgot_hint:"Enter the number your account is registered with and we will send a code by SMS.",
a_send:"Send code",a_code_title:"Enter the code",a_code_sent:"The code was sent to {p}.",a_code:"6-digit code",a_verify:"Verify",a_resend:"Resend",a_resend_in:"Resend ({s} s)",
a_demo:"Demo: the code is shown here instead of an SMS: ",a_new_title:"New password",a_new_pw:"New password",a_new_pw2:"Repeat password",a_save_pw:"Save password",a_back:"Back",pr_change_pw:"Change password (via SMS)",
e_phone:"Enter the full phone number (9 digits).",e_cred:"Wrong phone number or password. If you have no account, sign up.",e_lock:"Too many attempts. Try again in {s} s.",
e_nopw:"No password is set for this account. Set a new one via “Forgot password?”.",e_exists:"This number is already registered. Log in or reset your password.",e_noacc:"This number is not registered. Sign up first.",
e_pw_short:"The password must be at least 8 characters.",e_pw_match:"Passwords do not match.",e_code:"Wrong code or it has expired. Request a new one if needed.",e_code_exp:"The code has expired. Request a new one.",e_code_tries:"No attempts left. Request a new code.",
e_company:"Enter the company name.",e_crypto:"A secure connection is required: open the site via localhost or HTTPS.",
e_soon:"Please wait: try again in {s} s.",e_rate:"Too many requests. Try again later.",e_reset:"Permission expired. Start the password reset again.",e_sms:"Could not send the SMS. Try again later.",
e_net:"Cannot reach the server. Check that the server is running and the site is opened via http://127.0.0.1:5000.",e_server:"Something went wrong. Please try again.",e_email:"Invalid email.",e_photo:"The photo is invalid or too large.",e_unauth:"Session expired. Please log in again.",
a_dev:"Test mode: no SMS is sent. See the code for {p} in the server window (terminal).",
privacy_link:"Privacy policy",terms_link:"Terms of use",cons_pre:"I agree to:",e_consent:"To continue, accept the privacy policy and the terms of use.",
bot_title:"Confirm via Telegram",bot_hint:"The code is sent via Telegram. You need to confirm your number once:",bot_s1:"Open the bot with the button below",bot_s2:"Press “Start” in the bot",bot_s3:"Press “Share number”",bot_open:"Open the Telegram bot",bot_wait:"Waiting for confirmation. This window continues by itself afterwards.",a_code_tg:"The code was sent to the IshTopar Telegram bot ({p}).",
menu_my:"My jobs",menu_admin:"Admin panel",my_title:"My jobs",my_empty:"You have not posted any jobs yet.",my_confirm:"Confirm deletion?",st_pending:"Under review",st_approved:"Published",st_rejected:"Rejected",st_hidden:"Hidden",delete:"Delete",
adm_title:"Moderation",adm_pending:"New",adm_hidden:"Reported",adm_empty:"Nothing here yet.",adm_approve:"Approve",adm_reject:"Reject",adm_reports:"Reports:",
p_sal_mln:"Salary, mln UZS (optional)",p_extra:"Extra",x_none:"None",p_remote:"Remote work",p_req:"Requirements",p_need_login:"Log in as an employer to post a job.",p_ok_admin:"The job is live.",
del_h:"Delete account",del_t:"Your account and all your jobs will be deleted permanently. This cannot be undone.",del_btn:"Delete account",del_confirm:"Delete the account permanently?",del_btn:"Delete account",
e_net_t:"Cannot connect",empty_all_t:"No jobs yet",empty_all_d:"Post the first job or come back later.",
e_job:"Fill in the fields correctly (title, description, contact, region).",e_salary:"The salary is invalid.",e_employer:"Only employers can post jobs.",e_forbidden:"Access denied.",e_notfound:"Not found.",
e_h:"For employers",e_p:"Looking for staff? Post a job and it will appear on the site after review.",
e1_h:"Standard listing",e1_t:"Send your job through the form. It goes live after review.",
e2_h:"Highlighting",e2_t:"Show an important vacancy at the top of the list.",
e3_h:"Telegram channel reach",e3_t:"Your listing is also posted to the IshTopar channel.",
foot1:"Gathers jobs from open channels into one list.",foot3:"Demo design: the listings are made up.",
c_all:"All",c_sales:"Sales",c_transport:"Transport",c_edu:"Education",c_office:"Office",c_it:"IT",c_service:"Service",c_build:"Construction"}
};

/* ---------- Hududlar ---------- */
const REG={
"Toshkent shahri":{ru:"город Ташкент",d:["Bektemir","Chilonzor","Mirobod","Mirzo Ulug'bek","Olmazor","Sergeli","Shayxontohur","Uchtepa","Yakkasaroy","Yashnobod","Yunusobod"]},
"Toshkent viloyati":{ru:"Ташкентская область",d:["Nurafshon sh.","Angren sh.","Olmaliq sh.","Chirchiq sh.","Bekobod","Bo'ka","Bo'stonliq","Chinoz","Ohangaron","Oqqo'rg'on","Parkent","Piskent","Qibray","Quyi Chirchiq","O'rta Chirchiq","Yangiyo'l","Yuqori Chirchiq","Zangiota","Toshkent tumani"]},
"Samarqand viloyati":{ru:"Самаркандская область",d:["Samarqand sh.","Kattaqo'rg'on sh.","Bulung'ur","Ishtixon","Jomboy","Kattaqo'rg'on","Narpay","Nurobod","Oqdaryo","Pastdarg'om","Paxtachi","Payariq","Qo'shrabot","Samarqand","Toyloq","Urgut"]},
"Farg'ona viloyati":{ru:"Ферганская область",d:["Farg'ona sh.","Marg'ilon sh.","Qo'qon sh.","Quvasoy sh.","Oltiariq","Bag'dod","Beshariq","Buvayda","Dang'ara","Farg'ona","Furqat","Qo'shtepa","Quva","Rishton","So'x","Toshloq","Uchko'prik","O'zbekiston","Yozyovon"]},
"Andijon viloyati":{ru:"Андижанская область",d:["Andijon sh.","Xonobod sh.","Andijon","Asaka","Baliqchi","Bo'z","Buloqboshi","Izboskan","Jalaquduq","Xo'jaobod","Qo'rg'ontepa","Marhamat","Oltinko'l","Paxtaobod","Shahrixon","Ulug'nor"]},
"Namangan viloyati":{ru:"Наманганская область",d:["Namangan sh.","Chortoq","Chust","Davlatobod","Kosonsoy","Mingbuloq","Namangan","Norin","Pop","To'raqo'rg'on","Uchqo'rg'on","Uychi","Yangiqo'rg'on"]},
"Buxoro viloyati":{ru:"Бухарская область",d:["Buxoro sh.","Kogon sh.","Buxoro","G'ijduvon","Jondor","Kogon","Olot","Peshku","Qorako'l","Qorovulbozor","Romitan","Shofirkon","Vobkent"]},
"Navoiy viloyati":{ru:"Навоийская область",d:["Navoiy sh.","Zarafshon sh.","Karmana","Konimex","Navbahor","Nurota","Qiziltepa","Tomdi","Uchquduq","Xatirchi"]},
"Qashqadaryo viloyati":{ru:"Кашкадарьинская область",d:["Qarshi sh.","Shahrisabz sh.","Chiroqchi","Dehqonobod","G'uzor","Kasbi","Kitob","Koson","Ko'kdala","Mirishkor","Muborak","Nishon","Qamashi","Qarshi","Shahrisabz","Yakkabog'"]},
"Surxondaryo viloyati":{ru:"Сурхандарьинская область",d:["Termiz sh.","Angor","Boysun","Denov","Jarqo'rg'on","Muzrabot","Oltinsoy","Qiziriq","Qumqo'rg'on","Sariosiyo","Sherobod","Sho'rchi","Termiz","Uzun"]},
"Jizzax viloyati":{ru:"Джизакская область",d:["Jizzax sh.","Arnasoy","Baxmal","Do'stlik","Forish","G'allaorol","Mirzacho'l","Paxtakor","Sharof Rashidov","Yangiobod","Zafarobod","Zarbdor","Zomin"]},
"Sirdaryo viloyati":{ru:"Сырдарьинская область",d:["Guliston sh.","Shirin sh.","Yangiyer sh.","Boyovut","Guliston","Mirzaobod","Oqoltin","Sardoba","Sayxunobod","Sirdaryo","Xovos"]},
"Xorazm viloyati":{ru:"Хорезмская область",d:["Urganch sh.","Xiva sh.","Bog'ot","Gurlan","Hazorasp","Xiva","Xonqa","Qo'shko'pir","Shovot","Tuproqqal'a","Urganch","Yangiariq","Yangibozor"]},
"Qoraqalpog'iston Respublikasi":{ru:"Республика Каракалпакстан",d:["Nukus sh.","Amudaryo","Beruniy","Bo'zatov","Chimboy","Ellikqal'a","Kegeyli","Mo'ynoq","Nukus","Qanliko'l","Qo'ng'irot","Qorao'zak","Shumanay","Taxiatosh","Taxtako'pir","To'rtko'l","Xo'jayli"]}
};

const REG_EN={"Toshkent shahri":"Tashkent city","Toshkent viloyati":"Tashkent region","Samarqand viloyati":"Samarkand region","Farg'ona viloyati":"Fergana region","Andijon viloyati":"Andijan region","Namangan viloyati":"Namangan region","Buxoro viloyati":"Bukhara region","Navoiy viloyati":"Navoi region","Qashqadaryo viloyati":"Kashkadarya region","Surxondaryo viloyati":"Surkhandarya region","Jizzax viloyati":"Jizzakh region","Sirdaryo viloyati":"Syrdarya region","Xorazm viloyati":"Khorezm region","Qoraqalpog'iston Respublikasi":"Republic of Karakalpakstan"};
const CATS=["all","sales","transport","edu","office","it","service","build"];
const PAGE=10;

/* ---------- Yordamchi Funksiyalar ---------- */
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const state={lang:"uz",cat:"all",view:"all",saved:new Set(),user:null,jobs:[],total:0,stats:{total:0,today:0},loaded:false,err:false};
const t=k=>T[state.lang][k]??T.uz[k]??k;
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const regName=r=>!REG[r]?r:state.lang==="ru"?REG[r].ru:state.lang==="en"?REG_EN[r]:r;
const ago=h=>h<24?h+" "+t("ago_h"):Math.floor(h/24)+" "+t("ago_d");

function salaryText(j){
  if(!j.s)return "";
  const [a,b]=j.s;let s=(a===b?a:a+"-"+b).toString();
  if(state.lang!=="en")s=s.replace(".",",");
  s+=" "+t("mln");if(j.x)s+=" "+t("x_"+j.x);return s;
}

async function api(url,opt={}){
  try{
    const r=await fetch(url,{headers:{"Content-Type":"application/json",...opt.headers},...opt});
    const d=await r.json();
    return {ok:r.ok,data:d};
  }catch(e){
    return {ok:false,data:null};
  }
}

/* ---------- UI va Tilni Yangilash ---------- */
function updateI18n(){
  $$("[data-i18n]").forEach(el=>{
    const k=el.getAttribute("data-i18n");
    if(T[state.lang][k]) el.textContent=T[state.lang][k];
  });
  $$("[data-ph]").forEach(el=>{
    const k=el.getAttribute("data-ph");
    if(T[state.lang][k]) el.placeholder=T[state.lang][k];
  });
  renderCats();
  fillRegions($("#regionTop"),"all_reg");
  fillRegions($("#region"),"all_reg");
  fillRegions($("#pRegion"),"choose");
  fillRegions($("#prRegion"),"choose");
}

function renderCats(){
  const box=$("#cats"); if(!box) return;
  box.innerHTML=CATS.map(c=>`<button class="chip" data-cat="${c}" aria-pressed="${state.cat===c}">${esc(t("c_"+c))}</button>`).join("");
}

function renderStats(){
  if($("#statCount")) $("#statCount").textContent=state.stats.total;
  if($("#statNew")) $("#statNew").textContent=state.stats.today;
}

function fillRegions(sel,allKey){
  if(!sel) return;
  const cur=sel.value;
  sel.innerHTML=(allKey?`<option value="">${esc(t(allKey))}</option>`:"")+Object.keys(REG).map(r=>`<option value="${esc(r)}">${esc(regName(r))}</option>`).join("");
  sel.value=cur&&REG[cur]?cur:"";
}

const cardHtml=j=>`
  <article class="job" data-id="${j.id}" tabindex="0">
    <div class="avatar" aria-hidden="true">${esc((j.c||"?")[0])}</div>
    <div>
      <h3>${esc(j.t)}${j.hours<24?`<span class="badge-new">${esc(t("new"))}</span>`:""}</h3>
      <div class="meta"><button class="colink" data-co="${esc(j.c)}">${esc(j.c)}</button> • ${esc(j.dist?j.dist+", ":"")}${esc(regName(j.reg))}</div>
      <div class="tags">
        ${j.s?`<span class="tag salary">${esc(salaryText(j))}</span>`:""}
        <span class="tag">${esc(t("t_"+j.type))}</span>
        ${j.remote?`<span class="tag">${esc(t("remote_tag"))}</span>`:""}
      </div>
    </div>
    <div class="side">
      <button class="save" data-id="${j.id}" aria-label="Save" aria-pressed="${state.saved.has(j.id)}">♡</button>
      <span>${ago(j.hours)}</span>
    </div>
  </article>
`;

async function loadJobs(){
  const box=$("#jobs"); if(!box) return;
  box.innerHTML=`<div class="empty"><strong>Yuklanmoqda...</strong></div>`;
  const r=await api("/api/jobs");
  if(r.ok && r.data){
    state.jobs=r.data.jobs||[];
    state.stats=r.data.stats||{total:state.jobs.length,today:0};
    renderStats();
    if(state.jobs.length===0){
      box.innerHTML=`<div class="empty"><strong>${esc(t("empty_t"))}</strong><p>${esc(t("empty_d"))}</p></div>`;
    }else{
      box.innerHTML=state.jobs.map(cardHtml).join("");
    }
  }else{
    box.innerHTML=`<div class="empty"><strong>${esc(t("empty_t"))}</strong></div>`;
  }
}

/* ---------- Boshlang'ich Sozlamalar ---------- */
document.addEventListener("DOMContentLoaded",()=>{
  updateI18n();
  loadJobs();

  // Til o'zgartirish
  $$(".lang button").forEach(btn=>{ btn.addEventListener("click",()=>{ $$
(".lang button").forEach(b=>b.setAttribute("aria-pressed","false"));
      btn.setAttribute("aria-pressed","true");
      state.lang=btn.getAttribute("data-lang");
      updateI18n();
      loadJobs();
    });
  });

  // Kategoriya tanlash
  if($("#cats")){
    $("#cats").addEventListener("click",e=>{
      const btn=e.target.closest(".chip");
      if(!btn) return;
      state.cat=btn.getAttribute("data-cat");
      renderCats();
      loadJobs();
    });
  }

  // Mavzu (Dark/Light) o'zgartirish
  if($("#themeBtn")){
    $("#themeBtn").addEventListener("click",()=>{
      const dark=document.documentElement.getAttribute("data-theme")==="dark";
      document.documentElement.setAttribute("data-theme",dark?"light":"dark");
    });
  }
});
