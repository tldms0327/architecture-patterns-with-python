from dataclasses import dataclass
from datetime import date
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
        if self.can_allocate(line) and line.orderid not in self.allocated_orders:
            self.available_quantity -= line.qty
            self.allocated_orders.add(line.orderid)
            
    def deallocate(self, line: OrderLine):
        if line.orderid in self.allocated_orders:
            self.allocated_orders.remove(line.orderid)
            self.available_quantity += line.qty
                    
    def can_allocate(self, line: OrderLine):
        if self.available_quantity >= line.qty and self.sku == line.sku:
            return True
        return False

     
def allocate(line: OrderLine, batches: List[Batch]):
       return True
