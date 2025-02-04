import pytest
from sqlalchemy.orm import scoped_session, sessionmaker
from app import create_app
from app.core.database import db as _db
from app.core.config import TestConfig

@pytest.fixture(scope='session')
def app():
    """Cria uma instância do app Flask configurada para testes."""
    app = create_app()
    app.config.from_object(TestConfig)

    with app.app_context():
        _db.create_all()
    
    yield app

    with app.app_context():
        _db.drop_all()  # Remove tabelas após os testes

@pytest.fixture(scope='session')
def db(app):
    """Fornece o banco de dados para os testes."""
    return _db

@pytest.fixture(scope='function')
def client(app):
    """Fornece um cliente de teste para a API Flask."""
    return app.test_client()

@pytest.fixture(scope='function')
def session(db, app):
    """Cria uma sessão isolada para cada teste."""
    with app.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()  # Inicia transação
        session_factory = scoped_session(sessionmaker(bind=connection))
        
        test_session = session_factory()
        test_session.begin_nested()  # Cria uma transação aninhada

        yield test_session  # Fornece a sessão para os testes

        test_session.rollback()  # Rollback no final de cada teste
        test_session.close()  # Fecha a sessão
        transaction.rollback()  # Reverte a transação principal
        connection.close()  # Fecha a conexão
        session_factory.remove()  # Remove a sessão escopada