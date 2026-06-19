from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

class CalculatorGameApp(App):
    def build(self):
        self.title = "Калькулятор"
        self.game_mode = False
        
        self.width_field = 15
        self.dino_pos = 2
        self.cactus_pos = 14
        self.is_jumping = False
        self.jump_timer = 0
        self.score = 0
        
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Экран ёпта
        self.display = Label(
            text="0", 
            font_size='40sp', 
            size_hint_y=0.2, 
            halign='right', 
            valign='middle'
        )
        self.display.bind(size=self.display.setter('text_size'))
        self.main_layout.add_widget(self.display)
        
        self.buttons_layout = GridLayout(cols=4, spacing=5, size_hint_y=0.8)
        
        # Создаю кнопки блять и вы будете использовать только 7 и = я заебался писать
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        for btn in buttons:
            button = Button(text=btn, font_size='30sp')
            button.bind(on_press=self.on_button_press)
            self.buttons_layout.add_widget(button)
            
        self.main_layout.add_widget(self.buttons_layout)
        return self.main_layout

    def on_button_press(self, instance):
        text = instance.text
        
        # любаю кнопка это прыжок блять
        if self.game_mode:
            if not self.is_jumping:
                self.is_jumping = True
                self.jump_timer = 4 # будет 4 кадра воздуханом
            return

        # обычный калуькулятор блять его логика 
        if text == 'C':
            self.display.text = '0'
        elif text == '=':
            # вот код аутисты
            if self.display.text == '777':
                self.start_game()
            else:
                try:
                    self.display.text = str(eval(self.display.text))
                except:
                    self.display.text = 'Ошибка'
        else:
            if self.display.text == '0' or self.display.text == 'Ошибка':
                self.display.text = text
            else:
                self.display.text += text

    def start_game(self):
        self.game_mode = True
        self.score = 0
        self.cactus_pos = 14
        self.is_jumping = False
        self.display.font_size = '30sp' #убираю жир у шрифта
        
        # радуйся 7 кадрам в секунду
        Clock.schedule_interval(self.game_update, 0.15)

    def game_update(self, dt):
        if not self.game_mode:
            return False

        # проверка на жирность
        if self.is_jumping:
            self.jump_timer -= 1
            if self.jump_timer <= 0:
                self.is_jumping = False

        # Двигаю себя
        self.cactus_pos -= 1
        if self.cactus_pos < 0:
            self.cactus_pos = self.width_field - 1
            self.score += 1

        # Проверяю роняли ли вас в детстве
        if self.cactus_pos == self.dino_pos and not self.is_jumping:
            self.display.text = f"ахахаха лох пососи! СЧЕТ: {self.score} (ахахаах как ты слился )by ПЕНИС"
            self.game_mode = False
            Clock.unschedule(self.game_update)
            return

        # рисую для вас кадры
        frame = ["_"] * self.width_field
        
        # Ставлю себя
        frame[self.cactus_pos] = "8"
        
        # код 777 для запуска динозаврика это для далбаеёбов
        if self.is_jumping:
            frame[self.dino_pos] = " " # хай от Пениса
        else:
            frame[self.dino_pos] = "5" 

        self.display.text = "".join(frame)

if __name__ == '__main__':
    CalculatorGameApp().run()
  
