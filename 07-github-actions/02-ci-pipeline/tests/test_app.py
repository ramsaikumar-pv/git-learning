from app import health_check, start_server, get_config


def test_health_check_returns_ok():
    result = health_check()
    assert result["status"] == "ok"


def test_health_check_has_version():
    result = health_check()
    assert "version" in result


def test_start_server_returns_true():
    result = start_server()
    assert result is True


def test_get_config_has_required_keys():
    config = get_config()
    assert "debug" in config
    assert "timeout" in config
