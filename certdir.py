#!/usr/bin/env python
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

""" Scans a directory for .certspec files and creates a corresponding PEM
encoded certificate for each certspec file found."""

import argparse
import os
import pycert

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create test certificates')
    parser.add_argument('path', type=str, help='a path containing some certspec files')

    args = parser.parse_args()
    path = args.path
    suffix = ".certspec"
    for f in filter(lambda name: name.lower().endswith(suffix), os.listdir(path)):
        (name, base_name) = f, f[:-len(suffix)]
        #TODO: Add a check for existing files and an option on whether to overwrite
        pem = open(os.path.join(path, base_name),'w')
        pycert.main(output= pem, inputPath= os.path.join(path, name))
        pem.flush()
        pem.close()
