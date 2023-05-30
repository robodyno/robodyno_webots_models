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

"""Collaborative Robot demo controller."""

from robodyno.interfaces import Webots
from robodyno.components import Motor

webots = Webots()

webots.sleep(1)

motors = []
for motor_id in range(0x10, 0x16):
    _motor = Motor(webots, motor_id)
    _motor.position_filter_mode(8)
    motors.append(_motor)

for _motor in motors:
    _motor.enable()


def set_robot_joint_pos(*pos) -> None:
    """Sets robot joint positions."""
    for i, motor in enumerate(motors):
        motor.set_pos(pos[i])


def get_robot_joint_pos() -> list:
    """Gets robot joint positions."""
    motor_pos = []
    for motor in motors:
        motor_pos.append(motor.get_pos())
    return motor_pos


set_robot_joint_pos(1.57, 0.28, -1.23, 0.5, -0.8, 0.7)
webots.sleep(2)
print(get_robot_joint_pos())
