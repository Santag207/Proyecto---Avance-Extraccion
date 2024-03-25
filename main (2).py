import tweepy

# Claves de acceso a la API de Twitter
#Ejemplo con mi cuenta funcional
consumer_key = 'abcdef1234567890' #API Key o clave de consumo
consumer_secret = 'zyxwv9876543210' # API Secret Key o secreto de consumo
access_token = '1234567890-abcdefghijk1234567890' # Token de acceso
access_token_secret = '0987654321-zyxwvutsrqponmlkjihgfedcba0987654321' # Access Token Secreto

# Autenticación API de Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

nombre_usuario = 'Usuario' #Nombre de usuario que se desea buscar dependiendo del caso para la extraccion

# Número de tweets a extraer
num_tweets = 10

# Extraer los tweets del usuario especificado
tweets = api.user_timeline(screen_name=nombre_usuario, count=num_tweets, tweet_mode="extended")

# Mostrar los tweets y sus datos
for tweet in tweets:
    print("Texto del tweet:", tweet.full_text)
    print("Fecha y hora de publicación:", tweet.created_at)
    print("ID del tweet:", tweet.id)
    print("Número de retweets:", tweet.retweet_count)
    print("Número de favoritos:", tweet.favorite_count)
    print("-" * 50)
