from products.abs_builder import AbsBuilder


class Mac(AbsBuilder):
    def build_board(self):
        self._computer.cpu = "645"
        self._computer.wifi = False
        self._computer.colour = "Silver"