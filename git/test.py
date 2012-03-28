#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
academy/gitの学習の進捗を確認するスクリプト
"""
import cPickle
import types
import importlib
import os
import argparse
from scenario import SCENARIO

MISSIONS = {}

def add_missions():
    for f in os.listdir('missions'):
        if not f.endswith('.py'): continue
        if f == '__init__.py': continue
        modname = '.' + f[:-3] # 'foo.py' -> '.foo'
        m = importlib.import_module(modname, 'missions')
        assert hasattr(m, 'name') and isinstance(m.name, str)
        assert hasattr(m, 'desc') and isinstance(m.desc, unicode)
        assert hasattr(m, 'goal') and isinstance(m.goal, types.FunctionType)
        if hasattr(m, 'on_enter'):
            assert isinstance(m.on_enter, types.FunctionType)
        if hasattr(m, 'on_exit'):
            assert isinstance(m.on_exit, types.FunctionType)

        MISSIONS[m.name] = m


def check_mission_achieved():
    current_mission = data['mission']
    m = MISSIONS.get(current_mission)
    if not m:
        raise RuntimeError(
            "active mission name '%s'in savedata is not found in missions"
            % current_mission)
    is_OK = m.goal()
    if is_OK:
        print "OK", current_mission, "CLEAR!!"
    else:
        print "NG"
        print_mission_desc('current mission', m)
    return is_OK


def print_mission_desc(title, mission):
    header =  "=" * 5 + " %s: %s " % (title, mission.name) + "=" * 5
    print header
    print mission.desc
    print "=" * len(header)


def enter_next_mission():
    current_mission = data['mission']
    next_mission = SCENARIO[current_mission]
    data['solved'].append(current_mission)
    enter_to(next_mission)


def enter_to(mission_name):
    assert isinstance(mission_name, str)
    data['mission'] = mission_name
    m = MISSIONS[mission_name]
    print_mission_desc('next mission', m)
    if hasattr(m, "on_enter"):
        m.on_enter()


def load():
    global data
    try:
        data = cPickle.load(file('savedata', 'rb'))
    except:
        data = {'mission': 'clone_from_github',
                'solved': []}


def save():
    cPickle.dump(data, file('savedata', 'wb'))


def parse_args():
    parser = argparse.ArgumentParser(description='Check whether mission cleared or not.')
    parser.add_argument('--enter', dest='enter_mission', action='store',
                        metavar='mission',
                        help='enter to a mission (for debug)')

    args = parser.parse_args()
    return args


def main():
    add_missions()
    load()
    args = parse_args()
    if args.enter_mission:
        enter_to(args.enter_mission)
    else:
        is_ok = check_mission_achieved()
        if is_ok:
            enter_next_mission()
    save()


if __name__ == '__main__':
    main()
