import pytest
from sqlalchemy.orm import scoped_session, sessionmaker
from app import create_app
from app.core.database import db as _db
from app.core.config import TestConfig


@pytest.fixture(scope='session')
def app():
    """Creates a Flask test app with test configuration."""
    app = create_app()
    app.config.from_object(TestConfig)
    with app.app_context():
        _db.create_all()
    yield app
    with app.app_context():
        _db.drop_all()


@pytest.fixture(scope='session')
def db(app):
    """Provides a database session for tests."""
    return _db


@pytest.fixture(scope='function', autouse=True)
def session(db, app):
    """Creates a new session for a test and ensures rollback."""
    with app.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()
        session_factory = scoped_session(sessionmaker(bind=connection))
        db.session = session_factory
        yield session_factory
        session_factory.remove()
        transaction.rollback()
        connection.close()


@pytest.fixture(scope='function')
def client(app):
    """Provides a test client."""
    return app.test_client()
