from datetime import date

from models import Batch, OrderLine


def test_batch를_할당하면_가용재고가_줄어든다():
    batch = Batch('batch-001', 'SMALL-TABLE', qty=20, eta=date.today())
    line = OrderLine('order-ref', 'SMALL-TABLE', 2)

    batch.allocate(line)

    assert batch.available_quantity == 18


def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch('batch-001', sku, batch_qty, eta=date.today()),
        OrderLine('order-123', sku, line_qty)
    )


def test_가용재고가_주문량보다_많으면_할당할_수_있다():
    large_batch, small_line = make_batch_and_line('ELEGANT-LAMP', 20, 2)
    assert large_batch.can_allocate(small_line)


def test_가용재고가_주문량보다_적으면_할당할_수_없다():
    small_batch, large_line = make_batch_and_line('ELEGANE-LAMP', 2, 20)
    assert small_batch.can_allocate(large_line) is False


def test_가용재고와_주문량이_같다면_할당할_수_있다():
    batch, line = make_batch_and_line('ELEGANT-LAMP', 2, 2)
    assert batch.can_allocate(line)


def test_sku가_서로_다르면_할당할_수_없다():
    batch = Batch('batch-001', 'UNCOMFORTABLE-CHAIR', 100, eta=None)
    differenct_sku_line = OrderLine('order-123', 'EXPENSIVE-TOASTER', 30)
    assert batch.can_allocate(differenct_sku_line) is False


def test_할당되지_않은_batch를_해제해도_가용재고는_변함없다():
    batch, unallocated_line = make_batch_and_line('DECORATIVE-TRINKET', 20, 2)
    batch.deallocate(unallocated_line)
    assert batch.available_quantity == 20


def test_할당은_멱등이다():
    batch, line = make_batch_and_line('ANGULAR-DESK', 20, 2)
    batch.allocate(line)
    batch.allocate(line)
    assert batch.available_quantity == 18
