import telekit

from telekit.styles import * # pyright: ignore[reportWildcardImportFromLibrary]

import screenshot
import input_controller
import config

input_ctrl = input_controller.InputController(20)
whitelist = [int(config.ADMIN)]

class StartHandler(telekit.Handler):
    @classmethod
    def init_handler(cls) -> None:
        cls.on.command("start", whitelist=whitelist).invoke(cls.handle)

    def handle(self) -> None:
        self.chain.disable_timeout_warnings()
        self.main_keyboard = {
            "↖️": self.freeze(input_ctrl.move_up_left),
            "⬆️": self.freeze(input_ctrl.move_up),
            "↗️": self.freeze(input_ctrl.move_up_right),

            "⬅️": self.freeze(input_ctrl.move_left),
            "Click": self.freeze(input_ctrl.click),
            "➡️": self.freeze(input_ctrl.move_right),

            "↙️": self.freeze(input_ctrl.move_down_left),
            "⬇️": self.freeze(input_ctrl.move_down),
            "↘️": self.freeze(input_ctrl.move_down_right),

            "Slower": self.freeze(self.modify_cursor_speed, -5),
            "Faster": self.freeze(self.modify_cursor_speed, 5),
            "Default Speed": self.freeze(self.modify_cursor_speed, 0),

            "Screenshot": self.freeze(self.attach_photo),
            "Write": self.type_text
        }
        self.update()

    def update(self) -> None:
        with self.chain.sender as sender:
            sender.set_title("🧑‍💻 Your PC is connected")
            sender.set_message(
                f"{Bold("Cursor Speed")} – {int(input_ctrl.speed)}",
            )
            sender.set_use_italics(False)

        self.chain.set_inline_keyboard(
            self.main_keyboard, row_width=3
        )
        self.chain.edit()

    def attach_photo(self):
        screenshot.make_screenshot(config.SCREENSHOT_PATH)
        self.chain.sender.set_photo(config.SCREENSHOT_PATH)

    def modify_cursor_speed(self, speed: int):
        if speed in (0, 1, -1):
            input_ctrl.speed = 20
            return
        
        if 0 < speed:
            input_ctrl.speed *= speed
        else:
            input_ctrl.speed /= -speed

        if input_ctrl.speed <= 0:
            input_ctrl.speed = 20
        
    def type_text(self):
        with self.chain.sender as sender:
            sender.set_title("⌨️ Type your text...")
            sender.set_message("Enter the text you want to type on your Mac")
            sender.set_use_italics(False)
        
        @self.chain.entry_text(delete_user_response=True)
        def _(message, text: str):
            input_ctrl.type_text(text)
            self.update()

        self.chain.set_inline_keyboard(
            {
                "« Back": self.update
            }
        )

        self.chain.edit()
