# -*- coding: utf-8 -*-

from confiture import Confiture

def test_empty():
    confiture = Confiture('tests/yaml/template/empty.yaml')
    confiture.check('tests/yaml/config/empty_valid.yaml')
    confiture.check('tests/yaml/config/simple_valid.yaml')

def test_simple():
    confiture = Confiture('tests/yaml/template/simple.yaml')
    confiture.check('tests/yaml/config/simple_valid.yaml')

def test_nested():
    confiture = Confiture('tests/yaml/template/nested.yaml')
    confiture.check('tests/yaml/config/nested_valid.yaml')

def test_travis_configuration():
    confiture = Confiture('tests/yaml/template/travis.yaml')
    confiture.check('.travis.yml')

