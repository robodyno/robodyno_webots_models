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

"""Cartesian Robot demo controller."""

from robodyno.interfaces import Webots
from robodyno.components import SliderModule

webots = Webots()

webots.sleep(1)

sliders = []
for slider_id in range(0x10, 0x13):
    sliders.append(SliderModule(webots, slider_id))

for _slider in sliders:
    _slider.enable()


def set_robot_slider_pos(*pos) -> None:
    """Sets robot slider positions."""
    for i, slider in enumerate(sliders):
        slider.set_pos(pos[i])


def get_robot_slider_pos() -> list:
    """Gets robot slider positions."""
    slider_pos = []
    for slider in sliders:
        slider_pos.append(slider.get_pos())
    return slider_pos


set_robot_slider_pos(0.07, -0.1, -0.05)
webots.sleep(8)
print(get_robot_slider_pos())

set_robot_slider_pos(0, 0, 0)
webots.sleep(8)
