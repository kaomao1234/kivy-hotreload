from kivy.config import Config
from PIL import ImageGrab
from kivymd.uix.screenmanager import MDScreenManager

resolution = ImageGrab.grab().size
Config.set('graphics', 'resizable', False)
# resolution of the application
Config.set("graphics", "height", resolution[1])
Config.set("graphics", "width", "400")
from kaki.app import App
from kivymd.app import MDApp

"""
Script สำหรับจัดการ hot reload ใน project
"""
import importlib
from file_path import kv_files
from kivy.core.window import Window

# วาง app window ไว้ด้านขวา
Window.top = 0
Window.left = resolution[0] - Window.width




class Test(MDApp, App):
    DEBUG = 1
    KV_FILES = kv_files

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_view = None

    def build_app(self, first=False):
        """
        การ reload app จะรันผ่าน method นี้
        :param first:
        :return: Widget
        """

        import views.all_views as views
        self.base_view = MDScreenManager()
        Window.bind(
            on_key_down=self.on_keyboard
        )
        for name, view in views.views.items():
            self.base_view.add_widget(view(name=name))
        return self.base_view

    def on_keyboard(self, window, keyboard, keycode, text, modifier):
        """
        โดยปกติการ reload ของ app จะ keycode ที่กำหนดจะเป็น PauseBreak ใน Windows
        สามารถเปลี่ยน keycode ที่จะกดได้
        :param window:
        :param keyboard:
        :param keycode:
        :param text: คีย์ที่กด
        :param modifier:
        :return: None
        """
        if text == "Ĩ":
            # PauseBreak == "Ĩ"
            self.reload_py()
            self.rebuild()

    def reload_py(self):
        """
        method นี้มีไว้สำหรับทำ reload python file ยกเว้น file main(file นี้)
        :return: None
        """
        import file_path
        importlib.reload(file_path)
        for module in file_path.python_files:
            importlib.reload(module)


if __name__ == "__main__":
    Test().run()
