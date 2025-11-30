from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
import random
# Import KivMob untuk iklan
from kivmob import KivMob, TestIds

# Warna background gelap (Dark Mode)
Window.clearcolor = (0.08, 0.08, 0.08, 1)

class SafeAdApp(App):
    def build(self):
        # --- KONFIGURASI ADMOB ---
        # Saat ini menggunakan ID TEST.
        # Nanti ganti dengan ID ASLI kamu di sini sebelum rilis.
        self.ads = KivMob(TestIds.APP)
        self.ads.new_rewarded_video(TestIds.REWARDED_VIDEO)
        self.ads.set_rewarded_ad_listener(self)
        
        # --- LAYOUT ---
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.counter = 0
        self.label_info = Label(text="Saldo Poin: 0", font_size='40sp', color=(1,1,1,1))
        self.status_label = Label(text="Menunggu sistem...", font_size='18sp', color=(0.7,0.7,0.7,1))
        
        self.btn_main = Button(
            text="MEMUAT...", 
            font_size='30sp',
            background_color=(0.3, 0.3, 0.3, 1),
            disabled=True,
            size_hint=(1, 0.5)
        )
        self.btn_main.bind(on_press=self.user_watch_ad)

        layout.add_widget(self.label_info)
        layout.add_widget(self.status_label)
        layout.add_widget(self.btn_main)
        
        # Jalankan siklus pertama
        self.schedule_next_load()
        return layout

    def schedule_next_load(self, *args):
        # Fitur Keamanan: Jeda Random 3 sampai 9 detik
        delay = random.uniform(3.0, 9.0)
        
        self.status_label.text = f"Istirahat {int(delay)} detik (Anti-Spam)..."
        self.btn_main.text = "MENUNGGU..."
        self.btn_main.background_color = (0.3, 0.3, 0.3, 1)
        self.btn_main.disabled = True
        
        # Jadwalkan penarikan iklan
        Clock.schedule_once(self.load_ad_from_server, delay)

    def load_ad_from_server(self, *args):
        self.status_label.text = "Sedang mengambil iklan..."
        self.btn_main.text = "LOADING..."
        self.ads.load_rewarded_ad()

    # --- LISTENER KIVMOB (Respon Iklan) ---
    def on_rewarded_video_ad_loaded(self):
        # Iklan siap, tombol jadi HIJAU
        self.status_label.text = "Iklan Siap! Silakan tonton."
        self.btn_main.text = "▶ TONTON VIDEO"
        self.btn_main.background_color = (0, 0.8, 0, 1) # Hijau
        self.btn_main.disabled = False # Tombol aktif
        
    def on_rewarded_video_ad_closed(self):
        self.counter += 1
        self.label_info.text = f"Saldo Poin: {self.counter}"
        self.schedule_next_load()
        
    def on_rewarded_video_ad_failed_to_load(self, error):
        self.status_label.text = "Gagal memuat (Sinyal/No Fill). Coba lagi..."
        Clock.schedule_once(self.load_ad_from_server, 5)

    def on_rewarded_video_ad_started(self): pass
    def on_rewarded_video_ad_completed(self): pass
        
    def user_watch_ad(self, instance):
        # Interaksi Manual (Wajib agar tidak banned)
        self.btn_main.disabled = True
        self.ads.show_rewarded_ad()

if __name__ == '__main__':
    SafeAdApp().run()
