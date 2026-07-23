from __future__ import annotations

import pytest

from click._utils import UNSET, FLAG_NEEDS_VALUE, Sentinel, T_UNSET, T_FLAG_NEEDS_VALUE


class TestSentinel:
    def test_repr_unset(self) -> None:
        assert repr(Sentinel.UNSET) == "Sentinel.UNSET"

    def test_repr_flag_needs_value(self) -> None:
        assert repr(Sentinel.FLAG_NEEDS_VALUE) == "Sentinel.FLAG_NEEDS_VALUE"

    def test_identity_unset(self) -> None:
        assert Sentinel.UNSET is UNSET

    def test_identity_flag_needs_value(self) -> None:
        assert Sentinel.FLAG_NEEDS_VALUE is FLAG_NEEDS_VALUE

    def test_unset_not_none(self) -> None:
        assert Sentinel.UNSET != None  # noqa: E711

    def test_unset_not_false(self) -> None:
        assert Sentinel.UNSET != False

    def test_unset_is_sentinel_instance(self) -> None:
        assert isinstance(UNSET, Sentinel)

    def test_flag_needs_value_is_sentinel_instance(self) -> None:
        assert isinstance(FLAG_NEEDS_VALUE, Sentinel)

    def test_t_unset_type_alias(self) -> None:
        val: T_UNSET = UNSET
        assert val is UNSET

    def test_t_flag_needs_value_type_alias(self) -> None:
        val: T_FLAG_NEEDS_VALUE = FLAG_NEEDS_VALUE
        assert val is FLAG_NEEDS_VALUE
