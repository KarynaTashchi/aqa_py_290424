import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# Ініціалізація веб-драйвера
driver = webdriver.Chrome()

# Відкриття початкової сторінки
driver.get("http://localhost:8000/dz.html")

# Функція для верифікації тексту у фреймі
def verify_frame(frame_id, input_id, secret_text, expected_text):
    # Переключаємося на фрейм
    driver.switch_to.frame(driver.find_element(By.ID, frame_id))

    # Введення секретного тексту
    input_field = driver.find_element(By.ID, input_id)
    input_field.send_keys(secret_text)

    # Натискання кнопки "Перевірити"
    check_button = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
    check_button.click()

    # Очікуємо появи діалогового вікна
    time.sleep(1)

    # Перемикаємося на діалогове вікно
    alert = Alert(driver)

    # Отримуємо текст діалогового вікна
    alert_text = alert.text

    # Порівняння тексту для підтвердження успішності
    if alert_text == expected_text:
        print(f"Verification successful in {frame_id}")
    else:
        print(f"Verification failed in {frame_id}: Expected '{expected_text}', but got '{alert_text}'")

    # Закриваємо діалогове вікно
    alert.accept()

    # Повертаємося на основну сторінку перед переходом до наступного фрейму
    driver.switch_to.default_content()

# Верифікація тексту у фреймах
verify_frame("frame1", "input1", "Frame1_Secret", "Верифікація пройшла успішно!")
verify_frame("frame2", "input2", "Frame2_Secret", "Верифікація пройшла успішно!")

# Закриття браузера
driver.quit()
