# -*- coding: utf-8 -*-

import pytest
from confiture import Confiture, ConfigFileError

def test_unsafe_loading_config():
    confiture = Confiture('tests/yaml/template/empty.yaml')
    with pytest.raises(ConfigFileError):
        confiture.check('tests/yaml/security/unsafe_loading.yaml')
