# MongoDB cheat cheat for CompostBuddy




Filter for documents that contain IoT errors:
~~~
{errors:{$exists:true,$ne:[]}}
~~~

Delete documents based on temperature values:
~~~
db.esp32.deleteMany({'temp1': { '$gt': 10.0 }})
~~~

Sort clause for latest documents first:
~~~
{ timestamp: -1}
~~~