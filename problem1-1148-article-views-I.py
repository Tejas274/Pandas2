import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[(views['author_id'] == views['viewer_id'])]

    df.drop_duplicates(subset=["author_id"], inplace=True)

    df = df[["author_id"]]

    df = df.rename(columns={"author_id": "id"})

    return df.sort_values(by='id')



def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']] \
        .drop_duplicates(subset=['author_id']) \
        .rename(columns={'author_id': 'id'})[['id']] \
        .sort_values(by='id')

    return df