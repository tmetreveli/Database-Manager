# Database Manager

The DatabaseManager class provides functionalities to interact with a MongoDB database. It offers methods to perform common database operations such as adding data, searching, updating, and aggregating results.

## Installation

To use the DatabaseManager, you need to have Python installed along with the pymongo library.
```
pip install requirements.txt
```
### Initialization:
```
from pymongo import MongoClient
from database_manager import DatabaseManager

# Initialize DatabaseManager
db_manager = DatabaseManager()
```

### Adding data:
```
# Add data to a specific collection
db_manager.add_data("collection_name", key1=value1, key2=value2, ...)
```

### Searching data:
```
# Search for documents in a collection based on criteria
result = db_manager.search("collection_name", name="John")
```

### Updating data:
```
# Update a document in a collection
db_manager.update("collection_name", id="document_id", name="John", age=30)
```

### Aggregating data:
```
# Aggregate data to perform complex queries
advisors = db_manager.list_advisors_with_students_count(order_by=1)
students = db_manager.list_students_with_advisors_count(order_by=1)
```

### Deleting data:
```
# Delete a document from a collection
db_manager.delete_row("collection_name", row_id="document_id")
```

## Note

Ensure that you have MongoDB running on your local machine or accessible via the specified host and port ("localhost", 27017). Also, make sure to replace "collection_name" with the actual collection names in your MongoDB database.
