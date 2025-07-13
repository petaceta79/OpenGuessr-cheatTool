import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import re
import undetected_chromedriver as uc



# Obtener el src con ID PanoramaIframe
def obtenerSrc(driver):
    driver.switch_to.default_content()  # Volver al contexto principal
    iframe = driver.find_element(By.ID, "PanoramaIframe")
    src = iframe.get_attribute("src")

    return src

# Dado el src obtienes una lista con las dos coordenadas
def obtenerCoordDeSrc(src):
    coord = re.findall(r'-?\d+\.?\d*', src)

    return [coord[1], coord[2]]

# Obtienes un array con las coordenadas del lugar
def obtenerCoord(driver):
    src = obtenerSrc(driver)

    coord = obtenerCoordDeSrc(src)

    return coord

def abrirPestannaMaps(driver):
    coords = obtenerCoord(driver)

    print("Coordenadas: " + ' ' + str(coords[0]) + ' ' + str(coords[1]))

    google_maps_url = f"https://www.google.com/maps?q={coords[0]},{coords[1]}"
    driver.execute_script(f"window.open('{google_maps_url}', '_blank');")







# Configuración uc.Chrome
options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

# Inicializar el driver con undetected_chromedriver
driver = uc.Chrome(options=options)

# Resto del código (igual que antes)
driver.get("https://openguessr.com/")
time.sleep(5)

try:
    print("Para cerrarlo Control + C")
    while True:
        input("Presiona Enter para abrir la ubicación en Google Maps...")
        abrirPestannaMaps(driver)
except Exception as e:
    print("Hubo un error:", str(e))
finally:
    driver.quit()