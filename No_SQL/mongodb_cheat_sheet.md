**NOSQL(not only sql) characteristics**  
- Scalability
- Availability, replication, and eventual consistency
- Replication models(Master-slave , Master-master)
- Sharding of files
- High performance data apcess(Hashing , Range partitioning)
- simple query only and constrian in the application not in the server like sql server 

Most NOSQL systems are **distributed databases** or **distributed storage systems**

**Strong consistency** guarantees that every read operation returns the latest write operation’s result, regardless of the node on which the read operation is executed. This is typically achieved using consensus algorithms like Paxos or Raft1.  
**Sequential consistency** implies that there is some order without any timing guarantees. For example, let’s say we have a system where nodes have some state machines and these machines process some events. In a sequentially consistent system, all these events have the same processing order - A,B,C,D - hence state machines execute exactly the same sequence. But if you ask a specific node about its state, you can get any of those, as there is no timing guarantee2.  
**Eventual consistency** guarantees that updates will propagate through the system and eventually be applied to all nodes, given enough time. In other words, if no new updates are made to a particular data item, eventually, all nodes will converge on the same value for that item. However, this may allow the system to have temporary inconsistencies  

**CAP theorem**  
Consistency, availability, and partition tolerance
- Not possible to guarantee all three simultaneously In distributed system with data replication

**Consistency** means that all the computers in the network have the same data at the same time. For example, if you update your profile picture on a social media app, consistency means that everyone who sees your profile will see the same picture, no matter which computer they use.  
**Availability** means that the system can respond to any request from the users, even if some of the computers in the network are not working. For example, if you send a message to your friend on a chat app, availability means that your friend will receive your message, even if some of the computers that handle the messages are down.  
**Partition tolerance** means that the system can continue to work even if there are problems with the network connections between the computers. For example, if you are watching a video on a streaming app, partition tolerance means that you can still watch the video, even if some of the computers that deliver the video are disconnected from each other.

------
## columnar database 
![alt text](<columnar vs row_DB.png>)
| Feature          | Columnar Database                                      | Row Database                                         |
|------------------|--------------------------------------------------------|------------------------------------------------------|
| **Data Storage**     | Stores data by columns.                                | Stores data by rows.                                 |
|Data Block Usage  |Each data block holds column field values for multiple rows.	|Data blocks store values sequentially for each consecutive column, making up the entire row.	|
|Block Size vs. Record Size|Columnar storage allows each data block to hold column field values for as many as three times the number of records compared to row-based storage		|If the block size is smaller than the size of a record, storage for an entire record may span(divide) multiple blocks. Conversely, if the block size is larger than the record size, it results in inefficient use of disk space..|
| **Speed**            | Fast for reading and analyzing specific columns of data. | Fast for adding, updating, or deleting rows of data. |
|**Use Case**         | Ideal for analytical queries(data warehouse) where specific columns are accessed. | Suited for transactional processing(OLTP) with frequent row-level updates. |
| I/O Operations   | Requires fewer I/O operations for column-specific queries. | Requires more I/O operations for full-row retrievals. |
| Compression      | Can compress data more efficiently due to similar data in columns. | Less efficient compression as rows contain varied data types. |
| Indexing         | Often requires less indexing.                          | Often heavily indexed to optimize performance.       |
| Memory Efficiency     |Retrieving and storing data in memory benefits from columnar storage, requiring a fraction(less) of the I/O operations.                              |  |
| **Advantages**   | - Efficient for read-heavy **analytical** queries **because you’re only working with a few columns** <br> - High compression ratios due to **similar data type in columns**<br>- Less I/O for column-specific operations **because you’re only working with a few columns**<br>- Better performance for queries involving large datasets | - Efficient for write-heavy **transactional** workloads<br>- Quick at adding, updating, or deleting rows of data<br>- Better suited for OLTP (Online Transaction Processing) systems |
| **Disadvantages**| - Not optimal for frequent inserts and updates<br>- Deletes require tombstones, affecting compression<br>- Inserts require row reconstruction              | - Slower for analytical queries that only need specific columns<br>- More I/O for full-row retrievals<br>- Less efficient compression as rows contain varied data types |




**use case example** 
- Consider a company that keeps **data for all orders** it receives using row-based storage,tracking data such as the OrderlD, OrderDate, Customer,Priority, Status, and TotalAmount.  
- Each row of data logically corresponds to an **order(transaction)**,and all data in a single row is physically stored together.
- This model makes it easy to quickly add or update orders.Orders can be added one at a time,and each database write corresponds to exactly one row.With transactions like this, there is no need to access or update any data in the table except the row you are changing.

![alt text](image.png)  

- Say the company wants to find the average earnings per sale in each month For this, you would only need the information from two columns:OrderDate and TotalAmount.(However, with row-based storage, you must retrieve all the data for each order to get this information.if you use an index on the order date column you would still need to read the full Row for each order within the date range to get the total amount with a large number of orders this can be very inefficient).  
- this is where columnar storage comes into play **rather than storing data together by row data is stored together by column** logically the table and the associations between the data remain the same it is only the physical storage method that changes.

![alt text](image-1.png)

nterSystems IRIS allows for a flexible data storage approach by using globals, which can store data in both row-based and columnar formats. **This means you can choose to store specific data**   
- like the total amount, in columnar storage for quick analytical queries
- while other data, such as priority and status that may change frequently, can be stored in row format for fast transactional updates.
- Implementing columnar storage is straightforward: simply add storage type = columnar to your table definition. This won’t affect how you query your data, enabling you to perform fast analytics immediately after setting up your table with columnar storage.

![alt text](image-2.png)
----------

# MongoDB Cheat Sheet

## Show All Databases

```
show dbs
```

## Show Current Database

```
db
```

## Create Or Switch Database

```
use acme
```

## Drop

```
db.dropDatabase()
```

## Create Collection

```
db.createCollection('posts')
```

## Show Collections

```
show collections
```

## Insert Row

```
db.posts.insert({
  title: 'Post One',
  body: 'Body of post one',
  category: 'News',
  tags: ['news', 'events'],
  user: {
    name: 'John Doe',
    status: 'author'
  },
  date: Date()
})
```

## Insert Multiple Rows

```
db.posts.insertMany([
  {
    title: 'Post Two',
    body: 'Body of post two',
    category: 'Technology',
    date: Date()
  },
  {
    title: 'Post Three',
    body: 'Body of post three',
    category: 'News',
    date: Date()
  },
  {
    title: 'Post Four',
    body: 'Body of post three',
    category: 'Entertainment',
    date: Date()
  }
])
```

## Get All Rows

```
db.posts.find()
```

## Get All Rows Formatted

```
db.posts.find().pretty()
```

## Find Rows

```
db.posts.find({ category: 'News' })
```

## Sort Rows

```
# asc
db.posts.find().sort({ title: 1 }).pretty()
# desc
db.posts.find().sort({ title: -1 }).pretty()
```

## Count Rows

```
db.posts.find().count()
db.posts.find({ category: 'news' }).count()
```

## Limit Rows

```
db.posts.find().limit(2).pretty()
```

## Chaining

```
db.posts.find().limit(2).sort({ title: 1 }).pretty()
```

## Foreach

```
db.posts.find().forEach(function(doc) {
  print("Blog Post: " + doc.title)
})
```

## Find One Row

```
db.posts.findOne({ category: 'News' })
```

## Find Specific Fields

```
db.posts.find({ title: 'Post One' }, {
  title: 1,
  author: 1
})
```

## Update Row

```
db.posts.update({ title: 'Post Two' },
{
  title: 'Post Two',
  body: 'New body for post 2',
  date: Date()
},
{
  upsert: true
})
```

## Update Specific Field

```
db.posts.update({ title: 'Post Two' },
{
  $set: {
    body: 'Body for post 2',
    category: 'Technology'
  }
})
```

## Increment Field (\$inc)

```
db.posts.update({ title: 'Post Two' },
{
  $inc: {
    likes: 5
  }
})
```

## Rename Field

```
db.posts.update({ title: 'Post Two' },
{
  $rename: {
    likes: 'views'
  }
})
```

## Delete Row

```
db.posts.remove({ title: 'Post Four' })
```

## Sub-Documents

```
db.posts.update({ title: 'Post One' },
{
  $set: {
    comments: [
      {
        body: 'Comment One',
        user: 'Mary Williams',
        date: Date()
      },
      {
        body: 'Comment Two',
        user: 'Harry White',
        date: Date()
      }
    ]
  }
})
```

## Find By Element in Array (\$elemMatch)

```
db.posts.find({
  comments: {
     $elemMatch: {
       user: 'Mary Williams'
       }
    }
  }
)
```

## Add Index

```
db.posts.createIndex({ title: 'text' })
```

## Text Search

```
db.posts.find({
  $text: {
    $search: "\"Post O\""
    }
})
```

## Greater & Less Than

```
db.posts.find({ views: { $gt: 2 } })
db.posts.find({ views: { $gte: 7 } })
db.posts.find({ views: { $lt: 7 } })
db.posts.find({ views: { $lte: 7 } })
```
