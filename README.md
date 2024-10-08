# MiniGrid Sizing Tool
> A quick lil' utility.

A simulator and optimizer for Solar Mini Grids.

## Table of Contents
1. [Getting Started](#getting-started)

### Getting Started
---

#### Setting Up The Backend

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
flask --app app run
```
or

```
gunicorn app:app
```