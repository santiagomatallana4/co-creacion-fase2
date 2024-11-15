## Clonado y correcta ejecución del proyecto
Una vez clonado el proyecto se deben ejecutar los siguientes pasos:
- **Tener instalado Python**: Asegurarse de que Python este instalado en el equipo.
- **Ejecucion de comandos**: Se debe abrir un CMD en la carpeta raíz del proyecto, en el que se ejecutaran los siguientes comandos:
  - pip install virtualenv
  - python -m venv virtual
  - virtual\Scripts\activate
  - Pyhton (para asegurarse que el python esta corriendo correctamente)
  - Ctrl+Z+Enter
  - pip install flask
  - pip install pandas
  - pip install plotly
- Y finalmente ejecutar el siguiente comando: Python app.py

## Co-Creación Fase II: Implementación de Flask y Web Scraping

En esta fase, se implementó **Flask** como framework principal del proyecto. Debido a problemas con las rutas en la carga dinámica del **header** y **footer** utilizando JavaScript, se optó por reemplazarlo con **Jinja**, lo que permitió cargar de manera eficiente y sin errores los componentes comunes entre las páginas.

### Avances

- **Web Scraping**: Se utilizó **BeautifulSoup** y **Requests** para realizar un web scraping y obtener datos sobre **especies invasoras**. Esta nueva sección fue añadida en la página principal para ofrecer información relevante.
  
- **Almacenamiento de datos**: Los datos obtenidos del scraping fueron almacenados en un archivo **JSON**. Este archivo fue posteriormente cargado en la página correspondiente usando JavaScript.

- **Edición del JSON**: El archivo JSON fue editado manualmente para agregar imágenes y hacer el contenido más atractivo, mejorando la presentación visual de las especies invasoras.

### Registro Fotográfico
![webscrapping](https://github.com/santiagomatallana4/co-creacion-fase2/blob/main/fase2/1.png)
![webscrapping](https://github.com/santiagomatallana4/co-creacion-fase2/blob/main/fase2/2.png)
![webscrapping](https://github.com/santiagomatallana4/co-creacion-fase2/blob/main/fase2/3.png)
![webscrapping](https://github.com/santiagomatallana4/co-creacion-fase2/blob/main/fase2/4.png)
![webscrapping](https://github.com/santiagomatallana4/co-creacion-fase2/blob/main/fase2/5.png)
![webscrapping](https://github.com/santiagomatallana4/co-creacion-fase2/blob/main/fase2/6.png)
![webscrapping](https://github.com/santiagomatallana4/co-creacion-fase2/blob/main/fase2/7.png)
**Implementación del WebScrapping e inclusión con la fase anterior**
