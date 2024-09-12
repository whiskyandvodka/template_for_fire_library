import warnings

import fire


class DefaultConfig(object):
    env = 'default'
    model = 'SequeezeNet'

    batch_size = 4
    use_gpu = False

    lr = 0.1

    def parse(self, kwargs):
        '''
        根据字典kwargs更新配置参数
        :param kwargs:
        :return:
        '''
        for k, v in kwargs.items():
            if not hasattr(self, k):
                warnings.warn("Warning: opt has not attribut %s" % k)
            setattr(self, k, v)

        # 打印配置信息
        print('user config:')
        for k, v in self.__class__.__dict__.items():
            if not k.startswith('__'):
                print(k, getattr(self, k))


opt = DefaultConfig()
