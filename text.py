from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

commandsGlobal = '/IELTS - get access to IELTS files\n/SAT - get access to SAT files'
commandsGlobalRU = 'Нажмите на /IELTSru чтобы получить файлы по IELTS\nНажмите на /SATru чтобы получить файлы по SAT'
commandsGlobalKZ = '/IELTSkz командасына басып, IELTS файлдарын алыңыз\n/SATkz командасына басып, SAT файлдарын алыңыз'

eng_SATCommands = '/SAT_reading - get access to SAT Reading Book by Erica Meltzer\n/SAT_writing - get access to SAT Writing Book by Erica Meltzer\n/SAT_math - get access to SAT Panda Math Book\n/SAT_vocabulary1 - get access to SAT Vocabulary list (1)\n/SAT_vocabulary2 - get access to SAT Vocabulary list (2)\n/SAT_allRealTests - get access to All SAT Real Tests (2017-2020)\n/SAT_bubbleSheet - get access to Official SAT Bubble Sheet'
ru_SATCommands = '/SAT_reading - получить SAT Reading Book от Erica Meltzer\n/SAT_writing - получить SAT Writing Book от Erica Meltzer\n/SAT_math - получить SAT Panda Math Book\n/SAT_vocabulary1 - получить лист слов SAT (1)\n/SAT_vocabulary2 - получить лист слов SAT (2)\n/SAT_allRealTests - получить Все Реальный SAT Тесты (2017-2020)\n/SAT_bubbleSheet - получить Официальный Бланк SAT'
kz_SATCommands = '/SAT_reading - Erica Meltzer-дың SAT Reading Book алу\n/SAT_writing - Erica Meltzer-дың SAT Writing Book алу\n/SAT_math - SAT Panda Math Book алу\n/SAT_vocabulary1 - SAT Vocabulary list алу (1)\n/SAT_vocabulary2 - SAT Vocabulary list алу (2)\n/SAT_allRealTests - Барлық SAT Тестілерін алу (2017-2020)\n/SAT_bubbleSheet - SAT Ресми Тест Қағазын алу'

eng_IELTSCommands = '/IELTS_usefulBooks - get access to IELTS Useful Books\n/Speaking_Recordings - get access to IELTS Speaking Recordings\n/MockTest1 - get access to IELTS Mock Test 1\n/SpeakingFiles - get access to IELTS Speaking Files\n/Reading_Tips_Practice - get access to Reading Tips and Practice'
ru_IELTSCommands = '/IELTS_usefulBooks - получить полезные книги для IELTS\n/Speaking_Recordings - получить записи IELTS Speaking\n/MockTest1 - Получить IELTS Mock Test 1\n/SpeakingFiles - Получить файлы по IELTS Speaking\n/Reading_Tips_Practice - Получитьo Reading Tips и Practice'
kz_IELTSCommands = '/IELTS_usefulBooks - IELTS-қа қатысты пайдалы кітаптарды алу\n/Speaking_Recordings - IELTS Speaking жазбаларын алу\n/MockTest1 - IELTS Mock Test 1 алу\n/SpeakingFiles - IELTS Speaking файлдарын алу\n/Reading_Tips_Practice - Reading Tips және Practice алу'

Btn = ReplyKeyboardMarkup(
	[
	    [
	        KeyboardButton(text='🇬🇧 English')
	            
	    ],
	    [
	        KeyboardButton(text='🇷🇺 Русский'),
	        KeyboardButton(text='🇰🇿 Қазақша')
	    ]
	], resize_keyboard=True, one_time_keyboard=True
)