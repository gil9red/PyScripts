#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


def create_random_file(repo):
    import uuid
    file_name = str(uuid.uuid4())

    import os
    full_file_name = os.path.join(repo.working_tree_dir, file_name)

    with open(full_file_name, 'w') as f:
        import random
        import string
        text = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(64))
        f.write(text)

    return file_name, file_name


if __name__ == '__main__':
    from config import get_repo
    repo = get_repo()
    print(repo)
    print()

    from print_repo_log import print_log
    print_log(repo)
    print()

    new_file_name = create_random_file(repo)[1]
    message = 'Create: ' + new_file_name
    print(message)

    repo.index.add([new_file_name])
    # # or:
    # repo.index.add(['*'])
    # repo.git.add(new_file_name)
    # repo.git.add('-A')

    repo.index.commit(message)

    # repo.remotes.origin.pull()
    repo.remotes.origin.push()
