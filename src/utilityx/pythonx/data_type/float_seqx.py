from utilityx.pythonx.data_type.number_seqx import NumberSeq


class Seqx(NumberSeq):
    def __init__(self, seq:Sequence[float,...]):
        super().__init__(seq)