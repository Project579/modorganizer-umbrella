# Copyright (C) 2015 Sebastian Herbord.  All rights reserved.
# Copyright (C) 2016 - 2018 Mod Organizer contributors.
#
# This file is part of Mod Organizer.
#
# Mod Organizer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mod Organizer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mod Organizer.  If not, see <http://www.gnu.org/licenses/>.
import os


class ProgressFile:
    def __init__(self, filename, progress_cb):
        self.f = open(filename, "rb")

        assert callable(progress_cb)
        self.__progress_cb = progress_cb
        self.f.seek(0, os.SEEK_END)
        self.__size = self.f.tell()
        self.f.seek(0, os.SEEK_SET)

    def read(self, *args, **kwargs):
        self.__progress_cb(self.f.tell(), self.__size)

        return self.f.read(*args, **kwargs)
