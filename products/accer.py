from products.abs_builder import AbsBuilder


class Accer(AbsBuilder):
    def build_board(self):
        self._computer.cpu = "123"
        self._computer.wifi = True