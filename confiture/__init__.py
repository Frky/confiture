# -*- coding: utf-8 -*-

import yaml


class ConfigFileError(Exception):
    def __init__(self, message):
        self.message = message
        super(ConfigFileError, self).__init__(message)


class Confiture(object):

    def __init__(self, tpl_file=None):
        self._tpl_file = tpl_file
        self.__tpl = None
        self.__parse()
        self.config = None

    @property
    def tpl_file(self):
        return self._tpl_file

    @tpl_file.setter
    def tpl_file(self, path):
        self._tpl_file = path
        self.__parse()

    def __parse(self):
        try:
            with open(self._tpl_file, 'r') as ymlfile:
                self.__tpl = yaml.safe_load(ymlfile)
            # In case the parsed file was empty
            if self.__tpl is None:
                self.__tpl = dict()
        except (IOError, yaml.error.YAMLError):
            raise ConfigFileError("File \"{0}\" not found -- aborting".format(self._tpl_file))

    def __check_required_fields(self, tpl, config):
        for section in tpl.keys():
            if config is None or section not in config.keys():
                raise ConfigFileError("\"{0}\" field not found -- aborting".format(section))
            field = tpl[section]
            if isinstance(field, dict):
                self.__check_required_fields(field, config[section])

    def check(self, config_path):
        if self.__tpl is None:
            raise ConfigFileError("You must load a template file first -- aborting")
        try:
            with open(config_path, 'r') as ymlfile:
                self.config = yaml.safe_load(ymlfile)
        except (IOError, yaml.error.YAMLError):
            raise ConfigFileError("File \"{0}\" not found -- aborting".format(config_path))
        self.__check_required_fields(self.__tpl, self.config)

    def check_and_get(self, config_path):
        self.check(config_path)
        return self.config
