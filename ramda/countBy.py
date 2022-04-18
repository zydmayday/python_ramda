from .reduceBy import reduceBy

countBy = reduceBy(lambda acc, _: acc + 1, 0)
