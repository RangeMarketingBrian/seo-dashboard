def table_insert_rows(table_id):

    # [START bigquery_table_insert_rows]
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of table to append to.
    # table_id = "your-project.your_dataset.your_table"

    rows_to_insert = [
        {u"account": u"testaccount", u"organic_traffic_ga": 88888888},
    ]

    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))
    # [END bigquery_table_insert_rows]
    
# table_insert_rows('range-marketing-seo-dashboard.brian_v1_dataset.fact_web_metrics_cont')