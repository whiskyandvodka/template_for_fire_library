from config import opt


def train(**kwargs):
    opt.parse(kwargs)


if __name__ == '__main__':
    import fire
    fire.Fire()