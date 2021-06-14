def test_delete_entry(client):
    res = client.delete("/entries/pets/feline/cat")
    assert res.status_code == 202
