FROM python:3.11
WORKDIR /code
COPY pyproject.toml .
RUN pip install --upgrade pip
RUN pip install --upgrade poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
COPY . .
