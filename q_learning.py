#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# qlagent.py
#
# Copyright 2017-2018 Tohgoroh Matsui All Rights Reserved.
#
from rlagent import ReinforcementLearningAgent
import numpy as np


class QLearningAgent(ReinforcementLearningAgent):
    """Q学習エージェント。"""

    def learn(self):
        """Q学習を用いて学習する。"""
        env = self.environment  # 環境
        gamma = self.discount_rate  # 割引率
        alpha = self.step_size  # ステップ・サイズ
        episodes = 0    # エピソード数
        total_steps = 0 # 全ステップ数
        self.q = np.zeros([env.states, env.actions])    # Q値をゼロに初期化する
        while total_steps < self.max_steps:
            steps = 0   # このエピソードにおけるステップ数
            state = env.init_state()    # 状態を初期化する
            while total_steps < self.max_steps and not env.is_terminal(state):  # 終端状態になるまで繰り返す:
                action = self.epsilon_greedy(state) # 行動を選択する
                reward , state_ = env.take_action(state, action) # 行動を実行し、次の状態と報酬を観測する
                if self.verbose_level > 1:
                    env.print_log(steps, state, action, reward, state_) # ログを出力する
                action_ = self.greedy(state_)   # 次の状態でQ値が最大の行動を調べる
                s, a, = env.get_s(state), env.get_a(action)
                s_, a_ = env.get_s(state_), env.get_a(action_)
                self.q[s, a] += alpha * (reward + gamma * self.q[s_, a_] - self.q[s, a])    # Q値を更新する
                state = state_  # 状態を更新する
                steps += 1
                total_steps += 1
                if self.evaluation and total_steps % np.power(10, np.floor(np.log10(total_steps))) == 0:
                    eval = self.evaluate()  # 評価する
                    print('%d, %f' % (total_steps, eval))
            episodes += 1
        if self.verbose_level > 0:
            print(self.q)   # Q値を出力

    def __init__(self, environment=None, seed=None, discount_rate=0.9, step_size=0.1, epsilon=0.1, max_steps=1000000, evaluation=True, verbose_level=0):
        super().__init__(environment, seed, discount_rate, step_size, epsilon, max_steps, evaluation, verbose_level)
