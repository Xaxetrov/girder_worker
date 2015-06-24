import contextlib
import os
import tarfile


output = os.path.splitext(input)[0]

try:
    os.makedirs(output)
except OSError:
    if not os.path.exists(output):
        raise

with contextlib.closing(tarfile.open(input, 'r')) as tf:
    tf.extractall(output)
