const res = [
    db.domains.drop(),
    db.entries.drop(),
    db.domains.createIndex({ slug: 1 }, { unique: true }),
    db.entries.createIndex({ title: 1, group: 1, domain: 1 }, { unique: true }),
]

printjson(res)

