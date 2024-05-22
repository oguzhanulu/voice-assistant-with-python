import random
import time
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import pyaudio
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import cv2


r=sr.Recognizer()

class SesliAsistan:

    def seslendirme(self, metin):
        metin_seslendirme = gTTS(text=metin, lang="tr")
        dosya = str(random.randint(0, 10000000000)) + ".mp3"
        metin_seslendirme.save(dosya)
        playsound(dosya)
        os.remove(dosya)

    def mikrofon(self):
        with sr.Microphone() as kaynak:
            print("Sizi dinliyorum..")
            listen=r.listen(kaynak)
            ses=""
            try:
                ses=r.recognize_google(listen,language="tr-TR")
            except sr.UnknownValueError:
                self.seslendirme("ne dediğinizi anlayamadım")
            return ses

    def ses_karslik(self,gelen_Ses):
        if(gelen_Ses in "merhaba"):
            self.seslendirme("merhaba nasıl yardımcı olabilirim")
        elif(gelen_Ses in "nasılsın"):
            self.seslendirme("teşekkürler sen nasılsın")
        elif (gelen_Ses in "müzik aç" or gelen_Ses in "video aç"):

            try:
                self.seslendirme("hangi videoyu açmamı istersiniz")
                cevap = self.mikrofon()

                url = "https://www.youtube.com/results?search_query=" + cevap
                tarayici = webdriver.Chrome()
                tarayici.get(url)

                ilk_video = tarayici.find_element(By.XPATH, "//*[@id='video-title']/yt-formatted-string").click()

                time.sleep(5)

                self.seslendirme("aaçmamı istediğiniz video bu mu")
                gelen_komut = self.mikrofon()
                if (gelen_komut in "Hayır"):
                    sayac = 2
                    tarayici.back()
                    while (sayac < 5):
                        diger_videolar = tarayici.find_element(By.XPATH,"//*[@id='contents']/ytd-video-renderer[{}]".format(sayac)).click()
                        time.sleep(5)
                        self.seslendirme("açmamı istediğiniz video bu mu")
                        komut = self.mikrofon()
                        if (komut in "Evet"):
                            self.seslendirme("iyi seyirler")
                            break
                        else:
                            self.seslendirme("o zaman diğer videolara bakalım")
                            tarayici.back()
                            sayac += 1
                else:
                    self.seslendirme("iyi seyirler")

            except:
                self.seslendirme("bir sorunla karşılaştım lütfen tekrar dener misin")

        elif (gelen_Ses in "google aç" or gelen_Ses in "arama yap" or gelen_Ses in "film aç"):
            self.seslendirme("ne aramamı istersiniz")
            cevap = self.mikrofon()

            url = "https://www.google.com/search?q=" + cevap
            self.seslendirme("{} ile ilgili bulabildiğim içerikler bunlar".format(cevap))
            tarayici = webdriver.Chrome()
            tarayici.get(url)

            site = tarayici.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a/h3").click()

            time.sleep(5)
            tarayici.quit()


        elif(gelen_Ses in "film öner" or gelen_Ses in "film önerisi yap" or gelen_Ses in "film önerir misin"):

            try:
                self.seslendirme("hangi tarz film önerermemi istersiniz")
                cevap=self.mikrofon()

                if (cevap == "bilim kurgu"):
                    cevap = "bilim-kurgu-film-full-izle"
                elif (cevap == "aile"):
                    cevap = "aile-film-izle"
                elif (cevap == "aksiyon"):
                    cevap = "aksiyon-filmler-hd-izle"
                elif (cevap == "romantik"):
                    cevap = "romantik-filmler-full-hd-izle"
                elif (cevap == "suc"):
                    cevap = "suc-filmleri-izle"
                elif (cevap == "psikolojik"):
                    cevap = "psikolojik-filmler-izle"
                elif (cevap == "savaş"):
                    cevap = "savas-filmleri-izle"
                elif (cevap == "korku"):
                    cevap = "korku-film-izle"
                elif (cevap == "gerilim"):
                    cevap = "gerilim-filmleri-izle"
                elif (cevap == "komedi"):
                    cevap = "komedi-film-izle"
                else:
                    cevap="yabanci-film-izle" #eğer farklı bir komut gelirse doğrudan yabancı filmlere gidelim / #if a different command comes, let's go directly to foreign movies

                tarayici=webdriver.Chrome()
                tarayici.get("https://www.fullhdfilmizlesene.pw/filmizle/{}".format(cevap))
                ilk_kart=tarayici.find_element(By.XPATH,"/html/body/div[5]/div[1]/main/section/ul/li[1]").click()
                time.sleep(3)
                self.seslendirme("bu filmi açmamı ister misin")
                gelen_cevap=self.mikrofon()
                if(gelen_cevap in "Hayır"):
                    self.seslendirme("o zaman diğer filmlere bakalım")
                    tarayici.back()
                    sayac=2
                    while(sayac<10):
                        diger_filmler=tarayici.find_element(By.XPATH,"/html/body/div[5]/div[1]/main/section/ul/li[{}]".format(sayac)).click()
                        time.sleep(4)
                        self.seslendirme("bu filmi açmamı ister misin")
                        komut=self.mikrofon()
                        print(komut)
                        if(komut=="Evet"):
                            self.seslendirme("keyifli seyirler")
                            time.sleep(5)
                            break
                        else:
                            self.seslendirme("o zaman diğer filmlere bakalım")
                            tarayici.back()
                            sayac+=1

                else:
                    self.seslendirme("keyifli seyirler")
                    time.sleep(5)

            except:
                self.seslendirme("bir hata meydana geldi")


        elif(gelen_Ses in "hava durumu"):

            self.seslendirme("Hangi şehrin hava durumunu kontrol etmemi istersiniz")
            cevap=self.mikrofon()
            print(cevap)

            def HavaRaporlari(gununIndexi):

                url = "https://havadurumu15gunluk.xyz/havadurumu/630/{}-hava-durumu-15-gunluk.html".format(cevap)

                response = requests.get(url)

                if response.status_code == 200:
                    # print("İŞLEM BAŞARILI") / # print("PROCESS SUCCESSFUL")
                    soup = BeautifulSoup(response.text, "html.parser")
                    # print(soup)

                    tumVeriler = soup.find_all("tr")[gununIndexi].text
                    tumVeriler = tumVeriler.replace("Saatlik", "").strip()
                    print(tumVeriler)

                    gunluk_hava = ""
                    gunduz_sicaklik = tumVeriler[-6:-4]
                    gece_sicaklik = tumVeriler[-3:-1]
                    print("Gunduz Sıcaklık: " + gunduz_sicaklik)
                    print("Gece Sıcaklık: " + gece_sicaklik)

                    tumVeriler = tumVeriler[6:-6].strip()

                    gunun_ismi = tumVeriler[:3]

                    gunKisaltma = ["Sal", "Çar", "Per", "Cum", "Cmt", "Paz", "Pzt"]

                    for x in gunKisaltma:
                        if x in tumVeriler:
                            gunluk_hava = tumVeriler.replace(x, "")

                    print("Hava Durumu: " + gunluk_hava)

                    gununIsimleri = {"Paz": "Pazartesi", "Pzt": "Pazartesi", "Sal": "Salı", "Çar": "Çarşamba",
                                     "Per": "Perşembe", "Cum": "Cuma", "Cmt": "Cumartesi"}
                    gunun_ismi = gununIsimleri[gunun_ismi]
                    print("Gunun Adı: " + gunun_ismi)

                    return "{} için {} günün hava raporları şu şekilde: Hava: {} Gündüz Sıcaklığı: {} derece Gece Sıcaklığı: {} derece".\
                        format(cevap,gunun_ismi,gunluk_hava,gunduz_sicaklik,gece_sicaklik)

                else:
                    print("Hata meydana geldi")

            self.seslendirme("{} şehir için yarının mı yoksa 5 günlük raporlarını mı istersiniz".format(cevap))
            cevap2=self.mikrofon().lower()
            print(cevap2)

            if(cevap2 in "yarının"):

                self.seslendirme(HavaRaporlari(2))
            else:
                sayac=1

                while sayac<6:
                    self.seslendirme(HavaRaporlari(sayac))
                    sayac+=1


        elif(gelen_Ses in "Fotoğraf çek"):

            self.seslendirme("Kameranızı hemen açıyorum")

            kamera=cv2.VideoCapture(0)

            kontrol,resim=kamera.read()

            self.seslendirme("Gülümseyin çekiyorum...")

            cv2.imwrite("deneme.jpg",resim)

            kamera.release()

            cv2.destroyAllWindows()

            time.sleep(2)

            self.seslendirme("fotoğrafınızı görmek istiyor musunuz")
            cevap=self.mikrofon()

            if cevap in "Evet":
                resim=cv2.imread("deneme.jpg")
                cv2.imshow("Deneme Resim 1",resim)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            elif cevap in "Hayır":
                cv2.destroyAllWindows()




    def uyanma_fonksiyonu(self,gelen_Ses):
        if(gelen_Ses in "hey elon"):
            self.seslendirme("dinliyorum...")
            ses=self.mikrofon()
            if(ses!=""):
                print(ses)
                self.ses_karslik(ses)



asistan = SesliAsistan()

while True:
    gelen_Ses=asistan.mikrofon().lower()
    if(gelen_Ses!=""):
        print(gelen_Ses)
        asistan.uyanma_fonksiyonu(gelen_Ses)

