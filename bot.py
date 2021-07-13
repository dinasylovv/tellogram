from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import input_file
from text import commandsGlobal, commandsGlobalRU, commandsGlobalKZ, eng_SATCommands, ru_SATCommands, kz_SATCommands, Btn, eng_IELTSCommands, ru_IELTSCommands, kz_IELTSCommands
import os

bot = Bot(token='1883330499:AAFbxcWps8_-izMFMQ6XU9-DJ_bs0sQzNsg')
dp = Dispatcher(bot)

#start or Menu commands
@dp.message_handler(commands={"start"})
@dp.message_handler(commands={"Menu"})
async def start(message: types.Message):
	await message.reply('Hello!/Привет!/Сәлем!')
	await message.reply(text = 'Choose lang', reply_markup=Btn)

@dp.message_handler(content_types='document')
async def download_SAT_reading(message:types.Message):
	print(message.to_python())

#Global commands
@dp.message_handler(commands={'commandsGlobal'})
async def commandsGlobalen(message: types.Message):
	await message.answer(text=commandsGlobal)


@dp.message_handler(commands={'commandsGlobalRU'})
async def commandsGlobalru(message: types.Message):
	await message.answer(text=commandsGlobalRU)


@dp.message_handler(commands={'commandsGlobalKZ'})
async def commandsGlobalkz(message: types.Message):
	await message.answer(text=commandsGlobalKZ)


#IELTS menu
@dp.message_handler(commands={'IELTS'})
async def IELTS(message: types.Message):
	await message.answer(text=eng_IELTSCommands)
	await message.answer(text='/Menu - return to main menu')
@dp.message_handler(commands={'IELTSru'})
async def IELTSru(message: types.Message):
	await message.answer(text=ru_IELTSCommands)
	await message.answer(text='/Menu - вернуться в главное меню')
@dp.message_handler(commands={'IELTSkz'})
async def IELTSkz(message: types.Message):
	await message.answer(text=kz_IELTSCommands)
	await message.answer(text='/Menu - бастапқы мәзірге оралу')

#SAT menu
@dp.message_handler(commands={'SAT'})
async def commands(message: types.Message):
	await message.answer(text=eng_SATCommands)
	await message.answer(text='/Menu - return to main menu')

@dp.message_handler(commands={'SATru'})
async def commandsRU(message: types.Message):
	await message.answer(text=ru_SATCommands)
	await message.answer(text='/Menu - вернуться в главное меню')

@dp.message_handler(commands={'SATkz'})
async def commandsKZ(message: types.Message):
	await message.answer(text=kz_SATCommands)
	await message.answer(text='/Menu - бастапқы мәзірге оралу')


#IELTS FILES START
@dp.message_handler(commands={'IELTS_usefulBooks'})
async def IELTS(message: types.Message):
	await message.answer_document('BQACAgIAAxkBAAIDOGDtq05IlAW8XxocYwvBkJVGhFJ7AAI_DgACfNdxS8GRmjUyt4Y8IAQ')


@dp.message_handler(commands={'Speaking_Recordings'})
async def IELTS(message: types.Message):
	input_file = open('./files/speaking recordings.zip', 'rb')
	await message.answer_document(input_file)


@dp.message_handler(commands={'MockTest1'})
async def IELTS(message: types.Message):
	input_file = open('./files/Mock Test 1.zip', 'rb')
	await message.answer_document(input_file)


@dp.message_handler(commands={'SpeakingFiles'})
async def IELTS(message: types.Message):
	input_file = open('./files/21.12 Speaking.zip', 'rb')
	await message.answer_document(input_file)


@dp.message_handler(commands={'Reading_Tips_Practice'})
async def IELTS(message: types.Message):
	await message.answer_document('BQACAgIAAxkBAAIDRWDtq-sK3126IftX5hzc759-c8lYAAJUEQAC5QxwS3PluZt_CdfkIAQ')
#IELTS FILES END


#SAT FILES START
@dp.message_handler(commands={'SAT_writing'})
async def SATwriting(message: types.Message):
	await message.answer_document('BQACAgIAAxkBAAICx2DtFTJz6Cs1z2l37HmCA_oeWctBAAK0EAACfNdpS2smIB7Phc41IAQ')

@dp.message_handler(commands={'SAT_bubbleSheet'})
async def SATbubbleSheet(message: types.Message):
	input_file = open('./files/SAT - Bubble Sheet.pdf', 'rb')
	await message.answer_document(input_file)

@dp.message_handler(commands={'SAT_reading'})
async def SATbubbleSheet(message: types.Message):
	#input_file = open('./files/SAT - Erica Meltzer Reading.pdf', 'rb')
	await message.answer_document('BQACAgIAAxkBAAICr2DtFFrPqpAeBnSXVgSjUxDM6ZO_AAKvEAACfNdpS20BEZvhYVCEIAQ')

@dp.message_handler(commands={'SAT_math'})
async def SATbubbleSheet(message: types.Message):
	input_file = open('./files/SAT - Panda Math.pdf', 'rb')
	await message.answer_document(input_file)

@dp.message_handler(commands={'SAT_vocabulary1'})
async def SATbubbleSheet(message: types.Message):
	input_file = open('./files/SAT - Vocabulary.docx', 'rb')
	await message.answer_document(input_file)

@dp.message_handler(commands={'SAT_vocabulary2'})
async def SATbubbleSheet(message: types.Message):
	input_file = open('./files/SAT - Vocabulary 2nd.pdf', 'rb')
	await message.answer_document(input_file)

@dp.message_handler(commands={'SAT_allRealTests'})
async def SATbubbleSheet(message: types.Message):
	await message.answer_document('BQACAgIAAxkBAAIC52DtG8iAyOylIC7H872QL66BgZkUAALpDAACfNdxSy9CdvrOJ-q8IAQ')
#SAT FILES END

@dp.message_handler()
async def chosen_lang(message: types.Message):
	if message.text == '🇬🇧 English':
		await message.reply(text='You chose English')
		await message.answer(text='Tap on /commandsGlobal to view commands list')
	elif message.text == '🇷🇺 Русский':
		await message.reply(text='Вы выбрали русский язык')
		await message.answer(text='Нажмите на /commandsGlobalRU чтобы увидеть список команд')
	elif message.text == '🇰🇿 Қазақша':
		await message.reply(text='Сіз қазақ тілін таңдадыңыз')
		await message.answer(text='/commandsGlobalKZ командасына басып, толық тізімге қол жеткізе аласыз')
	lang = message.text

if __name__ == '__main__':
    executor.start_polling(dp)