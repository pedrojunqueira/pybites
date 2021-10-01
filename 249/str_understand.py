
table = 'movies'
params = []
sql = f"SELECT * FROM {table}"

print(sql)

title = "Aristocats"

sql += " WHERE title LIKE ?"
params.append(f"%{title}%")

print(sql)

print(params)

year = 1976

sql += " WHERE year = ?"
params.append(year)

print(sql)

print(params)


score_gt = 4

sql += " WHERE score > ?"
params.append(score_gt)

print(sql)

print(params)
