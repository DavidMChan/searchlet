# Copyright (c) 2018 David Chan
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pytest
import os

from .Environment import Action, ReverseAction, State, Environment, WeightedEnvironment  # noqa: F401

def test():
    print(os.path.join(*(__file__.split('__init__.py'))))
    pytest.main([os.path.join(*(__file__.split('__init__.py')))])