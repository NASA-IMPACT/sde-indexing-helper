import json

from sde_collections.models import Collection

data = json.load(open("jupyter_notebooks/mydata.json"))

for item in data:
    spreadsheet_status_mapping = {
        "needs curation": 1,
        "needs engineering": 2,
        "ready to be reindexed on test": 3,
        "indexing in progress on test": 4,
        "ready to be quality checked on test": 5,
        "ready to be deployed to prod": 6,
        "indexing in progress on prod": 7,
        "ready for final quality check": 8,
        "finished!!!": 9,
        "ignore": 10,
        "need clarification": 11,
        "delete from everywhere": 12,
        "indexing problem on test": 13,
        "indexing problem on prod": 14,
        "turn off": 15,
        "finished curation": 16,
    }
    try:
        collection = Collection.objects.get(config_folder=item["config_folder"])
    except collection.DoesNotExist:
        print(f"Collection does not exist: {item['config_folder']}")
        continue

    collection.final_notes = item["final_notes"]
    collection.spreadsheet_status = spreadsheet_status_mapping[item["status"]]
    collection.current_action_needed = item["current_action_needed"]
    collection.indexing_log = item["indexing_log"]
    collection.save()
