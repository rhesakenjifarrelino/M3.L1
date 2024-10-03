from flask import Flask
import random

facts_list = [
    "1.Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka",
    "2.Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka",
    "3.Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan",
    "4.Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja",
    "5.Salah satu cara untuk memerangi ketergantungan teknologi adalah dengan mencari kegiatan yang membawa kesenangan dan meningkatkan suasana hati",
    "6.Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten",
    "7.Elon Musk juga menganjurkan regulasi jejaring sosial dan perlindungan data pribadi pengguna. Dia mengklaim bahwa jejaring sosial mengumpulkan sejumlah besar informasi tentang kita, yang kemudian dapat digunakan untuk memanipulasi pikiran dan perilaku kita",
    "8.Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini"
]

app = Flask(__name__)

@app.route("/random_fact")
def random_fact():
    fact = random.choice(facts_list)
    return f'<p>{fact}</p><a href="/flip_coin">Flip a coin!</a>'

@app.route("/")
def home():
    return '<a href="/random_fact">View a random fact!</a>'

@app.route("/flip_coin")
def flip_coin():
    result = random.choice(["Heads", "Tails"])
    return f'<p>{result}</p>'

if __name__ == "__main__":
    app.run(debug=True)
