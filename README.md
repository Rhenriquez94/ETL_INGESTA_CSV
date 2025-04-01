# 🛠️ Proyecto ETL - Ingesta de Stack Overflow

Este proyecto implementa un pipeline ETL completo usando Python, Pandas y Docker. Se ingestan datos de Stack Overflow (`Questions.csv`, `Answers.csv`, `Tags.csv`), se transforman y se cargan a una base de datos PostgreSQL.

---

## 📁 Estructura del Proyecto

```
├── data/                  # CSVs de origen (ignorado por Git)
├── db/
│   └── connection.py      # Conexión a PostgreSQL (usando .env)
├── scripts/
│   ├── extract.py         # Lectura de archivos CSV
│   ├── transform.py       # Limpieza y transformación
│   └── load.py            # Carga a PostgreSQL
├── main.py                # Orquestador principal del ETL
├── .env                   # Configuración de entorno (no subir a Git)
├── Dockerfile             # Contenedor para ejecutar el ETL
├── docker-compose.yml     # Orquestación del ETL + PostgreSQL
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación general
```

---

## ⚙️ Configuración

### 1. `.env` con variables de conexión

```
DB_USER=pwd
DB_PASSWORD=pwd
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ingesta_csv
CHUNKSIZE=300000
```

### 2. Instalar dependencias (modo local)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🐳 Uso con Docker

### 1. Construir la imagen
```bash
docker-compose build
```

### 2. Ejecutar todo el pipeline ETL
```bash
docker-compose up
```

---

## 🧪 Flujo ETL

1. **Extract:** lee y limpia los CSV
2. **Transform:** convierte fechas, limpia HTML, calcula promedios por usuario/año
3. **Load:** inserta los datos en PostgreSQL usando SQLAlchemy por `chunks`

---

## 📦 Tablas generadas
- `questions`
- `answers`
- `tags`

---

## ✅ Mejores prácticas aplicadas
- Modularización (`extract`, `transform`, `load`)
- Logging
- `.env` con configuración desacoplada
- `.gitignore` con protección de datos sensibles y archivos grandes
- Docker para portabilidad total

---

## ✍️ Autor
**Rodrigo Henriquez**

---

> ℹ️ Nota: los archivos CSV no están incluidos en este repositorio debido a su tamaño (>100 MB).