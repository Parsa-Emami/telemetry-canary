import re


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)
    elif isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from strings(item)


def evaluate(data, fixture_path):
    markers = data["canaries"]
    if not isinstance(markers, list) or not markers:
        raise ValueError("at least one synthetic canary is required")
    if any(not re.fullmatch(r"tc-test-[a-z0-9]{3,32}", marker) for marker in markers):
        raise ValueError("canaries must use the synthetic tc-test- prefix")
    findings = []
    for signal in ("logs", "traces"):
        records = data[signal]
        if not isinstance(records, list):
            raise ValueError("each signal must contain an array of records")
        for index, record in enumerate(records):
            values = tuple(strings(record))
            for marker_index, marker in enumerate(markers):
                if any(marker in value for value in values):
                    findings.append({"code": "synthetic_canary_observed", "signal": signal,
                                     "record": index, "canary": marker_index})
    return findings
