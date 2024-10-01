# MiniGrid Sizing Tool
> A quick lil' utility.

A simulator and optimizer for Solar Mini Grids.

## Table of Contents
1. [Getting Started](#getting-started)
    * [Setting up the Backend](#setting-up-the-backend)
    * [Setting Up The Frontend](#setting-up-the-frontend)

### Getting Started
---

#### Setting Up The Backend

To bootstrap the app, start changing directories to the `backend`.
```
cd backend
```

Spin up a Python virtual environment.

```
python -m venv .venv
```

Then activate the environment.

```
. .venv/bin/activate
```

Then run the Python server.

```
flask --app main run
```

#### Setting Up The Frontend

To run the frontend, change directories to the `frontend`.
```
cd frontend
```

Run the frontend development server
```
npm run start
```

🎉