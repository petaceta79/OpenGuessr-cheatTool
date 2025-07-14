# OpenGuessr-cheatTool
Herramienta para obtener ubicación exacta en OpenGuessr (uso ético cuestionable, riesgo de ban).

---

## Índice  
- [Disclaimer Legal](#️-disclaimer-legal)  
- [Objetivo](#-objetivo)  
- [Proceso](#️-proceso)  
- [Requerimientos](#-requerimientos)  
- [Uso](#-uso)  
- [Resultado](#-resultado)  

## Disclaimer Legal  

> **Aviso importante:** Este software se proporciona únicamente con **fines educativos y de investigación**. Su uso en entornos competitivos, exámenes o sistemas productivos sin autorización expresa constituye una violación de los términos de servicio de la mayoría de plataformas y puede acarrear consecuencias legales.

**El autor renuncia expresamente a toda responsabilidad** por:
- Sanciones, baneos o restricciones de cuenta impuestas por terceros
- Daños directos o indirectos derivados del uso inadecuado
- Pérdidas económicas o perjuicios reputacionales

**Condiciones de uso:**
✔️ Permitido para aprendizaje y desarrollo personal  
❌ Prohibido para engaño, automatización no autorizada o ventaja competitiva  

📌 **Advertencia final:**  
Este proyecto se distribuye bajo licencia [MIT](LICENSE) y debe utilizarse **exclusivamente** en entornos controlados. El usuario asume todos los riesgos asociados a su implementación. Se recomienda encarecidamente:
1. Revisar minuciosamente la documentación
2. Evaluar el cumplimiento normativo en su jurisdicción
3. No utilizarlo en sistemas críticos sin pruebas exhaustivas

**ÚSELO BAJO SU PROPIO RIESGO Y RESPONSABILIDAD**

💡 **Recuerda:** La verdadera diversión está en jugar limpiamente. Este proyecto existe para aprender, no para ganar ventajas.

## Objetivo

Desarrollar la habilidad para investigar y comprender código HTML y JavaScript ajeno, utilizando las herramientas de desarrollo del navegador (DevTools). Además, adquirir la capacidad de adaptarse a distintas situaciones y desarrollar software que analice entornos y se adapte a ellos.

## Proceso

Una vez dentro de la partida, utilizando las herramientas de desarrollo de Chrome, decidí buscar si se utilizaba la API de Google Maps u otro método para cargar la vista Street View. Descubrí que, en uno de los iframes donde se incrusta Street View, las coordenadas iniciales aparecen directamente en la URL del atributo `src`.

```html
<iframe id="PanoramaIframe" referrerpolicy="no-referrer-when-downgrade" frameborder="0" src="https://www.google.com/maps/embed/v1/streetview?location=41.25349938040411,-83.57514848812019&key=AIzaSyAHt3QJRBDISRaWaqblQl2VwjWiHvjpgIs&fov=90" class="svelte-3nuhic" style="filter: none;"></iframe>
```
Con esta información, el siguiente paso fue obtener el HTML mediante Selenium para automatizar el proceso y hacerlo interactivo. A través de una función personalizada, se extraen las coordenadas (números) desde la URL del iframe.

Además, se utilizó la librería undetected_chromedriver para evitar que el navegador revele que está siendo controlado por un script, permitiendo que actúe como un navegador común y corriente.

## Requerimientos

### 1. Lenguaje

- **Python**

### 2. Dependencias (librerías de Python)

| Librería                 | Descripción                                                                 | Instalación                             |
|--------------------------|-----------------------------------------------------------------------------|------------------------------------------|
| `selenium`               | Automatización de navegadores web.                                          | `pip install selenium`                   |
| `undetected_chromedriver`| Versión modificada de ChromeDriver para evitar la detección como bot.       | `pip install undetected-chromedriver`    |
| `re` (built-in)          | Manejo de expresiones regulares (incluida en Python por defecto).           | No requiere instalación                  |
| `time` (built-in)        | Manejo de tiempos y retardos.                                               | No requiere instalación                  |












🚧 *Documentación en construcción - Próximamente más detalles* 🚧
