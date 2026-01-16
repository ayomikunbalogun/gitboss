import pytest
from app.parsing import parse_amount, parse_date


def test_parse_amount_handles_currency_and_commas():
    assert parse_amount("£1,200.50") == 1200.50


def test_parse_amount_handles_negative_refunds():
    assert parse_amount("-£5.00") == -5.00


def test_parse_date_handles_iso_format():
    assert parse_date("2026-01-13").year == 2026
