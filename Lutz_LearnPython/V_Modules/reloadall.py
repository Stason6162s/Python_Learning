"""
reloadall: транзитивная перезагрузка вложенных модулей
"""
import types
from imp import reload


def status(module):
    print('reloading: ', module.__name__)


def transitive_reload(module, visited):
    if module not in visited:
        status(module)
        reload(module)
        visited[module] = None
        for attrobg in module.__dict__.values():
            if attrobg.isinstance(types.ModuleType):
                # if type(attrobg) == types.ModuleType:
                transitive_reload(attrobg, visited)


def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)


if __name__ == '__main__':
    import reloadall

    reload_all(reloadall)
