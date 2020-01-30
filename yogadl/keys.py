import random
from typing import Any, List, Optional


def sequential_shard(keys: List[Any], shard_index: int, world_size: int) -> List[Any]:
    num_keys = len(keys) // world_size
    if shard_index < len(keys) % world_size:
        num_keys += 1
    start_index = num_keys * shard_index + min(len(keys) % world_size, shard_index)
    return keys[start_index : start_index + num_keys]


def non_sequential_shard(keys: List[Any], shard_index: int, world_size: int) -> List[Any]:
    index = shard_index
    sharded_keys = []
    while index < len(keys):
        sharded_keys.append(keys[index])
        index += world_size
    return sharded_keys


def shard_keys(
    keys: List[Any], shard_index: int, world_size: int, sequential: bool = False
) -> List[Any]:
    assert shard_index >= 0
    assert shard_index < world_size
    if sequential:
        return sequential_shard(keys=keys, shard_index=shard_index, world_size=world_size)
    else:
        return non_sequential_shard(keys=keys, shard_index=shard_index, world_size=world_size)


def shuffle_keys(keys: List[Any], seed: Optional[int] = None) -> List[Any]:
    if seed:
        random.seed(seed)
    random.shuffle(keys)
    return keys
