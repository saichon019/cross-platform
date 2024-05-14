from kivy.uix.rst import role_doc
from kivy.uix.settings import text_type
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen


class Scr_bmi(Screen):
    def cal_bmi(self):
        # ค่า bmi = น้ำหนัก กก / ()
        weight = float (self.ids.txt_weight.text)
        height = float (self.ids.txt_height.text)
        height = height/100

        bmi = weight/(height*height)
        self.ids.lbl_bmi.text=str(bmi)
        if bmi > 35:
            self.ids.lbl_bmi.color="red"
            self.ids.img_bmi.source="pic/5.PNG"
        elif bmi >30:
            self.ids.lbl_bmi.color="orange"
            self.ids.img_bmi.source="pic/4.PNG"
        elif bmi >25:
            self.ids.lbl_bmi.color="yellow"
            self.ids.img_bmi.source="pic/3.PNG"
        elif bmi >18:
            self.ids.lbl_bmi.color="blue"
            self.ids.img_bmi.source="pic/2.PNG"
        else:
            self.ids.lbl_bmi.color="green"
            self.ids.img_bmi.source="pic/1.PNG"

        

class Scr_Knowledge(Screen): #หน้าจอที่1
    pass

class UI(ScreenManager): #ทำหน้าที่จัดการหน้าจอต่างๆ
    pass
    
class bmiApp(App):
    def build(self):
        return UI()
    
if __name__=="__main__":
    bmiApp().run()