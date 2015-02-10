from lettuce import step
from lettuce import world

from journal import connect_db
from journal import DB_SCHEMA
from journal import INSERT_ENTRY

TEST_DSN = 'dbname=test_learning_journal user=ndraper2'


def init_db(settings):
    with closing(connect_db(settings)) as db:
        db.cursor().execute(DB_SCHEMA)
        db.commit()


def clear_db(settings):
    with closing(connect_db(settings)) as db:
        db.cursor().execute("DROP TABLE entries")
        db.commit()


def clear_entries(settings):
    with closing(connect_db(settings)) as db:
        db.cursor().execute("DELETE FROM entries")
        db.commit()


def run_query(db, query, params=(), get_results=True):
    cursor = db.cursor()
    cursor.execute(query, params)
    db.commit()
    results = None
    if get_results:
        results = cursor.fetchall()
    return results


@before.all
def open_db(request):
    settings = {'db': TEST_DSN}
    init_db(settings)
    return settings


@after.all
def close_db(request):
    settings = {'db': TEST_DSN}

    def cleanup():
        clear_db(settings)

    request.addfinalizer(cleanup)


@step('a journal entry list')
def journal_entry_list()