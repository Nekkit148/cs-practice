def count_by_extension(paths: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for path in paths:
        name = path.rsplit("/", 1)[-1]
        ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
        result[ext] = result.get(ext, 0) + 1
    return result
