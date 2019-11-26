# PostGreSQL JSONB demo, with SQLAlchemy

This is a toy project that goes along with [presentation.pdf](presentation.pdf)

Start with:

```bash
mkvirtualenv jsonbdemo
pip install -r requirements.txt
cp example_conf.ini conf.ini
```

Then create an empty database in Postgres, edit `conf.ini` and set-up the schema with:

```bash
PYTHONPATH='.' alembic -c conf.ini upgrade head
```

Alembic migrations (in ``alembic_migrations/versions``) follow the schema
enhancements in the slides' order.

If you modify model classes, you may create an alembic migration with
`PYTHONPATH='.' alembic -c conf.ini revision --autogenerate -m "<revision name>"`
