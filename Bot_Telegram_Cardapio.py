import telebot
import time
from telebot import types

bot_token = 'TOKEN_BOT_TELEGRAM'

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(func=lambda message: True)
@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda msg: msg.text is not None and 'menu' in msg.text.lower().replace(" ",""))
def menu(message):
    primeiro_nome = message.from_user.first_name
    id_chat = message.chat.id
    custom = types.ReplyKeyboardRemove()
    if message.text.lower().replace(" ","") == 'menu' or message.text.lower().replace(" ","") == '/start':
        bot.send_message(id_chat, f"🔹Olá <strong>{primeiro_nome}</strong> 😄\n\n💬Bem-vindo ao cardápio online de Jerônimo Monteiro!!!\n\n🍔🍦Digite o <strong><em><u>NOME</u></em></strong> ou escolha um <strong><em><u>ID</u></em></strong> para mais informações🍟🍕\n\n🆔<u>01</u>  ▶Point da Villa\n🆔<u>02</u>  ▶Los Burgers\n🆔<u>03</u>  ▶Antonio Lanches\n🆔<u>04</u>  ▶Primor Delivery\n🆔<u>05</u>  ▶Fazenda\n🆔<u>06</u>  ▶Altas Horas\n🆔<u>07</u>  ▶Garagem Açaí\n🆔<u>08</u>  ▶Cia dos Lanches\n🆔<u>09</u>  ▶Cia do Açaí\n🆔<u>10</u>  ▶Barba Russa\n🆔<u>11</u>  ▶Serve Bem\n🆔<u>12</u>  ▶Pastelaria Mix Lanches\n🆔<u>13</u>  ▶Bar do Nicola\n🆔<u>14</u>  ▶DoceriAna\n🆔<u>15</u>  ▶Elisia Amaral Gourmet\n🆔<u>16</u>  ▶Mirim Lanches\n🆔<u>17</u>  ▶Garagem Lanches\n🆔<u>18</u>  ▶Os Brutos",reply_markup=custom, disable_web_page_preview=True, parse_mode='HTML')
        botao_categoria(message)
    elif message.text.lower().replace(" ","") == '0' or message.text.lower().replace(" ","") == 'categorias' or message.text.lower().replace(" ","") == 'categoria':
        categorias(message)
    elif message.text.lower().replace(" ","") == 'pizzas🍕' or message.text.lower().replace(" ","") == 'pizzas' or message.text.lower().replace(" ","") == '🍕pizzas🍕':
        pizzas(message)
    elif message.text.lower().replace(" ","") == 'artesanais🍔' or message.text.lower().replace(" ","") == 'artesanais' or message.text.lower().replace(" ","") == '🍔artesanais🍔':
        artesanais(message)
    elif message.text.lower().replace(" ","") == 'tradicionais🥪' or message.text.lower().replace(" ","") == 'tradicionais' or message.text.lower().replace(" ","") == '🥪tradicionais🥪':
        tradicionais(message)
    elif message.text.lower().replace(" ","") == 'açaís🍨' or message.text.lower().replace(" ","") == 'acais' or message.text.lower().replace(" ","") == '🍨açaís🍨':
        acais(message)
    elif message.text.lower().replace(" ","") == 'salgados🍟' or message.text.lower().replace(" ","") == 'salgados' or message.text.lower().replace(" ","") == '🍟salgados🍟':
        salgados(message)
    elif message.text.lower().replace(" ","") == 'doces🍰' or message.text.lower().replace(" ","") == 'doces' or message.text.lower().replace(" ","") == '🍰doces🍰':
        doces(message)
    elif message.text.lower().replace(" ","") == '01' or message.text.lower().replace(" ","") == '1' or message.text.lower().replace(" ","") == 'pointdavilla' or message.text.lower().replace(" ","") == 'pointdavila' or message.text.lower().replace(" ","") == 'pointedavila' or message.text.lower().replace(" ","") == 'poinedavilla':
        bot.send_message(id_chat, '''✅ <strong>POINT DA VILLA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99948-3296\n\n📱<strong><em>Instagram:</em></strong> instagram.com/pointdavilajm/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/vOZE9\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '02' or message.text.lower().replace(" ","") == '2' or message.text.lower().replace(" ","") == 'losburgers' or message.text.lower().replace(" ","") == 'losburguers' or message.text.lower().replace(" ","") == 'losburgues':
        bot.send_message(id_chat, '''✅ <strong>LOS BURGERS</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99881-8124\n\n📱<strong><em>Instagram:</em></strong> instagram.com/los.burgers/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/hGsMP\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '03' or message.text.lower().replace(" ","") == '3' or message.text.lower().replace(" ","") == 'antoniolanches' or message.text.lower().replace(" ","") == 'antôniolanches':
        bot.send_message(id_chat, '''✅ <strong>ANTONIO LANCHES</strong>\n\n📞<strong><em>Telefone:</em></strong> \n\n📱<strong><em>Instagram:</em></strong> \n\n📓<strong><em>Cardápio:</em></strong> \n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '04' or message.text.lower().replace(" ","") == '4' or message.text.lower().replace(" ","") == 'primordelivery' or message.text.lower().replace(" ","") == 'primordeliveri' or message.text.lower().replace(" ","") == 'primor':
        bot.send_message(id_chat, '''✅ <strong>PRIMOR DELIVERY</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 98817-4621\n\n📱<strong><em>Instagram:</em></strong> instagram.com/primordelivery/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/YjSCt\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '05' or message.text.lower().replace(" ","") == '5' or message.text.lower().replace(" ","") == 'fazenda' or message.text.lower().replace(" ","") == 'fazendalanches' or message.text.lower().replace(" ","") == 'fasenda':
        bot.send_message(id_chat, '''✅ <strong>FAZENDA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99939-9851\n\n📱<strong><em>Instagram:</em></strong> \n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/LWaXY\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '06' or message.text.lower().replace(" ","") == '6' or message.text.lower().replace(" ","") == 'altashoras' or message.text.lower().replace(" ","") == 'autashoras':
        bot.send_message(id_chat, '''✅ <strong>ALTAS HORAS</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99939-6417\n\n📱<strong><em>Instagram:</em></strong> instagram.com/altashoras_delivery_/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/30kkd\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '07' or message.text.lower().replace(" ","") == '7' or message.text.lower().replace(" ","") == 'garagemaçaí' or message.text.lower().replace(" ","") == 'garagemaçai' or message.text.lower().replace(" ","") == 'garagemacai' or message.text.lower().replace(" ","") == 'garagemaçai':
        bot.send_message(id_chat, '''✅ <strong>GARAGEM AÇAÍ</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99926-3916\n\n📱<strong><em>Instagram:</em></strong> instagram.com/garagemm_acai/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/E07nb\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '08' or message.text.lower().replace(" ","") == '8' or message.text.lower().replace(" ","") == 'ciadoslanches':
        bot.send_message(id_chat, '''✅ <strong>CIA DOS LANCHES</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99937-1304\n\n📱<strong><em>Instagram:</em></strong> instagram.com/lanchesciados04/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/7sfg9\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '09' or message.text.lower().replace(" ","") == '9' or message.text.lower().replace(" ","") == 'ciadoacai' or message.text.lower().replace(" ","") == 'ciadoaçaí' or message.text.lower().replace(" ","") == 'ciadoaçai':
        bot.send_message(id_chat, '''✅ <strong>CIA DO AÇAÍ</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99919-8483\n\n📱<strong><em>Instagram:</em></strong> instagram.com/ciadoacaidelivery/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/ddtTR\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '10' or message.text.lower().replace(" ","") == 'barbarussa' or message.text.lower().replace(" ","") == 'barbarusa':
        bot.send_message(id_chat, '''✅ <strong>BARBA RUSSA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99949-7720\n\n📱<strong><em>Instagram:</em></strong> instagram.com/barbarussa.rustic/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/H3g1M\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '11' or message.text.lower().replace(" ","") == 'servebem' or message.text.lower().replace(" ","") == 'cervebem':
        bot.send_message(id_chat, '''✅ <strong>SERVE BEM</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99976-6152\n\n📱<strong><em>Instagram:</em></strong> instagram.com/servebemrive/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/m1lkr\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '12' or message.text.lower().replace(" ","") == 'pastelariamix' or message.text.lower().replace(" ","") == 'pastelariamiz':
        bot.send_message(id_chat, '''✅ <strong>PASTELARIA MIX LANCHES</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99944-6473\n\n📱<strong><em>Instagram:</em></strong> instagram.com/mixlanches028/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/3dIGA\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '13' or message.text.lower().replace(" ","") == 'nicola' or message.text.lower().replace(" ","") == 'bardonicola' or message.text.lower().replace(" ","") == 'barnicola' or message.text.lower().replace(" ","") == 'nicolla' or message.text.lower().replace(" ","") == 'barnicolla' or message.text.lower().replace(" ","") == 'bardonicolla':
        bot.send_message(id_chat, '''✅ <strong>BAR DO NICOLA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99917-4885\n\n📱<strong><em>Instagram:</em></strong> instagram.com/bardonicola/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/UPGrE\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '14' or message.text.lower().replace(" ","") == 'doceriana' or message.text.lower().replace(" ","") == 'docerianna' or message.text.lower().replace(" ","") == 'docerrianna' or message.text.lower().replace(" ","") == 'docerriana':
        bot.send_message(id_chat, '''✅ <strong>DOCERIANA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99916-5259\n\n📱<strong><em>Instagram:</em></strong> instagram.com/doce.riana/\n\n📓<strong><em>Cardápio:</em></strong> \n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '15' or message.text.lower().replace(" ","") == 'elisiaamaralgourmet' or message.text.lower().replace(" ","") == 'elisiaamaral' or message.text.lower().replace(" ","") == 'elisiagourmet':
        bot.send_message(id_chat, '''✅ <strong>ELISIA AMARAL GOURMET</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99991-8096\n\n📱<strong><em>Instagram:</em></strong> instagram.com/elisia_amaral/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/CiGvY\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '16' or message.text.lower().replace(" ","") == 'mirim' or message.text.lower().replace(" ","") == 'mirimlanches':
        bot.send_message(id_chat, '''✅ <strong>MIRIM LANCHES</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99969-3197\n\n📱<strong><em>Instagram:</em></strong> \n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/FohoO\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '17' or message.text.lower().replace(" ","") == 'garagemlanches' or message.text.lower().replace(" ","") == 'garagemlanche':
        bot.send_message(id_chat, '''✅ <strong>GARAGEM LANCHES</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99984-8796\n\n📱<strong><em>Facebook:</em></strong> facebook.com/Garagem-Lanches-1655307744705616/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/csQJw\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    elif message.text.lower().replace(" ","") == '18' or message.text.lower().replace(" ","") == 'osbrutos' or message.text.lower().replace(" ","") == 'osbrutus' or message.text.lower().replace(" ","") == 'brutos':
        bot.send_message(id_chat, '''✅ <strong>OS BRUTOS</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99912-3748\n\n📱<strong><em>Instagram:</em></strong> instagram.com/osbrutoshamburgueria/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/cdtWZ\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪''',parse_mode='HTML',disable_web_page_preview=True)
    else:
        bot.send_message(id_chat, '''❌ Digite apenas as opções disponíveis! ❌\n\n⚠ Digite <strong><em><u>MENU</u></em></strong> para ver as opções ⚠''',parse_mode='HTML')

@bot.message_handler(func=lambda msg: msg.text is not None and '0' in msg.text.lower().replace(" ",""))
@bot.message_handler(func=lambda msg: msg.text is not None and 'categorias' in msg.text.lower().replace(" ",""))
def categorias(message):
    id_chat = message.chat.id

    markup = types.ReplyKeyboardMarkup()
    pizzas = types.KeyboardButton('🍕PIZZAS🍕')
    artesanais = types.KeyboardButton('🍔ARTESANAIS🍔')
    tradicionais = types.KeyboardButton('🥪TRADICIONAIS🥪')
    acais = types.KeyboardButton('🍨AÇAÍS🍨')
    salgados = types.KeyboardButton('🍰DOCES🍰')
    doces = types.KeyboardButton('🍟SALGADOS🍟')
    menu = types.KeyboardButton('MENU')
    markup.row(artesanais, tradicionais)
    markup.row(pizzas, acais)
    markup.row(doces, salgados)
    markup.row(menu)
    bot.send_message(id_chat, "Escolha uma categoria:", reply_markup=markup)


@bot.message_handler(func=lambda msg: msg.text is not None and 'PIZZAS🍕' in msg.text)
@bot.message_handler(func=lambda msg: msg.text is not None and 'PIZZAS' in msg.text)
def pizzas(message):
    primeiro_nome = message.from_user.first_name
    id_chat = message.chat.id
    custom = types.ReplyKeyboardRemove()
    bot.send_message(id_chat, f"✅ <strong>POINT DA VILLA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99948-3296\n\n📱<strong><em>Instagram:</em></strong> instagram.com/pointdavilajm/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/vOZE9\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>SERVE BEM</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99976-6152\n\n📱<strong><em>Instagram:</em></strong> instagram.com/servebemrive/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/m1lkr\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>BAR DO NICOLA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99917-4885\n\n📱<strong><em>Instagram:</em></strong> instagram.com/bardonicola/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/UPGrE\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>OS BRUTOS</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99912-3748\n\n📱<strong><em>Instagram:</em></strong> instagram.com/osbrutoshamburgueria/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/cdtWZ\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>ANTONIO LANCHES</strong>\n\n📞<strong><em>Telefone:</em></strong> \n\n📱<strong><em>Instagram:</em></strong> \n\n📓<strong><em>Cardápio:</em></strong> \n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n😄 Muito bem <strong>{primeiro_nome}</strong> !\n\n☝Aqui estão todos os estabelecimentos que\ntrabalham com <strong><em>pizzas</em></strong> 🍕",reply_markup=custom, disable_web_page_preview=True, parse_mode='HTML')
    voltar(message)

@bot.message_handler(func=lambda msg: msg.text is not None and 'ARTESANAIS🍔' in msg.text)
@bot.message_handler(func=lambda msg: msg.text is not None and 'ARTESANAIS' in msg.text)
def artesanais(message):
    primeiro_nome = message.from_user.first_name
    id_chat = message.chat.id
    custom = types.ReplyKeyboardRemove()
    bot.send_message(id_chat, f"✅ <strong>POINT DA VILLA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99948-3296\n\n📱<strong><em>Instagram:</em></strong> instagram.com/pointdavilajm/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/vOZE9\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>LOS BURGERS</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99881-8124\n\n📱<strong><em>Instagram:</em></strong> instagram.com/los.burgers/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/hGsMP\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>BARBA RUSSA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99949-7720\n\n📱<strong><em>Instagram:</em></strong> instagram.com/barbarussa.rustic/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/H3g1M\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>SERVE BEM</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99976-6152\n\n📱<strong><em>Instagram:</em></strong> instagram.com/servebemrive/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/m1lkr\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>BAR DO NICOLA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99917-4885\n\n📱<strong><em>Instagram:</em></strong> instagram.com/bardonicola/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/UPGrE\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>OS BRUTOS</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99912-3748\n\n📱<strong><em>Instagram:</em></strong> instagram.com/osbrutoshamburgueria/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/cdtWZ\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n😄 Muito bem <strong>{primeiro_nome}</strong> !\n\n☝Aqui estão todos os estabelecimentos que\ntrabalham com <strong><em>lanches artesanais</em></strong> 🍔",reply_markup=custom, disable_web_page_preview=True, parse_mode='HTML')
    voltar(message)

@bot.message_handler(func=lambda msg: msg.text is not None and 'TRADICIONAIS🥪' in msg.text)
@bot.message_handler(func=lambda msg: msg.text is not None and 'TRADICIONAIS' in msg.text)
def tradicionais(message):
    primeiro_nome = message.from_user.first_name
    id_chat = message.chat.id
    custom = types.ReplyKeyboardRemove()
    bot.send_message(id_chat, f"✅ <strong>POINT DA VILLA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99948-3296\n\n📱<strong><em>Instagram:</em></strong> instagram.com/pointdavilajm/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/vOZE9\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>ALTAS HORAS</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99939-6417\n\n📱<strong><em>Instagram:</em></strong> instagram.com/altashoras_delivery_/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/30kkd\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>CIA DOS LANCHES</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99937-1304\n\n📱<strong><em>Instagram:</em></strong> instagram.com/lanchesciados04/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/7sfg9\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>FAZENDA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99939-9851\n\n📱<strong><em>Instagram:</em></strong> \n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/LWaXY\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>BARBA RUSSA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99949-7720\n\n📱<strong><em>Instagram:</em></strong> instagram.com/barbarussa.rustic/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/H3g1M\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>PASTELARIA MIX LANCHES</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99944-6473\n\n📱<strong><em>Instagram:</em></strong> instagram.com/mixlanches028/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/3dIGA\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>SERVE BEM</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99976-6152\n\n📱<strong><em>Instagram:</em></strong> instagram.com/servebemrive/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/m1lkr\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>BAR DO NICOLA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99917-4885\n\n📱<strong><em>Instagram:</em></strong> instagram.com/bardonicola/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/UPGrE\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>MIRIM LANCHES</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99969-3197\n\n📱<strong><em>Instagram:</em></strong> \n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/FohoO\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>GARAGEM LANCHES</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99984-8796\n\n📱<strong><em>Facebook:</em></strong> facebook.com/Garagem-Lanches-1655307744705616/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/csQJw\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>OS BRUTOS</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99912-3748\n\n📱<strong><em>Instagram:</em></strong> instagram.com/osbrutoshamburgueria/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/cdtWZ\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>ANTONIO LANCHES</strong>\n\n📞<strong><em>Telefone:</em></strong> \n\n📱<strong><em>Instagram:</em></strong> \n\n📓<strong><em>Cardápio:</em></strong> \n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n😄 Muito bem <strong>{primeiro_nome}</strong> !\n\n☝Aqui estão todos os estabelecimentos que\ntrabalham com <strong><em>lanches tradicionais</em></strong> 🥪",reply_markup=custom, disable_web_page_preview=True, parse_mode='HTML')
    voltar(message)


@bot.message_handler(func=lambda msg: msg.text is not None and 'AÇAÍS🍨' in msg.text)
@bot.message_handler(func=lambda msg: msg.text is not None and 'ACAIS' in msg.text)
def acais(message):
    primeiro_nome = message.from_user.first_name
    id_chat = message.chat.id
    custom = types.ReplyKeyboardRemove()
    bot.send_message(id_chat, f"✅ <strong>GARAGEM AÇAÍ</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99926-3916\n\n📱<strong><em>Instagram:</em></strong> instagram.com/garagemm_acai/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/E07nb\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>CIA DO AÇAÍ</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99919-8483\n\n📱<strong><em>Instagram:</em></strong> instagram.com/ciadoacaidelivery/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/ddtTR\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n😄 Muito bem <strong>{primeiro_nome}</strong> !\n\n☝Aqui estão todos os estabelecimentos que\ntrabalham com <strong><em>açaís</em></strong> 🍨",reply_markup=custom, disable_web_page_preview=True, parse_mode='HTML')
    voltar(message)

@bot.message_handler(func=lambda msg: msg.text is not None and 'DOCES🍰' in msg.text)
@bot.message_handler(func=lambda msg: msg.text is not None and 'DOCES' in msg.text)
def doces(message):
    primeiro_nome = message.from_user.first_name
    id_chat = message.chat.id
    custom = types.ReplyKeyboardRemove()
    bot.send_message(id_chat, f"✅ <strong>DOCERIANA</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99916-5259\n\n📱<strong><em>Instagram:</em></strong> instagram.com/doce.riana/\n\n📓<strong><em>Cardápio:</em></strong> \n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n😄 Muito bem <strong>{primeiro_nome}</strong> !\n\n☝Aqui estão todos os estabelecimentos que\ntrabalham com <strong><em>doces</em></strong> 🍰",reply_markup=custom, disable_web_page_preview=True, parse_mode='HTML')
    voltar(message)

@bot.message_handler(func=lambda msg: msg.text is not None and 'SALGADOS🍟' in msg.text)
@bot.message_handler(func=lambda msg: msg.text is not None and 'SALGADOS' in msg.text)
def salgados(message):
    primeiro_nome = message.from_user.first_name
    id_chat = message.chat.id
    custom = types.ReplyKeyboardRemove()
    bot.send_message(id_chat, f"✅ <strong>PRIMOR DELIVERY</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 98817-4621\n\n📱<strong><em>Instagram:</em></strong> instagram.com/primordelivery/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/YjSCt\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>CIA DOS LANCHES</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99937-1304\n\n📱<strong><em>Instagram:</em></strong> instagram.com/lanchesciados04/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/7sfg9\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>PASTELARIA MIX LANCHES</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99944-6473\n\n📱<strong><em>Instagram:</em></strong> instagram.com/mixlanches028/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/3dIGA\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n✅ <strong>ELISIA AMARAL GOURMET</strong>\n\n📞<strong><em>Telefone:</em></strong> 28 99991-8096\n\n📱<strong><em>Instagram:</em></strong> instagram.com/elisia_amaral/\n\n📓<strong><em>Cardápio:</em></strong> https://url.gratis/CiGvY\n\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n\n😄 Muito bem <strong>{primeiro_nome}</strong> !\n\n☝Aqui estão todos os estabelecimentos que\ntrabalham com <strong><em>salgados</em></strong> 🍟",reply_markup=custom, disable_web_page_preview=True, parse_mode='HTML')
    voltar(message)

def botao_categoria(message):
    id_chat = message.chat.id

    markup = types.ReplyKeyboardMarkup()
    _categorias = types.KeyboardButton('CATEGORIAS')
    _01 = types.KeyboardButton('01')
    _02 = types.KeyboardButton('02')
    _03 = types.KeyboardButton('03')
    _04 = types.KeyboardButton('04')
    _05 = types.KeyboardButton('05')
    _06 = types.KeyboardButton('06')
    _07 = types.KeyboardButton('07')
    _08 = types.KeyboardButton('08')
    _09 = types.KeyboardButton('09')
    _10 = types.KeyboardButton('10')
    _11 = types.KeyboardButton('11')
    _12 = types.KeyboardButton('12')
    _13 = types.KeyboardButton('13')
    _14 = types.KeyboardButton('14')
    _15 = types.KeyboardButton('15')
    _16 = types.KeyboardButton('16')
    _17 = types.KeyboardButton('17')
    _18 = types.KeyboardButton('18')
    markup.row(_01,_02,_03)
    markup.row(_04,_05,_06)
    markup.row(_07,_08,_09)
    markup.row(_10,_11,_12)
    markup.row(_13,_14,_15)
    markup.row(_16,_17,_18)
    markup.row(_categorias)
    bot.send_message(id_chat,text="🔎 Caso deseje procurar por uma categoria específica, digite <strong><em><u>CATEGORIA</u></em></strong> ou pressione o botão ▶<strong><em><u>CATEGORIAS</u></em></strong>",reply_markup=markup,parse_mode='HTML')


def voltar(message):
    id_chat = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    _categorias_btn = types.KeyboardButton('CATEGORIAS')
    _menu_btn = types.KeyboardButton('MENU')
    markup.row(_categorias_btn,_menu_btn)
    bot.send_message(id_chat,text="\n▶ <strong>VOLTAR:</strong> <strong><em><u>Categorias</u></em></strong> ou <strong><em><u>Menu</u></em></strong>",reply_markup=markup,parse_mode='HTML')

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)