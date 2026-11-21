# Outage Watch

Tells the L1 support shift which outage is upstream before the tickets pile up.
IT26210 DEVASC, Topic 10. Full README arrives in Sprint 3 (OW-13).

## Run
    pip install -r requirements.txt
    python status_check.py

## Test
    pip install -r requirements-dev.txt
    flake8 status_check.py ci tests
    pytest
