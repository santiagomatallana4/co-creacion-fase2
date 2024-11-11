## Co-Creación Fase II: Implementación de Flask y Web Scraping

En esta fase, se implementó **Flask** como framework principal del proyecto. Debido a problemas con las rutas en la carga dinámica del **header** y **footer** utilizando JavaScript, se optó por reemplazarlo con **Jinja**, lo que permitió cargar de manera eficiente y sin errores los componentes comunes entre las páginas.

### Avances

- **Web Scraping**: Se utilizó **BeautifulSoup** y **Requests** para realizar un web scraping y obtener datos sobre **especies invasoras**. Esta nueva sección fue añadida en la página principal para ofrecer información relevante.
  
- **Almacenamiento de datos**: Los datos obtenidos del scraping fueron almacenados en un archivo **JSON**. Este archivo fue posteriormente cargado en la página correspondiente usando JavaScript.

- **Edición del JSON**: El archivo JSON fue editado manualmente para agregar imágenes y hacer el contenido más atractivo, mejorando la presentación visual de las especies invasoras.