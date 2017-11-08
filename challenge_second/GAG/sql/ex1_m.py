import sqlite3
import time
from multiprocessing import Process, Pool
import string
import heapq


con = sqlite3.connect('/Users/GretarAtli/Documents/GitHub/Dtu/Dtu-ToolsForBigData/challenge_second/GAG/reddit.db')
con.text_factory = str
cur = con.cursor()

def query(subreddit_id):

	symbols = ['\n','`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[',']','}','|','\\',':',';','"',"'",'<','>','.','?','/',',']

	cur.execute(""" 
	SELECT body 
	FROM comments
	WHERE subreddit_id = ?
	""",
	subreddit_id)

	all_words = set()

	for d in cur.fetchall():
		# extract the data of the tuple
		comment = d[0]

		# ===================== clean the data ======================================
		comment = comment.lower()
		comment = comment.translate(string.maketrans("",""), string.punctuation)

		all_words.update(comment.split())

		#for word in set(comment.split()):
		#	all_words.add(word)
		# ====================== end of cleaning ====================================


	nr_of_words = len(all_words)

	return (nr_of_words, subreddit_id)


if __name__ == '__main__':

	with con:

		cur.execute("SELECT DISTINCT LOWER(id) FROM subreddits LIMIT 100")   #(%s, %s, %s)", (var1, var2, var3))
		#cur.execute("SELECT DISTINCT LOWER(id) FROM subreddits WHERE id='t5_2qh0u'") 
		#cur.execute("SELECT DISTINCT id FROM subreddits where id = 't5_2fwo'")
		
		t3 = time.time()
		p = Pool(8)

		results = p.map(query, cur.fetchall())
		
		p.close()

		print heapq.nlargest(10, results)

		t4 = time.time()

		print "Execution time {}".format(t4-t3)
		
