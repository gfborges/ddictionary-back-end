def entry_to_simple_json(**entry):
    definitions = entry.get("definitions") or []
    return {
        "_id": str(entry.get("_id")),
        "domain": entry.get("domain"),
        "title": entry.get("title"),
        "group": entry.get("group"),
        "definitions": definitions[:1],
        "created_at": entry.get("created_at").isoformat(),
    }


def entry_to_json(**entry):
    json = entry_to_simple_json(**entry)
    return json | {
        "definitions": entry.get("definitions"),
        "translations": entry.get("translations"),
        "image": entry.get("image"),
    }


class Entry:
    pass
