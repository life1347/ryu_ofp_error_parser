# Intro:
Ryu_ofp_error_parser is the OpenFlow error msg parser. All information come from OpenFlow Spec v1.3
https://www.opennetworking.org/images/stories/downloads/sdn-resources/onf-specifications/openflow/openflow-spec-v1.3.0.pdf

# Usage:
```python
from of_error import parse_ofp_err_msg
error_type_msg, error_code_msg = parse_ofp_err_msg(err_type, err_code)
```
