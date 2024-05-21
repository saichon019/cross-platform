from kivy.app import App
from kivy.uix.screenmanager import Screen



class UI(Screen): #ทำหน้าที่จัดการหน้าจอต่างๆ
    def add_item(self):
        #นำค่าที่พิมพ์ผ่านช่อง textinput ปเพิ่มใน spinner
        self.ids.spin_lang.values.append(self.ids.txt_input.text)

    
class spinnerApp(App):
    def build(self):
        return UI()
    
if __name__=="__main__":
    spinnerApp().run()