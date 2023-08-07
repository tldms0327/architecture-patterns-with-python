from datetime import datetime, timedelta

from models import Batch, OrderLine, allocate

today = datetime.now()
tomorrow = today + timedelta(days=1)
later = today + timedelta(days=5)


def test_창고에_있는_재고를_먼저_배송한다():
    in_stock_batch = Batch('in-stock-batch', 'RETRO-CLOCK', 100, eta=None)
    shipment_batch = Batch('shipment-batch', 'RETRO-CLOCK', 100, eta=tomorrow)
    line = OrderLine('oref', 'RETRO-CLOCK', 10)

    allocate(line, [in_stock_batch, shipment_batch])

    assert in_stock_batch.available_quantity == 90
    assert shipment_batch.available_quantity == 100


def test_먼저_들어온_재고를_먼저_배송한다():
    earliest = Batch('speedy-batch', 'MINIMALIST-SPOON', 100, eta=today)
    medium = Batch('normal-batch', 'MINIMALIST-SPOON', 100, eta=tomorrow)
    latest = Batch('slow-batch', 'MINIMALIST-SPOON', 100, eta=later)
    line = OrderLine('order1', 'MINIMALIST-SPOON', 10)

    allocate(line, [medium, earliest, latest])

    assert earliest.available_quantity == 90
    assert medium.available_quantity == 100
    assert latest.available_quantity == 100


def test_배치는_reference를_리턴한다():
    in_stock_batch = Batch('in-stock-batch-ref', 'HIGHBROW-POSTER', 100, eta=None)
    shipment_batch = Batch('shipment-batch-ref', 'HIGHBROW-POSTER', 100, eta=tomorrow)
    line = OrderLine('oref', 'HIGHBROW-POSTER', 10)

    allocation = allocate(line, [in_stock_batch, shipment_batch])

    assert allocation == in_stock_batch.reference
