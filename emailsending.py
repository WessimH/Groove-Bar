import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Informations de connexion pour le serveur SMTP
gmail_user = 'groovbar35@gmail.com'
gmail_app_password = 'jajf flej poix vlmo'

# L'adresse e-mail du destinataire
destinataire = 'thomas@lnmprod.com'

# Le message à envoyer
message = """
Au Groove Bar, nous sommes ravis de vous annoncer notre prochain événement musical qui promet de vous faire danser toute la nuit. 🌟

🎤 Événement : Concert Groovy
📅 Date : [Date]
🕖 Heure : [Heure]
📍 Lieu : Groove Bar, Place du Bouffay, Nantes

Nous avons préparé une soirée exceptionnelle mettant à l'honneur la musique groove des années 70 à aujourd'hui. Attendez-vous à des rythmes entraînants, des mélodies inoubliables et une ambiance électrique qui vous fera vibrer!

Pourquoi ne pas vous joindre à nous? Voici un avant-goût de ce qui vous attend :

Performances live époustouflantes.
Cocktails spéciaux inspirés par les légendes de la musique groove.
Une atmosphère électrique pour une soirée mémorable.
N'oubliez pas de réserver votre place dès maintenant pour vous assurer de ne pas manquer cette expérience musicale unique. Les billets sont limités, alors assurez-vous de les obtenir avant qu'il ne soit trop tard!

Cliquez sur le lien ci-dessous pour réserver vos billets dès maintenant : [Lien de réservation]

Nous avons hâte de partager cette nuit inoubliable avec vous et de célébrer la musique groove dans toute sa splendeur.

Restez à l'écoute pour plus de détails et d'annonces excitantes! 🎉

Bien à vous,

L'équipe du Groove Bar
"""

def send_email():
    # Création de la connexion SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_app_password)

    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = destinataire
    msg['Subject'] = 'Groove Bar Presents: Un Concert Groovy à Ne Pas Manquer! 🎶'
    msg.attach(MIMEText(message, 'plain'))

    try:
        server.send_message(msg)
        print(f"Email envoyé avec succès à {destinataire}")
    except Exception as e:
        print(f"Échec de l'envoi de l'email à {destinataire}: {e}")

    server.quit()

if __name__ == '__main__':
    # Planifier l'envoi de l'e-mail pour demain à 14h05
    schedule.every().day.at("14:05").do(send_email)

    # Boucle pour garder le script en exécution
    while True:
        schedule.run_pending()
        time.sleep(1)
