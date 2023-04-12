**Project Portfolio: https://github.com/calebyhan/CalebHan**

[![PyPI version](https://badge.fury.io/py/airlabs.svg)](https://badge.fury.io/py/airlabs)
[![Documentation Status](https://readthedocs.org/projects/airlabs/badge/?version=latest)](https://airlabs.readthedocs.io/en/latest/?badge=latest)

# airlabs

Python wrapper for [AirLabs](https://airlabs.co/).


## Installation
----------------------

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install airlabs.

```bash
pip install airlabs
```


## Usage
----------------------

```python
import airlabs

# Gets airline information about American Airlines
airlabs.airlines(iata_code="AA")

# Gets information about real-time flights
airlabs.flights()
```


## Documentation
----------------------

Documentation found in https://airlabs.readthedocs.io/en/latest/.


## Contributing
----------------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
----------------------

[MIT](https://choosealicense.com/licenses/mit/)
