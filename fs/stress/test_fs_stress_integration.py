############################################################################
#
# SPDX-License-Identifier: Apache-2.0
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.  The
# ASF licenses this file to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#
############################################################################

import pytest


@pytest.mark.skip("Not Ready for multiple core")
@pytest.mark.dep_config("CONFIG_TESTING_FSTEST")
@pytest.mark.cmd_check("fstest_main")
def test_fs_fstest():
    pytest.sendCommand("mkdir /data/fstest")
    ret = pytest.product.sendCommand(
        "fstest -n 100 -m /data", "Final memory usage", timeout=3600
    )
    pytest.sendCommand("ls -l /data/fstest")
    pytest.sendCommand("rm -rf /data/fstest")
    assert ret == 0
