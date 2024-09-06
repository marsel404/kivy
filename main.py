from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import constants


# Экран ввода номера телефона
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)


    def get_code(self):
        if self.ids.phone_number.text == constants.phone_number:
            self.manager.current = 'code'
        else:
            self.ids.rules.text = 'Неверный номер телефона'


# Экран ввода кода из смс
class CodeScreen(Screen):
    def __init__(self, **kwargs):
        super(CodeScreen, self).__init__(**kwargs)


    # Функция для корректной работы инпута заполнения кода
    def get_text(self, text_input, position):
        text = text_input.text
        if len(text) > 1:
            text_input.text = text[0]
        next_input = None
        if position < 6:
            next_input = self.ids[f'digit{position + 1}']
        if next_input:
            next_input.focus = True


    # Проверяем код; если правильный, пускаем в кабинет
    def check_code(self):
        code = (
            self.ids.digit1.text +
            self.ids.digit2.text +
            self.ids.digit3.text +
            self.ids.digit4.text +
            self.ids.digit5.text +
            self.ids.digit6.text
        )
        if code == constants.code:
            self.manager.current = 'main_page'
        else:
            self.ids.message_sent.text = 'Неверный код'
            

    def logout(self):
        self.manager.current = 'login'


# Экран главной страницы
class MainPageScreen(Screen):
    def __init__(self, **kwargs):
        super(MainPageScreen, self).__init__(**kwargs)


    def logout(self):
        self.manager.current = 'login'


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.add_widget(LoginScreen(name='login'))
        self.add_widget(CodeScreen(name='code'))
        self.add_widget(MainPageScreen(name='main_page'))


class TestApp(App):
    def build(self):
        return MyScreenManager()

if __name__ == '__main__':
    TestApp().run()