import discord
from discord.ext import commands
from config import token
from fonksiyon import gen_pass
from renk import renkler
import random
import requests

class MyBot(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.commands = {}  # Komutları dinamik olarak saklayacağız
        self.register_default_commands()

    async def on_ready(self):
        print(f'{self.user} olarak giriş yaptık.')

    async def on_message(self, message):
        if message.author == self.user:
            return

        # Komutları kontrol et
        command_found = False
        for command, func in self.commands.items():
            if message.content.lower().startswith(command.lower()):
                command_found = True
                try:
                    await func(message)
                except Exception as e:
                    await message.channel.send(f"Bir hata oluştu: {e}")
                return

        if not command_found:
            # Eğer komut bulunamazsa, bir yanıt ver
            await message.channel.send("Üzgünüm, bu komutu anlamadım. `!yardım` yazarak komutları görebilirsin.")

    def register_command(self, command, func):
        """Yeni komut eklemek için kullanılır."""
        self.commands[command] = func

    def register_default_commands(self):
        """Varsayılan komutları kaydeder."""
        self.register_command("merhaba", self.send_hello)
        self.register_command("bye", self.send_bye)
        self.register_command("bana bir şifre yapar mısın", self.generate_password)
        self.register_command("bana yardım eder misin", self.send_help)
        self.register_command("bana bir renk seç", self.choose_color)
        self.register_command("benimle arkadaş olur musun?", self.be_friends)
        self.register_command("bana yardım ettiğin için teşekkür ederim", self.thank_you)
        self.register_command("bana 2 tane çevre dostu uygulama söyler misin?", self.suggest_apps)
        self.register_command("bana şans dileyin", self.send_good_luck)
        self.register_command("çevre dostu bilgi ver", self.environmental_info)
        self.register_command("!yardım", self.show_help)

        # Yeni Komutlar
        self.register_command("şiir oku", self.read_poem)
        self.register_command("ilginç bilgi", self.random_fact)
        self.register_command("hava durumu", self.weather_info)
        self.register_command("zeka sorusu", self.brain_teaser)
        self.register_command("motivasyon sözü", self.motivation_quote)
        self.register_command("rastgele resim", self.random_image)
        self.register_command("yıldız durumu", self.star_sign)
        self.register_command("tavsiye et", self.give_recommendation)
        self.register_command("yazı tura", self.coin_flip)
        self.register_command("günlük şans", self.daily_luck)
        self.register_command("rastgele sayı", self.random_number)
        self.register_command("şarkı öner", self.song_recommendation)
        self.register_command("kullanıcı bilgisi", self.user_info)
        self.register_command("bugün ne var?", self.today_info)
        self.register_command("film önerisi", self.movie_recommendation)
        self.register_command("günlük hava durumu", self.daily_weather)

    # Komutlara karşılık gelen fonksiyonlar
    async def send_hello(self, message):
        await message.channel.send("Selam!")

    async def send_bye(self, message):
        await message.channel.send("\U0001f642 Görüşürüz!")

    async def generate_password(self, message):
        try:
            password = gen_pass(10)
            await message.channel.send(f"İşte şifren: {password}")
        except Exception as e:
            await message.channel.send(f"Şifre oluşturulurken bir hata oluştu: {e}")

    async def send_help(self, message):
        await message.channel.send("Tabi, ne konuda yardımcı olmamı istersin?")

    async def choose_color(self, message):
        await message.channel.send(f"İşte birkaç renk: {', '.join(renkler)}")

    async def be_friends(self, message):
        await message.channel.send("Tabii ki arkadaş olabiliriz! 😊")

    async def father_question(self, message):
        await message.channel.send("Tabii ki seninle vakit geçirmeli. İşler bekleyebilir!")

    async def thank_you(self, message):
        await message.channel.send("Rica ederim! Her zaman buradayım. 😊")

    async def suggest_apps(self, message):
        await message.channel.send("Tabii, işte iki çevre dostu uygulama: 1. Ecosia  2. Too Good To Go")

    async def send_good_luck(self, message):
        await message.channel.send("Bol şans! 🍀")

    async def environmental_info(self, message):
        info = """
        İşte çevre dostu birkaç öneri ve uygulama:
        1. **Ecosia**: Bu arama motoru, elde ettiği gelirin büyük bir kısmını ağaç dikme projelerine bağışlar.
        2. **Too Good To Go**: Restoranlardan ve mağazalardan fazla yiyecekleri alarak israfı azaltmanızı sağlar.
        3. **Olio**: Komşularınızla veya yerel işletmelerle yiyecek ve diğer eşyaları paylaşmanızı sağlar.
        4. **JouleBug**: Sürdürülebilir yaşam alışkanlıkları edinmenize yardımcı olan bir uygulama.
        
        Çevreyi korumak için ipuçları:
        - Geri dönüşüm yapmayı unutmayın.
        - Tek kullanımlık plastik yerine yeniden kullanılabilir ürünler tercih edin.
        - Enerji tasarrufu için elektronik cihazları kullanılmadığında kapatın.
        - Daha az kağıt tüketmek için dijital çözümler kullanın.
        """
        await message.channel.send(info)

    async def show_help(self, message):
        commands_list = "\n".join([f"- {cmd}" for cmd in self.commands.keys()])
        help_message = f"Mevcut komutlar:\n{commands_list}\n\nBir komut yazarken doğru şekilde yazmaya dikkat edin."
        await message.channel.send(help_message)

    # Yeni komut fonksiyonları
    async def read_poem(self, message):
        poem = "Gözlerim, yıldızlarla parlar,\nKalbim, her an seni anar.\nGeceler seni bekler,\nGünler seni arar..."
        await message.channel.send(poem)

    async def random_fact(self, message):
        facts = [
            "Dünyadaki en uzun dağ, Everest değil, Mauna Kea'dır. Bu dağ, deniz seviyesinden 4,205 metre yüksektir, ancak deniz seviyesinin altından ölçüldüğünde 10,210 metreye kadar yükselir.",
            "Bir yıldızın ömrü, genellikle milyonlarca yıl sürer. Ancak, bir yıldızın hayatının sonuna yaklaşması, patlamasına neden olabilir ve bu patlama bir süpernova olarak bilinir.",
            "Bir çikolata barı, neredeyse 2 milyon yıl önceye kadar uzanan eski Meksika medeniyetlerine kadar dayanabilir. Kakao, eski Meksikalılar tarafından çok değerli bir ürün olarak kabul edilirdi."
        ]
        await message.channel.send(random.choice(facts))

    async def weather_info(self, message):
        city = message.content.split(" ", 1)[1]
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=your_api_key")
        data = response.json()
        if data["cod"] == "404":
            await message.channel.send(f"Üzgünüm, '{city}' için hava durumu bilgisi bulunamadı.")
        else:
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temp = main["temp"] - 273.15  # Kelvin'den Celcius'a dönüştür
            await message.channel.send(f"{city} için hava durumu: {weather_desc}, sıcaklık: {temp:.2f}°C")

    async def brain_teaser(self, message):
        question = "Bir çiftlikte 100 inek var. Her bir inek 4 bacaklıdır. Çiftlikte toplam kaç bacak vardır?"
        await message.channel.send(question)

    async def motivation_quote(self, message):
        quotes = [
            "Başarı, cesaretle başlar ve azimle devam eder.",
            "Hayat, zorlukları aşabilenlerin yolculuğudur.",
            "Her gün bir adım daha at, büyük hedeflere ulaşmak için."
        ]
        await message.channel.send(random.choice(quotes))

    async def random_image(self, message):
        # Bir rastgele resim URL'si gönderme
        await message.channel.send("https://source.unsplash.com/random")

    async def star_sign(self, message):
        await message.channel.send("Hangi burç olduğunu belirtir misin?")

    async def give_recommendation(self, message):
        recommendations = [
            "Ecosia: Çevre dostu bir arama motoru.",
            "Too Good To Go: Gıda israfını önlemek için harika bir uygulama.",
            "Audible: Sesli kitaplar dinleyerek yeni bilgiler öğrenebilirsiniz."
        ]
        await message.channel.send(random.choice(recommendations))

    async def coin_flip(self, message):
        result = random.choice(["Yazı", "Tura"])
        await message.channel.send(f"Sonuç: {result}. Şansını dene!")

    async def daily_luck(self, message):
        luck = random.choice(["Bugün şanslısın!", "Bugün şanssızsın!"])
        await message.channel.send(luck)

    async def random_number(self, message):
        number = random.randint(1, 100)
        await message.channel.send(f"Rastgele sayı: {number}")

    async def song_recommendation(self, message):
        songs = [
            "Shape of You - Ed Sheeran",
            "Blinding Lights - The Weeknd",
            "Levitating - Dua Lipa"
        ]
        await message.channel.send(f"Şarkı önerisi: {random.choice(songs)}")

    async def user_info(self, message):
        user = message.author
        await message.channel.send(f"Kullanıcı Adı: {user.name}\nID: {user.id}")

    async def today_info(self, message):
        await message.channel.send("Bugün yeni bir fırsatla dolu, ne yapacaksın?")

    async def movie_recommendation(self, message):
        movies = [
            "Inception",
            "The Dark Knight",
            "The Matrix"
        ]
        await message.channel.send(f"Film önerisi: {random.choice(movies)}")

    async def daily_weather(self, message):
        city = message.content.split(" ", 1)[1]
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=your_api_key")
        data = response.json()
        if data["cod"] == "404":
            await message.channel.send(f"Üzgünüm, '{city}' için hava durumu bilgisi bulunamadı.")
        else:
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temp = main["temp"] - 273.15  # Kelvin'den Celcius'a dönüştür
            await message.channel.send(f"Bugün {city} için hava durumu: {weather_desc}, sıcaklık: {temp:.2f}°C")

# Botu başlatıyoruz
intents = discord.Intents.default()
intents.message_content = True

# Botu başlatıyoruz
bot = MyBot(intents=intents)
bot.run(token)  # Token burada kullanılacak