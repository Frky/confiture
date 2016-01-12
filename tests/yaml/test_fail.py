# -*- coding: utf-8 -*-

import pytest
from confiture import Confiture, ConfigFileError

def test_template_not_found():
    with pytest.raises(ConfigFileError):
        Confiture('tests/yaml/template/404.yaml')

def test_config_not_found():
    confiture = Confiture('tests/yaml/template/simple.yaml')
    with pytest.raises(ConfigFileError):
        confiture.check('tests/yaml/config/404.yaml')

def test_missing_simple_field():
    confiture = Confiture('tests/yaml/template/simple.yaml')
    with pytest.raises(ConfigFileError):
        confiture.check('tests/yaml/config/simple_fail.yaml')

def test_missing_nested_field():
    confiture = Confiture('tests/yaml/template/nested.yaml')
    with pytest.raises(ConfigFileError):
        confiture.check('tests/yaml/config/simple_fail.yaml')
