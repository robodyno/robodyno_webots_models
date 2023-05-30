# -*-coding:utf-8 -*-
#
# Apache License
# Version 2.0, January 2004
#
# Copyright (c) 2023 Robottime(Beijing) Technology Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Motor demo controller."""

from robodyno.components import Motor
from robodyno.interfaces import Webots

webots = Webots()
motor = Motor(webots, 0x10)

motor.position_track_mode(5, 2, 2)
motor.enable()
motor.set_pos(31.4)

while True:
    print(f'pos: {motor.get_pos():.2f}, vel: {motor.get_vel():.2f}')
    if webots.sleep(0.5) == -1:
        break
