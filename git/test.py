#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
academy/gitの学習の進捗を確認するスクリプト
"""
import cPickle
import types
import importlib
import os
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
        print "=" * 5 + " current mission " + "=" * 5
        print m.desc
        print "=" * 20
    return is_OK


def enter_next_mission():
    current_mission = data['mission']
    next_mission = SCENARIO[current_mission]
    data['mission'] = next_mission
    data['solved'].append(current_mission)
    m = MISSIONS[next_mission]
    print "=" * 5 + " next mission " + "=" * 5
    print m.desc
    print "=" * 20



def load():
    global data
    try:
        data = cPickle.load(file('savedata', 'rb'))
    except:
        data = {'mission': 'clone_from_github',
                'solved': []}


def save():
    cPickle.dump(data, file('savedata', 'wb'))


def main():
    add_missions()
    load()
    is_ok = check_mission_achieved()
    if is_ok:
        enter_next_mission()
    save()


if __name__ == '__main__':
    main()
