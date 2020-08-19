#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# rlagent.py
#
# Copyright 2017-2018 Tohgoroh Matsui All Rights Reserved.
#
from abc import ABCMeta, abstractmethod
import numpy as np


class ReinforcementLearningAgent(metaclass=ABCMeta):
    """強化学習エージェント。"""

    @abstractmethod
    def learn(self):
        """強化学習を用いて学習する。"""
        pass

    def evaluate(self):
        """学習した行動価値が最も高い行動を選択したときの平均ステップ数を返す。"""
        env = self.environment  # 環境
        episodes = 0    # エピソード数
        total_steps = 0  # ステップ数
        while episodes < 100:   # 100エピソード繰り返す：
            steps = 0   # このエピソードにおけるステップ数
            state = env.init_state() # 状態を初期化する            state = self.getState(rawState) # 状態を状態番号に
            while not env.is_terminal(state) and steps < 100:   # 状態が終端状態になるか、または、100ステップになるまで繰り返す:
                action = self.greedy(state)  # グリーディーに行動を選択する
                reward, state_ = env.take_action(state, action) # 行動を実行し、報酬と次の状態を観測する
                if self.verbose_level > 2:
                    env.printLog(steps, state, action, reward, state_)  # ログを出力する
                state = state_
                steps += 1
                total_steps += 1
            episodes += 1
        return total_steps / 100

    def uniformly(self):
        """一様ランダムに行動を選択して返す。"""
        action = np.random.randint(self.environment.actions)    # 0からaction-1までの整数をランダムに生成する
        return action

    def greedy(self, state):
        """グリーディーに行動を選択して返す。"""
        s = self.environment.get_s(state)   # 状態番号
        max = self.q[s].max()   # 最大のQ値
        aIds = np.where(self.q[s] == max)[0]    # Q値がmaxである要素のインデックスの配列
        r = np.random.randint(len(aIds))    # 0から要素数-1までの整数をランダムに生成する
        action = aIds[r]    # Q値がmaxQである要素のインデックスから行動を選択する
        return action

    def epsilon_greedy(self, state):
        """ε-グリーディー選択を用いて行動を選択して返す。"""
        r = np.random.rand()    # 乱数を生成する
        action = self.uniformly() if  r < self.epsilon else self.greedy(state)  # 確率εで一様ランダムに、確率1-εでグリーディーに行動を選択する
        return action

    def __init__(self, environment=None, seed=None, discount_rate=0.9, step_size = 0.1, epsilon=0.1, max_steps=1000000, evaluation=True, verbose_level=0):
        self.environment = environment  # 環境
        self.seed = seed    # 乱数のシード
        self.discount_rate = discount_rate  # 割引率 γ
        self.step_size = step_size  # ステップ・サイズ α
        self.epsilon = epsilon  # ε-グリーディー選択のε
        self.max_steps = max_steps  # 最大ステップ数
        self.evaluation = evaluation    # 評価
        self.verbose_level = verbose_level  # ログ出力
        self.env = None # 環境
        self.q = None   # Q値
        if self.seed is not None:
            np.random.seed(seed)
