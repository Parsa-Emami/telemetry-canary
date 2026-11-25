# CLI contract

Run `python3 check.py <fixture.json>` from the repository or pass the absolute path to `check.py`. Inputs are UTF-8 JSON objects up to 2 MiB. The [passing fixture](../examples/pass.json) and [finding fixture](../examples/finding.json) define the current project inputs. This is a pre-1.0 interface.

| Exit | JSON status | Meaning |
| --- | --- | --- |
| 0 | ok | No findings |
| 1 | findings | One or more observations need review |
| 2 | invalid_input | Input could not be evaluated |

The output contains a `findings` array. The negative fixture demonstrates `synthetic_canary_observed`.

Run `python3 scripts/benchmark.py` for 100 measured evaluator invocations against the checked-in negative fixture after one warm-up. Results are machine-specific. See R12 before comparing performance across systems.
