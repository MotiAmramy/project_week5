from database.connect import accidents_collection


def index_get_accidents_by_area(area):
    no_index_execution_stats = accidents_collection.find({'area': area}).hint({'$natural': 1}).explain()['executionStats']
    print(f"Query without index took {no_index_execution_stats['executionTimeMillis']} ms")
    print(f"Total docs examined without index: {no_index_execution_stats['totalDocsExamined']}")
    with_index_execution_stats = accidents_collection.find({'area': area}).hint({'area': 1}).explain()['executionStats']
    # Print execution stats with index
    print(f"Query with index took {with_index_execution_stats['executionTimeMillis']} ms")
    print(f"Total docs examined with index: {with_index_execution_stats['totalDocsExamined']}")
    # Return the actual query result (using index)
