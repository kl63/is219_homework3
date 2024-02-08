from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
from decimal import Decimal
from typing import Callable
class Calculator:
    @staticmethod
    def perform_operation(a: Decimal, b: Decimal , operations: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(a,b, operation)
        Calculation.add_calculation(calculation)
        return calculation.perform()
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return calculation.perform_operation(a, b, add)
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return calculation.perform_operation(a,b, subtract)
    @staticmethod
    def multiply (a: Decimal, b: Decimal) -> Decimal:
        return calculation.perform_operation(a, b, muliply)
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return calculation.perform_operation(a, b, divide)


