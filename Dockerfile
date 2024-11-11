# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files to the container
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install poetry

# Install the project dependencies
RUN poetry install

# Copy the rest of the application code to the container
COPY main.py ./

VOLUME [ "/data" ]

LABEL org.opencontainers.image.source https://github.com/jcsumlin/plex-listen-brainz-cron

# Command to run the application
CMD ["poetry", "run", "python", "main.py"]