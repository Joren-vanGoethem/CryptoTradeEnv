from gym.envs.registration import register
from copy import deepcopy

from . import datasets


register(
    id='crypto-v0',
    entry_point='gym_crypto.envs:CryptoEnv',
    kwargs={
        'df': deepcopy(datasets.BTCUSDT),
        'window_size': 60,
        'frame_bound': (60, len(datasets.BTCUSDT))
    }
)

