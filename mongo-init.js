const res = [
    db.domains.drop(),
    db.domains.createIndex({ slug: 1 }, { unique: true })
]

printjson(res)

