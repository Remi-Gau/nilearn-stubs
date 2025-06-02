from pathlib import Path
from typing import Union

import libcst as cst
from rich import print

file = "mass_univariate/permuted_least_squares.pyi"
cwd = Path(__file__).parents[1]
stub_file = cwd / "nilearn-stubs"
source_file = cwd / "nilearn" / "nilearn"


def parse_stub_file(
    stub_path: str,
) -> dict[str, Union[str, tuple[str, dict[str, str]]]]:
    """Parse the stub file and return a mapping of function/method signatures to their type annotations."""
    with Path(stub_path).open() as f:
        stub_tree = cst.parse_module(f.read())

    annotations = {}

    class StubVisitor(cst.CSTVisitor):
        def visit_FunctionDef(self, node: cst.FunctionDef) -> None:
            func_name = node.name.value
            args = {
                param.name.value: cst.Module([]).code_for_node(param.annotation.annotation)
                for param in node.params.params
                if param.annotation
            }
            return_type = cst.Module([]).code_for_node(node.returns.annotation) if node.returns else None
            annotations[func_name] = (return_type, args)

        def visit_ClassDef(self, node: cst.ClassDef) -> None:
            class_name = node.name.value
            class_annotations = {}
            for body_elem in node.body.body:
                if isinstance(body_elem, cst.FunctionDef):
                    func_name = body_elem.name.value
                    args = {
                        param.name.value: cst.Module([]).code_for_node(param.annotation.annotation)
                        for param in body_elem.params.params
                        if param.annotation
                    }
                    return_type = (
                        cst.Module([]).code_for_node(body_elem.returns.annotation) if body_elem.returns else None
                    )
                    class_annotations[func_name] = (return_type, args)
            annotations[class_name] = class_annotations

    stub_tree.visit(StubVisitor())

    return annotations


class AnnotationTransformer(cst.CSTTransformer):
    """Apply annotations."""

    def __init__(self, annotations: dict[str, Union[str, tuple[str, dict[str, str]]]]):
        self.annotations = annotations

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef) -> cst.FunctionDef:
        func_name = original_node.name.value
        if func_name in self.annotations and isinstance(self.annotations[func_name], tuple):
            return_type, args = self.annotations[func_name]
            print(f"Applying annotations to function: {func_name}, args: {args}, return: {return_type}")

            updated_params = [
                param.with_changes(annotation=cst.Annotation(cst.parse_expression(args[param.name.value])))
                if param.name.value in args
                else param
                for param in updated_node.params.params
            ]

            updated_returns = cst.Annotation(cst.parse_expression(return_type)) if return_type else updated_node.returns

            return updated_node.with_changes(
                params=updated_node.params.with_changes(params=updated_params),
                returns=updated_returns,
            )
        return updated_node

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef) -> cst.ClassDef:
        class_name = original_node.name.value
        if class_name in self.annotations and isinstance(self.annotations[class_name], dict):
            class_annotations = self.annotations[class_name]
            updated_body = []

            for elem in updated_node.body.body:
                if isinstance(elem, cst.FunctionDef) and elem.name.value in class_annotations:
                    method_name = elem.name.value
                    return_type, args = class_annotations[method_name]
                    print(
                        f"Applying annotations to method: {class_name}.{method_name}, "
                        f"args: {args}, return: {return_type}"
                    )

                    updated_params = [
                        param.with_changes(annotation=cst.Annotation(cst.parse_expression(args[param.name.value])))
                        if param.name.value in args
                        else param
                        for param in elem.params.params
                    ]

                    updated_returns = cst.Annotation(cst.parse_expression(return_type)) if return_type else elem.returns

                    elem = elem.with_changes(
                        params=elem.params.with_changes(params=updated_params),
                        returns=updated_returns,
                    )

                updated_body.append(elem)

            return updated_node.with_changes(body=updated_node.body.with_changes(body=updated_body))

        return updated_node


def main(
    source: str,
    annotations: dict[str, Union[str, tuple[str, dict[str, str]]]],
):
    """Apply the annotations from the stub file to the source code."""
    source_path = Path(source)
    with source_path.open("r") as f:
        source_code = f.read()

    source_tree = cst.parse_module(source_code)
    transformer = AnnotationTransformer(annotations)
    updated_tree = source_tree.visit(transformer)

    with source_path.open("w") as f:
        f.write(updated_tree.code)


if __name__ == "__main__":
    annotations = parse_stub_file(stub_file)
    print("Extracted Annotations:", annotations)
    main(source_file, annotations)
