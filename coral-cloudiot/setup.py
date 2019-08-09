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
    name='coral-cloudiot',
    version='1.0',
    description='Coral Cloud IoT API',
    author='Coral Team',
    author_email='coral-support@google.com',
    url="https://coral.withgoogle.com/",
    license='Apache 2',
    packages=['coral.cloudiot'],
    install_requires=[
        'jwt',
        'paho-mqtt',
        'cryptoauthlib',
    ],
    python_requires='>=3.5.3',
)
