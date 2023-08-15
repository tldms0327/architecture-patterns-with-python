from dataclasses import dataclass
from datetime import datetime, date, timedelta
from typing import List, Optional, Set
@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int


class Batch:
    def __init__(self, ref:str, sku:str, qty: int, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self.available_quantity = qty
        self.allocated_orders: Set[str] = set()


    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self.available_quantity -= line.qty
            self.allocated_orders.add(line.orderid)
            
    def deallocate(self, line: OrderLine):
        if line.orderid in self.allocated_orders:
            self.allocated_orders.remove(line.orderid)
            self.available_quantity += line.qty
                    
    def can_allocate(self, line: OrderLine):
        if self.available_quantity >= line.qty and self.sku == line.sku and line.orderid not in self.allocated_orders:
            return True
        return False


def allocate(line: OrderLine, batches: List[Batch]):
    selected_batch = Batch("", "", 0, None)
    for batch in batches:
        # 있는 재고
        if batch.eta is None and batch.can_allocate(line):
            batch.allocate(line)
            return batch.reference
        # 도착 예정 재고
        else:
            if batch.can_allocate(line) and (selected_batch.eta is None or selected_batch.eta > batch.eta):
                selected_batch = batch
                
    selected_batch.allocate(line)
    return selected_batch.reference
