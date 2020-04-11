#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © Nekoka.tt 2019-2020
#
# This file is part of Hikari.
#
# Hikari is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hikari is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along ith Hikari. If not, see <https://www.gnu.org/licenses/>.
from hikari.internal import urls


def test_generate_cdn_url():
    url = urls.generate_cdn_url("not", "a", "path", fmt="neko", size=42)
    assert url == "https://cdn.discordapp.com/not/a/path.neko?size=42"


def test_generate_cdn_url_with_size_set_to_none():
    url = urls.generate_cdn_url("not", "a", "path", fmt="neko", size=None)
    assert url == "https://cdn.discordapp.com/not/a/path.neko"
