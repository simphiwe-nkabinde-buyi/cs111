from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("T", "Oct") == "Oct; T"
    assert make_full_name("Augustus", "Henry-Peterson") == "Henry-Peterson; Augustus"
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Oct; T") == "Oct"
    assert extract_family_name("Henry-Peterson; Augustus") == "Henry-Peterson"
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Oct; T") == "T"
    assert extract_given_name("Henry-Peterson; Augustus") == "Augustus"
    assert extract_given_name("; ") == ""

pytest.main(["-v", "--tb=line", "-rN", __file__])