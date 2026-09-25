import pytest

from toolkit.converter import conv
from toolkit.errors import ToolkitError

##from typer.testing import CliRunner
##from toolkit.__main__ import app

def test_kg_g():
    assert conv(10,"kg","g") == 10000.0


def test_g_kg():
    assert conv(200,"g","kg") == 0.2


def test_mm_m():
    assert conv(10000,"mm","m") == 10.0


def test_mm_cm():
    assert conv(190,"mm","cm") == 19


def test_mm_km():
    assert conv(190000,"mm","km") == 0.19


def test_m_cm():
    assert conv(2.5,"m","cm") == 250.0


def test_km_cm():
    assert conv(1.75,"km","cm") == 175000.0


def test_km_m():
    assert conv(12,"km","m") == 12000.0


def test_c_k():
    assert conv(27,"c","k") == 300.15


def test_c_f():
    assert conv(10,"c","f") == 50.0


def test_k_f():
    assert conv(273.15,"k","f") == 32.0


def test_incompatible_units():
    with pytest.raises(ToolkitError):
        conv(100,"mm","kg")


def test_temperature_below_absolute_zero():
    with pytest.raises(ToolkitError):
        conv(-300,"k","f")


def test_negative_weight():
    with pytest.raises(ToolkitError):
        conv(-23,"kg","g")


def test_negative_length():
    with pytest.raises(ToolkitError):
        conv(-20,"km","m")





##runner = CliRunner()

##def test_cli_conv_success():
    ##result = runner.invoke(app,["conv","390","cm","m"])
    ##assert result.exit_code == 0
    ##assert result.stderr == ""
    ##assert result.stdout.strip() == 3.9
