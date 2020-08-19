#!/usr/bin/env python
        # -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
q_table = np.random.uniform(low=-1, high=1, size=(5**2, env.action_space.n))
def bins(clip_min, clip_max, num):
   return np.linspace(clip_min, clip_max, num + 1)[1:-1]

def digitize_state(observation):
   cart_pos, cart_v, pole_angle, pole_v = observation
   digitized = [np.digitize(cart_pos, bins=bins(-2.4, 2.4, 4)),
                np.digitize(cart_v, bins=bins(-3.0, 3.0, 4)),
                np.digitize(pole_angle, bins=bins(-0.5, 0.5, 4)),
                np.digitize(pole_v, bins=bins(-2.0, 2.0, 4))]
   return sum([x * (4 ** i) for i, x in enumerate(digitized)])
class QLearning:
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        # actions = [0, 1, 2, 3]
        self.actions = actions
        self.alpha = learning_rate
        self.discount_factor = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions)

    # 以前に行ったstateでないかを判別して、行っていないstateであれば初期化
    def check_state_exist(self, state):
        # 行っていないstateの場合にのみ初期化
        if state not in self.q_table.index:
            # 新しいstateをq_tableに追加
            # 初期化は、[0、0、0、0]で
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )

    # Q関数をQ学習アルゴリズムに基づいて更新する
    def learn(self, s, a, r, s_):
        # まず行ったことがあることを確認して、いない場合初期化
        self.check_state_exist(s_)
        q_1 = self.q_table.ix[s, a]
        # 次の状態のQ関数の最大を求める
        q_2 = r + self.discount_factor * self.q_table.ix[s_, :].max()
        self.q_table.ix[s, a] += self.alpha * (q_2 - q_1)

    # 現在の状態についての行動を受けてくる関数
    def get_action(self, state):
        self.check_state_exist(state)
        # epsilonよりrand関数で選ばれた数が少ない場合、Q関数による行動リターンを得る
        if np.random.rand() < self.epsilon:
            # 最適の行動の選択
            state_action = self.q_table.ix[state, :]
            state_action = state_action.reindex(np.random.permutation(state_action.index))
            action = state_action.argmax()

        # epsilonよりrand関数で選ばれた数が大きい場合、ランダムに行動を返す
        else:
            # 任意の行動を選択
            action = np.random.choice(self.actions)
        return action
