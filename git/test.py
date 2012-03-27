#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
academy/gitの学習の進捗を確認するスクリプト
"""
import cPickle
import types
import importlib
import os

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
    m = MISSIONS.get(data['mission'])
    if not m:
        raise RuntimeError(
            "active mission name '%s'in savedata is not found in missions"
            % data['mission'])
    is_OK = m.goal()
    if is_OK:
        print "OK"
    else:
        print "NG"
        print m.desc
    return is_OK


SCENARIO = {
    'clone_from_github': 'git_status',
    'git_status': 'make_gitignore',
    'make_gitignore': 'sentinel',
}


def enter_next_mission():
    next_mission = SCENARIO[data['mission']]
    data['mission'] = next_mission
    m = MISSIONS[next_mission]
    print m.desc


def load():
    global data
    try:
        data = cPickle.load(file('savedata', 'rb'))
    except:
        data = {'mission': 'clone_from_github'}


def save():
    cPickle.dump(data, file('savedata', 'wb'))


if __name__ == '__main__':
    add_missions()
    load()
    is_ok = check_mission_achieved()
    if is_ok:
        enter_next_mission()
    save()
