import logging
import re
import datetime
import random

from telegram import ForceReply, Update # type: ignore
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters # type: ignore

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Expresiones regulares
saludo_expresion_regular = re.compile(r"hello|hi|hey|hola", re.IGNORECASE)
bien_expresion_regular = re.compile(r"bien|good", re.IGNORECASE)
mal_expresion_regular = re.compile(r"mal|bad", re.IGNORECASE)

mensaje_conversion = re.compile(r"Conversion|conversion|convertir|conver", re.IGNORECASE)

conversion_temperatura_CAF_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(celsius|c)", re.IGNORECASE)
conversion_temperatura_FAC_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(fahrenheit|f)", re.IGNORECASE)

conversion_distancia_KMAM_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(kilometros|km)", re.IGNORECASE)
conversion_distancia_MAKM_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(millas|mi)", re.IGNORECASE)

conversion_peso_KGALB_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(kilogramos|kg)", re.IGNORECASE)
conversion_peso_LBAKG_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(libras|lbs)", re.IGNORECASE)

conversion_velocidad_KMHAMPH_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(km/h|kph)", re.IGNORECASE)
conversion_velocidad_MPHAKMH_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*(mph)", re.IGNORECASE)


# Factores de conversión de pulgadas a centímetros
factor_pulgadas_a_cm = 2.54

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

    

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message if it matches any regular expression."""
    message_text = update.message.text

    if saludo_expresion_regular.search(message_text):
        await update.message.reply_text("¿Cómo estás?")

    elif bien_expresion_regular.search(message_text):
        await update.message.reply_text("¡Qué bien!")

    elif mal_expresion_regular.search(message_text):
        await update.message.reply_text("¡Qué mal!")

    elif mensaje_conversion.search(message_text):
        await update.message.reply_text("¡Bienvenido, que deseas convertir el dia de hoy ? !")
    elif conversion_temperatura_CAF_expresion_regular.search(message_text):
        match = conversion_temperatura_CAF_expresion_regular.search(message_text)
        temp = float(match.group(1))

        conversion =(temp * 9/5) + 32
        await update.message.reply_text(f"{temp}°C equivalen a {conversion}°F.")

    elif conversion_temperatura_FAC_expresion_regular.search(message_text):
        match = conversion_temperatura_FAC_expresion_regular.search(message_text)
        temp = float(match.group(1))

        conversion =(temp - 32) * 5/9
        await update.message.reply_text(f"{temp}°F equivalen a {conversion}°C.")

    elif conversion_distancia_KMAM_expresion_regular.search(message_text):
        match = conversion_distancia_KMAM_expresion_regular.search(message_text)
        dist = float(match.group(1))

        conversion =dist * 0.621371
        await update.message.reply_text(f"{dist} km equivalen a {conversion} mi.")

    elif conversion_distancia_MAKM_expresion_regular.search(message_text):
        match = conversion_distancia_MAKM_expresion_regular.search(message_text)
        dist = float(match.group(1))

        conversion =dist * 1.60934
        await update.message.reply_text(f"{dist} mi equivalen a {conversion} km.")

    elif conversion_peso_KGALB_expresion_regular.search(message_text):
        match = conversion_peso_KGALB_expresion_regular.search(message_text)
        peso = float(match.group(1))

        conversion =peso * 2.20462
        await update.message.reply_text(f"{peso} kg equivalen a {conversion} lb.")

    elif conversion_peso_LBAKG_expresion_regular.search(message_text):
        match = conversion_peso_LBAKG_expresion_regular.search(message_text)
        peso = float(match.group(1))

        conversion =peso * 0.453592
        await update.message.reply_text(f"{peso} lb equivalen a {conversion} kg.")

    elif conversion_velocidad_KMHAMPH_expresion_regular.search(message_text):
        match = conversion_velocidad_KMHAMPH_expresion_regular.search(message_text)
        velocidad = float(match.group(1))

        conversion =velocidad * 0.621371
        await update.message.reply_text(f"{velocidad} km/h equivalen a {conversion} mph.")

    elif conversion_velocidad_MPHAKMH_expresion_regular.search(message_text):
        match = conversion_velocidad_MPHAKMH_expresion_regular.search(message_text)
        velocidad = float(match.group(1))

        conversion =velocidad * 1.60934
        await update.message.reply_text(f"{velocidad} mph  equivalen a {conversion} km/h.")

    else:
        await update.message.reply_text("No entendí tu mensaje.")

def main() -> None:
    """Start the bot."""
    application = Application.builder().token("7168947739:AAFud72bVxMRX6ybOcEkFVEAh6Jap4TA14M").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()