#!/usr/bin/env python2.7
import psycopg2
database_name = "news"


# What are the most popular three articles of all time?
most_popular_posts_txt = ("The most popular articles of all times:")
most_popular_posts_query = ("SELECT a.title, COUNT(*) FROM log l INNER JOIN articles a ON REPLACE(l.path, '/article/', '')=a.slug WHERE path LIKE '%/article/%' AND status = '200 OK' GROUP BY 1 ORDER BY 2 DESC")

# Who are the most popular article authors of all time?
most_popular_authors_txt = ("The most popular article authors of all times:")
most_popular_authors_query = ("SELECT au.name, COUNT(*) FROM log l INNER JOIN articles a ON REPLACE(l.path, '/article/', '')=a.slug INNER JOIN authors au ON au.id = a.author WHERE path LIKE '%/article/%' AND status = '200 OK' GROUP BY 1 ORDER BY 2 DESC")

# On which days did more than 1% of requests lead to errors?
most_erroneous_days_txt = ("Days with more than 1% of requests lead to errors:")
most_erroneous_days_query = ("WITH err AS(SELECT time::DATE AS calendar_date, status, COUNT(*) FROM log WHERE status = '404 NOT FOUND' GROUP BY 1, 2 ORDER BY 1 DESC), no_err AS (SELECT time::DATE AS calendar_date, status, COUNT(*) FROM log WHERE status = '200 OK' GROUP BY 1, 2 ORDER BY 1 DESC) SELECT err.calendar_date, ROUND(100.00*err.count/(err.count+no_err.count),2) AS err_rate, err.count AS num_err, no_err.count AS num_success FROM err INNER JOIN no_err ON err.calendar_date = no_err.calendar_date GROUP BY 1, 3, 4 HAVING 100.00*err.count/(err.count+no_err.count) > 1;")


def connect(database=database_name):
    """Connect to PostgreSQL database & return database connection"""
    try:
        db = psycopg2.connect("dbname={}".format(database))
        cursor = db.cursor()
        return db, cursor
    except:
        print ("Unable to connect to database")


def get_query_results(query):
    """Return results for given query"""
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def print_query_results(query_txt, query_results):
  print(query_txt+str('\n'))
  for i in range(len(query_results)):
    print(str('\t')+str(query_results[i][0])+str(': ')+str(query_results[i][1]))
  print('\n')


if __name__ == '__main__':
    # store query results
    popular_articles_results = get_query_results(most_popular_posts_query)
    popular_authors_results = get_query_results(most_popular_authors_query)
    load_error_days = get_query_results(most_erroneous_days_query)

    # print query results
    print_query_results(most_popular_posts_txt, popular_articles_results)
    print_query_results(most_popular_authors_txt, popular_authors_results)
    print_query_results(most_erroneous_days_txt, load_error_days)
