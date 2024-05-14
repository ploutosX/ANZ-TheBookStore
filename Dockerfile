FROM python:3.11-slim as base

WORKDIR /app

RUN apt-get update

# libpq-dev needed for psycopg2 compilation to avoid the error: pg_config executable not found.
# uncomment the following line if your service uses PostgreSQL
RUN apt-get install -y libpq-dev

# ---------------------------- Builder stage ---------------------------- #
FROM base as builder

# gcc compiles pscopg2. Error: 'gcc' failed: No such file or directory
RUN apt-get install -y gcc

# poetry 1.2 generated lock files are not compatible with poetry 1.1
ARG PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.7

RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN ./venv/bin/activate && poetry install --only main --no-root

# ---------------------------- Final stage ------------------------------ #
FROM base as final

# clean files created from apt-get update
RUN apt-get clean

COPY --from=builder /venv /venv

ENV PORT=8080
ENV APP_MODULE=app.server:api
ENTRYPOINT ["sh", "-c", "/venv/bin/python -m uvicorn $APP_MODULE --host 0.0.0.0 --port $PORT"]

ARG COMMIT_SHA
ENV COMMIT_SHA=$COMMIT_SHA

COPY . .

ARG APP_VERSION
ENV APP_VERSION=$APP_VERSION

ARG TIMESTAMP=1
ENV TIMESTAMP=$TIMESTAMP

ENV PYTHONUNBUFFERED=1

