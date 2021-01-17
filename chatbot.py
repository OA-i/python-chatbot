import random, os, time, sys, webbrowser


os.system("clear")
def menu_screen():
  print(
"""
  (1) Chatting
  (2) Pengaturan
  (3) Tentang
""")

  menu = input("  Pilih Menu : ")
  
  if menu == "1":
    os.system("clear")
    chat_screen()
    
  elif menu == "2":
    os.system("clear")
    setting_screen()
    
  elif menu == "3":
    os.system("clear")
    about_screen()
    
  else:
    os.system("clear")
    print("\n  Menu Tidak Ada")
    time.sleep(1.0)
    os.system("clear")
    menu_screen()

#Pengaturan
def setting_screen():
    print(
  """ 
  (1) Kembali
  (2) Ganti Nama
  """)
    pilih = input("  Pilih Menu : ")
    
    if pilih == "1":
      os.system("clear")
      menu_screen()
      
    if pilih == "2":
      nama = input("\n  Masukkan Nama Baru : ")
      os.system("rm -rf /sdcard/.chatbotOAi")
      os.system("mkdir /sdcard/.chatbotOAi")
      os.system("touch /sdcard/.chatbotOAi/nama.txt")
      file = open("/sdcard/.chatbotOAi/nama.txt" , "w")
      filer = open("/sdcard/.chatbotOAi/nama.txt" , "r")
      file.write(nama)
      file.close()
      print("\n  Nama Berhasil Diubah")
      time.sleep(1.0)
      os.system("clear")
      setting_screen()
      
    else:
      os.system("clear")
      print("\n  Menu Tidak Ada")
      time.sleep(1.0)
      os.system("clear")
      setting_screen()

#Tentang
def about_screen():
    print(
  """ 
  (1) Kembali
  
  [ By OAi ]
  
  (2) Facebook = OAi
  (3) Github = OA-i
  """)
    pilih = input("  Pilih Menu : ")
    
    if pilih == "1":
      os.system("clear")
      menu_screen()
      
    elif pilih == "2":
      os.system("clear")
      webbrowser.open("https://m.facebook.com/profile.php?id=100033678670273")
      about_screen()
      
    elif pilih == "3":
      os.system("clear")
      webbrowser.open("https://github.com/OA-i")
      about_screen()
      
    else:
      os.system("clear")
      print("\n  Menu Tidak Ada")
      time.sleep(1.0)
      os.system("clear")
      about_screen()


#Chat
def chat_screen():
  global jawaban
  filenama = "/sdcard/.chatbotOAi/nama.txt"
  nama = ""
  
  adafile = os.path.isfile(filenama)
  if adafile:
    carifile = open("/sdcard/.chatbotOAi/nama.txt" , "r")
    nama = carifile.readlines()[0]
  else:
    nama = input("\n  Masukkan Nama : ")
    os.system("rm -rf /sdcard/.chatbotOAi")
    os.system("mkdir /sdcard/.chatbotOAi")
    os.system("touch /sdcard/.chatbotOAi/nama.txt")
    file = open("/sdcard/.chatbotOAi/nama.txt" , "w")
    filer = open("/sdcard/.chatbotOAi/nama.txt" , "r")
    file.write(nama)
    file.close()
    os.system("clear")
  
  
  #Daftar jawaban yang dipanggil
  help = "Halo, Hai, Pantun, Kamu Lagi Apa, Lagi apa, Siapa namaku, Siapa namamu, Apa kabar"
  pantun = random.choice([
          """Ada jahe ada kencur
          Semua dicampur jadilah bumbu
          Beberapa hari ini aku susah tidur
          Karena selalu ingat dirimu""",
          
          """Beribu-ribu pohon beringin
          Hanya satu di pohon randu
          Saat malam terasa dingin
          Hanya wajahmu yang aku rindu""",
          
          """Jalan-jalan ke kebun
          Membeli buah nangka dan jambu
          Tak peduli dalam situasi apapun
          Saya tetap akan menemanimu"""])
  lagiapa = random.choice(["Lagi duduk", "Lagi nugas :(", "Lagi makan", "Lagi eek hehe"])
  ketawa = random.choice(["Haha", "Wkwkwk", "Hehe"])
  
  
  print("\n  Halo " + nama + " Selamat Datang Di Chat Bot " + "\n  Ketik !Help Untuk Bantuan, Ketik Kembali Untuk Kembali")
  
  #Daftar jawaban
  jawaban = {
    "p" : "Dilarang p",
    "halo" : "Halo juga " + nama ,
    "hai" : "Hai juga " + nama,
    "siapa namamu" : "Namaku Bot",
    "siapa namaku" : "Nama Kamu " + nama,
    "apa kabar" : "Alhamdulilah sehat",
    "pantun" : pantun,
    "!help" : help,
    "kamu lagi apa" : lagiapa,
    "lagi apa" : lagiapa,
    "makan yang banyak ya" : "Udah kenyang",
    "semangat" : "Oke :)",
    "bau" : "Hoek",
    "iri" : "Bilang bos hahay bal bale bal bale",
    "stress" : "Gws",
    "oke" : "sip",
    "ketawa" : ketawa,
    "haha" : "Cie ketawa",
    "wkwkwk" : "Cie ketawa",
    "xixixi" : "Cie ketawa",
    "hehe" : "Cie Ketawa"
  }
  tanya()



#Pertanyaan dan jawaban dari bot
def tanya():
  pertanyaan = input("\n  Ketik Pesan : ")
  
  #Mengecek daftar jawaban, jika tidak ada maka bot tidak mengerti
  if pertanyaan.lower() in jawaban:
    print("\n  Bot : " + jawaban[pertanyaan.lower()])
    tanya()
    
  elif pertanyaan.lower() == "kembali":
    print("\n  Bot : Bye bye")
    time.sleep(0.7)
    os.system("clear")
    menu_screen()
    
  else:
    print("\n  Bot : Saya tidak mengerti")
    tanya()

menu_screen()