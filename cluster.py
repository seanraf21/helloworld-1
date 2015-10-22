from sklearn.cluster import KMeans
import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root',password='',port="3307", host='127.0.0.1',database='userposts')

cursor = cnx.cursor()

query = ("SELECT post_message FROM cleanposts")
cursor.execute(query)
kmeans = KMeans(n_clusters=5)
arr = []
for (user_posts) in cursor:
	arr.append(user_posts[0].split(", ",1)) #add lists of each user post
	#break
print(arr)

#kmeans.fit(arr)

cursor.close()
cnx.close()