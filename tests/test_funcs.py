import pytest
from coursework3.funcs import correct_data, json_to_list


def test_json_to_list():
     with pytest.raises(FileNotFoundError):
         test_json_to_list('egewgerg/elef.txt')