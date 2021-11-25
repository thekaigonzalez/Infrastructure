# Copyright (C) 2021 Kai D. Gonzalez
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

TAB1 = '\t'
TAB2 = '    '

def return_infraDict(string):
    dic = {}

    buf = ""

    dt = ""

    decl = ""

    lvl = 0

    state = 0
    for i in range(len(string)):
        if string[i] == ' ' and state == 0:
            dt = buf
            state = 1
            buf = ""
        elif string[i] == '-' and state == 1:
            decl = buf
            buf = ""
            state = 2

            buf = ""

        elif string[i] == '>' and state == 2:
            state = 3
            # print("moving")
            dic[lvl] = {}
            dic[lvl]["declaration"] = decl
            dic[lvl]['type'] = dt
            dic[lvl]['body'] = ''

            decl = ""
            dt = ""

            # print("happened " + buf)

            buf = ""
        elif string[i] == '.' and state == 5:
            lvl += 1
            state = 0;
            buf = ""
            dt = ""
            decl = ""
            print("move")
        elif string[i] == TAB1 and state == 3 or state == 4:
            # print("yes")
            state = 5
        # elif string[i] == '\n' and state == 5:
        #     print("body " + buf)
    
        #     dic[lvl]['body'] += buf + "\n"

        #     buf = ""
        # elif string[i] == '\n' and state == 3:
        #     state = 0
        #     lvl += 1
        #     print("switch")
        #     buf = "";
        else:
            print("adding '" + string[i] + "'")
            buf += string[i]
            print(buf)
    # print(buf + " : ")
    if len(buf) > 0 and state == 5:
        # print("hrllo")
        dic[lvl]['body'] = buf

        buf = ""

    
    return dic
# filestr = """

# #include <stdio.h>
# #include <stdint.h>

# // generated

# """
# # with open(sys.argv[1]) as f:
# #     for i in f.readlines():
# #         di = return_infraDict(i)

# #         print(di)
# #         for item in di:
# #             filestr += di[item]['type'] + " " + di[item]['declaration'].strip() + " " + "{" + di[item]['body'] + "}"
# #         print(filestr)