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

"""SCARA Robot demo controller."""

from robodyno.interfaces import Webots
from robodyno.components import SliderModule, Motor

webots = Webots()

webots.sleep(1)

actuators = []

actuators.append(SliderModule(webots, 0x10))
for motor_id in range(0x11, 0x14):
    m = Motor(webots, motor_id)
    m.position_filter_mode(8)
    actuators.append(m)

for _actuator in actuators:
    _actuator.enable()


def set_robot_joint_pos(*pos) -> None:
    """Sets robot joint positions."""
    for i, actuator in enumerate(actuators):
        actuator.set_pos(pos[i])


def get_robot_joint_pos() -> list:
    """Gets robot joint positions."""
    actuator_pos = []
    for actuator in actuators:
        actuator_pos.append(actuator.get_pos())
    return actuator_pos


set_robot_joint_pos(-0.08, 0.7, 0.7, 0.7)
webots.sleep(8)
print(get_robot_joint_pos())

set_robot_joint_pos(0, 0, 0, 0)
webots.sleep(8)
