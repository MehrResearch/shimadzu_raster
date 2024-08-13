# Shimadzu raster file reader

- [X] Read circular profiles (diameter, spacing)

## Example usage

```python
from shimadzu_raster import parse_raster

parsed = parse_raster('linear_ma_acc.rst')
assert parsed['n_points'] == 211
assert parsed['diameter'] == 2300.0
assert parsed['spacing'] == 150.0
assert len(parsed['xys']) == 211
```