#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# environment.py
#
# Copyright 2017-2018 Tohgoroh Matsui All Rights Reserved.
#
from abc import ABCMeta, abstractmethod


class Environment(metaclass=ABCMeta):
    """強化学習の環境。"""

    states = None   # 状態数
    actions = None  # 行動数

    @classmethod
    @abstractmethod
    def init_state(cls):
        """初期状態を返す。"""
        pass

    @classmethod
    @abstractmethod
    def is_terminal(cls):
        """終端状態ならTrue、そうでないならFalseを返す。"""
        pass

    @classmethod
    @abstractmethod
    def get_reward(cls, state):
        """報酬を返す。"""
        pass

    @classmethod
    @abstractmethod
    def take_action(cls, state, action):
        """行動を実行して状態を更新し、報酬と次の状態を返す。"""
        pass

    @classmethod
    @abstractmethod
    def str_state(cls, state):
        """状態を表す文字列を返す。"""
        pass

    @classmethod
    @abstractmethod
    def str_action(cls, action):
        """行動を表す文字列を返す。"""
        pass

    @classmethod
    def print_log(cls, steps, state, action, reward, state_):
        """ログを出力する。"""
        print('# %d, %s, %s, %f, %s' % (steps, cls.str_state(state), cls.str_action(action), reward, cls.str_state(state_)))
