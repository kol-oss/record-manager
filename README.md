# Record Manager

Simple app to demonstrate ability to work with next technologies:
* Python 3
* Flask
* Docker & docker-compose
* Postman

## Installation

To run this project locally follow next steps:

1. Clone the repository to your machine:

`git clone https://github.com/kol-oss/record-manager.git`

2. Install containerization tools:

**For Linux:**
* Docker: https://docs.docker.com/engine/install/
* docker-compose: https://docs.docker.com/compose/install/

**For Windows:**
* Docker Desktop: https://docs.docker.com/desktop/install/windows-install/

## Usage

### Raw Docker

To create image and run container by yourself via Docker follow next commands:

```shell
docker build . -t records:latest
docker run -it --rm --network=host -e PORT=8080 records:latest
```

Now you can visit http://localhost:8080/ and check if app is up.

### Docker-compose

If you want to use docker-compose tool to automize container creation, follow next steps:

```shell
docker-compose build
docker-compose up
```

### Deployed

You can also check the current version of repository on the remote deployed page via https://healthcheck-8g8l.onrender.com/.

If you want to test it, you can work with Postman via:
* [Workspace](https://web.postman.co/workspace/My-Workspace~c61d5642-b08b-4050-8c08-a49e84c2fa60/flow/6727a5fcad03151df9e0ae93)
* [Workflow](https://web.postman.co/workspace/c61d5642-b08b-4050-8c08-a49e84c2fa60/flow/6727a5fcad03151df9e0ae93)

