### Environment variables

Copy the `.env.example` file values and paste it into a new `.env` file under the project root

### Setup

- `poetry install` - got to have `poetry` installed globally

### Development server

Starting the development server

```bash
export FLASK_APP=app:create_app
poetry run flask run --reload
```

### Database migrations

We use `flask-migrate` to manage our database migrations. Built on top of `alembic`.

- Use `flask db init` to initialize(if not already done)
- Use `flask db migrate -m <migration_name>` to create a migration
- Use `flask db upgrade` to run the up query
- Use `flask db downgrade` to run the down query
