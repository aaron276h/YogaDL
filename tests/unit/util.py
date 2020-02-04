import os
import pathlib

import tensorflow as tf

import yogadl.tensorflow_util as tensorflow_util


def create_tf_dataset_from_range(range_size: int) -> tf.data.Dataset:
    return tf.data.Dataset.range(range_size)


def create_lmdb_checkpoint_using_range(range_size: int) -> pathlib.Path:
    dataset = create_tf_dataset_from_range(range_size=range_size)
    checkpoint_path = pathlib.Path("/tmp/test_lmdb_checkpoint.mdb")
    if checkpoint_path.exists():
        checkpoint_path.unlink()
    assert not checkpoint_path.exists()

    tensorflow_util.serialize_tf_dataset_to_lmdb(
        dataset=dataset, checkpoint_path=checkpoint_path,
    )

    return checkpoint_path