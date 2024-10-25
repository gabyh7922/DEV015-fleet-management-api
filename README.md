# Fleet Management Software API

## Índice

* [1. Preámbulo](#1-preámbulo)
* [2. Resumen del proyecto](#2-resumen-del-proyecto)
* [3. Objetivos de aprendizaje](#3-objetivos-de-aprendizaje)
* [4. Consideraciones generales](#4-consideraciones-generales)
* [5. Criterios de aceptación del proyecto](#5-criterios-de-aceptación-del-proyecto)
* [6. Stack de tecnologías](#6-stack-de-tecnologías)
* [7. Testing](#7-testing)
* [8. Pistas, tips y lecturas complementarias](#8-pistas-tips-y-lecturas-complementarias)
* [9. Funcionalidades opcionales](#9-funcionalidades-opcionales)

***

## 1. Preámbulo

De acuerdo con
[Wikipedia](https://es.wikipedia.org/wiki/Internet_de_las_cosas),
la internet de las cosas (IoT, por sus siglas en inglés)​ es un concepto que
se refiere a una interconexión digital de objetos cotidianos con internet.
Constituye un cambio radical en la calidad de vida de las personas en la
sociedad, ofreciendo nuevas oportunidades en el acceso a
datos, educación, seguridad, asistencia
sanitaria y en el transporte, entre otros campos. Por ejemplo,
en logística y manejo de flotas, se puede hacer seguimiento en
todo momento de la ubicación y las condiciones de vehículos
mediante sensores inalámbricos conectados a internet que envían alertas en
caso de eventualidades (demoras, daños, robos, etc.).

![zach-vessels-utMdPdGDc8M-unsplash](https://firebasestorage.googleapis.com/v0/b/laboratoria-945ea.appspot.com/o/fleet-management-api-java%2Fthumb.jpg?alt=media)

La IoT también plantea retos como el almacenamiento, análisis y
visualización de la gran cantidad de información que genera.
Se calcula que para el 2025 los dispositivos IoT generen
[79.4 zettabytes](https://www.statista.com/statistics/1017863/worldwide-iot-connected-devices-data-size/)
(1 zettabyte equivale a 1 trillón de gigabytes).
Como desarrolladoras debemos estar al tanto de estos retos y contribuir para
su solución desde nuestra experiencia, conocimiento y ganas de aprender.

## 2. Resumen del proyecto

En este proyecto construirás la API REST de un
[Fleet Management Software](https://en.wikipedia.org/wiki/Fleet_management)
para consultar las ubicaciones de los vehículos de una empresa
de taxis en Beijing, China.

Te entregaremos las ubicaciones de casi 10 mil
taxis. Esperamos que como desarrolladora explores nuevas alternativas y
técnicas para almacenar y consultar esta
información y puedas garantizar la mejor experiencia de usuaria en tu
API REST.

## 3. Objetivos de aprendizaje


Reflexiona y luego marca los objetivos que has llegado a entender y aplicar en tu proyecto. Piensa en eso al decidir tu estrategia de trabajo.

### Python

- [ ] **Variables (declaración, asignación, ámbito)**

  <details><summary>Links</summary><p>

  * [Variables in Python – Real Python (en inglés)](https://realpython.com/python-variables/)
  * [Variables in Python - GeeksforGeeks (en inglés)](https://www.geeksforgeeks.org/python-variables/)
</p></details>

- [ ] **Uso de condicionales (if, elif, ternario)**

  <details><summary>Links</summary><p>

  * [Conditional Statements in Python – Real Python (en inglés)](https://realpython.com/python-conditional-statements/)
</p></details>

- [ ] **Operadores (identidad, aritméticos, comparación etc)**

  <details><summary>Links</summary><p>

  * [Python Operators - GeeksforGeeks (en inglés)](https://www.geeksforgeeks.org/python-operators/)
</p></details>

- [ ] **Docstrings (y su diferencia de comentarios)**

  <details><summary>Links</summary><p>

  * [Docstrings - Python Docs (en inglés)](https://docs.python.org/3/tutorial/controlflow.html#documentation-strings)
</p></details>

- [ ] **Linting (pylint)**

  <details><summary>Links</summary><p>

  * [Pylint - Documentación oficial](https://pylint.pycqa.org/en/latest/)
  * [Linting Python in Visual Studio Code - Visual Studio Code Docs (en inglés)](https://code.visualstudio.com/docs/python/linting)
</p></details>

- [ ] **Serialización (y deserialización)**

  <details><summary>Links</summary><p>

  * [Serialize Your Data With Python – Real Python (en inglés)](https://realpython.com/python-serialize-data/)
</p></details>

#### Tipos de datos

- [ ] **Tipos de datos primitivos (int, float, str, bool)**

  <details><summary>Links</summary><p>

  * [Data Types - Python Docs (en inglés)](https://docs.python.org/3/library/datatypes.html)
  * [Data types in Python (en inglés)](https://www.educative.io/answers/data-types-in-python)
</p></details>

- [ ] **Listas (arrays)**

  <details><summary>Links</summary><p>

  * [Lists - Python Docs (en inglés)](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
  * [Lists and Tuples in Python - Real Python (en inglés)](https://realpython.com/python-lists-tuples/)
</p></details>

- [ ] **Tuples**

  <details><summary>Links</summary><p>

  * [Tuples - Python Docs (en inglés)](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
  * [Lists and Tuples in Python - Real Python (en inglés)](https://realpython.com/python-lists-tuples/)
</p></details>

- [ ] **Dictionaries (Dicts)**

  <details><summary>Links</summary><p>

  * [Dictionaries - Python Docs (en inglés)](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
  * [Dictionaries in Python - Real Python (en inglés)](https://realpython.com/python-dicts/)
</p></details>

- [ ] **Sets**

  <details><summary>Links</summary><p>

  * [Sets - Python Docs (en inglés)](https://docs.python.org/3/tutorial/datastructures.html#sets)
  * [Sets in Python - Real Python (en inglés)](https://realpython.com/python-sets/)
</p></details>

#### Funciones

- [ ] **Conceptos basicos (params, args, default values, return)**

  <details><summary>Links</summary><p>

  * [Python Functions - GeeksforGeeks (en ingles)](https://www.geeksforgeeks.org/python-functions/)
</p></details>

- [ ] ***args y **kwargs**

  <details><summary>Links</summary><p>

  * [*args and **kwargs in Python - GeeksforGeeks (en inglés)](https://www.geeksforgeeks.org/args-kwargs-python/)
</p></details>

- [ ] **Cierres (closures)**

  <details><summary>Links</summary><p>

  * [Closures - Python Docs (en inglés)](https://docs.python.org/3/reference/datamodel.html#emulating-closures-and-nested-scope)
</p></details>

- [ ] **Funciones lambda**

  <details><summary>Links</summary><p>

  * [Lambda Functions - Python Docs (en inglés)](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
  * [How to Use Python Lambda Functions – Real Python (en inglés)](https://realpython.com/python-lambda/)
</p></details>

- [ ] **Decoradores**

  <details><summary>Links</summary><p>

  * [Decorators - Python Docs (en inglés)](https://docs.python.org/3/glossary.html#term-decorator)
  * [Decorators in Python - Geeks for Geeks (en inglés)](https://www.geeksforgeeks.org/decorators-in-python/)
</p></details>

#### Iteración

- [ ] **Uso de bucles/ciclos (while, for..in)**

  <details><summary>Links</summary><p>

  * [Loops in Python - For, While and Nested Loops - GeeksforGeeks](https://www.geeksforgeeks.org/loops-in-python/)
  * [Loops - Learn Python - Free Interactive Python Tutorial](https://www.learnpython.org/en/Loops)
</p></details>

- [ ] **Comprensión de listas**

  <details><summary>Links</summary><p>

  * [List Comprehension - Python Docs (en inglés)](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
  * [List Comprehension in Python - GeeksforGeeks (en inglés)](https://www.geeksforgeeks.org/list-comprehensions-in-python/)
  * [When to Use a List Comprehension in Python – Real Python (en inglés)](https://realpython.com/list-comprehension-python/)
</p></details>

- [ ] **Técnicas funcionales (map, filter, reduce)**

  <details><summary>Links</summary><p>

  * [Our Guide to Map, Filter, and Reduce Functions in Python - Udacity (en inglés)](https://www.udacity.com/blog/2020/12/our-guide-to-map-filter-and-reduce-functions-in-python.html)
  * [Map, Filter, Reduce - Learn Python - Free Interactive Python Tutorial (en inglés)](https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce)
</p></details>

#### Testing en Python

- [ ] **Pruebas unitarias (unit tests, unittest, pytest)**

  <details><summary>Links</summary><p>

  * [unittest - Python Docs (en inglés)](https://docs.python.org/3/library/unittest.html)
  * [pytest - Documentación oficial](https://docs.pytest.org/en/6.2.x/)
</p></details>

- [ ] **Uso de mocks (y patch)**

  <details><summary>Links</summary><p>

  * [unittest.mock - Python Docs (en inglés)](https://docs.python.org/3/library/unittest.mock.html)
  * [Python Mock Library - Real Python (en inglés)](https://realpython.com/python-mock-library/)
</p></details>

- [ ] **Uso de fixtures**

  <details><summary>Links</summary><p>

  * [pytest fixtures - Documentación oficial](https://docs.pytest.org/en/6.2.x/fixture.html)
</p></details>

#### Modularización

- [ ] **Módulos**

  <details><summary>Links</summary><p>

  * [Módulos - Python Docs (en inglés)](https://docs.python.org/3/tutorial/modules.html)
</p></details>

- [ ] **Paquetes**

  <details><summary>Links</summary><p>

  * [Paquetes - Python Docs (en inglés)](https://docs.python.org/3/tutorial/modules.html#packages)
</p></details>

#### Manejo de dependencias

- [ ] **pip (instalación y uso de paquetes)**

  <details><summary>Links</summary><p>

  * [pip - Python Docs (en inglés)](https://docs.python.org/3/installing/index.html)
</p></details>

- [ ] **Virtual Environment (ambientes virtuales, virtualenv)**

  <details><summary>Links</summary><p>

  * [venv — Creation of virtual environments — Python 3.12.2 documentation (en inglés)](https://docs.python.org/3/library/venv.html)
  * [Python Virtual Environments: A Primer – Real Python (en inglés)](https://realpython.com/python-virtual-environments-a-primer/)
</p></details>

- [ ] **requirements.txt**

  <details><summary>Links</summary><p>

  * [requirements.txt - Documentación oficial](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
</p></details>

#### Flask

##### Rutas _(Flask)_

- [ ] **Decorador de ruta**

  <details><summary>Links</summary><p>

  * [Routing - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#routing)
</p></details>

- [ ] **Función de vista**

  <details><summary>Links</summary><p>

  * [View Functions - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#view-functions)
</p></details>

- [ ] **Reglas de variables (urls dinamica)**

  <details><summary>Links</summary><p>

  * [Variable Rules - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#variable-rules)
</p></details>

##### Request Object _(Flask)_

- [ ] **Argumentos**

  <details><summary>Links</summary><p>

  * [Request - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#accessing-request-data)
</p></details>

- [ ] **Headers (cabeceras)**

  <details><summary>Links</summary><p>

  * [Request - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#accessing-request-data)
</p></details>

##### Response Object _(Flask)_

- [ ] **Partes de la respuesta (status, body, headers)**

  <details><summary>Links</summary><p>

  * [Response - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#about-responses)
</p></details>

- [ ] **jsonify**

  <details><summary>Links</summary><p>

  * [jsonify - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/api/#flask.json.jsonify)
</p></details>

##### Testing en Flask _(Flask)_

- [ ] **Configuración de fixtures**

  <details><summary>Links</summary><p>

  * [Testing - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/testing/#fixtures)
</p></details>

- [ ] **Test Client**

  <details><summary>Links</summary><p>

  * [Testing - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/testing/#sending-requests-with-the-test-client)
</p></details>

### Java

- [ ] **Modificadores de acesso (public, private, protected)**

- [ ] **Variables**

- [ ] **Uso de condicionales**

- [ ] **Uso de bucles (Loops)**

#### Tipos de data

- [ ] **Primitivos**

- [ ] **Datos primitivos vs no primitivos**

- [ ] **Cadenas**

- [ ] **Arreglos**

#### Colecciones

- [ ] **ArrayList**

- [ ] **HashMap**

- [ ] **HashSet**

#### Testing

- [ ] **JUnit**

- [ ] **Mockito**

#### Spring Framework

- [ ] **Initializr**

  <details><summary>Links</summary><p>

  * [Spring Initializr](https://start.spring.io/)
</p></details>

- [ ] **Spring Boot**

  <details><summary>Links</summary><p>

  * [Spring Boot Reference Documentation](https://docs.spring.io/spring-boot/docs/current/reference/html/)
</p></details>

- [ ] **Controladores**

- [ ] **Servicios**

- [ ] **Spring Data JPA**

  <details><summary>Links</summary><p>

  * [Spring Data JPA - Reference Documentation](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/)
</p></details>

- [ ] **Entidad**

- [ ] **Repositorio**

##### Conceptos Core _(Spring Framework)_

- [ ] **Beans**

- [ ] **Inversión de Control**

- [ ] **Anotaciones**

##### Spring Web _(Spring Framework)_

- [ ] **RestController**

- [ ] **RequestMapping**

- [ ] **RequestParam**

##### Testing _(Spring Framework)_

- [ ] **Spring Test**

- [ ] **Hamcrest**

#### Hibernate ORM

- [ ] **Configuración**

- [ ] **Esquema**

- [ ] **Entidad**

- [ ] **Tabla**

- [ ] **Columna**

- [ ] **Identificadores**

- [ ] **Asociaciones**

- [ ] **Colecciones**

- [ ] **Persistencia**

- [ ] **Consultas**

### Programación Orientada a Objetos (OOP)

- [ ] **Clases**

- [ ] **Objetos**

- [ ] **Métodos**

- [ ] **Atributos**

- [ ] **Constructores**

- [ ] **Encapsulamiento**

- [ ] **Abstracción**

- [ ] **Composición**

- [ ] **Interfaces**

- [ ] **Herencia (super, extends, override)**

- [ ] **Lenguaje de Modelado Unificado (UML, class diagrams)**

### HTTP

- [ ] **Consulta o petición (request) y respuesta (response).**

  <details><summary>Links</summary><p>

  * [Generalidades del protocolo HTTP - MDN](https://developer.mozilla.org/es/docs/Web/HTTP/Overview)
  * [Mensajes HTTP - MDN](https://developer.mozilla.org/es/docs/Web/HTTP/Messages)
</p></details>

- [ ] **Cabeceras (headers)**

  <details><summary>Links</summary><p>

  * [HTTP headers - MDN](https://developer.mozilla.org/es/docs/Web/HTTP/Headers)
</p></details>

- [ ] **Cuerpo (body)**

  <details><summary>Links</summary><p>

  * [Cuerpo de Mensajes HTTP - MDN](https://developer.mozilla.org/es/docs/Web/HTTP/Messages#cuerpo)
</p></details>

- [ ] **Verbos HTTP**

  <details><summary>Links</summary><p>

  * [Métodos de petición HTTP - MDN](https://developer.mozilla.org/es/docs/Web/HTTP/Methods)
</p></details>

- [ ] **Códigos de status de HTTP**

  <details><summary>Links</summary><p>

  * [Códigos de estado de respuesta HTTP - MDN](https://developer.mozilla.org/es/docs/Web/HTTP/Status)
  * [The Complete Guide to Status Codes for Meaningful ReST APIs - dev.to](https://dev.to/khaosdoctor/the-complete-guide-to-status-codes-for-meaningful-rest-apis-1-5c5)
</p></details>

- [ ] **Encodings y JSON**

  <details><summary>Links</summary><p>

  * [Introducción a JSON - Documentación oficial](https://www.json.org/json-es.html)
</p></details>

- [ ] **CORS (Cross-Origin Resource Sharing)**

  <details><summary>Links</summary><p>

  * [Control de acceso HTTP (CORS) - MDN](https://developer.mozilla.org/es/docs/Web/HTTP/CORS)
</p></details>

### Autenticación

- [ ] **JWT (JSON Web Token)**

- [ ] **Almacenamiento y acceso de contraseñas**

### SQL

- [ ] **Operaciones CRUD (Create-Read-Update-Delete)**

  <details><summary>Links</summary><p>

  * [INSERT](https://www.postgresql.org/docs/9.5/sql-insert.html)
  * [SELECT](https://www.postgresql.org/docs/9.5/sql-select.html)
  * [UPDATE](https://www.postgresql.org/docs/9.1/sql-update.html)
  * [DELETE](https://www.postgresql.org/docs/8.1/sql-delete.html)
</p></details>

### Bases de datos

- [ ] **Modelado de datos**

- [ ] **Conexión**

### PostgreSQL

- [ ] **Tipos de datos**

  <details><summary>Links</summary><p>

  * [Chapter 8. Data Types - Docs (en inglés)](https://www.postgresql.org/docs/14/datatype.html)
</p></details>

- [ ] **Índices**

  <details><summary>Links</summary><p>

  * [Chapter 11. Indexes - Docs (en inglés)](https://www.postgresql.org/docs/14/indexes.html)
</p></details>

### Control de Versiones (Git y GitHub)

#### Git

- [ ] **Git: Instalación y configuración**

- [ ] **Git: Control de versiones con git (init, clone, add, commit, status, push, pull, remote)**

- [ ] **Git: Integración de cambios entre ramas (branch, checkout, fetch, merge, reset, rebase, tag)**

#### GitHub

- [ ] **GitHub: Creación de cuenta y repos, configuración de llaves SSH**

- [ ] **GitHub: Colaboración en Github (branches | forks | pull requests | code review | tags)**

- [ ] **GitHub: Organización en Github (projects | issues | labels | milestones | releases)**

## 4. Consideraciones generales

* Este proyecto se debe "resolver" en duplas.
* El rango de tiempo estimado para completar el proyecto es de 4 a 6 Sprints.

## 5. Criterios de aceptación del proyecto

Nuestra cliente ha instalado dispositivos GPS en sus taxis.
Estos dispositivos utilizan señales satelitales para determinar
con precisión las coordenadas geográficas del taxi.

Nuestra clienta requiere:

1. Cargar la información de archivos SQL a una
base de datos PostgreSQL.
2. Desarrollar una API REST que permita consultar, mediante
peticiones HTTP, la información almacenada en la base de datos.

### Definición del producto

El [_Product Owner_](https://www.youtube.com/watch?v=r2hU7MVIzxs&t=202s)
nos presenta este _backlog_ que es el resultado de su trabajo con la clienta
hasta hoy
y la [documentación de la API REST](https://app.swaggerhub.com/apis-docs/ssinuco/FleetManagementAPI/2.0.0#/)
a desarrollar.

***

#### [Historia de usuario 1] Cargar información a base de datos

Yo, como desarrolladora, quiero cargar la información almacenada hasta ahora en
[archivos sql](https://drive.google.com/file/d/1T5m6Vzl9hbD75E9fGnjbOiG2UYINSmLx/view?usp=drive_link)
en una base de datos PostgreSQL, para facilitar su consulta y análisis.

##### Criterios de aceptación

* Se debe tener en cuenta el siguiente diagrama para la implementación de las
relaciones entre las tablas

![mer](https://firebasestorage.googleapis.com/v0/b/laboratoria-945ea.appspot.com/o/fleet-management-api-java%2Fsql-diagram.png?alt=media)

* La tabla de _trajectories_ se debe crear con el "id" que se incremente
automáticamente (SERIAL) para poder insertar los valores sin necesidad
de especificar un identificador

##### Definición de terminado

* La base de datos tiene creada la tabla de taxis
* La tabla de taxis tiene cargada la data de taxis
* La base de datos tiene creada la tabla de trayectorias
* La tabla de taxis tiene cargada la data de trayectorias

***

#### [Historia de usuario 2] Endpoint listado de taxis

Yo como clienta de la API REST requiero un _endpoint_ para
listar todos los taxis.

Por ejemplo, este _endpoint_ podria ser usado por una aplicación
web para filtrar un listado de taxis.

<img
src="https://github.com/Laboratoria/curriculum/assets/16993732/c4acb543-a422-4e79-ab6c-53c656a7ee47"
alt="Posible uso del endpoint GET /taxis"
aria-describedby="get-taxis-ui-control" />

<p id="get-taxis-ui-control">
Animación que muestra un menú desplegable para elegir un taxi.
Las opciones se filtran según el text que se escriba en la lista.
</p>

##### Criterios de aceptación

* El _endpoint_ es implementado de acuerdo a la
  [documentación swagger](https://app.swaggerhub.com/apis-docs/ssinuco/FleetManagementAPI/2.0.0#/taxis/getTaxi).
  a excepción de la respuesta 401 que sera implementada
  hasta la Historia de Usuaria 7.
* El _endpoint_ responde para cada taxi: id y placa.
* El _endpoint_ paginamos los resultados para asegurar que las
respuestas sean más fáciles de manejar.
* El _endpoint_ soporta un parametro `plate` para retornar unicamente
los taxis cuya placa contenga el texto especificado
* El _endpoint_ paginamos los resultados para asegurar que las
respuestas sean más fáciles de manejar.

##### Definición de terminado

* El código del _endpoint_ debe recibir _code review_ de al
menos una compañera.
* El código del _endpoint_ debe estar cargado en un repositorio de Github.
* El código del _endpoint_ debe contar con test unitarios.
* Pasa los tests de endpoint `/taxis` en la colección postman.

***

#### [Historia de usuario 3] Endpoint historial de ubicaciones

Yo como clienta de la API REST requiero un _endpoint_ para
consultar todas las ubicaciones de un taxi dado el id y una fecha.

Por ejemplo, este _endpoint_ podría ser usado por una aplicación
web para mostrar en un mapa la trayectoria de un taxi.

<img
src="https://github.com/Laboratoria/curriculum/assets/16993732/d716cc84-47c2-4cdd-8f67-74128aa6ec01"
alt="Posible uso del endpoint GET /trajectories/{taxiId}"
aria-describedby="get-trajectories-ui-control" />

<p id="get-trajectories-ui-control">
Animación que muestra en un mapa la trayectoria de un taxi.
</p>

##### Criterios de aceptación

* El _endpoint_ es implementado de acuerdo a la
  [documentación swagger](https://app.swaggerhub.com/apis-docs/ssinuco/FleetManagementAPI/2.0.0#/trajectories/getTrajectories)
  a excepción de la respuesta 401 que sera implementada
  hasta la Historia de Usuaria 7.
* El _endpoint_ responde para un id de taxi y una fecha mostrando
  la siguiente información: latitud, longitud y timestamp (fecha y hora).

##### Definición de terminado

* El código del _endpoint_ debe recibir _code review_ de al
menos una compañera.
* El código del _endpoint_ debe estar cargado en un repositorio de Github.
* El código del _endpoint_ debe contar con test unitarios.
* Pasa los tests de endpoint `/trajectories` en la colección postman.

***

#### [Historia de usuario 4] Endpoint última ubicación

Yo como clienta de la API REST requiero un _endpoint_ para
consultar la última ubicación reportada por cada taxi.

Por ejemplo, este _endpoint_ podria ser usado por una aplicación
web para mostrar en una mapa la última posición de cada taxi.

<img
src="https://github.com/Laboratoria/curriculum/assets/16993732/a6bd8631-244d-4d9b-a297-2519d9313855"
alt="Posible uso del endpoint GET /trajectories/latest"
aria-describedby="get-latest-trajectories-ui-control" />

<p id="get-latest-trajectories-ui-control">
Animación que un listado de taxis y al hacer clic en cada uno
muestra un mapa la última posición de un taxi.
</p>

##### Criterios de aceptación

* El _endpoint_ es implementado de acuerdo a la
  [documentación swagger](https://app.swaggerhub.com/apis-docs/ssinuco/FleetManagementAPI/2.0.0#/trajectories/getLatestTrajectories)
  a excepción de la respuesta 401 que sera implementada
  hasta la Historia de Usuaria 7.
* El _endpoint_ responde para cada taxi la siguiente información:
id, placa, latitud, longitud y timestamp (fecha y hora).
* Pasa los tests de endpoint `/trajectories/latest` en la colección postman.

##### Definición de terminado

* El código del _endpoint_ debe recibir _code review_ de al
menos una compañera.
* El código del _endpoint_ debe estar cargado en un repositorio de Github.
* El código del _endpoint_ debe contar con test unitarios.

***

#### [Historia de usuario 5] Gestión de usuarios

Yo, como clienta de la API REST, requiero un conjunto de endpoints para poder
realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los
usuarios de la plataforma.

##### Criterios de aceptación

* Crear un endpoint para la creación de usuarios de acuerdo a la
[documentación Swagger](https://app.swaggerhub.com/apis-docs/ssinuco/FleetManagementAPI/2.0.0#/users/createUser)
proporcionada.
* Desarollar un endpoint para la obtención de usuarios de acuerdo a la
[documentación Swagger](https://app.swaggerhub.com/apis-docs/ssinuco/FleetManagementAPI/2.0.0#/users/getUsers)
proporcionada.
* Implementar un endpoint para actualizar la
información de un usuario existente de acuerdo a la
[documentación Swagger](https://app.swaggerhub.com/apis-docs/ssinuco/FleetManagementAPI/2.0.0#/users/updateUser)
proporcionada.
* Crear un endpoint para eliminar un usuario de acuerdo a la
[documentación Swagger](https://app.swaggerhub.com/apis-docs/ssinuco/FleetManagementAPI/2.0.0#/users/deleteUser)
proporcionada.
* No implementar la respuesta 401 pues sera implementada
  hasta la Historia de Usuaria 7.

##### Definición de terminado

* El código de los _endpoints_ debe pasar por una revisión de código realizada
por al menos una compañera.
* El código de los _endpoints_ debe contar con test unitarios.
* Pasa los tests de endpoints `/users` en la colección postman.

Por supuesto, aquí tienes la historia de usuario para un endpoint de login que
devuelve un JWT (JSON Web Token) dado un correo electrónico y contraseña válidos:

***

#### [Historia de usuario 6] Autenticación de usuarios mediante JWT

Yo, como clienta de la API REST, necesito un _endpoint_ para poder autenticarme
en la plataforma utilizando mi correo electrónico y contraseña, y recibir un
JWT válido que pueda ser utilizado para acceder a recursos protegidos.

##### Criterios de aceptación

* Implementar el _endpoint_ de autenticación de acuerdo a la
[documentación Swagger](https://app.swaggerhub.com/apis-docs/ssinuco/FleetManagementAPI/2.0.0#/auth/getToken)
proporcionada.
* El _endpoint_ debe aceptar un correo electrónico y una contraseña válidos
como parámetros de entrada.
* Al autenticarse con éxito, el _endpoint_ debe devolver un JWT que contenga la
información de identificación del usuario.
* El JWT generado debe tener un tiempo de expiración adecuado y debe ser válido
para realizar peticiones a recursos protegidos durante ese tiempo.
* El _endpoint_ debe manejar adecuadamente los casos de error,
devolviendo mensajes descriptivos en caso de credenciales
inválidas o cualquier otro problema durante el proceso de autenticación.

##### Definición de terminado

* El código del _endpoint_ de login debe pasar por una revisión de código
realizada por al menos una compañera.
* El código del _endpoint_ debe contar con test unitarios.
* Pasa los tests de endpoint `/login/auth` en la colección postman.

***

#### [Historia de usuario 7] Protección de endpoints con JWT

Yo, como desarrolladora del sistema, necesito asegurarme de que todos los endpoints
de la API estén protegidos utilizando un token JWT en el encabezado de autorización
de cada petición, para garantizar la seguridad de los datos y
recursos de la plataforma.

##### Criterios de aceptación

* Configurar la API para que todos los endpoints requieran un token JWT
válido en el encabezado de autorización de cada petición.
* Implementar un middleware o interceptor en la capa de seguridad de la
API para verificar la validez y autenticidad del token JWT en cada petición
entrante.
* En caso de recibir una petición sin un token JWT válido o sin token en
el encabezado de autorización, la API debe devolver un código de estado
HTTP 401 (Unauthorized) y un mensaje de error apropiado.

##### Definición de terminado

* Todos los endpoints de la API deben estar protegidos con un token JWT
en el encabezado de autorización.
* El código del middleware o interceptor de seguridad debe pasar por una
revisión de código realizada por al menos una compañera.
* Se deben incluir test unitarios.
* Pasa los tests de endpoints en la colección con auth en postman.

***

## 6. Stack de tecnologías

Puedes implementar este proyecto en JavaScript, Python o Java.

* [NodeJs](./docs/stack-node.md)
* [Java](./docs/stack-java.md)
* [Python](./docs/stack-python.md)
* [C#](./docs/stack-csharp.md)

## 7. Testing

Incluido en el proyecto hay una suite de pruebas que se deben ejecutar
para ver si tu API cumple con lo que espera la especificación.
Debes ejecutar estas pruebas con cada historia de usuario para verificar
que has completado la funcionalidad.

Las pruebas están incluidas en el directorio `postman`.

Para ejecutar las pruebas, puedes usar
[la extensión de Postman para Visual Studio Code,](https://learning.postman.com/docs/getting-started/basics/about-vs-code-extension/)
e importar el director `postman`.
Pero para ejecutar toda la colección de pruebas simultáneamente (y de forma gratuita),
necesitas instalar [una herramienta de línea de comandos llamada `newman`.](https://learning.postman.com/docs/collections/using-newman-cli/)

Sigue [las instrucciones para instalar `newman`](https://learning.postman.com/docs/collections/using-newman-cli/installing-running-newman/)
globalmente. Luego puedes ejecutar la colección con el entorno incluido así:

```bash
newman run postman/collection.json -e postman/environment.json
```

`postman/collection.json` es una colección para los endpoints del API
sin autenticación.

Si también completas las historias de usuario de autenticación del API,
entonces ejecuta `postman/collection-auth.json` en su lugar.

Mostramos el proceso en [este video de como correr pruebas de Postman](https://youtu.be/SKrSh_jjreQ).

Ambas colecciones se pueden ejecutar contra la base de datos de producción
real, pero puedes considerar crear una base de datos de prueba ya que las
pruebas para los endpoints de `/user` realizan operaciones CRUD y crean y
eliminan un usuario cuyo correo es `newUser@test.com`.

Para el login y los endpoints autenticados, tu base de datos necesita
tener un usuario cuyas credenciales coincidan con las variables
`testUserEmail` y `testUserPassword` de las pruebas del API que se
encuentran en `./postman/environment.json`, cuyos valores son
`admin@test.com` y `test` respectivamente. Recuerda que las contraseñas
están encriptadas, por lo que tu usuario no tendrá `test` como una
contraseña sin cifrar en tu base de datos.

Además de estas pruebas y cualquier prueba unitaria,
puedes considerar escribir pruebas adicionales para probar los datos
devueltos por tu API. Agregar una colección de pruebas adicional
es una opción, o usar una biblioteca como [`supertest` para Node](https://www.npmjs.com/package/supertest)
u otra biblioteca con tu lenguaje de preferencia.

## 8. Pistas, tips y lecturas complementarias

Te proponemos los siguientes pasos para iniciar con el proyecto

### Paso 1. Comprender que es una API REST

En primer lugar, asegúrate de comprender qué es una API REST.
Para esto puedes consultar en internet o preguntarle a
ChatGPT. Habla con una coach en tu proximo Office Hours para confirmar tus aprendizajes.
En particular, te recomendamos ver leer este
[artículo]( https://dev.to/dennysjmarquez/todo-lo-que-necesitas-saber-sobre-api-rest-glosario-de-terminos-esenciales-y-mas-29pc).

### Paso 2. Crear una instancia de PostgreSQL en Vercel

La base de datos recomendada para tu aplicación es PostgreSQL. Te
recomendamos usar [vercel PostgreSQL](https://vercel.com/docs/storage/vercel-postgres)
para que no tengas que instalar PostgreSQL en tu computadora.

Para crear una base de datos PostgreSQL en Vercel usa la
[documentación oficial](https://vercel.com/docs/storage/vercel-postgres/quickstart).
Identifica la siguiente información porque la necesitarás para
conectarte a tu base de datos

* POSTGRES_USER
* POSTGRES_HOST
* POSTGRES_PASSWORD
* POSTGRES_DATABASE

### Paso 3. Conectar la instancia de PostgresSQL usando pgAdmin

Una vez hayas creado una instancia de PostgreSQL en Vercel,
deberás conectarte a ella. Te recomendamos que instales
[pgAdmin](https://www.pgAdmin.org/download/),
un GUI (Graphical User Interface) para interactuar con la base de datos.

Con _pgAdmin_ intenta conectarte a la base de datos
usando la información suministrada por vercel.

### Paso 4. Crear las tablas y cargar la información

En este punto, ya puedes trabajar en la
[Historia de Usuaria 1](#historia-de-usuario-1-cargar-información-a-base-de-datos).
Deberás crear las tablas en tu base de datos y cargar la
información solicitada.
Puedes crear una tabla usando la interfaz gráfica de pgAdmin
o en usando
[SQL](https://www.postgresqltutorial.com/postgresql-create-table/).

### Paso 5. Crear tu primer endpoint

Ya es hora de escribir código. Tu primer objetivo
es crear un proyecto que al ejecutarse cree un
servidor HTTP que responda a la petición GET /taxis
con un "hola mundo".

Te recomendamos usar
[Postman](https://learning.postman.com/docs/getting-started/first-steps/overview/)
para confirmar
que el endpoint que desarrolles responda segun
lo solicitado.

El procedimiento recomendado dependerá del lenguaje de programación
que hayas elegido:

* Si estás usando NodeJS, puedes seguir este
[tutorial](https://hackernoon.com/how-to-setup-a-nodejs-app-with-express-and-typescript)
para crear un servidor HTTP con express y TypeScript
* Si estás usando Java, puedes seguir este
[video de Primer Endpoint con Java](https://youtu.be/-FRu28PvH6Q)
* Si estás usando Python, puedes seguir
[el tutorial _Minimal Application_](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application)
de la documentación oficial de Flask
* Si estás usando C#, puedes seguir
[el tutorial de la  
documantación oficial de C#](https://learn.microsoft.com/es-es/aspnet/core/tutorials/first-web-api?view=aspnetcore-8.0&tabs=visual-studio)

### Paso 6.Conectar la instancia de Postgresql desde código

Luego vas a necesitar elegir un módulo o librería para
interactuar con nuestra base de datos desde el lenguaje
de desarrollo elegido.

La librería recomendada dependerá del lenguaje de programación
que hayas elegido:

* Si estás usando NodeJS, puedes instalar y configurar
[Prisma](https://www.prisma.io/docs/orm/overview/introduction/what-is-prisma)
* Si estás usando Java, puedes instalar y configurar
[Hibernate](https://docs.spring.io/spring-framework/reference/data-access/orm/hibernate.html)
* Si estás usando Python, puedes instalar y configurar
[SqlAlchemy](https://docs.sqlalchemy.org/en/latest/orm/quickstart.html)
* Si estás usando C#, puedes instalar  y configurar
[Npgsql](https://www.npgsql.org/doc/index.html)

### Paso 7. Modificar endpoint para consultar base de datos  

Utiliza la librería elegida para consultar la base de
datos y que tu API responda a la petición GET
/taxis con el listado de taxis tal como se especifica
en [la documentación de API](https://app.swaggerhub.com/apis-docs/ssinuco/FleetManagementAPI/1.0.0#/taxis/getTaxi).

De nuevo, usa [Postman](https://learning.postman.com/docs/getting-started/first-steps/overview/)
para confirmar que el endpoint que desarrolles responda
según lo solicitado.

### Paso 8. Soportar parametros en el endpoint

De acuerdo a la documantación
[documantación](https://app.swaggerhub.com/apis-docs/ssinuco/FleetManagementAPI/1.0.0#/taxis/getTaxi)
el endpoint GET /taxis soporta 3 parametros: `plate`, `page` y `limit`.

Modifica tu código para soportar peticiones a tu endpoint
con estos parámetros. Usa [Postman](https://learning.postman.com/docs/getting-started/first-steps/overview/)
para probar tu endpoint con diferentes valores de estos parámetros.

### Paso 9. Escribir pruebas e2e para el endpoint

Elige un módulo o librería para escribir pruebas e2e de tu endpoint.

La librería recomendada dependerá del lenguaje de programación
que hayas elegido:

* Si estás usando NodeJS, puedes instalar y configurar
[Node-postgres](https://node-postgres.com/)
o
[Prisma](https://www.prisma.io/docs/orm/overview/introduction/what-is-prisma).
Discute una coach cuales son las diferencias entre ambas librerías.
* Si estás usando Java, puede instalar y configurar
* Si estás usando Python, puedes instalar y configurar [pytest](https://docs.pytest.org/en/8.1.x/)
* Si estás usando C#, puedes instalar  y configurar

### Paso 10. Implementar los demás endpoints

¡Felicitaciones! Hasta este punto ya has completado la
Historia de Usuaria 2. Puedes continuar implementado
las demás historias.

## 9. Funcionalidades opcionales

Si completaste todas las funcionalidades del proyecto te invitamos a trabajar en
las [funcionalides opcionales](./docs/extension.md)
