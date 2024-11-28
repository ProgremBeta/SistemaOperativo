FROM python:3.9-slim

# Instalar las dependencias del sistema necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    libmariadb-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r Requerimientos.txt

# Comando de inicio
CMD ["python", "index.py"]
