import pytest

from app import create_app


@pytest.fixture
def client(tmp_path):
    """Client dengan database SQLite sementara, terisolasi per tes."""
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "tes.db")})
    return app.test_client()
