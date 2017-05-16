# coding: utf-8

#     Copyright 2017, Novak Boškov, mailto:gnovak.boskov@gmail.com
#
#     Part of "Nuitka", an optimizing Python compiler that is compatible and
#     integrates with CPython, but also works on its own.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#

""" Additional tools aimed to help newcomers explore Nuitka.

"""

import logging

def log_compare(**kwargs):
    """ This is aimed to be applied as decorator to
        compare_with_cpython.compareOutput.

    """
    try:
        filename = kwargs['filename']
    except:
        raise Exception("filename should be supplied as keyword argument")

    def decorator(compareOutput):
        def wrapper(*args, **kwargs):
            logging.basicConfig(filename=filename, level=logging.DEBUG)
            logging.debug("Nuitka:\n" + args[1])
            logging.debug("Cpython:\n " + args[2])
            compareOutput(*args, **kwargs)
        return wrapper

    return decorator
