"""
QRadar SDK - Filter module

This module provides utilities for constructing and parsing QRadar API filter strings.

QRadar API filters are used to specify criteria for selecting resources in API requests. They consist of one or more expressions combined with logical operators (AND, OR). Each expression compares a field to a value using an operator (e.g., =, !=, >, <).
Example filter string:
    "name = 'example' AND (status = 'active' OR status = 'pending')"

The main class in this module is :class:`FilterBuilder`, which provides a fluent interface for building filter strings programmatically. It supports adding expressions, grouping them with parentheses, and combining them with logical operators.

Example usage:
    from qradar_sdk.filter import FilterExpression as F
    filter_str = (F("name").eq("example") & (F("status").eq("active") | F("status").eq("pending"))).build()
    # filter_str will be: "(name = "example") AND ((status = "active") OR (status = "pending"))"

The module also includes helper functions for parsing existing filter strings into structured representations, which can be useful for analyzing or modifying filters.
"""

from __future__ import annotations
from typing import Any

class FilterOperator:
    def __init__(self, expr: str) -> None:
        self.expr = expr
    
    def __and__(self, other: FilterOperator) -> FilterOperator:
        return FilterOperator(f"({self.expr}) AND ({other.expr})")
    def __or__(self, other: FilterOperator) -> FilterOperator:
        return FilterOperator(f"({self.expr}) OR ({other.expr})")
    def __invert__(self) -> FilterOperator:
        return FilterOperator(f"NOT ({self.expr})")
    
    def build(self) -> str:
        return self.expr
    

class FilterExpression:
    def __init__(self, field: str):
        self.field = field
    
    def _validate(self, value: Any) -> str:
        if isinstance(value, bool):
            return str(value).lower()
        if isinstance(value, (int, float)):
            return str(value)
        if value is None:
            return "null"
        return f'"{value}"'
        

    def eq(self, value: Any) -> FilterOperator:
        return FilterOperator(f"{self.field} = {self._validate(value)}")
    def neq(self, value: Any) -> FilterOperator:
        return FilterOperator(f"{self.field} != {self._validate(value)}")
    def gt(self, value: Any) -> FilterOperator:
        return FilterOperator(f"{self.field} > {self._validate(value)}")
    def gte(self, value: Any) -> FilterOperator:
        return FilterOperator(f"{self.field} >= {self._validate(value)}")
    def lt(self, value: Any) -> FilterOperator:
        return FilterOperator(f"{self.field} < {self._validate(value)}")
    def lte(self, value: Any) -> FilterOperator:
        return FilterOperator(f"{self.field} <= {self._validate(value)}")
    def like(self, value: Any) -> FilterOperator:
        return FilterOperator(f"{self.field} LIKE {self._validate(value)}")
    def ilike(self, value: Any) -> FilterOperator:
        return FilterOperator(f"{self.field} ILIKE {self._validate(value)}")
    def _in(self, values: list[Any]) -> FilterOperator:
        value_str = ", ".join(self._validate(v) for v in values)
        return FilterOperator(f"{self.field} IN ({value_str})")
    def not_in(self, values: list[Any]) -> FilterOperator:
        value_str = ", ".join(self._validate(v) for v in values)
        return FilterOperator(f"{self.field} NOT IN ({value_str})")
    def between(self, low: Any, high: Any) -> FilterOperator:
        return FilterOperator(f"{self.field} BETWEEN {self._validate(low)} AND {self._validate(high)}")
    def not_between(self, low: Any, high: Any) -> FilterOperator:
        return FilterOperator(f"{self.field} NOT BETWEEN {self._validate(low)} AND {self._validate(high)}")
    def is_null(self) -> FilterOperator:
        return FilterOperator(f"{self.field} IS NULL")
    def is_not_null(self) -> FilterOperator:
        return FilterOperator(f"{self.field} IS NOT NULL")
    
    