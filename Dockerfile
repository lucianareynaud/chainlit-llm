# Versão leve do Python
FROM python:3.10-slim

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Instala dependências básicas
RUN apt-get update && apt-get install -y \
    build-essential curl && \
    pip install --upgrade pip

# Copia o requirements.txt e instala
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia o restante do app
COPY . .

# Expõe a porta padrão do Chainlit
EXPOSE 8000

# Comando default
CMD ["chainlit", "run", "app.py", "--host", "0.0.0.0"]
