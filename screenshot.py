import platform
import pyautogui

system = platform.system()

def make_screenshot_no_cursor(path: str):
    screenshot = pyautogui.screenshot()
    screenshot.save(path)

# OS-specific imports and functions
if system in ("Windows", "Darwin"):  # Darwin = macOS
    from PIL import ImageGrab, ImageDraw
    if system == "Darwin":
        import AppKit

        def get_scale_factor(): # type: ignore
            screen = AppKit.NSScreen.mainScreen() # type: ignore
            return screen.backingScaleFactor()
    else:
        def get_scale_factor():
            return 1  # no scaling on Windows by default

    def get_cursor():
        x, y = pyautogui.position()
        return int(x * get_scale_factor()), int(y * get_scale_factor())

    def make_screenshot(path: str):
        img = ImageGrab.grab()
        x, y = get_cursor()
        draw = ImageDraw.Draw(img)
        draw.ellipse((x-5, y-5, x+5, y+5), fill="red")
        img.save(path)

elif system == "Linux":
    import pyscreenshot as ImageGrab # type: ignore
    from PIL import ImageDraw

    def get_cursor():
        pos = pyautogui.position()
        return pos.x, pos.y

    def make_screenshot(path: str):
        img = ImageGrab.grab()
        x, y = get_cursor()
        draw = ImageDraw.Draw(img)
        draw.ellipse((x-5, y-5, x+5, y+5), fill="red")
        img.save(path)

else:
    raise RuntimeError("Unsupported OS")