import ast
import logging
import operator


class Monk:
    @staticmethod
    def safe_eval(s):

        ops = {
            ast.Eq: operator.eq,
            ast.NotEq: operator.ne,
            ast.Gt: operator.gt,
            ast.GtE: operator.ge,
            ast.Lt: operator.lt,
            ast.LtE: operator.le,
        }

        def _eval(node):
            logging.debug(f"{type(node)} {node}")
            if isinstance(node, ast.Expression):
                return _eval(node.body)
            elif isinstance(node, ast.Str):
                return node.s
            elif isinstance(node, ast.Num):
                return node.value
            elif isinstance(node, ast.Constant):
                return node.value
            elif isinstance(node, ast.Compare):
                left = _eval(node.left)
                truth = [ops[type(op)](left, _eval(comp)) for op, comp in zip(node.ops, node.comparators)]  # noqa
                return all(truth)
            else:
                raise SyntaxError(f"invalid syntax, {type(node)}")

        tree = ast.parse(s, mode="eval")
        return _eval(tree)
