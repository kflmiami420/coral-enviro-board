# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

setup(
    name='coral-enviro',
    version='1.0',
    description='API and Demo Application for Coral Environmental Sensor Board',
    author='Coral Team',
    author_email='coral-support@google.com',
    url="https://coral.withgoogle.com/",
    license='Apache 2',
    packages=['coral.enviro'],
    include_package_data=True,
    install_requires=[
        'luma.oled>=2.3.2',
        'spidev',
        'coral-cloudiot',
    ],
    python_requires='>=3.5.3',
)
