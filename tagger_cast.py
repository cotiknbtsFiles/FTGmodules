from asyncio import sleep
from .. import loader, utils

def register(cb):
	cb(TaggerMod())
	
class TaggerMod(loader.Module):
	"""Часто отмечает выбранного пользователя"""
	strings = {'name': 'Tagger cust by cotik_'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
		
	async def taggercmd(self, message):
		""".tagger <колличество> <реплей>"""
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("<b>Зачем звал, тут же никого нет? >=(</b>")
			return
		id = reply.sender_id
		args = utils.get_args(message)
		count = 50
		if args:
			if args[0].isdigit():
				if int(args[0]) < 0:
					count = 50
				else:
					count = int(args[0])
		txt = '<a href="tg://user?id={}">{}</a>'
		await message.edit(txt.format(id, "Ну покормить меня! >=("))
		for _ in range(count):
			await sleep(0.3)
			msg = await message.client.send_message(message.to_id, txt.format(id, "Покормить меня 🥟"), reply_to=message)
			if not msg.is_reply:
				await msg.edit("<b>Ураааааа!</b>")
				break
			await sleep(0.3)
			await msg.delete()
				
			