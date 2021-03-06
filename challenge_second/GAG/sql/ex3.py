from __future__ import division,print_function
import sqlite3
import time
import heapq
import numpy as np
from multiprocessing import Process, Pool 


con = sqlite3.connect('/Users/GretarAtli/Documents/GitHub/Dtu/Dtu-ToolsForBigData/challenge_second/GAG/reddit.db')
con.text_factory = str

cur = con.cursor()

# Function that finds the average depth
def find_avg_depth(subreddit_id):

	# For each subreddit find all of the top level comments. 
	# They can be identified by the fact that they all start with t3
	cur.execute(""" 
				SELECT id
				FROM comments
				WHERE subreddit_id = ?
				AND parent_id LIKE 't3%'
				""",
				subreddit_id)

	sum_of_depths = 0
	total_nrof_comments = 0

	# For each top level comment find the dept of the corresponding comment thread 
	# We achieved this with a recursive function in sql (CTE in sql)
	for d in cur.fetchall():
		# Find the depth with a recursive function in sql
		cur.execute(""" WITH deepness (id,depth) AS 
					(
						-- INITIALIZATION  STEP
						values (?,0)
		
						UNION ALL
		
						-- RECURSIION STEP
						SELECT comments.id, deepness.depth+1
						FROM comments JOIN deepness on comments.parent_id = deepness.id
					)
					Select max(depth) from deepness

					""", [d[0]])	

		# For each thread we sum up the deepness of the comments
		# We also sum up the number of toplevel comments within this subreddit ID 
		query_answer = cur.fetchall()

		for i in query_answer:
			#print (i)
			sum_of_depths += i[0]

		total_nrof_comments += len(query_answer) 

	# If there are no comments associated with this subreddit Id then we simply return 0
	if total_nrof_comments == 0:
		return ( 0, subreddit_id)
	else:
		return ( sum_of_depths/total_nrof_comments, subreddit_id)


if __name__ == '__main__':

	t1 = time.time()

	print ("\n######### STARTING #########")
	print ("")

	# Get all of the reddit ids
	cur.execute("SELECT id FROM subreddits WHERE id = 't5_2rosc'")
	#cur.execute("SELECT id FROM subreddits WHERE id = 't5_2zlk4'")
	#cur.execute("SELECT id FROM subreddits WHERE id = 't5_2vjsb'")

	# Start multiprocessing
	p = Pool(100)
	results = p.map(find_avg_depth, cur.fetchall())
	p.close()

 	# Find the 10 subreddits with deepest average comment threads 
	top_ten = heapq.nlargest(10, results)

	# Print out the result
	result_for_file = []
	fetch = ""
	for i in top_ten:
		cur.execute("select name from subreddits  where id = ?",i[1])
		fetch = cur.fetchall()[0][0]
		print (i, fetch)
		result_for_file.append(str(i[0]) +"     " + str(i[1][0]) + "      " + fetch)

	t2 = time.time()

	print ("Execution time {}".format(t2-t1))

	print ("\n######### ENDING #########")
	print











