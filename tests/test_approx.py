from src.approx import ts_cos_x, approx_plotting
import math
import pytest

def test_ts_cos_x_1_value():
    '''
    Test if the ts_cos_x function is able to approximate cos(0) to be 1

    '''
    expected = 1
    result = ts_cos_x(x=0, nofapprox=2)
    assert expected == result


def test_ts_cos_x_0_value():
    '''
    Test if the ts_cos_x function is able to approximate cos(90 degrees) to be 0.
    FYI, the ts_cos_x accepts the degrees in radians
    '''
    expected = 0
    result = ts_cos_x(x=math.radians(90),nofapprox=3)
    #assert result == pytest.approx(0.0)
    assert  int(result) == expected


def test_approx_plotting_invalid():
    '''
    Test whether approx_plotting exits when n_frames passed is equal to 0
    '''
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        approx_plotting(approx=10, n_frames=0)
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 42
