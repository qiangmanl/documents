

# test_pool = [str(i) for i in range(1000)]

class CircleChain(object):
    def __init__(self, chain) -> None:
        self.circle = self.__push(chain)
        self.next_task = None
        self.task = None

    def __push(self, items):
        while True:
            for item in items:
                yield item

    def nextpop(self):
        return next(self.circle)
    

    def rolling(self):
        while True:
            self.task = self.next_task
            self.next_task = self.nextpop()
            ack_task = self._get_ack_task()
            print(self.next_task)
            if ack_task == self.task:
            #string ack pedding
                self._save_ack_task(self.next_task)
            #self._print_ack_task()

    def _save_ack_task(self, task):
        raise NotImplementedError("method _save_ack_task no implement")

    def _get_ack_task(self):
        raise NotImplementedError("method _get_ack_task no implement")
