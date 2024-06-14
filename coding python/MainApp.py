from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# อ่านไฟล์ KV
Builder.load_file('login.kv')

class LoginScreen(Screen):
    def validate_login(self, username, password):
        if username == 'admin' and password == 'password':
            self.manager.current = 'training'
        else:
            print("Invalid username or password")

        # เพิ่มเงื่อนไขเพื่อเปลี่ยนหน้าไปยังหน้าลงทะเบียนใหม่
        if username == 'admin' and password == 'password':
            self.manager.current = 'register'

class TrainingScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class LicenseApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(TrainingScreen(name='training'))
        sm.add_widget(RegisterScreen(name='register'))
        return sm
    
class RegisterScreen(Screen):
    def validate_inputs(self):
        id_card1 = self.ids.id_card_input1.text.strip()
        id_card2 = self.ids.id_card_input2.text.strip()
        phone_number = self.ids.phone_number_input.text.strip()
        email = self.ids.email_input.text.strip()

        if len(id_card1) != 13 or len(id_card2) != 13:
            print("ID Card must be exactly 13 characters long!")
        elif id_card1 != id_card2:
            print("ID Cards do not match!")
        else:
            print("Form submitted!")



if __name__ == '__main__':
    LicenseApp().run()