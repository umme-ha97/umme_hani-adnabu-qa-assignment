import os
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def before_scenario(context, scenario):
    options = Options()

    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    if os.getenv("CI"):
        context.driver.set_window_size(1920, 1080)
    else:
        context.driver.maximize_window()

def after_scenario(context, scenario):
    if scenario.status == "failed":
        os.makedirs("reports/screenshots", exist_ok=True)
        screenshot_name = scenario.name.replace(" ", "_").replace("/", "_")
        screenshot_path = f"reports/screenshots/{screenshot_name}.png"
        context.driver.save_screenshot(screenshot_path)


        with open(screenshot_path, "rb") as image_file:
            allure.attach(
                image_file.read(),
                name=screenshot_name,
                attachment_type=allure.attachment_type.PNG
            )
    context.driver.delete_all_cookies()
    context.driver.quit()