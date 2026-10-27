
import configparser

import pytest

from src.config import ConfigurationError, load_config


def test_load_config_success(monkeypatch):
    monkeypatch.setenv("MYSQL_PASSWORD", "test_password")

    config = load_config()

    assert config["host"] == "localhost"
    assert config["port"] == 3306
    assert config["database"] == "employees"
    assert config["user"] == "root"
    assert config["password"] == "test_password"
    assert config["batch_size"] == 1000


def test_missing_password(monkeypatch):
    monkeypatch.delenv("MYSQL_PASSWORD", raising=False)

    with pytest.raises(ConfigurationError, match="MYSQL_PASSWORD"):
        load_config()


def test_invalid_batch_size(monkeypatch, tmp_path):
    config_file = tmp_path / "config.ini"
    config_file.write_text(
        "[database]\n"
        "host = localhost\n"
        "port = 3306\n"
        "database = employees\n"
        "user = root\n"
        "\n"
        "[processing]\n"
        "batch_size = 0\n",
        encoding="utf-8",
    )

    monkeypatch.setenv("MYSQL_PASSWORD", "test_password")

    import src.config as config_module

    monkeypatch.setattr(
        config_module,
        "__file__",
        str(tmp_path / "src" / "config.py"),
    )
    (tmp_path / "src").mkdir(exist_ok=True)

    with pytest.raises(ConfigurationError, match="Batch size"):
        load_config()
