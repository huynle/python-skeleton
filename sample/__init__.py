
class Sample(object):

    def __init__(self, value_sample):
        self._sample = value_sample

    def sample(self):
        return self._sample

class TestClass(object):
    def __init__(self, input1, other=None):
        self._other =input1

