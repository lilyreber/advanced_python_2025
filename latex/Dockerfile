FROM python:3.10

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive-latex-base

WORKDIR /app

COPY pyproject.toml README.md ./

RUN pip install latex-generator-lilyreber

COPY latex_generator/ ./latex_generator/
COPY main.py ./
COPY cat.png ./

CMD ["python", "main.py"]