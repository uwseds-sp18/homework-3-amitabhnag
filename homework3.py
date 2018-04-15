import sqlite3
import pandas as pd
import os.path

def create_dataframe(dbPath):
    if (os.path.exists(dbPath) != True):
        raise ValueError("{0} path does not exist".format(dbPath))
    else:
    	conn = sqlite3.connect(dbPath)
    	df = pd.read_sql_query("SELECT video_id,category_id,'us' AS language FROM USVideos UNION SELECT video_id,category_id,'gb' AS language FROM GBVideos UNION SELECT video_id,category_id,'fr' AS language FROM FRVideos UNION SELECT video_id,category_id,'de' AS language FROM DEVideos UNION SELECT video_id,category_id,'ca' AS language FROM CAVideos;", conn)
    	return(df)
