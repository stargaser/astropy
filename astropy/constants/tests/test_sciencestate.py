import pytest
import subprocess
import sys
import tempfile

from astropy import physical_constants, astronomical_constants
import astropy.constants as const


def test_version_match():
    pversion = physical_constants.get()
    refpversion = const.h.__class__.__name__.lower()
    assert pversion == refpversion
    aversion = astronomical_constants.get()
    refaversion = const.M_sun.__class__.__name__.lower()
    assert aversion == refaversion


def test_previously_imported():
    with pytest.raises(RuntimeError):
        physical_constants.set('codata2018')

    with pytest.raises(RuntimeError):
        astronomical_constants.set('iau2015')


def test_new_session():
    teststr = """
import astropy
astropy.physical_constants.set('codata2014')
import astropy.constants as const
import astropy.units as u
assert abs((const.M_sun / u.M_sun).to(u.dimensionless_unscaled) - 1) < 1.e-14
assert const.M_sun.reference[-11:] == 'CODATA 2014'
    """

    with tempfile.NamedTemporaryFile() as fd:
        fd.write(teststr.encode())
        fd.seek(0)
        result = subprocess.run([sys.executable, fd.name])
        assert result.returncode == 0

    newstr = teststr.replace('CODATA 2014', 'CODATA 2012')

    with tempfile.NamedTemporaryFile() as fd:
        fd.write(newstr.encode())
        fd.seek(0)
        result = subprocess.run([sys.executable, fd.name])
        assert result.returncode == 1
