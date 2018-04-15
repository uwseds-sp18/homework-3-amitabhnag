import unittest
import homework3

class UnitTest(unittest.TestCase):
	path = "C:/Users/amnag/DATA515/LectureNotes/Data-Essentials/class.db"
	def test_invalid_path(self):
		#tests if the db path is valid 
		try:
			homework3.create_dataframe("C:/abracadabra.db")
			self.assertTrue(False)
		except ValueError:
			self.assertTrue(True)

	def test_column_name(self):
		#tests if the column names are video_id, language, category_id
		df = homework3.create_dataframe(self.path)
		check = df.columns.contains('video_id') & df.columns.contains('language') & df.columns.contains('category_id')
		self.assertTrue(check)

	def test_row_count(self):
		#tests if the row count >0
		df = homework3.create_dataframe(self.path)
		check = df.shape[0] > 0
		self.assertTrue(check)

	def test_key1(self):
		#tests if video_id and language can possibly be a key
		df = homework3.create_dataframe(self.path)
		dflen = df.shape[0]
		df_small = df['video_id'] + df['language']
		distinctValuesByKey = df_small.nunique()
		check = dflen == distinctValuesByKey	
		self.assertTrue(check)

	def test_key2(self):
		#tests if video_id, language and category_id can possibly be a key
		df = homework3.create_dataframe(self.path)
		dflen = df.shape[0]
		df_small = df['video_id'].astype(str) + df['language'].astype(str) +  df['category_id'].astype(str)
		distinctValuesByKey = df_small.nunique()
		check = dflen == distinctValuesByKey	
		self.assertTrue(check)
		
suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest)
_ = unittest.TextTestRunner().run(suite)