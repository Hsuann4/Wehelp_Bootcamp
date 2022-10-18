# WEEK 5 Assignment 

### Requiremnet 3

#### 3-1
~~~sql 
INSERT INTO member(id, name, username, password, follower_count,time)' VALUES (1, 'Seda', 'test', 'test', 10, DEFAULT);
~~~~

![Screenshot 2022-10-17 at 18 28 29](https://user-images.githubusercontent.com/108836777/196542144-08287875-b9df-49ca-a88d-2a0da07124e5.png)


#### 3-2
~~~sql 
SELECT * FROM member;
~~~

![Screenshot 2022-10-17 at 18 28 29](https://user-images.githubusercontent.com/108836777/196542154-11876d5c-69d7-4ea2-998a-3c3bd6e5c0e3.png)





#### 3-3
~~~sql
SELECT * FROM member
ORDER BY time DESC;
~~~

![Screenshot 2022-10-17 at 18 30 53](https://user-images.githubusercontent.com/108836777/196545811-c397b3c3-c90f-4afe-9170-b20838beacd4.png)



#### 3-4
~~~sql
SELECT * FROM member
ORDER BY time DESC
LIMIT 1,3;
~~~

<img width="560" alt="Screenshot 2022-10-17 at 20 10 59" src="https://user-images.githubusercontent.com/108836777/196542578-d362cfc2-23a9-43f5-98bf-18e2eb836f06.png">

#### 3-5
~~~sql
SELECT * FROM member 
WHERE username = 'test';
~~~

![Screenshot 2022-10-17 at 18 40 58](https://user-images.githubusercontent.com/108836777/196542754-c2952981-99dc-4110-9ddf-dc8e4616c2a5.png)



#### 3-6
~~~sql
SELECT * FROM member 
WHERE username = 'test' AND name = 'test';
~~~

![Screenshot 2022-10-17 at 18 39 20](https://user-images.githubusercontent.com/108836777/196542651-56927177-637e-42ad-a717-31a6890f0720.png)



#### 3-7

~~~sql
UPDATED member
SET name = 'test2'
WHERE username = 'test';
~~~

<img width="552" alt="Screenshot 2022-10-18 at 10 38 30" src="https://user-images.githubusercontent.com/108836777/196542865-57dc54b3-24b9-422d-b530-021334e33a98.png">





### Requirement 4

#### 4-1
~~~sql
SELECT COUNT(id)
FROM member;
~~~
<img width="244" alt="Screenshot 2022-10-18 at 10 54 50" src="https://user-images.githubusercontent.com/108836777/196545991-18d5662b-cd17-4f3e-ab51-79cefae49406.png">


#### 4-2
~~~sql
ELECT SUM(follower_count)
FROM member;
~~~
<img width="350" alt="Screenshot 2022-10-18 at 10 57 20" src="https://user-images.githubusercontent.com/108836777/196546214-8d0b34fe-c225-40c8-a6e7-6116f2b95130.png">



#### 4-3
~~~sql
SELECT AVG(follower_count)
FROM member;
~~~

<img width="281" alt="Screenshot 2022-10-18 at 10 58 01" src="https://user-images.githubusercontent.com/108836777/196546269-9671aa1a-ad28-43c3-8912-73908efedefb.png">





### Requirement 5 (Optional)


#### 5-1
~~~sql
SELECT member.id, member.name, message.content
FROM member
INNER JOIN message
ON member.id = message.member_id;
~~~


<img width="352" alt="Screenshot 2022-10-18 at 19 50 24" src="https://user-images.githubusercontent.com/108836777/196546813-ed74db00-cac8-4fec-b7c3-067d5a70f51f.png">


#### 5-2
~~~sql
SELECT member.id, member.name, member.username, message.content
FROM member
INNER JOIN message
ON member.id = message.member_id
WHERE member.username = 'test';
~~~

<img width="511" alt="Screenshot 2022-10-18 at 19 55 29" src="https://user-images.githubusercontent.com/108836777/196546925-5ce73cd8-3f47-45f9-85db-60605730dc35.png">



#### 5-3
~~~sql
SELECT member.username, sum(message.like_count)
FROM member
INNER JOIN message
ON member.id = message.member_id
WHERE member.username = 'test'
GROUP BY username;
~~~

<img width="483" alt="Screenshot 2022-10-18 at 20 10 10" src="https://user-images.githubusercontent.com/108836777/196546993-34521a21-4600-4864-8ef6-d6899cf0ff49.png">

