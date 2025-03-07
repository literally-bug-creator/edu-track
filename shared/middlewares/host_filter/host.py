import ipaddress as ip


class Host:
    def __init__(self, host: str):
        self.host = host
        self.checks = dict()
        if host == "*":
            return
        if ip := _to_ip(host):
            self.checks["ip"] = ip
        if network := _to_network(host):
            self.checks["network"] = network
        if special := _to_special(host):
            self.checks["special"] = special
        if domain := _to_domain(host):
            self.checks["domain"] = domain
        assert self.checks, f"Unknown host type: {host}"

    @property
    def is_any(self) -> bool:
        return self.host == "*"

    def is_same(self, host: str) -> bool:
        if self.is_any:
            return True
        return (
            self._check_ip(host) or
            self._check_network(host) or
            self._check_special(host) or
            self._check_domain(host)
        )

    def _check_ip(self, host: str) -> bool:
        if "ip" not in self.checks:
            return False
        return _to_ip(host) == self.checks["ip"]

    def _check_network(self, host: str) -> bool:
        if "network" not in self.checks:
            return False
        return _to_ip(host) in self.checks["network"]

    def _check_special(self, host: str) -> bool:
        if "special" not in self.checks:
            return False
        return _to_special(host) == self.checks["special"]

    def _check_domain(self, host: str) -> bool:
        if "domain" not in self.checks:
            return False
        domain = self.checks["domain"]
        if domain.startswith("*"):
            return host.endswith(domain)
        return host == domain


def _to_ip(host: str) -> ip.IPv4Address | ip.IPv6Address | None:
    try:
        return ip.ip_address(host)
    except ValueError:
        return None


def _to_network(host: str) -> ip.IPv4Network | ip.IPv6Network | None:
    try:
        return ip.ip_network(host)
    except ValueError:
        return None


def _to_domain(host: str) -> str | None:
    if "." in host:
        return host
    return None


def _to_special(host: str) -> str | None:
    host = host.lower()
    if host in _SPECIAL_HOSTS:
        return host
    return None


_SPECIAL_HOSTS = {"localhost", }