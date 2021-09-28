# meli-challenge

El objetivo de este challenge es resolver un desafío que involucra y aglomera muchas
de las tecnologías que solemos usar en el día a día en el equipo de Monitoreo de
Seguridad Informática.

### ⚒ Quickstart
primero se debe de configurar el archivo .env para la coneccion hacia la base de datos **Mongodb**

#### esquema
| ip | pais | distancia | invocaciones |
|----|------|-----------|--------------|
| 210.22.11.1 | china | 18510 | 1 |
| 110.22.11.1 | australia | 13270 | 2 |

### 📡 API's
* **/api/8.8.8.8**
---
``` json
{
    "ip": "8.8.8.8",
    "fecha_actual": "28/09/2021 01:57:44 GMT",
    "pais": "united states",
    "iso_code": "us",
    "distancia_estimada": "9328 km",
    "pertenece_a_aws": false
}
```
Verifica el pais de donde pertenece la ip, a cuanta distancia esta de buenos aires y si pertenece ah aws

* **/closeDistance/**
---
``` json
{
    "ip": "8.8.8.8",
    "pais": "united states",
    "distancia_estimada": "9328 km",
    "invocaciones": 8,
}
```
Extrae el pais mas sercano ah Buenos Aires

* **/farDistance/**
---
``` json
{
    "ip": "210.22.11.1",
    "pais": "china",
    "distancia_estimada": "18510 km",
    "invocaciones": 1,
}
```
Extrae el pais mas lejano ah Buenos Aires

* **/avgDistance/**
---
``` json
{
    "country": "china",
    "avg_position": 1
}
```
Realiza un avegrage de las invocaciones