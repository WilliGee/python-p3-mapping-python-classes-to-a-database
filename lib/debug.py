#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song

Song.create_table()


if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
