#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
academy/gitの学習の進捗を確認するスクリプト
"""
import cPickle
import types
from collections import namedtuple
Mission = namedtuple('Mission', ['name', 'desc', 'goal', 'exit_msg'])

MISSIONS = {}

def _add_mission(name, desc, goal, exit_msg):
    assert isinstance(name, str)
    assert isinstance(desc, unicode)
    assert isinstance(goal, types.FunctionType)
    assert isinstance(exit_msg, unicode)
    MISSIONS[name] = Mission(name, desc, goal, exit_msg)


_add_mission(
    'clone_from_github',
    u'Githubからcloneしよう',
    lambda: True,
    u'おめでとう！')

_add_mission(
    'sentinel',
    u'すべてのミッションが完了しました。',
    lambda: False,
    u'おめでとう！')


def check_mission_achieved():
    m = MISSIONS.get(data['mission'])
    if not m:
        raise RuntimeError("active mission name in savedata is not found in missions")
    is_OK = m.goal()
    if is_OK:
        print "OK"
        print m.exit_msg
    else:
        print "NG"
        print m.desc
    return is_OK


SCENARIO = {
    'clone_from_github': 'sentinel'
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
    load()
    is_ok = check_mission_achieved()
    if is_ok:
        enter_next_mission()
    save()
