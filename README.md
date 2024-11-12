# Plex ListenBrainz Cron

Plex ListenBrainz Cron is a service that monitors your Plex server and ListenBrainz account, and sends notifications to a Gotify server. It helps you keep track of your media consumption and receive timely updates.

## Features

- Monitor Plex server activity
- Track listens on ListenBrainz
- Send notifications to Gotify

## Requirements

- Python 3.12 or higher
- Poetry for dependency management

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/jcsumlin/plex-listen-brainz-cron.git
   cd plex-listen-brainz-cron
   ```

2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

## Configuration

### Environment Variables

Create a `.env` file in the root directory of the project by copying the provided `.env.example` file:

```sh
cp .env.example .env
```

Fill in the values in the `.env` file with your own credentials:

```env
LISTENBRAINZ_TOKEN=your_listenbrainz_token
TAUTULLI_API_KEY=your_tautulli_api_key
TAUTULLI_URL=your_tautulli_url
GOTIFY_URL=your_gotify_url
GOTIFY_APP_TOKEN=your_gotify_app_token
PLEX_USER=your_plex_user
```

### Running the Application

To run the application, use the following command:

```sh
poetry run python main.py
```

## Docker

You can also run the application using Docker. Build the Docker image and run the container:

```sh
docker build -t <image_name> .
docker run --env-file .env <image_name>
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.
