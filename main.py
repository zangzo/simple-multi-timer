
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.progressbar import MDProgressBar
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import time





class MainApp(MDApp):     
    def build(self):  
# BOXES
       self.screen = Screen()
       self.box_1 = MDBoxLayout(orientation="vertical",pos_hint={'center_x':.5, 'center_y':.87},size_hint_x= 0.6,size_hint_y = 0.05)
       self.box_2 = MDBoxLayout(orientation="vertical",pos_hint={'center_x':.5, 'center_y':.57},size_hint_x= 0.6,size_hint_y = 0.05)
       self.box_3 = MDBoxLayout(orientation="vertical",pos_hint={'center_x':.5, 'center_y':.27},size_hint_x= 0.6,size_hint_y = 0.05)
       self.screen.add_widget(self.box_1)
       self.screen.add_widget(self.box_2)
       self.screen.add_widget(self.box_3)    
# TIMERS
       self.timer_1 = MDLabel(text="00:00:00", halign="center",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),pos_hint={'center_x':.5, 'center_y':.93} )
       self.screen.add_widget(self.timer_1)
       self.timer_2 = MDLabel(text="00:00:00", halign="center",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),pos_hint={'center_x':.5, 'center_y':.63} )
       self.screen.add_widget(self.timer_2)
       self.timer_3 = MDLabel(text="00:00:00", halign="center",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),pos_hint={'center_x':.5, 'center_y':.33} )
       self.screen.add_widget(self.timer_3) 
# SLIDERS       
       self.slider_1 = MDSlider(min= 0,max= 3600,value= 0,color=(0,0.5,0.7,1))
       self.slider_1.hint = False
       self.box_1.add_widget(self.slider_1)
       self.slider_1.bind(value = self.value_change_1)
       self.slider_2 = MDSlider(min= 0,max= 3600,value= 0,color=(0,0.5,0.7,1))
       self.slider_2.hint = False
       self.box_2.add_widget(self.slider_2)
       self.slider_2.bind(value = self.value_change_2)
       self.slider_3 = MDSlider(min= 0,max= 3600,value= 0 ,color=(0,0.5,0.7,1))
       self.slider_3.hint = False
       self.box_3.add_widget(self.slider_3)
       self.slider_3.bind(value = self.value_change_3)
# BUTTONS      
       self.start_1 = MDRectangleFlatButton(text="start",md_bg_color=(0,0.5,0.7,0.1),pos_hint={'center_x':.35, 'center_y':.8},font_size= "14sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.start_1_pressed)
       self.screen.add_widget(self.start_1)
       self.stop_1 = MDRectangleFlatButton(text="stop",md_bg_color=(0,0.5,0.7,0.1),pos_hint={'center_x':.65, 'center_y':.8},font_size= "14sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.stop_1_pressed)
       self.screen.add_widget(self.stop_1)
       self.plus_hour_1 = MDFlatButton(text = "+",pos_hint={'center_x':.7, 'center_y':.93},font_size= "14sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.plus_1_pressed)
       self.screen.add_widget(self.plus_hour_1)
       self.minus_hour_1 = MDFlatButton(text = "—",pos_hint={'center_x':.3, 'center_y':.93},font_size= "14sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.minus_1_pressed)
       self.screen.add_widget(self.minus_hour_1)
       self.start_2 = MDRectangleFlatButton(text="start",md_bg_color=(0,0.5,0.7,0.1),pos_hint={'center_x':.35, 'center_y':.5},font_size= "14sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.start_2_pressed)
       self.screen.add_widget(self.start_2)
       self.stop_2 = MDRectangleFlatButton(text="stop",md_bg_color=(0,0.5,0.7,0.1),pos_hint={'center_x':.65, 'center_y':.5},font_size= "14sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.stop_2_pressed)
       self.screen.add_widget(self.stop_2)
       self.plus_hour_2 = MDFlatButton(text = "+",pos_hint={'center_x':.7, 'center_y':.63},font_size= "14sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.plus_2_pressed)
       self.screen.add_widget(self.plus_hour_2)
       self.minus_hour_2 = MDFlatButton(text = "—",pos_hint={'center_x':.3, 'center_y':.63},font_size= "14sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.minus_2_pressed)
       self.screen.add_widget(self.minus_hour_2)
       self.start_3 = MDRectangleFlatButton(text="start",md_bg_color=(0,0.5,0.7,0.1),pos_hint={'center_x':.35, 'center_y':.2},font_size= "14sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.start_3_pressed)
       self.screen.add_widget(self.start_3)
       self.stop_3 = MDRectangleFlatButton(text="stop",md_bg_color=(0,0.5,0.7,0.1),pos_hint={'center_x':.65, 'center_y':.2},font_size= "14sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.stop_3_pressed)
       self.screen.add_widget(self.stop_3)  
       self.plus_hour_3 = MDFlatButton(text = "+",pos_hint={'center_x':.7, 'center_y':.33},font_size= "14sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.plus_3_pressed)
       self.screen.add_widget(self.plus_hour_3)
       self.minus_hour_3 = MDFlatButton(text = "—",pos_hint={'center_x':.3, 'center_y':.33},font_size= "14sp",theme_text_color= "Custom",text_color =  (0, 0.5, 0.7, 1),on_release = self.minus_3_pressed)
       self.screen.add_widget(self.minus_hour_3)
       return self.screen   
   
# VALUE CONVERTERS  
    # Convert seconds (slider's value) to hours/minutes on display
    def value_change_1(self, instance,value):
        converted_value = time.strftime('%H:%M:%S', time.gmtime(int(float(value))))
        self.timer_1.text = str(converted_value)
    def value_change_2(self, instance,value):
        converted_value = time.strftime('%H:%M:%S', time.gmtime(int(float(value))))
        self.timer_2.text = str(converted_value)
    def value_change_3(self, instance,value):
        converted_value = time.strftime('%H:%M:%S', time.gmtime(int(float(value))))
        self.timer_3.text = str(converted_value)
        
#BUTTONS BEHAVIOUR        
    # Button start was pressed
    def start_1_pressed(self,*args):
        if self.slider_1.value == 0:
            return
        if self.start_1.text == "start":
            self.start_1.text = "pause"
            self.screen.remove_widget(self.box_1)
            self.bar_1 = MDProgressBar(value = 100, color=(0,0.5,0.7,1),pos_hint={'center_x':.5, 'center_y':.87},size_hint_x= 0.5,size_hint_y = 0.05,type= "determinate",running_duration= self.slider_1.value,running_transition = "linear")
            self.screen.add_widget(self.bar_1)
            self.bar_1.start()
            self.timer_1_interval = Clock.schedule_interval(self.timer_1_change, 1)
            return 
        elif self.start_1.text == "pause":
            self.start_1.text = "start"
            self.bar_1.stop()
            self.screen.remove_widget(self.bar_1)
            self.screen.add_widget(self.box_1)
            self.timer_1_interval.cancel()
            return
    def start_2_pressed(self,*args):
        if self.slider_2.value == 0:
            return
        if self.start_2.text == "start":
            self.start_2.text = "pause"
            self.screen.remove_widget(self.box_2)
            self.bar_2 = MDProgressBar(max = 100,color=(0,0.5,0.7,1),pos_hint={'center_x':.5, 'center_y':.57},size_hint_x= 0.5,size_hint_y = 0.05,type= "determinate",running_duration= self.slider_2.value,running_transition = "linear")
            self.screen.add_widget(self.bar_2)
            self.bar_2.start()
            self.timer_2_interval = Clock.schedule_interval(self.timer_2_change, 1)
            return
        elif self.start_2.text == "pause":
            self.start_2.text = "start"
            self.bar_2.stop()
            self.screen.remove_widget(self.bar_2)
            self.screen.add_widget(self.box_2)
            self.timer_2_interval.cancel()
            return
    def start_3_pressed(self,*args):
        if self.slider_3.value == 0:
            return
        if self.start_3.text == "start":
            self.start_3.text = "pause"
            self.screen.remove_widget(self.box_3)
            self.bar_3 = MDProgressBar(value= 100,color=(0,0.5,0.7,1),pos_hint={'center_x':.5, 'center_y':.27},size_hint_x= 0.5,size_hint_y = 0.05,type= "determinate",running_duration= self.slider_3.value,running_transition = "linear")
            self.screen.add_widget(self.bar_3)
            self.bar_3.start()
            self.timer_3_interval = Clock.schedule_interval(self.timer_3_change, 1)
            return
        elif self.start_3.text == "pause":
            self.start_3.text = "start"
            self.bar_3.stop()
            self.screen.remove_widget(self.bar_3)
            self.screen.add_widget(self.box_3)
            self.timer_3_interval.cancel()
            return
    # Stop was pressed
    def stop_1_pressed(self,*args):
        if self.slider_1.value >= 0 and self.start_1.text == "start":
            self.slider_1.value = 0
            self.screen.remove_widget(self.box_1)
            self.screen.add_widget(self.box_1)
            return
        self.slider_1.value = 0
        self.start_1.text = "start"
        self.timer_1_interval.cancel()
        self.screen.add_widget(self.box_1)
        self.screen.remove_widget(self.bar_1)
        return
    def stop_2_pressed(self,*args):
        if self.slider_2.value >= 0 and self.start_2.text == "start":
            self.slider_2.value = 0
            self.screen.remove_widget(self.box_2)
            self.screen.add_widget(self.box_2)
            return
        self.slider_2.value = 0
        self.start_2.text = "start"
        self.timer_2_interval.cancel()
        self.screen.add_widget(self.box_2)
        self.screen.remove_widget(self.bar_2)
        return
    def stop_3_pressed(self,*args):
        if self.slider_3.value >= 0 and self.start_3.text == "start":
            self.slider_3.value = 0
            self.screen.remove_widget(self.box_3)
            self.screen.add_widget(self.box_3)
            return
        self.slider_3.value = 0
        self.start_3.text = "start"
        self.timer_3_interval.cancel()
        self.screen.add_widget(self.box_3)
        self.screen.remove_widget(self.bar_3)
        return
    def plus_1_pressed(self,*args):
        self.slider_1.max +=3600
    def plus_2_pressed(self,*args):
        self.slider_2.max += 3600
    def plus_3_pressed(self,*args):
        self.slider_3.max += 3600
    def minus_1_pressed(self,*args):
        if self.slider_1.max <= 3600:
            return
        else:
            self.slider_1.max -= 3600
    def minus_2_pressed(self,*args):
        if self.slider_2.max <= 3600:
            return
        else:
            self.slider_2.max -= 3600
    def minus_3_pressed(self,*args):
        if self.slider_3.max <= 3600:
            return
        else:
            self.slider_3.max -= 3600

# TIMERS ANIMATIONS
    # Animation of timer running
    def timer_1_change(self,*args):
        if self.slider_1.value <= 0:
                self.start_1.text = "start"
                self.timer_1_interval.cancel()
                self.screen.add_widget(self.box_1)
                self.screen.remove_widget(self.bar_1)
                self.slider_1.value = 0
                self.sound = SoundLoader.load('bell.wav')
                self.sound.play()
        else:
            self.screen.remove_widget(self.timer_1)
            self.slider_1.value -=1
            self.screen.add_widget(self.timer_1)
        return
    def timer_2_change(self,*args):
        if self.slider_2.value <= 0:
                self.start_2.text = "start"
                self.timer_2_interval.cancel()
                self.screen.add_widget(self.box_2)
                self.screen.remove_widget(self.bar_2)
                self.slider_2.value = 0
                self.sound = SoundLoader.load('bell.wav')
                self.sound.play()
        else:
            self.screen.remove_widget(self.timer_2)
            self.slider_2.value -=1
            self.screen.add_widget(self.timer_2)
        return
    def timer_3_change(self,*args):
        if self.slider_3.value <= 0:
                self.start_3.text = "start"
                self.timer_3_interval.cancel()
                self.screen.add_widget(self.box_3)
                self.screen.remove_widget(self.bar_3)
                self.slider_3.value = 0
                self.sound = SoundLoader.load('bell.wav')
                self.sound.play()
        else:
            self.screen.remove_widget(self.timer_3)
            self.slider_3.value -=1
            self.screen.add_widget(self.timer_3)
        return


       
       
MainApp().run()




