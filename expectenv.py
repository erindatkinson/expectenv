"""a package to kinda hack together something
similar to how golang viper works for pulling
environment variables"""

from os import getenv
from typing import Any, AnyStr


class EnvError(Exception):
    """error for missing env"""


class Parser:
    """ExpectEnvParser is a parser class to manage expected environment variables
    and pulling them in from the system"""

    def __init__(self, prefix: str | None = None):
        self.prefix = prefix
        self._keys: list[tuple[str, bool]] = []
        self._configs = {}

    def bind(self, key: str, optional: bool = False) -> None:
        """bind sets that a key is expected to be in the environment for the application
        if a prefix was set, it expects it under {prefix}_{key}"""
        self._keys.append((key, optional))

    def get(self, key: str) -> Any | KeyError:
        """get returns the value for the given key"""
        return self._configs[self.__build_key(key)]

    def get_str(self, key: str) -> AnyStr | KeyError:
        """get_str returns a string casted value for the given key"""
        return str(self.get(key))

    def get_int(self, key: str) -> int | KeyError | ValueError:
        """get_int returns an integer casted value for the given key"""
        return int(self.get(key))

    def keys(self) -> list[str]:
        """keys returns a list of bound keys"""
        return list(map(lambda item: item[0], self._keys))

    def configs(self) -> dict:
        """configs returns a dict of all k:v pairs that have been pulled from the env"""
        return self._configs

    def parse(self) -> None | EnvError:
        """parse looks through all the bound expectations and attempts to pull them
        into a dict, if it cannot find one, it raises an EnvError"""

        for key, optional in self._keys:
            envkey = self.__build_key(key)
            val = getenv(envkey)
            if val is None:
                if not optional:
                    raise EnvError(f"missing env var: {envkey}")
                continue
            self._configs[key] = val

    def __build_key(self, key: str) -> str:
        """__build_key builds the key based on common logic"""
        out = ""
        if self.prefix is not None:
            out += f"{self.prefix}_"
        out += key
        return out.upper()
