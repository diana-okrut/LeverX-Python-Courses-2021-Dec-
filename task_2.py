class VersionElement:
    def __init__(self, element):
        if element.isdigit():
            self.version = int(element)
            self.suffix = ""

        else:
            for i, char in enumerate(element):
                if not char.isdigit():
                    break
            digits, not_digits = element[:i], element[i:]
            self.version = int(digits) if digits else 0
            self.suffix = not_digits

    def __str__(self):
        return f"{self.version}{self.suffix}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):

        number_eq = self.version == other.version
        if number_eq:
            return self.suffix == other.suffix
        return number_eq

    def __gt__(self, other):
        number_eq = self.version == other.version
        if number_eq:
            if self.suffix == "" and other.suffix == "":
                return False
            elif self.suffix == "" or other.suffix == "":
                return self.suffix == ""
            else:
                return self.suffix > other.suffix
        return self.version > other.version

    def __lt__(self, other):
        number_eq = self.version == other.version
        if number_eq:
            if self.suffix == "" and other.suffix == "":
                return False
            elif self.suffix == "" or other.suffix == "":
                return self.suffix != ""
            else:
                return self.suffix < other.suffix
        return self.version < other.version


class Version:
    def __init__(self, version: str):
        parsed_text = version.split(".")
        self.versions = []
        for element in parsed_text:
            item = VersionElement(element)
            self.versions.append(item)

    def __eq__(self, other):
        return self.versions == other.versions

    def __gt__(self, other):
        return self.versions > other.versions

    def __lt__(self, other):
        return self.versions < other.versions


def test():
    to_test = [
        ("1-alpha", "1"),
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
        ("1-alpha", "1.1"),
        ("1", "1.0"),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"


if __name__ == "__main__":
    test()
